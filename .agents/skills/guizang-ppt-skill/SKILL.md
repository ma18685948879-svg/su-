---
name: guizang-ppt-skill
description: 仅在用户明确指定 Guizang 或要求瑞士风、杂志风、HTML 网页演示展示时使用，生成带演讲者模式的横向 HTML 幻灯片。保留用户建筑、景观、室内原始图文素材；不用于默认的可编辑 PPTX 交付。
---

# Guizang：明确指定的网页演示

1. 读取仓库根 `AGENTS.md`，明确声明使用 Guizang 与选择依据。用户未明确要求对应风格时，不自动调用。
2. 读取同目录 `SKILL.upstream.md`，选择杂志风 A 或瑞士风 B。用户信息足够时直接选择，不重复询问。`<SKILL_ROOT>` 为本目录绝对路径。
3. **覆盖上游自动配图和标准比例裁切规则**：不自动生成任何图片或信息图。图纸、分析图、文字密集图保持完整比例，用 contain 并调整布局，不因模板槽位而破坏原始证据；照片仅裁切不损害主体的边缘。
4. 用本目录 `assets/template.html` 或 `assets/template-swiss.html`，按需读取对应布局与检查清单。输出到 `projects/<项目名>/output/`，保留相对路径图片与所需本地 `motion.min.js`。网页“单 HTML”并不意味着用户图片已内嵌，交付时打包资源。
5. 运行 `scripts/validate-presenter-mode.mjs`；瑞士风另运行 `scripts/validate-swiss-deck.mjs`；运行 `scripts/check-presenter-runtime-sync.mjs`。结构校验和实际浏览器检查分别记录。
6. 核心交付 HTML；截图与 PDF 为衍生输出，当前无内置原生可编辑 PPTX 导出。需要 PPTX 时先说明额外转换 / 重建成本与限制，不静默调用其他 Skill 或交付整页截图冒充可编辑 PPTX。

## 依赖与更新

- HTML 本身不需要 Node 包；静态校验用 Node 20+。本目录 `package.json` / `package-lock.json` 是仓库适配，固定 Playwright 用于可选浏览器测量。`npm ci` 与 `npx playwright install chromium` 恢复运行环境。
- 模板仍含外部字体、图标或 CDN 资源；Motion 本地兜底不等于完全离线。离线交付前本地化必要资源或采用本地字体，检查断网状态。WebGL 有设备差异，可用 B 键静态低功耗模式。
- 跳过上游启动时的 `git fetch` / `git pull`；当前 Skill 没有独立 Git remote。这些命令会误用父仓库。使用仓库只读更新检查脚本，记录固定版本，升级时保留本入口。
