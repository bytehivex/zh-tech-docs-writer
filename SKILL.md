---
name: zh-tech-docs-writer
description: "Use when writing or editing Chinese docs. No AI fluff."
version: 1.0.0
author: JIE, Yara
license: MIT
platforms: [linux, macos, windows]
tags: [writing, documentation, style-guide, chinese, humanize, linter]
category: productivity
---

# 中文技术文档与文案写作规范 (zh-tech-docs-writer)

面向中文技术方案、系统架构、API 说明、运维 Runbook、README 与界面文案的写作规范与自动化工具链。

**核心目标**：写出资深工程师风格的中文文档 —— **事实保真、平实短句、动作明确、无 AI 腔**。

---

## When to Use

- 编写、重构或审阅中文技术方案、架构文档、需求说明 (PRD) 或技术博客。
- 编写 API 接口说明、错误码本地化文案、配置手册与排障指南。
- 校验界面按钮、状态提示、操作警示等 UI 文案。
- 清除大模型生成的套话、翻译腔与设问排比。
- **不要用于**：代码字面量、JSON 键名、URL、API 路径、数据库字段名、系统命令与配置项（保持原样，严禁改写）。

---

## 规则优先级

发生冲突时，按以下顺序处理：

1. **事实保真**：保留原文或可信上下文的事实、数据、限制和安全含义。严禁凭空编造数字、时限、SLA 或结论；缺少信息明确标记 `[待确认]`。
2. **保护机器可读内容**：代码、路径、字段、配置、命令必须使用代码环境严格保护。
3. **结构清晰与动作明确**：步骤动词明确，一个编号步骤只包含一个核心动作。
4. **消除 AI 腔与黑话**：删除套话引子、设问自答、空泛形容词和虚浮黑话。
5. **排版与标点规范**：遵循中西文留白、全半角标点、直角引号与大小写规范。

不得为了追求「句子更短」或「语气更有气势」而牺牲事实与逻辑。

---

## 核心写作规则

### 1. 消除 AI 腔（自检清单）
写完或改写文档后，逐条对照检查并修改以下表达：
- **开场套话**：删除 `随着……的发展`、`在当今数字化时代`、`值得注意的是`，第一句直入主题。
- **结尾升华**：删除 `总的来说`、`综上所述`，不写无增量总结；确需收尾仅说明明确的下一步操作。
- **设问自答**：删除 `为什么需要……？因为……`，直接陈述结论或因果关系。
- **宣传修饰**：删除 `强大`、`灵活`、`优雅`、`无缝`、`一站式`；有具体指标写指标，无数据直接删除。
- **机械递进**：拆解 `不仅……而且……`、`不是 A 而是 B`，改用客观陈述句。
- **动词虚化**：将 `对……进行修改` 改为 `修改……`；删除多余的 `通过……的方式`。
- **空泛黑话**：替换 `赋能`、`抓手`、`闭环`、`沉淀`、`拉通`，改用具体工程动作。

详细对照与改法见 [references/ai-fluff-checklist.md](references/ai-fluff-checklist.md)。

### 2. 句长与排版法则
- **分句长度限制**：逗号隔开的每一截分句，长度控制在 20 字以内；超过 30 字必须拆开；单句总长超过 100 字必须重构为多句。
- **数字与单位**：数字使用半角阿拉伯数字；英文单位不翻译时，数字与单位间保留一个半角空格（如 `16 GB`、`3,600 s`）；百分号视同数字（`6.5%`）。
- **中西文留白**：中文正文与英文单词、数字之间保留一个半角空格（如 `在 Linux 系统上启动 3 个实例`）；英文专有名词紧跟全角标点时中间不加空格（如 `推荐使用 Docker。`）。
- **标点符号**：使用全角中文标点；中文引号默认使用直角引号 `「」`；省略号使用 `……`；点号（句号、逗号、冒号）不得出现在标题末尾。
- **源码换行**：Markdown 源码保持一段一行（软换行），不做硬回车断行。

### 3. 受控技术语言
- **动词先行**：操作步骤以具体谓语动词开头，写清动作对象。
- **一事一步**：一个编号步骤只包含一个独立动作；顺序操作按执行流程编号。
- **指代明确**：避免滥用抽象的「该」「其」「此」；有歧义时直接重复具体名词。
- **状态与错误文案**：根据实际语义翻译，不机械直译单个英文词（如 `Bad Request` → `请求参数有误`）。

详细规则见 [references/controlled-technical-chinese.md](references/controlled-technical-chinese.md) 与 [references/api-status-copy.md](references/api-status-copy.md)。

---

## 检查工具使用

写完文档后，运行自带的 Python Linter 脚本进行静态检查：

```bash
# 检查单个文档或目录
python3 scripts/lint_tech_writing.py docs/README.md

# 严格模式（warning 与 style 也视为失败，适合 CI 门禁）
python3 scripts/lint_tech_writing.py --strict docs/
```

- 脚本基于 Python 3 标准库编写，无需安装第三方依赖。
- 自动屏蔽代码块、行内代码与 URL，避免误报代码。
- 内置大小写、标点、错别字、高频黑话及 AI 腔正则匹配。

---

## 参考资料路由

- AI 腔清洗全量对照表：读取 [references/ai-fluff-checklist.md](references/ai-fluff-checklist.md)
- 受控中文技术写作（步骤与因果）：读取 [references/controlled-technical-chinese.md](references/controlled-technical-chinese.md)
- API 状态码、错误文案与参数：读取 [references/api-status-copy.md](references/api-status-copy.md)
- 术语与排版细则：读取 [references/terminology-and-typography.md](references/terminology-and-typography.md)
- 项目自定义覆盖：读取 [references/project-overrides-example.md](references/project-overrides-example.md)
