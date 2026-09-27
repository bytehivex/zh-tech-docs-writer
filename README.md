# zh-tech-docs-writer

面向中文技术文档、系统架构、API 说明与界面文案的写作规范与检查工具链。

核心目标：**事实保真、平实短句、动作明确、消除 AI 腔**。

解决三类核心问题：
- **AI 腔泛滥**：大模型生成的引子套话、自问自答、夸大修饰与动词虚化。
- **事实与代码误改**：改写时臆造数据时限，改动代码、URL、JSON 键名与配置。
- **结构松散**：长句堆叠，缺少动作动词，扫读成本高。

---

## 规范来源

本项目融合三项实践基准：

1. **受控语言与工程底座（Fenng 规范）**：借鉴 **ASD-STE100** 理念，落实事实保真、保护机器标识符，规范 API 与 Runbook 处理。
2. **去 AI 腔清单（leter 清单）**：整理高频套话对照表，结合静态规则与提示词双重拦截。
3. **句长与排版标尺（阮一峰规范）**：逗号分句控制在 20 字内，超 30 字拆分，数字与英文之间保留半角空格。

---

## 适用范围

### 适用内容
- 技术方案、架构设计、PRD 文档
- API 接口说明、参数字典、错误码文案、变更日志
- 操作手册、部署流程、排障指南、运维 Runbook、安全警示
- UI 文案、按钮标签、系统提示、通知与报错信息
- 开源项目 README、快速上手指南

### 严禁改写内容（保持原样）
- 行内代码与代码块字面量
- JSON 键名与请求载荷
- URL、API 路径与路由端点
- 数据库表名与字段结构
- 环境变量、终端命令与配置文件字面量

---

## 核心规则概览

- **事实保真**：保留原意、数据、约束与确定程度。缺失信息标注 `[待确认]`，禁止凭空臆造。
- **保护标识符**：代码、路径、字段与命令必须使用行内代码包裹，禁止改写字面量。
- **消除 AI 腔**：
  - 剔除 `随着……的发展`、`值得注意的是` 等套话引子。
  - 剔除 `总的来说`、`综上所述` 等套话结尾。
  - 剔除 `强大`、`优雅`、`无缝` 等主观修饰词。
  - 拆解 `不仅……而且……` 与设问自答，改为客观陈述。
- **受控语言**：操作步骤动词先行（安装、配置、检查），单个编号步骤只包含单项动作。
- **控制句长**：分句控制在 20 字以内，超 30 字必须拆分，整句不超过 100 字。
- **排版规范**：中英文与数字间留空格，引号统一使用直角引号 `「」`，Markdown 保持一段一行。

详细规范见 [SKILL.md](./SKILL.md)。

---

## 仓库结构

```text
zh-tech-docs-writer/
├── README.md                               # 本说明文件
├── SKILL.md                                # 技能核心入口（供 Codex / Hermes 等使用）
├── references/                             # 按任务读取的详细规范与模板
│   ├── ai-fluff-checklist.md               # AI 腔与套话清洗对照全表
│   ├── controlled-technical-chinese.md     # 受控中文技术写作（步骤与因果规范）
│   ├── api-status-copy.md                  # API 状态码、错误文案与参数说明规范
│   ├── terminology-and-typography.md       # 术语排版、易混词与标点细则
│   └── project-overrides-example.md        # 项目级自定义覆盖模板
├── scripts/                                # 零依赖辅助工具链
│   ├── lint_tech_writing.py                # 纯 Python 标准库 Linter 静态检查器
│   └── unwrap_md_paragraphs.py             # 段落硬换行恢复展开工具
└── tests/                                  # 自动化回归测试套件
    ├── test_lint_tech_writing.py           # 检查器规则、边界与 AI 腔检测测试
    ├── test_skill_structure.py             # 技能结构与引用链接完整性测试
    └── test_unwrap_md_paragraphs.py        # 换行工具回归测试
```

---

## 在 Agent 中使用

本规范符合标准 **Agent Skill** 协议，适用于 Codex、Hermes Agent、Cursor、Windsurf 等各类 AI 编程工具。

### 1. 安装方式

#### 方式 A：使用 skills 工具一键安装（推荐）

已有 Node.js 环境时，直接通过通用的 `skills` CLI 安装：

