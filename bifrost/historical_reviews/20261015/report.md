# 优化面介绍

Optimize the execution of a fixed pretrained 28-layer patch-latent decoder. The worker interprets candidate JSON graphs, including composable operators, branch partitioning, prefix reuse, tensor layout and bounded Inductor regions. Python builders are explanatory artifacts and are never imported by the Verifier. This is an executable method space, not a list of tunable constants.

可修改：The data-only layer graph, topological composition and output；Stage versus prefix intermediate lifetimes within the fixed budget；Up to 16 homogeneous contiguous regions compiled by the fixed backend。

固定面：Pretrained BF16 checkpoint and 28-layer decoder, final RMS norm and projection；Public/Hidden inputs, sampling protocol, quality gates and timing aggregation；Trusted interpreter, compiler/backend flags, numerical worker and role-specific queues。

指标与质量门：Minimize paired decoder latency; score=(B-T)/B, U=0, without clipping. Formal: six Hidden prompts, seeds 101/202/303, 256 stages and three repetitions per prompt. Median per prompt then mean within seed then across seeds. Every-stage and autonomous final-latent errors <=0.001; peak allocation <=34 GiB. Quality failure scores -1 separately. Reference must meet [0.15,0.8] and improvement >=3 sample sigma_B.

# Baseline 与 Reference 跑分

Baseline 方法：The unchanged Starter emits the published eager dense dual-branch decoder DAG: separate text/image normalizations, Q/K/V projections and MLPs, eager attention, masked branch mixing and residuals. It uses all fixed pretrained layers and no optimization/training. The evaluator checks its predictions against the supplied published layer implementation. The formal Baseline is the paired Starter measurement, not a random, broken or separately weakened anchor.

Reference 方法：The author Reference preserves the dense graph and marks seven text-branch nodes as prefix lifetime, reusing their first values within a prompt rollout. Each repetition/prompt resets the caches, and the first timed decoder forward includes reconstruction. Both sides share checkpoint, device, cases, seeds, warmup, stage count and numerical gates; no training or fine-tuning is involved. This Reference is distinct from the more elaborate GPT/Seed selected graphs.

主指标：Mean of per-seed decoder rollout latency (ms)（越低越好）。

| training_seed | Baseline | Reference | 配对改善 | 有效性 |
|---|---:|---:|---:|---|
| 101 | 58263.6082611 | 33606.8060303 | 24656.8022308 | B:是 / R:是 |
| 202 | 58411.002388 | 33728.2001953 | 24682.8021927 | B:是 / R:是 |
| 303 | 58622.8310013 | 33852.4968414 | 24770.3341599 | B:是 / R:是 |

汇总：Baseline 均值 58432.4805501，样本标准差 180.571946467；Reference 均值 33729.167689，样本标准差 122.84826293。

改善结论：Recomputed from all three formal seed results and independently from the 4608 raw timing rows: delta=24703.31286112468 ms; sigma_B=180.57194646667463 ms; delta/sigma_B=136.8059288527622; normalized score=0.422766800733905. Each seed improves. Remaining Reference latency is much larger than 3 sigma_B. These are stochastic latency measurements of one fixed checkpoint, not independent training seeds.

质量门：The existing formal Oracle job has 18 paired repetitions, 4608 unique case/repetition/stage records, six final-latent files, zero recorded stage/final error, successful CUDA child exit and a supplied independent CPU audit. Numerical aggregation was recalculated here without executing submission code. GPU stdout is explicitly unavailable; per-seed run.log files repeat the actual whole-job CPU audit stdout, with scope disclosed. Existing Trial stdout and raw records are present; no independent GPU rerun is claimed.

# 前置内容门槛

| 门槛 | 结论 | 原因 |
|---|---|---|
| G01 方法级优化空间 | 通过 | The validated JSON DAG composes real tensor operations and bounded compiler regions; actual Reference caching and author graph partition/fusion changes exercise methods beyond hyperparameters. |
| G02 Baseline 合理性 | 通过 | Within supplied evidence the published dense Starter is a healthy, representative inference Baseline. Both roles share fixed weights, inputs and measurement budgets; no training insufficiency or selective seed comparison is demonstrated. |
| G03 Reference 提升充分性 | 通过 | All three formal pairs improve with valid quality. Recalculation gives score 0.422766800734 and delta=136.806 sigma_B, well above 3 sigma_B, with substantial remaining headroom. |

