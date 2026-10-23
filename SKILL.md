---
name: fullstack-blueprint
description: Use when starting a fullstack project, or building, changing, designing, or reviewing application architecture, frontend pages/components, backend APIs/business modules, middleware integration, module layering, frontend-to-backend calls, application logging, YAML configuration, or consistency between business documentation and implementation. 新项目初始化、架构设计、功能变更、模块重构、中间件接入、日志与配置维护、文档与代码一致性检查时适用。 Excludes unrelated prose or typo-only edits, pure algorithms, standalone scripts unrelated to these concerns, and non-software tasks.
---

# 全栈工程蓝图

将个人项目经验沉淀为可复用的全栈工程蓝图，提供新项目默认基线、模块职责、依赖方向和工程约定，并用于后续设计、实施与审核。

以最小够用的结构明确职责、依赖和失败处理。用户明确要求优先，默认沿用项目命名、公开入口、日志格式及质量门禁。

## 使用与交付

从请求和已确认上下文识别设计、审核或实施及本次范围；仅在缺失信息阻碍正确处理时提问。读取适用的 AGENTS.md、相关现行文档、实现、契约和测试，按下表加载必要章节。区分事实、约束和建议，资料不足时注明假设。

| 任务 | 处理与输出 |
|---|---|
| 设计 | 给出选择依据、必要模块职责与依赖、行为约定及验收方式；业务代码实施以用户请求为准 |
| 审核 | 按影响列出问题位置/证据、影响和最小建议；区分违规、可选优化及待验证疑点，无问题则如实说明；不改文件 |
| 实施 | 完成已授权改动，核对本次涉及的职责、依赖、契约及失败处理；报告实际变化、必要取舍、文档同步或无需更新的依据、实际验证及未验证部分 |

用中文交付并保留准确标识。局部任务几句话即可，无需套用整套标题；涉及关系时标明运行时调用或源码依赖，只展示相关部分。设计/审核不自动生成脚手架、添加依赖或提交代码。

## 核心约束

- 在本次任务范围内应用统一规范。按业务归属组织代码，层与目录按实际职责增加；少量文件、简单函数及直接依赖均可用。共享与抽象基于真实复用或变化需求，架构参考中的模式按条件选择。
- 前端统一使用同源 `/api/v1/...`，由开发代理和正式网关转发；后端各自从应用根目录的 `config.yaml` 加载并校验配置，不使用环境变量、.env 或覆盖链。
- Superpowers 可用时，由其适用技能控制当前阶段，本 skill 提供相关工程约束。复用设计、计划、确认和验证记录，将代码、文档与验收纳入同一任务；不重复流程/确认，不跳过尚未满足的要求，也不强制跑完整链路。不可用时按本 skill 执行，无需额外安装。故障先诊断，业务行为修改测试先行，完成结论以实际验证为据。

## 文档与业务逻辑一致性

- 定位本次受影响的 README、架构/功能/接口说明、配置/运行示例和代码注释。结合已确认需求、规则、契约、实现与测试判断应修哪方；不能仅凭旧文档或测试通过认定行为正确。
- 行为、职责、调用、接口、权限、状态、错误、日志、配置或运行方式变化时，同次更新现行说明及示例，缺少必要说明时就近补最小文档。纯内部调整未改变文档约定时说明无需更新的依据。
- 规划标明尚未实现；历史设计、评审和回放保留当时事实，必要时补现行指引。
- 对照“本次变化 → 实现/测试证据 → 现行文档位置”，核对字段、示例、边界与运行命令，并适当验证可执行例子。受影响内容仍矛盾时不报告完成；仅报告实际核查范围及未验证项。

## 按需参考

| 涉及内容 | 读取内容 |
|---|---|
| 新建项目或初始化工程 | [project-baseline.md](references/project-baseline.md)，再按业务确定 [架构职责](references/architecture.md) |
| 新业务模块职责/接口/依赖设计、模块边界重构或分层审核 | [architecture.md](references/architecture.md) |
| 前端页面、组件、状态或样式 | [frontend.md](references/frontend.md) |
| 后端模块、业务规则、数据访问、事务或中间件接入 | [backend.md](references/backend.md) |
| 接口新增/修改/审核、联调、请求失败或重复提交 | [http.md](references/http.md) |
| 日志或异常记录 | [logging-config.md：日志生命周期](references/logging-config.md#日志生命周期) |
| 后端 YAML 配置、中间件配置、代理配置或应用初始化 | [logging-config.md：配置生命周期](references/logging-config.md#配置生命周期) |

只读相关章节，按影响选择验证项并遵守项目检查要求；局部字段、样式或日志修改不自动加载架构参考。查询借鉴来源时才读 [sources.md](references/sources.md)。
