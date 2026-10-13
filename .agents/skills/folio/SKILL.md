---
name: folio
description: 默认用于建筑、景观、室内作品集、案例分析和原始图文素材的专业排版，导出文字及支持对象可编辑的 PPTX。保留摄影、效果图、图纸、分析图和文案，注重版心、留白、主次、对齐与跨页节奏。
---

# Folio：建筑排版适配入口

1. 读取仓库根 `AGENTS.md`，声明本次使用 Folio 及依据。只使用本 Skill。
2. 读取同目录 `SKILL.upstream.md`，按需读取 `design/`、`engines/`、`reference-layouts/` 与 `references/`。所有 `<SKILL_ROOT>` 替换为本目录绝对路径。
3. **覆盖上游默认**：根据用户素材规划页数；建筑 PPT 默认文字可编辑 PPTX，HTML 是编排与审阅中间稿。默认 Architectural / Editorial 的克制排版，白或暖白底，不强制森林绿主题。不要自动套用“8 页 + Minimal + 仅 HTML”。
4. 先做素材清单、图像角色与版心合同，再排页面。图纸、分析图、轴测图完整等比展示；照片裁切保留主体。素材缺失时记录缺口，不用 AI 重绘补齐。文案保持原意，不编造结论。
5. 从本目录 `index.html` 及布局参考起稿，将项目写入仓库 `projects/<项目名>/`。不覆盖输入原件，不把上游示例图片或文案当作用户作品。
6. 对需要 PPTX 的任务，选择上游导出器支持的布局；复杂自定义 HTML 必须检查转换损失。执行 `node <SKILL_ROOT>/scripts/export-native-pptx.mjs <项目 HTML 绝对路径>`。文字原生可编辑；图片与部分复杂视觉对象会栅格化，不保证图纸内部可编辑。
7. 执行合适的导出校验，并逐页视觉检查。没有 PowerPoint 应用渲染时，明确说明该项未验证。

## 依赖与更新

- `package.json` 和 `package-lock.json` 保持上游原件。Node 20+；`npm ci` 后执行 `npx playwright install chromium`。脚本需要 Playwright、PptxGenJS、pdf-lib；fig-kiwi 供可选 Figma 工作流。
- 常规 HTML / PPTX / PDF 无需 API key。Figma Code.to.Design 路线可选 `C2D_API_KEY`，不得写入 Git。
- 本安装是固定版本 vendoring，不是独立 Git clone。跳过上游自动检查 / self-update / hook，改用仓库 `scripts/check_skill_updates.py` 只读检查；版本与原文件哈希在 `UPSTREAM.json`。更新不应阻塞排版。
- 生产资源完整复制；大型 `demos/` 和上游 README 用展示截图 / 宣传图省略，上游文档里的演示链接可能需打开对应 GitHub 固定版本。
