from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class SkillStructureTest(unittest.TestCase):
    def test_core_skill_stays_concise(self):
        lines = (ROOT / "SKILL.md").read_text(encoding="utf-8").splitlines()
        self.assertLessEqual(len(lines), 300)

    def test_local_references_from_skill_exist(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        targets = re.findall(r"\[[^]]+\]\((references/[^)]+\.md)\)", skill)
        self.assertTrue(targets)
        for target in targets:
            with self.subTest(target=target):
                self.assertTrue((ROOT / target).is_file(), f"Target file missing: {target}")

    def test_ai_fluff_checklist_exists_and_has_rules(self):
        ref = (ROOT / "references" / "ai-fluff-checklist.md").read_text(encoding="utf-8")
        self.assertIn("开场背景套话", ref)
        self.assertIn("结尾升华与客套", ref)
        self.assertIn("宣传腔形容词", ref)

    def test_controlled_writing_reference_exists(self):
        ref = (ROOT / "references" / "controlled-technical-chinese.md").read_text(encoding="utf-8")
        self.assertIn("受控中文技术写作", ref)

if __name__ == "__main__":
    unittest.main()