```bash
npx skills add bytehivex/zh-tech-docs-writer
```

该工具会自动从 GitHub 拉取仓库并完成挂载，无需手动创建目录。

#### 方式 B：通过 Git 全局克隆

使用 `git clone` 将仓库拉取到目标工具的技能目录：

- **Codex**：
  ```bash
  git clone https://github.com/bytehivex/zh-tech-docs-writer.git ~/.codex/skills/zh-tech-docs-writer
  ```

- **Hermes Agent**：
  ```bash
  git clone https://github.com/bytehivex/zh-tech-docs-writer.git ~/.hermes/skills/productivity/zh-tech-docs-writer
  ```

- **其他支持 Agent Skills 的工具**：克隆到工具指定的全局技能路径（如 `~/.agent/skills/`）。

#### 方式 C：作为工程私有规范

仅在当前项目推行规范时使用：
- **项目级 Skill**：在项目根目录运行 `npx skills add bytehivex/zh-tech-docs-writer -p`，或克隆至项目 `.skills/` 目录。
- **项目级规则**：在工程的 `AGENTS.md`、`.cursorrules` 或 `.windsurfrules` 中引入本仓库的 `SKILL.md`。

### 2. 调用示例

- **自动触发**：Agent 在处理中文技术文档、PRD、接口说明或去 AI 腔任务时，会自动读取本规范。
- **显式指令**：

  **去 AI 腔与文档润色：**
  ```text
  请使用 zh-tech-docs-writer 规范优化 docs/api.md，去除文中的 AI 腔并规范排版。
  ```

  **审阅架构方案：**
  ```text
  使用 zh-tech-docs-writer 规范审阅当前的架构设计文档，标出违反受控语言和过度修饰的部分。
  ```

  **撰写 Runbook 或部署文档：**
  ```text
  依据 zh-tech-docs-writer 规范编写系统部署手册，要求步骤动词先行、代码与配置标识符严格保真。
  ```

---

## 静态检查工具与 CI 集成

仓库内置零依赖的 Python 校验脚本 `scripts/lint_tech_writing.py`，使用标准库即可运行。

诊断级别分为三级：
- **`error`**：明确错误（错别字等），返回非零退出码。
- **`warning`**：可疑表达与 AI 腔（套话引子、自问自答、过度修饰）。
- **`style`**：术语写法与排版风格建议。

### 执行命令

```bash
# 检查指定文件或目录
python3 scripts/lint_tech_writing.py docs/

# 严格模式（warning 与 style 均阻断，用于 CI 门禁）
python3 scripts/lint_tech_writing.py --strict docs/ README.md
```

### 忽略规则
单行需要保留特定写法时，在行尾添加注释：
```markdown
这里需要保留特定的写法 <!-- copy-lint-disable-line -->
```

---

## 恢复段落软换行

若 Markdown 源文件包含编辑器自动插入的硬回车，可使用本工具恢复为「一段一行」：

```bash
# 检查是否存在硬换行（只读）
python3 scripts/unwrap_md_paragraphs.py --check docs/

# 展开并写回原文件
python3 scripts/unwrap_md_paragraphs.py docs/ README.md
```

单文件需跳过展开时，在文件顶部独立成行添加 `<!-- unwrap-disable-file -->`。

---

## 自动化测试

仓库内置基于 `unittest` 的回归测试套件，覆盖代码块保护、未闭合符号、AI 腔拦截与链接有效性：

```bash
python3 -m unittest discover -s tests -v
```

88 项测试均基于 Python 标准库，无需安装任何第三方依赖。

---

## 项目级规则覆盖

本规范收录通用技术写作规则。若具体项目存在特定术语表或品牌语气，参考：
- `references/project-overrides-example.md`

在目标工程中配置覆盖规则，无需修改本仓库源码。

---

## 参考与致谢

本项目参考以下开源规范与实践：
- [Fenng/tech-doc-style-chinese](https://github.com/Fenng/tech-doc-style-chinese)：受控技术语言底座、工程结构与 Python 检查器。
- [leter/zh-tech-writing](https://github.com/leter/zh-tech-writing)：常见 AI 套话清单与短句写作参考。
- [ruanyf/document-style-guide](https://github.com/ruanyf/document-style-guide)：中文技术文档排版基准与字长指标。

---

## License

[MIT License](./LICENSE)
