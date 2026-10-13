"""Check skill folders and markdown links against AGENTS.md conventions.

Usage: python scripts/validate_skills.py [repo_root]

Checks:
- every skills/<name>/ has a SKILL.md; <name> is lowercase kebab-case
- SKILL.md starts with YAML frontmatter holding `name` (matching the folder)
  and a nonempty `description` (at most 1024 characters)
- every relative markdown link in the repo resolves to an existing file
- README.md links to every skill
- the game-design-companion router, if present, names every other skill

Exit code 1 lists every problem found. Standard library only.
"""
import os
import re
import sys

KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
MAX_DESCRIPTION = 1024


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        key, sep, value = line.partition(":")
        if sep and not line.startswith((" ", "\t")):
            fields[key.strip()] = value.strip()
    return fields


def check_skills(root, problems):
    skills_dir = os.path.join(root, "skills")
    names = []
    for name in sorted(os.listdir(skills_dir)):
        path = os.path.join(skills_dir, name)
        if not os.path.isdir(path):
            continue
        names.append(name)
        rel = f"skills/{name}"
        if not KEBAB.match(name):
            problems.append(f"{rel}: folder name is not lowercase kebab-case")
        skill = os.path.join(path, "SKILL.md")
        if not os.path.isfile(skill):
            problems.append(f"{rel}: missing SKILL.md")
            continue
        with open(skill, encoding="utf-8") as f:
            fields = frontmatter(f.read())
        if fields is None:
            problems.append(f"{rel}/SKILL.md: missing YAML frontmatter")
            continue
        if fields.get("name") != name:
            problems.append(f"{rel}/SKILL.md: name '{fields.get('name')}' does not match folder")
        desc = fields.get("description", "")
        if not desc:
            problems.append(f"{rel}/SKILL.md: empty description")
        elif len(desc) > MAX_DESCRIPTION:
            problems.append(f"{rel}/SKILL.md: description longer than {MAX_DESCRIPTION} chars")
    return names


def check_links(root, problems):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d != "LocalOnly"]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            text = re.sub(r"```.*?```", "", text, flags=re.S)
            for target in LINK.findall(text):
                if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                    continue
                file_part = target.split("#", 1)[0]
                resolved = os.path.normpath(os.path.join(dirpath, file_part))
                if not os.path.exists(resolved):
                    problems.append(f"{os.path.relpath(path, root)}: broken link {target}")


def check_readme(root, names, problems):
    with open(os.path.join(root, "README.md"), encoding="utf-8") as f:
        readme = f.read()
    for name in names:
        if f"skills/{name}/" not in readme:
            problems.append(f"README.md: no link to skills/{name}/")


def check_router(root, names, problems):
    path = os.path.join(root, "skills", "game-design-companion", "SKILL.md")
    if not os.path.isfile(path):
        return
    with open(path, encoding="utf-8") as f:
        text = f.read()
    for name in names:
        if name != "game-design-companion" and f"`{name}`" not in text:
            problems.append(f"skills/game-design-companion/SKILL.md: router does not name `{name}`")


def main(argv):
    root = os.path.abspath(argv[1] if len(argv) > 1 else
                           os.path.join(os.path.dirname(__file__), ".."))
    problems = []
    names = check_skills(root, problems)
    check_links(root, problems)
    check_readme(root, names, problems)
    check_router(root, names, problems)
    if problems:
        print("\n".join(problems))
        print(f"\n{len(problems)} problem(s)")
        return 1
    print(f"OK: {len(names)} skills, links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
