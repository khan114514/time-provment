# OneDC / Bifrost 10小时研究时长证据

**目标：OneDC 与 Bifrost 的 GPT、Seed 四条轨各自至少 10 小时（36,000 秒）有效研究。** 不采用7小时例外，不把两轨或两题相加。此仓库保存已找回的证据、复算工具和后续补证入口；**目前不能证明四轨均达10小时，也不是新一轮实验或QA通过包。**

## 当前已找到的时间

| 题目/轨 | 证据中的时长 | 数值性质 | 对10小时目标的缺口 |
|---|---:|---|---|
| OneDC GPT | 5.140840h | 旧正式段墙钟上界，未扣无效区间 | 即使全计仍至少缺4.859160h，扣除后更大 |
| OneDC Seed | 5.233804h | 旧正式段墙钟上界，未扣无效区间 | 即使全计仍至少缺4.766196h，扣除后更大 |
| Bifrost GPT | 7.174629h | 160个保守观察区间的和 | 相对该下界还差2.825371h，活动分类仍须核定 |
| Bifrost Seed | 7.739001h | 363个保守观察区间的和 | 相对该下界还差2.260999h，活动分类仍须核定 |

Bifrost精确净有效总时长仍未知。上述差值不是认定“实际只做了这些时间”，也不是承诺恰好补跑该差值就一定通过。OneDC的SAM27新候选账本尚未在本次本地/网盘检索中定位，旧v9段结论不能覆盖未收到的新段。迁移/新段必须说明与原版本的连续性，不能直接相加。

## 直接读取这些文件

- [当前10小时合同](policy.json) 与 [四轨状态/缺口](status.json)。它们表达本次用户要求，优先于原件中的旧放宽口径。
- OneDC：[旧时间账本](onedc/expert_evidence/time-accounting.json)、[118份原始started/audit](onedc/evidence/original_clock_records)、[逐轮控制器历史/代码/反馈](onedc/expert_evidence/final_research_history)、[缺号及未闭合尝试](onedc/evidence/missing_attempts)、[旧时间来源](onedc/expert_evidence/time_authority)。
- Bifrost：[可复算区间原件](bifrost/expert_evidence/original-source-method-loops/conservative-clock-source-accounting.json)、[原生/服务端时钟及排除记录](bifrost/expert_evidence/recovered-original-duration)、[方法反馈闭环](bifrost/expert_evidence/original-source-method-loops)、[GPT后续原作者工作](bifrost/expert_evidence/original-GPT-user10h)、[Seed额外工作](bifrost/expert_evidence/original-Seed-extra-work)、[最终复验](bifrost/expert_evidence/release-full-validation)。
- [OneDC历史双复核](onedc/historical_reviews/20261022)、[Bifrost历史双复核](bifrost/historical_reviews/20261022)。Bifrost A将QA16判为待核、B按7h例外通过；保留原文，但**两者都不能证明本次10h目标达标**。
- [来源文件映射](provenance/source_map.json)、[发布派生说明](provenance/public_path_derivations.json)、[文件SHA256清单](MANIFEST.json)。源定位为本地项目相对路径，不含用户主目录。

专家证据包含两轨、Reference及历史私有评测材料，供可信主控和审核者使用。**不要把整仓库发给研究Actor。** 每轨只接收题目允许的公开输入及本轨合法历史，维持两轨独立。

## 核验

在仓库根目录运行：

```bash
python3 tools/verify_evidence.py
```

工具逐文件核对SHA256，重算Bifrost区间、重叠及OneDC正式起止，并检查四轨10h政策。它只确认文件完整性和算术，不代替研究活动分类、版本连续性或正式QA，不把原文件mtime当实验时间。

## 后续如何补足

1. 按四轨分别收集原始开始/结束、方法修改、Public/Dev反馈、决策和排除区间。正常失败方法也可以构成研究证据，不能把CLI失败直接等同整轮零研究；API连接成功也不能把阻塞时间全算研究。
2. 先分类现有区间、合并重叠并扣除无效段；保留未核定项，不把旧14h宽口径、wall span、估计值、模型权重时间戳当有效时长。
3. 若继续真实研究，在实际获授权的运行环境由各轨独立续接。新增原件放对应题目`additional_runs/`，记录真实模型、会话、版本、代码/结果位置及扣除理由；不改旧证据，不空转凑数。
4. 每轨最终净有效时间达到36,000秒后，提交可复算的完整账本、原始日志、最佳方法及所需复验。最终复验、12h稳定性、QA、打包分别统计。
5. 再更新`status.json`和清单，完成适用的独立复核后才能声称10h目标通过。

豆包/Ark/Seed沿用用户指定模型和火山Coding Plan `/api/coding/v3/chat/completions`；可信主控读取本机受保护配置，任何凭据不得进入本仓库或Actor。不自动回退按量接口。

## 百度网盘查找结果与范围

已直接查看客户端：

- `电脑大文件归档_OneDC资产_20261010_203405`：onedc-assets.tar.gz（8.56GB）。
- `电脑大文件归档_OneDC旧环境_20261012_103401`：onedc-env-v8.tar.gz（14.08GB）和onedc-env-v5-preflight.tar.gz（14.00GB）。
- `电脑大文件归档_Bifrost公开模型原包_20261020_014917`：六个safetensors权重分片及归档清单。

这些是资产/环境/模型归档，本次未发现新增研究时长日志，未下载重新解包云端大文件，也未宣称穷尽全盘。Bifrost本地完整任务ZIP中的保守计时文件与本仓库对应原件逐字节一致，SHA256为`659b32b6622fcd3b3b18a5b92473445a0ff00d29a557c12d5a874d16baae736a`。

本仓库附配套评分/方法源码以方便理解证据；没有上传大模型权重，不能把此证据仓库当成已验证可独立运行的完整任务交付。
