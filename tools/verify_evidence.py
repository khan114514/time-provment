#!/usr/bin/env python3
"""Verify published bytes and timing arithmetic, without certifying research credit."""
import hashlib
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT / path).read_text())


def main():
    manifest = read('MANIFEST.json')
    expected = {entry['path'] for entry in manifest['files']}
    actual = {
        str(p.relative_to(ROOT)) for p in ROOT.rglob('*')
        if p.is_file() and '.git' not in p.relative_to(ROOT).parts
        and '__pycache__' not in p.parts and p.name != 'MANIFEST.json'
    }
    assert actual == expected, ('inventory mismatch', sorted(actual ^ expected))
    for entry in manifest['files']:
        data = (ROOT / entry['path']).read_bytes()
        assert len(data) == entry['bytes'], entry['path']
        assert hashlib.sha256(data).hexdigest() == entry['sha256'], entry['path']
    derivations = {x['path']: x for x in read('provenance/public_path_derivations.json')}
    for source in read('provenance/source_map.json'):
        digest = hashlib.sha256((ROOT / source['path']).read_bytes()).hexdigest()
        expected_digest = derivations.get(source['path'], {}).get(
            'published_sha256', source['source_sha256'])
        assert digest == expected_digest, source['path']
    policy, status = read('policy.json'), read('status.json')
    assert policy['required_effective_seconds_per_lane'] == 36000
    assert policy['seven_hour_exception_used'] is False
    result = {'scope': 'file integrity and arithmetic only', 'files_verified': len(expected), 'lanes': {}}
    accounting = read('bifrost/expert_evidence/original-source-method-loops/conservative-clock-source-accounting.json')
    for lane, record in accounting['lanes'].items():
        intervals = sorted(record['actual_disjoint_activity_intervals'])
        assert all(end >= start for start, end in intervals)
        assert all(intervals[i][0] >= intervals[i-1][1] for i in range(1, len(intervals)))
        seconds = sum(end - start for start, end in intervals)
        assert abs(seconds - record['conservative_measured_activity_seconds']) < 1e-6
        assert abs(seconds - status['lanes']['bifrost/' + lane]['seconds']) < 1e-6
        result['lanes']['bifrost/' + lane] = {
            'observed_lower_bound_seconds': seconds, 'interval_count': len(intervals),
            'gap_from_observed_lower_bound_to_36000': 36000-seconds,
            'net_effective_duration_certified': False,
        }
    one = read('onedc/expert_evidence/time-accounting.json')
    for track in one['final_v8_formal']['tracks']:
        lane = track['name']
        start = datetime.fromisoformat(track['current_qualifying_started_at'])
        end = datetime.fromisoformat(one['user_authorized_recalculation'][lane]['paused_at'])
        seconds = (end-start).total_seconds()
        assert abs(seconds-status['lanes']['onedc/' + lane]['seconds']) < 1e-6
        audit_root = ROOT / 'onedc/evidence/original_clock_records' / lane / 'private-rounds'
        audits = sorted(audit_root.glob('*/audit.json'))
        assert len(audits) == status['lanes']['onedc/' + lane]['raw_audit_count']
        assert all((p.parent / 'started.json').is_file() for p in audits)
        result['lanes']['onedc/' + lane] = {
            'historical_wall_upper_bound_seconds': seconds,
            'minimum_gap_before_exclusions_to_36000': 36000-seconds,
            'raw_audits': len(audits), 'net_effective_duration_certified': False,
        }
    assert set(result['lanes']) == {'onedc/gpt', 'onedc/seed', 'bifrost/gpt', 'bifrost/seed'}
    assert all(not v['target_proven'] for v in status['lanes'].values())
    result['verification'] = 'PASS: bytes and arithmetic; NOT a 10-hour acceptance'
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
