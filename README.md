# 建筑 / 景观 / 室内设计排版 Skills

三套独立 Skill 用于用户提供的摄影、效果图、图纸、分析图与文案编排。默认保留原始素材，不自动生图；调用规则见 [AGENTS.md](AGENTS.md)。

## 目录

```text
.agents/skills/
├── folio/
├── guizang-ppt-skill/
└── industrial-design-portfolio/
projects/
scripts/
├── setup_skills.py
├── verify_skills.py
└── check_skill_updates.py
AGENTS.md
README.md
INSTALLATION_REPORT.md
skills-lock.json
```

每个 Skill 均包含独立的 `SKILL.md` 适配入口、`SKILL.upstream.md` 上游原文、资源、脚本、许可证和 `UPSTREAM.json` 版本校验记录。无嵌套 `.git`，无 submodule。Folio 的大型 `demos/` 和上游 README 用展示截图 / 宣传图省略；生产资源与布局参考保留。具体省略清单可审计。

## 定位与格式

| Skill | 最适合 | 输入 | 原生输出 | 可编辑 PPTX |
|---|---|---|---|---|
| Folio（默认） | 建筑 / 景观 / 室内作品集、案例分析、设计汇报 | 原始摄影 / 效果图 / 图纸 / 分析图 / 文案，项目和来源信息 | HTML；提供 PPTX、PDF、IDML、Figma 导出路线 | 支持文字及部分原生对象；图片内部与复杂效果不保证可编辑 |
| Guizang PPT Skill | 明确要求的瑞士风 / 杂志风 / HTML 演讲展示 | 主题、文案、原图、风格选择；讲稿和时长可选 | HTML + 本地资源；截图 / PDF 需额外处理 | 没有内置原生导出；转换不等于原生可编辑 |
| Industrial Design Portfolio | 设计问题 → 方案演变 → 决策 → 成果，草图/CAD/渲染组合 | 项目素材、过程与个人贡献、证据和来源 | HTML、images、manifest、source_notes；可打印 PDF | 没有内置原生导出 |

推荐流程：默认 Folio → 素材清单 → 页序与主辅图 → 统一版心 → HTML 编排与逐页审阅 → PPTX 导出与校验。只有明确网页风格展示需求时切 Guizang；当过程与证据叙事是重点时用 Industrial。不未经说明混用。

## 调用示例

在 Codex 任务中选择 / 挂载本仓库，然后输入：

```text
使用 $folio，把我上传的建筑摄影、平面图、分析图和文案排成 12 页 16:9 作品集。保留图纸完整比例，输出文字可编辑 PPTX。
使用 $guizang-ppt-skill，做一份瑞士风 HTML 设计汇报，使用我提供的原图，不生成配图。
使用 $industrial-design-portfolio，整理我项目的现状分析、草图、CAD 和效果图，突出方案演变与设计依据，输出 HTML 和 PDF。
```

`$skill-name` 是给 Codex 的调用文本，不是 Shell 命令；不是所有宿主都支持斜杠命令。Skill 列表没刷新时，新建仓库会话，或明确写“读取 `.agents/skills/folio/SKILL.md` 并按它执行”。此仓库安装不会自动注册到所有其他聊天。

## 云端环境恢复

Git 保存规范、脚本与锁文件；`node_modules` 和浏览器二进制不进入 Git。新云端环境运行：

```bash
python scripts/setup_skills.py
python scripts/verify_skills.py --runtime
```

可以只恢复需要的 Skill：

```bash
python scripts/setup_skills.py --skill folio
python scripts/setup_skills.py --skill guizang-ppt-skill
python scripts/setup_skills.py --skill industrial-design-portfolio
```

Node 20+、Python 3、npm 和 Chromium 所需系统库是基础条件。下载依赖需要允许 npm registry 与 Playwright 浏览器下载域名；网络受限时如实报告，不能只凭入口文件宣称导出可用。Linux 缺系统库时，在允许安装的环境中运行对应 Skill 的 `npx playwright install-deps chromium`。

Industrial 核心不需安装第三方包；如要运行上游可选测试：

```bash
python scripts/setup_skills.py --skill industrial-design-portfolio --industrial-tests
```

三个目录的 Node 包独立。Folio / Guizang 固定 Playwright 1.60.0；Industrial 的可选测试固定 @playwright/test 1.62.1，不能合并依赖。可选 Python 测试通过该 Skill 的 `.venv` 隔离。

## 更新与限制

```bash
python scripts/check_skill_updates.py
```

仅查询上游 HEAD，不自动升级；固定提交见 `skills-lock.json`。不要在 Skill 目录直接 `git pull` 或运行 Folio 自更新脚本，它们不是独立 Git 仓库。升级在独立分支中审阅、保留本地入口并重跑验证。

- Folio PPTX 导出使用部分布局映射与栅格视觉资产；中文字体、换行和浏览器效果需要目标应用验收，不能保证 HTML 像素级复刻。
- Guizang 的本地 Motion 兜底不能替代所有外部字体 / 图标；离线展示应额外检查。PDF / 截图输出也不是可编辑 PPTX。
- Industrial 的证据叙事可迁移到空间设计，但上游不提供建筑专业事实或原生 PPTX 导出。
- 当前没有制作用户 PPT；安装验证不能替代未来每份成稿的视觉 QA。

保留各上游 LICENSE 与来源记录。Guizang 为 GPL-3.0，其他两者为 MIT；本安装不改变上游授权，也不把 GPL 文件重新声明为 MIT。详见每个目录的许可证。
