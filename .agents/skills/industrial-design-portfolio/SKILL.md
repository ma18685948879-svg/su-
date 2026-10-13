---
name: industrial-design-portfolio
description: 用于建筑、景观、室内设计作品集的证据叙事、方案演变和草图/CAD/渲染组合编排，适合过程展示、作品集重构与面试讲解。以结构化 HTML 作品集为原生输出，PDF 为衍生格式，不原生输出可编辑 PPTX。
---

# Industrial Design Portfolio：空间设计过程叙事适配

1. 读取仓库根 `AGENTS.md`，说明本次使用 Industrial Design Portfolio，因为需要过程 / 决策 / 证据叙事。
2. 读取 `SKILL.upstream.md`；路径都相对于本目录。按需读取 story-architecture、layouts、visual-system、style-presets、image-policy 与 checklist。
3. 将工业设计分析视角映射为空间设计：用户 / 场地 / 现状 → 空间问题；草图 / CAD / 分析图 / 模型 → 方案演变；效果图 / 建成摄影 → 结果与氛围。不要强行加入制造工艺、产品 CMF、测试人数、成本或不存在的性能数据。
4. 先审计素材与个人贡献，再做 evidence map、story table、layout plan。保留来源与不确定性。保持上游 manifest 的 schema 与证据字段，但只写用户已有材料支持的内容。
5. 使用 `assets/portfolio-template.html`、注册 IDxx 布局和一个统一视觉系统。图纸与分析图完整 contain；不拉伸、不裁掉标注。所有可选生图默认关闭，不用生成图代替真实 CAD 或研究证据。
6. 输出到 `projects/<项目名>/output/`：`index.html`、`images/`、`portfolio_manifest.json`、`source_notes.md`。HTML 的可编辑性不等于 PowerPoint 可编辑性。
7. 先运行 `python <SKILL_ROOT>/scripts/validate_manifest.py <manifest>`，再运行 `validate_portfolio.py <HTML>` 与 `validate_layout_library.py`；做实际浏览器检查后，按需打印 / 导出 PDF。
8. 需要可编辑 PPTX 时先说明本 Skill 没有内置原生导出；若用户允许 Folio 承接，先说明两个阶段与转换限制，不未经说明混用。

## 依赖与更新

- 核心校验脚本只依赖 Python 3 标准库，不要求 API key 或生成图片服务。
- 上游 `package.json` / lock 固定 `@playwright/test`，供可选浏览器测试，不是核心 HTML 排版运行依赖。`requirements-test.txt` 的 jsonschema 是可选 schema 测试依赖，可在独立 venv 中恢复。
- 上游适配文件改名为 `AGENTS.upstream.md` 以避免对本目录自动施加与仓库入口不同的默认指令。原件哈希与版本见 `UPSTREAM.json`。
- 使用仓库只读更新检查脚本；不通过上游安装器覆盖本地入口。
