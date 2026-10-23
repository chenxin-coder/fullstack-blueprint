# 借鉴来源与适用边界

查阅日期：2026-10-23。以下是一手仓库资料的设计思想摘要，均用本 skill 的中文规则重新表达；不复制实现、第三方提示词或完整模板。分支链接可能随上游更新，本 skill 不宣称始终与上游同步。

| 来源 | 采纳的思想 | 本 skill 的取舍 |
|---|---|---|
| [Bulletproof React：目录](https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md) | 业务聚合、单向依赖、仅创建所需目录 | 不固定完整 features 子目录；已有公开入口规则优先，不照搬直接导入策略 |
| [Bulletproof React：请求层](https://github.com/alan2207/bulletproof-react/blob/master/docs/api-layer.md) | 共用 client，明确 endpoint 类型与请求声明 | query hook 按状态与缓存需求引入，不给单次请求增加空包装 |
| [FastAPI 全栈模板：前端说明](https://github.com/fastapi/full-stack-fastapi-template/blob/master/frontend/README.md) | 后端 OpenAPI 与生成客户端同步 | 保持 OpenAPI 与前端类型同步，不复制模板的其他技术选型 |
| [FastAPI 全栈模板：配置](https://github.com/fastapi/full-stack-fastapi-template/blob/master/backend/app/core/config.py) | 类型化配置、配置有效性校验 | 仅借鉴校验思想，使用 YAML 唯一来源；不照搬环境变量、导入时实例化或忽略额外字段 |
| [Node Best Practices：分层](https://github.com/goldbergyoni/nodebestpractices/blob/master/sections/projectstructre/createlayers.md) | 传输入口、业务处理、数据访问分责 | 将三类职责用于设计判断，不要求三个目录或所有调用都经过包装层 |
| [Node Best Practices：日志](https://github.com/goldbergyoni/nodebestpractices/blob/master/sections/production/smartlogging.md) | 有意义的事件、结构化上下文和关联标识 | 按需采用；不自动引入特定日志库、APM 或集中日志集群 |
| [Node Best Practices：配置](https://github.com/goldbergyoni/nodebestpractices/blob/master/sections/projectstructre/configguide.md) | 配置分组、密钥隔离、尽早校验 | 舍弃文件与环境变量合并；明确采用 YAML 加载，无环境变量覆盖链 |
| [Anthropic：Skill Creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | 短入口、按需参考、真实任务验证 | 保持技能自包含，无必需联网、插件或其他 skill 依赖 |

## 当前项目提供的个人偏好

新项目使用 [个人默认基线](project-baseline.md)。职责清晰、测试先行、当前契约直接实现、抽象基于现实需要；日志先初始化且只记安全标识。前端统一使用同源 API，由开发代理和正式 Nginx 网关转发；后端各自读取应用根目录的 `config.yaml`，中间件在同一文件中独立分段维护。配置不使用环境变量或覆盖链。

Sphere 四层决策模型、共享数据库账户、特定 schema/表名、应用拆分和离线评估权限属于原项目。此 skill 不携带这些领域规定，也不为新项目添加 Sphere 命名。使用时仍需读取所在仓库的最新 AGENTS.md 和实际检查入口。
