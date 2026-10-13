# 安装验证报告

目标仓库：`ma18685948879-svg/su-`。检查时连接中仅此一个仓库，且没有既有文件；因此采用它作为安装目标。原始任务工作目录未挂载 Git 仓库，本次通过 GitHub 连接获取目标并建立仓库副本。

## 文件安装与版本

| Skill | 安装目录 | 上游固定提交 | 文件状态 |
|---|---|---|---|
| Folio | `.agents/skills/folio/` | `8b6ef0f4dfaef624ddcdd3b018b0fcb9d0358ae7` | 88 个上游文件，独立适配入口，生产资源已校验 |
| Guizang PPT Skill | `.agents/skills/guizang-ppt-skill/` | `c91369c449d34755d320a8b81d0734000d99d1ab` | 40 个上游文件，独立入口与可选测量依赖 |
| Industrial Design Portfolio | `.agents/skills/industrial-design-portfolio/` | `653fbd3c4b070c72cbd21a3253aa9300940835d8` | 123 个上游文件，空间设计叙事适配入口 |

Skill 的来源、原文件 SHA-256 与省略清单在各自 `UPSTREAM.json`；全局固定版本在 `skills-lock.json`。Folio VERSION 为 1.0.17；固定 commit 比版本名更精确。

保留上游原文为 `SKILL.upstream.md`；Industrial 的原 AGENTS 与 UI 元数据单独保留为 `AGENTS.upstream.md`、`agents/openai.upstream.yaml`。入口只保留 `name` / `description` 前置元数据，便于 Codex 识别。三个 Skill 各自一套原始文件，没有相互覆盖。

Folio 大型 `demos/` 与上游 README 用展示截图 / 宣传图未复制；模板、设计引擎、参考布局、脚本、生产资源完整保留。部分 README 演示链接因此需要访问固定版本上游，不影响生产入口；不将演示文件省略误报为完整镜像。

## 已执行的检查

- 三个适配入口通过 Skill Creator 的 `quick_validate.py`。
- `scripts/verify_skills.py` 核对三个目录、251 个上游文件哈希、版本索引与关键资源，0 error。
- Folio 使用原始 lock 执行 `npm ci --ignore-scripts`；Guizang 独立固定 Playwright 1.60.0 并生成 lock。Node 包恢复成功。
- Industrial 核心依赖为 Python 3 标准库；布局库校验、上游灯具案例 manifest 校验和 HTML 结构校验均通过。
- Guizang 两套模板的演讲者 CSS 与 JavaScript 字节同步检查通过。
- 只读上游版本查询成功；检查时三个固定提交均与各自上游 HEAD 一致。
- 本次没有制作任何用户 PPT，也没有调用图片生成。

## 依赖限制与未验证项

当前环境：Node 24.19.0、Python 3.12.14。核心脚本与 Node 包可用；**Chromium 未配置完成**。Playwright 下载 Chrome for Testing 148.0.7778.96 / revision 1223 返回无效 ZIP，解压失败；未发现可替代的本地 Chromium。

因此以下项目尚未验证，不应宣称导出端到端可用：

- Folio 实际 PPTX / PDF / IDML / Figma 导出运行；
- Guizang 的真实浏览器几何测量与演讲者交互；
- Industrial 的实际浏览器 / PDF 视觉效果；
- PowerPoint / Keynote / Google Slides 中的字体、换行与渲染。

在允许 Playwright 下载的 Codex 环境中运行 `python scripts/setup_skills.py`，完成 Chromium 安装；只恢复 Node 包可运行 `python scripts/setup_skills.py --skip-browser`。Linux 缺少系统库时需允许安装 Chromium 的系统依赖。模块验证通过不能代替浏览器启动与视觉验收。

Industrial 上游的浏览器测试包 `@playwright/test 1.62.1` 和 Python `jsonschema 4.26.0` 是可选开发测试依赖，本次未安装；核心 HTML 生成与 Python 校验不要求它们。需要时使用独立 `.venv` 与该 Skill 自己的 node_modules，不混入 Folio / Guizang。

## 输出能力与选择

| Skill | 必要输入 | 输出 | PPTX 可编辑性 | 本仓库用途 |
|---|---|---|---|---|
| Folio | 项目、原图与文案、图片归属；页数/比例可推断 | HTML 与多种导出路线：PPTX、PDF、IDML、Figma | 原生文字和支持对象；复杂视觉与图像资产可能栅格化 | 默认建筑 / 景观 / 室内图文汇报 |
| Guizang | 文案、图片、明确风格；讲稿/时长可选 | HTML；图片资源需随文件交付；截图/PDF 为额外衍生 | 无内置原生导出，不等同于传统 PowerPoint | 明确瑞士风 / 杂志风 / HTML 展示 |
| Industrial | 现状/问题、草图/CAD/渲染、过程、证据来源、个人贡献 | HTML + images + portfolio_manifest.json + source_notes.md；可打印 PDF | 无内置原生导出 | 过程展示、作品集叙事与方案演变 |

Folio 的 PPTX 不是所有 HTML 效果的等价复制；不能承诺图纸内部线条可编辑。Guizang / Industrial 需要 PPTX 时，应先说明重建或转换限制，不未经说明切换或组合 Skill。

## 复用与更新

下次在 Codex 中选择此仓库，按 README 示例指定 `$folio`、`$guizang-ppt-skill` 或 `$industrial-design-portfolio`。未自动识别时直接读取对应 `SKILL.md`；仓库安装不代表当前聊天的全局 Skill 列表已经刷新。

依赖不提交 Git，锁文件与恢复脚本随仓库保存。更新通过只读查询和独立分支审阅进行，不在子目录 `git pull`、自动覆盖适配入口或注册全局 hook。

Guizang 保留 GPL-3.0；Folio 与 Industrial 保留 MIT。安装不会更改原授权。

省略项还包括 Folio 的 README 截图和实验版式 PNG 概览、Guizang 宣传大图、Industrial 的 README / Showcase 预览截图。源文件逐项列于 UPSTREAM.json；Industrial 灯具示例 HTML 和所引用的生成图片仍保留。功能模板与校验器没有省略。
