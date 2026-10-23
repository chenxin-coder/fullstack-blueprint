# fullstack-blueprint · 全栈工程蓝图

一套供 Codex 使用的个人全栈工程设计 skill，将项目经验整理为可复用的前后端设计、模块分层、接口调用、配置、日志和文档维护约定。

新项目提供业务目标、核心流程、权限和实际约束，即可从统一的工程基线开始；已有项目按本次任务范围应用相关规范，结构随真实职责增加。

## 适用场景

- 新建全栈项目，确定默认技术栈、模块职责和工程结构。
- 新增页面、业务模块或 API，明确前后端调用和依赖方向。
- 调整模块边界，审核分层是否承载实际职责。
- 接入中间件，维护配置、资源生命周期和日志。
- 修改业务行为时，同步核对现行文档、示例与实现。

## 核心约定

| 方面 | 约定 |
|---|---|
| 默认技术栈 | 前端 React + TypeScript + Vite；后端 Python + FastAPI + Pydantic，使用 uv 与 uv.lock |
| 模块分层 | 按业务能力组织，模块内部按实际职责拆分接口、业务和数据访问；新项目从一个前端、一个模块化后端起步 |
| 前端归属 | 功能 UI、状态、辅助函数和专属样式随功能维护；新项目使用 CSS Modules，真实跨功能能力进入 shared |
| API 管理 | 统一 API 目录，按业务模块维护路径、类型和请求函数，共用 HTTP client；页面调用命名函数 |
| 前后端调用 | 浏览器使用同源 `/api/v1/...`，开发代理与正式 Nginx 网关维护后端目标地址 |
| 后端配置 | 每个后端应用以自身根目录的 config.yaml 为唯一配置来源，严格校验，修改后重启生效；不读取环境变量或 .env |
| 中间件 | 按业务需要引入，配置统一放在同一 config.yaml 的独立配置段；每个组件独立文件维护配置类与接入类，由入口装配和释放资源 |
| 日志 | 统一结构化 JSON 输出到 stdout，使用稳定标识和 request_id 关联；同一失败由负责边界记录，过滤敏感信息 |
| 文档一致性 | 行为或约定变化时，同次更新受影响的现行说明与示例，并用实现和验证证据核对 |

以最小够用为原则：简单功能可以使用少量文件和直接函数调用，抽象、共享与独立服务依据真实需求增加。完整规则以 [SKILL.md](SKILL.md) 及其参考文件为准。

## 安装到 Codex

准备好 Git，并确保 GitHub 账号拥有本仓库的访问权限。首次安装时，将仓库克隆到用户级 skill 目录：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/chenxin-coder/fullstack-blueprint.git ~/.agents/skills/fullstack-blueprint
```

以上命令用于目标目录尚不存在的情况。已有安装时，在确认本地改动已处理后更新：

```bash
git -C ~/.agents/skills/fullstack-blueprint pull --ff-only
```

Codex 会发现该目录中的 skill；若未显示，重启 Codex 后检查。用户级目录与加载方式见 [Codex 官方 skill 文档](https://learn.chatgpt.com/docs/build-skills#where-to-save-skills)。

## 使用方式

明确指定 skill：

```text
$fullstack-blueprint 帮我设计一个设备借用管理系统，包含申请、审批和归还流程。
```

```text
$fullstack-blueprint 为当前项目新增订单查询页面与 API，按现有模块边界实现，并同步相关文档。
```

```text
$fullstack-blueprint 审核当前项目的前后端分层、API 调用、配置和日志处理，只报告有证据的问题。
```

[agents/openai.yaml](agents/openai.yaml) 已设置 `allow_implicit_invocation: true`，允许 Codex 在任务匹配 skill 描述时自动选择它；希望明确使用时，在请求中写出 `$fullstack-blueprint`。

已安装 Superpowers 时，由其适用技能控制当前阶段，本 skill 提供工程约束，复用已有设计、计划、确认和验证记录。未安装时仍可独立使用。

## 内容导航

| 文件 | 内容 |
|---|---|
| [SKILL.md](SKILL.md) | 使用范围、任务交付、核心约束与文档一致性要求 |
| [agents/openai.yaml](agents/openai.yaml) | 显示信息、默认提示与自动调用策略 |
| [references/project-baseline.md](references/project-baseline.md) | 新项目默认技术栈与最小工程结构 |
| [references/architecture.md](references/architecture.md) | 业务职责、模块接口、分层选择与依赖方向 |
| [references/frontend.md](references/frontend.md) | 前端功能模块、状态、共用能力和样式归属 |
| [references/backend.md](references/backend.md) | 后端职责、事务、模块协作与中间件接入 |
| [references/http.md](references/http.md) | 接口集中维护、契约、错误、超时与重复提交 |
| [references/logging-config.md](references/logging-config.md) | 日志字段、配置校验、资源装配与生效方式 |
| [references/sources.md](references/sources.md) | 借鉴来源与采用范围 |

维护时更新对应规则文件，并同步本 README 中受影响的说明；按本次变更范围验证，避免将项目专属业务规则加入通用 skill。