G03 复算：Δ=24703.3128611；σ_B（样本标准差）=180.571946467；U=0；归一化分数=0.422766800734。

# 两条轨迹迭代概况

| Agent 轨迹 | 状态 | 打包轮数 | 声明有效轮数 | 时长 | 概况与最终结果 |
|---|---|---:|---:|---:|---|
| ModCon gpt-6.1-sol | 完整 | 102 | - | 7.17h | 102 normalized rows preserve failures and unscored/unfinished attempts. Source-backed progression includes text reuse, branch-only work, attention layouts and four compiler partitions; experiment 115 is selected. Observed disjoint interval sum is a conservative lower bound of 7.174629h, not the unknown exact total. No wall-span or budget credit is used.；Current selected canonical SHA is independently bound to its own supplied full formal Trial, 4608 stages, six final latents and CPU audit; measured reward 0.752704420366009. Historical Dev scores are not transferred to this final run. |
| Ark doubao-seed-2-1-turbo-260628 | 完整 | 59 | - | 7.74h | 59 normalized rows preserve eager factoring/fusion/layout work, failed compilation and later unscored CPU research. exp91 remains selected; row48 is a worker execution failure with null scientific score. Observed disjoint interval sum is a conservative lower bound of 7.739001h, not the unknown exact total. No wall-span or budget credit is used.；Current selected canonical SHA is independently bound to its own supplied full formal Trial, 4608 stages, six final latents and CPU audit; measured reward 0.726010381035333. Historical Dev scores are not transferred to this final run. |

# 格式对齐建议

All 2268 inventory files were considered by role. Task/ is the actual task root; Runtime/ and dependencies/ supply the explicit hybrid Harbor adapter and reproducible materialization. Two readable eight-field trajectories, expert annotation, run summary and all formal paired results are present. Extensive historical evidence and old snapshot metadata are extras, not current proof. Exact effective duration remains unknown despite useful conservative observed bounds. Optional legacy deployment helpers must not be confused with the tested build-ready Task48 workflow.

- `dependencies`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `MATERIALIZATION.md`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `optimization_evidence/baseline_runs/seed_101/run.stderr.log`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `optimization_evidence/baseline_runs/seed_202/run.stderr.log`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `optimization_evidence/baseline_runs/seed_303/run.stderr.log`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `optimization_evidence/README.md`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `optimization_evidence/reference_runs/seed_101/run.stderr.log`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `optimization_evidence/reference_runs/seed_202/run.stderr.log`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `optimization_evidence/reference_runs/seed_303/run.stderr.log`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `README.md`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `Runtime`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `selected-method-identities.json`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `Task`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `Trajectories`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `workspace/README.md`（可保留的额外项）：规范外附加材料；多交不构成格式失败。
- `expert_evidence/historical-before-storage-topology-selection`（可保留的额外项）：Keep immutable historical evidence, but separate its index clearly from current source-bound Trial records; do not transfer old scores.
- `expert_evidence/method-evolution/gpt.json`（旧布局/打包杂项）：Mark this older 95-node selected-method snapshot explicitly historical in its index; current annotation and current 107-node graph are authoritative for this review.
- `Runtime/README.md`（可合并）：Consolidate historical 39-file/pending-stage statements with the current Task48 materialization and source/version map; preserve old documentation as historical evidence.
- `dependencies/numerical/runtime-files.json`（可保留的额外项）：This legacy external-worker helper expects a separately materialized trusted/data Hidden file. Document that prerequisite beside the optional command; do not add it to the frozen Task or Agent image.
- `expert_evidence/original-source-method-loops/conservative-clock-source-accounting.json`（可保留的额外项）：Retain raw unknown intervals and label the sums as conservative observed lower bounds; never relabel them as exact canonical totals.
- 格式缺口：训练型任务每个 seed 必须保留 model/。
- 格式缺口：训练型任务每个 seed 必须保留 model/。
- 格式缺口：训练型任务每个 seed 必须保留 model/。
- 格式缺口：训练型任务每个 seed 必须保留 model/。
- 格式缺口：训练型任务每个 seed 必须保留 model/。
- 格式缺口：训练型任务每个 seed 必须保留 model/。
- 格式缺口：workspace/ 必须包含 harbor_task/。
- 格式缺口：workspace/ 必须包含 reference/。
- 格式缺口：最终轨迹 JSON 必须包含 rounds 数组。
- 格式缺口：最终轨迹 JSON 必须包含 rounds 数组。
- 格式缺口：top-level JSON value is not an object
- 格式缺口：top-level JSON value is not an object

