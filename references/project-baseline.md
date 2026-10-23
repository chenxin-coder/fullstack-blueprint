# 新项目默认基线

新项目直接采用下列个人工程约定，用户只需提供业务目标、核心流程、权限和其他实际约束。将业务设计纳入当前 Superpowers 阶段；不重复询问已明确的工程选择。局部修改只加载本次相关规范。

## 固定起点

| 内容 | 约定 |
|---|---|
| 前端 | React + TypeScript + Vite；页面按功能模块组织，专属样式使用 CSS Modules，公共视觉变量集中维护 |
| 后端 | Python + FastAPI + Pydantic；使用 uv 管理依赖并提交 uv.lock，创建时确定并锁定运行时与依赖版本 |
| 应用组织 | 一个前端、一个按业务模块组织的后端；模块在进程内通过公开操作协作 |
| 扩展依据 | 依据实际业务选择持久化及中间件；有明确部署或隔离需求时才拆独立服务，判断见 [架构参考](architecture.md#选择最小够用的模式) |

## 最小工程结构

```text
frontend/
  src/
    app/                         # 路由与页面组合
    features/<feature>/          # 功能 UI、状态、辅助函数、局部样式
    api/                         # client 与按业务分文件的接口
    shared/                      # 真正跨功能复用的 UI、工具、视觉变量
backend/
  config.yaml                    # 应用、日志、数据源与中间件独立配置段
  config.example.yaml            # 可提交的配置示例，凭据使用无效占位值
  pyproject.toml
  uv.lock
  src/<app>/
    main.py                      # 资源装配与生命周期
    modules/<feature>/           # api、业务、数据访问、契约模型
    infrastructure/
      settings.py                # 汇总配置模型，绑定各 YAML 配置段
      logging.py                 # 日志初始化
      middleware/<component>.py  # 每种中间件的配置类与接入类，按实际选用创建
  tests/
README.md
AGENTS.md
```

按真实职责创建所需文件，不预建空目录、空转 service 或通用中间件框架。业务模块内部拆分见 [后端参考](backend.md#先分职责再分目录)，前端依赖与样式归属见 [前端参考](frontend.md#职责与依赖)。

## 设计与实施落点

设计说明核心操作、不变量、模块归属、接口与数据所有权，分别列出运行时调用和源码依赖。同源调用与错误响应遵守 [HTTP 参考](http.md)，配置加载与日志字段遵守 [日志和配置规则](logging-config.md)，不另选一套规则。

获授权实施后，先建立配置校验、日志和资源生命周期，再打通一个真实功能的页面、接口、业务及数据访问，验证正常、拒绝与失败行为；仅设计任务交付方案。中间件按 [接入规则](backend.md#中间件接入) 追加，配置统一维护在同一 `config.yaml`。

README 记录项目用途、启动与检查命令；AGENTS.md 只记录项目特有的边界与质量要求，不复制整份 skill。设计与功能说明使用中文。验证类型检查、相关测试与构建，报告实际执行结果。
