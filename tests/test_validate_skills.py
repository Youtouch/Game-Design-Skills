"""Tests for scripts/validate_skills.py. Run: python -m unittest discover tests"""
import contextlib
import io
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))

import validate_skills as vs  # noqa: E402

GOOD_SKILL = "---\nname: {name}\ndescription: Does a thing. Use when testing.\n---\n\n# T\n"


def make_repo(skills, readme=None, extra=None):
    root = tempfile.mkdtemp()
    os.makedirs(os.path.join(root, "skills"))
    for name, text in skills.items():
        os.makedirs(os.path.join(root, "skills", name))
        if text is not None:
            with open(os.path.join(root, "skills", name, "SKILL.md"), "w") as f:
                f.write(text)
    if readme is None:
        readme = "\n".join(f"[{n}](skills/{n}/SKILL.md)" for n in skills)
    with open(os.path.join(root, "README.md"), "w") as f:
        f.write(readme)
    for rel, text in (extra or {}).items():
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(text)
    return root


def run(root):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = vs.main(["validate_skills.py", root])
    return code, out.getvalue()


class Validate(unittest.TestCase):
    def test_valid_repo_passes(self):
        code, out = run(make_repo({"good-skill": GOOD_SKILL.format(name="good-skill")}))
        self.assertEqual(code, 0, out)

    def test_name_mismatch(self):
        code, out = run(make_repo({"good-skill": GOOD_SKILL.format(name="other")}))
        self.assertEqual(code, 1)
        self.assertIn("does not match folder", out)

    def test_non_kebab_folder(self):
        code, out = run(make_repo({"Bad_Skill": GOOD_SKILL.format(name="Bad_Skill")}))
        self.assertIn("kebab-case", out)

    def test_missing_skill_file(self):
        code, out = run(make_repo({"empty-skill": None}))
        self.assertIn("missing SKILL.md", out)

    def test_missing_frontmatter(self):
        code, out = run(make_repo({"no-front": "# Just a heading\n"}))
        self.assertIn("missing YAML frontmatter", out)

    def test_empty_description(self):
        code, out = run(make_repo({"no-desc": "---\nname: no-desc\ndescription:\n---\n"}))
        self.assertIn("empty description", out)

    def test_broken_relative_link(self):
        skill = GOOD_SKILL.format(name="linky") + "[gone](missing.md)\n"
        code, out = run(make_repo({"linky": skill}))
        self.assertIn("broken link missing.md", out)

    def test_links_in_code_blocks_and_urls_ignored(self):
        skill = (GOOD_SKILL.format(name="linky")
                 + "```\n[not a link](nowhere.md)\n```\n[web](https://example.com) [anchor](#t)\n")
        code, out = run(make_repo({"linky": skill}))
        self.assertEqual(code, 0, out)

    def test_link_with_anchor_resolves_file(self):
        skill = GOOD_SKILL.format(name="linky") + "[sec](../../README.md#x)\n"
        code, out = run(make_repo({"linky": skill}))
        self.assertEqual(code, 0, out)

    def test_readme_must_list_every_skill(self):
        code, out = run(make_repo({"good-skill": GOOD_SKILL.format(name="good-skill")},
                                  readme="# Nothing here\n"))
        self.assertIn("README.md: no link to skills/good-skill/", out)

    def test_actual_repository_passes(self):
        code, out = run(os.path.join(HERE, ".."))
        self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()