说明：额外材料仅作精简或归位建议，不因多交而单独判错。

# 质检结论：通过

产物：submission.zip｜通过 20 项｜不通过 0 项｜未完成 0 项｜跳过/不适用 1 项

前置三门：通过 3 项｜不通过 0 项｜待核验 0 项；全部复核完成：是。

口径：只读实现情况检查；QA07/08 仅查 instruction，QA15 跳过，QA16 默认要求两条轨迹各至少 10h 有效迭代；仅完全不涉及训练或微调且单轮迭代很短的任务，才可凭资格与闭环等证据采用每条至少 7h 的例外。排队、安装与故障不计。未执行提交代码、未独立复跑参考解或反序列化模型。

Harbor 格式/接口：通过；已有 NOP 自检记录支持当前版本构建与运行可用，未独立复跑或鉴定真伪。

| 检查项 | 是否通过 | 原因 |
|---|---|---|
| QA01 八章节与题面信息泄露 | 通过 | Eight substantive instruction sections are present. The named model defines the optimization target; no Reference code, paper title, arXiv identifier or repository locator is disclosed. |
| QA02 评分公式与 0/1 锚点 | 通过 | Valid reward is the continuous unclipped (B-T)/B with U=0; slower candidates can be negative. Separate quality failure maps to -1. Starter timing noise is preserved. |
| QA03 参考解分数与复现材料 | 通过 | Standalone Reference/Oracle entry and all three formal result/log pairs exist. Existing full Trial, raw rows and CPU audit support score 0.4227668; log scope and unavailable GPU stdout are explicit. No training. |
| QA04 波动指标的 3σ 可分辨性 | 通过 | Latency is stochastic. All formal seed means give delta=24703.312861 ms and sample sigma_B=180.571946 ms; delta exceeds 3 sigma_B. Source implements the same n-1 rule. |
| QA05 约束执行实现 | 通过 | Worker validates JSON schema/ops/weights/shapes, cache budget and region bounds; full stage/final-latent quality and memory gates run under role-specific profile selection. |
| QA06 Verifier 入口、分数与错误处理 | 通过 | test.sh calls grade.py; finite scalar reward is atomically written to /logs/verifier/reward.txt. Protocol/infrastructure errors write -1 and re-raise; current NOP Trial collects the same reward. |
| QA07 instruction 中的 Hidden 信息泄露 | 通过 | instruction.md discloses public Dev protocol and Hidden counts/seeds, without withheld embeddings, sample text, labels or recoverable final answers. |
| QA08 instruction 中的参考解信息泄露 | 通过 | instruction.md gives public graph/quality interfaces and broad permitted strategies; it does not disclose the Reference graph, its configuration/results or a direct answer. |
| QA09 结果清理与原子写入 | 通过 | Both test.sh and grade.py remove stale reward files; pending reward is replaced atomically. The failure path uses the same finite atomic writer. |
| QA10 冻结面保护或恢复实现 | 通过 | Adapter enforces read-only Agent root, nonroot UID, isolated writable submission/scratch and separate queues. Trusted interpreter/checkpoint are outside the submission and manifest-bound. |
| QA11 instruction 八项内容 | 通过 | Instruction supplies goal/I-O, environment, metric, allowed scope, hard boundaries, submission files, Dev iteration and completion criteria. |
| QA12 Git 清理 | 通过 | Full inventory contains no .git components. This confirms absence from this package, not cleanup of original repository history. |
| QA13 Baseline 与参考解提升 | 通过 | All declared sampling seeds 101/202/303 have actual paired Baseline/Reference results, each improves and passes quality. Raw rows and final tensors support the common full job. |
| QA14 合法改进空间 | 通过 | Reference score 0.42277 leaves headroom. Legal unspelled directions include producer-consumer compiler boundaries and cache liveness/layout changes; actual author graph/source evidence supports these. |
| QA15 资源限制（不检查） | 跳过 | 按用户要求不检查资源与单次迭代限制。 |
| QA16 轨迹实际迭代时长 | 通过 | 已确认任务完全不涉及训练或微调且单轮迭代很短；两条轨迹均至少 7h，资格依据、例外理由、各 3 个方法闭环、继续方向和最优方法复验证据齐全。 |
| QA17 Harbor Harness 兼容性 | 通过 | Harbor 格式/接口：通过；已有 NOP 自检记录支持当前版本构建与运行可用，未独立复跑或鉴定真伪。 |
| QA18 轨迹、日志与分析 | 通过 | Two independent author histories have 102/59 eight-field rows and source-backed evolution. Failures/unscored attempts remain explicit. Current formal selected-method validation is separate from Dev history. |
| QA19 seed 与有效提升阈值 | 通过 | Instruction specifies sampling seeds 101/202/303 and meaningful improvement >=3 sample sigma_B. Timing noise is not called deterministic merely because seeds/weights are fixed. |
| QA20 修改范围、网络与工具策略 | 通过 | Instruction defines editable submission and public files, no-network/web/download/SSH restrictions and permitted local shell/Python plus bounded Dev evaluation. |
| QA21 三个 JSON 的填写内容 | 通过 | Both trajectories, annotation and summary parse and map to current methods. Seed round48 failed-worker fallback0 becomes score:null with original failure retained; export failures have no invented score/time. |

