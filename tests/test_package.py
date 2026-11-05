"""Package integrity checks; model selection/compliance require separate runs."""

import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def heading_anchors(content):
    """GitHub-style anchors for the package's plain Markdown headings."""
    counts = {}
    anchors = set()
    in_code = False
    for line in content.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        slug = re.sub(r"[^\w\s-]", "", match[1].lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        anchors.add(f"{slug}-{count}" if count else slug)
    return anchors


class PackageTests(unittest.TestCase):
    def test_local_markdown_links_and_anchors(self):
        documents = [ROOT / "SKILL.md", ROOT / "README.md"]
        documents += sorted((ROOT / "references").glob("*.md"))
        documents += sorted((ROOT / "evals").glob("*.md"))
        for document in documents:
            for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", document.read_text(encoding="utf-8")):
                with self.subTest(document=document.relative_to(ROOT), target=target):
                    url = urlsplit(target)
                    if url.scheme or url.netloc:
                        continue
                    path = (document.parent / unquote(url.path)).resolve() if url.path else document
                    self.assertTrue(path.is_relative_to(ROOT), "Link leaves the skill package")
                    self.assertTrue(path.is_file(), f"Missing target: {path}")
                    if url.fragment:
                        self.assertIn(unquote(url.fragment), heading_anchors(path.read_text(encoding="utf-8")))

    def test_evaluation_fixture_contract(self):
        data = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        self.assertEqual(set(data), {"routing_cases", "behavior_cases"})
        ids = set()
        for group, cases in data.items():
            self.assertIsInstance(cases, list)
            self.assertTrue(cases, f"Empty group: {group}")
            for case in cases:
                with self.subTest(group=group, case=case.get("id")):
                    self.assertIsInstance(case["id"], str)
                    self.assertTrue(case["id"].strip())
                    self.assertNotIn(case["id"], ids, "Duplicate case identity")
                    ids.add(case["id"])
                    self.assertIsInstance(case["prompt"], str)
                    self.assertTrue(case["prompt"].strip())
                    if group == "routing_cases":
                        self.assertIs(type(case["invoke"]), bool)
                        self.assertIsInstance(case["reason"], str)
                        self.assertTrue(case["reason"].strip())
                    else:
                        self.assertIsInstance(case["context"], str)
                        self.assertTrue(case["context"].strip())
                        self.assertIsInstance(case["checks"], list)
                        self.assertTrue(case["checks"])
                        for check in case["checks"]:
                            self.assertIsInstance(check, str)
                            self.assertTrue(check.strip())
        self.assertEqual({case["invoke"] for case in data["routing_cases"]}, {True, False})


if __name__ == "__main__":
    unittest.main()