风险提示（不额外计入清单结论）：Clock interpretation: expert_evidence/latest-user-research-clock-policy.json permits ordinary author reasoning, edits, tools, compilation, scoring and method failures and waives hard nominal minima; fixed QA0.3.4 still requires its 7h/10h gates. This review applies the independently justified short-iteration exception to demonstrated lower bounds only. Exact totals and unknown intervals remain null; collector-generated pass text must not be read as an exact-duration certification.；Log scope: optimization_evidence/训练证据说明.md and expert_evidence/current-worker-journal-provenance.json disclose absent current GPU stdout and repeated whole-job CPU audit logs. Raw stage rows, Trial output and existing CPU audit are available, but this static review neither authenticates the original logs nor independently reruns the model.；Portability/history: Runtime/README.md and expert_evidence/method-evolution/gpt.json contain older source/count/status snapshots. Current 48-file manifests, actual Trial configs and current selected artifacts were checked directly. Pinned dependencies and public checkpoint materialization descriptors are supplied; no network retrieval, external platform acceptance, privacy release certification or two-review consensus is established here.。

# 退回专家说明

待质检员核实的格式观察（等价材料可以认可，不直接作为专家整改结论）：
- expert_evidence/trajectory-format-mapping.json：最终轨迹 JSON 必须包含 rounds 数组。
- expert_evidence/trajectory-normalization-provenance.json：最终轨迹 JSON 必须包含 rounds 数组。
- expert_evidence/trajectory_codex-original-records.json：top-level JSON value is not an object
- expert_evidence/trajectory_seed-original-records.json：top-level JSON value is not an object
- optimization_evidence/baseline_runs/seed_101/model：训练型任务每个 seed 必须保留 model/。
- optimization_evidence/baseline_runs/seed_202/model：训练型任务每个 seed 必须保留 model/。
- optimization_evidence/baseline_runs/seed_303/model：训练型任务每个 seed 必须保留 model/。
- optimization_evidence/reference_runs/seed_101/model：训练型任务每个 seed 必须保留 model/。
- optimization_evidence/reference_runs/seed_202/model：训练型任务每个 seed 必须保留 model/。
- optimization_evidence/reference_runs/seed_303/model：训练型任务每个 seed 必须保留 model/。
- workspace/harbor_task：workspace/ 必须包含 harbor_task/。
- workspace/reference：workspace/ 必须包含 reference/。
