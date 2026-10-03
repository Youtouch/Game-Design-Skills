# Agent conventions

## Scope

- Design only: game design and level design reasoning, documentation, and critique.
- No engine implementation, gameplay code, or engine-specific tooling.

## Skill format

- One skill per folder: `skills/<name>/SKILL.md`, with `<name>` in lowercase kebab-case.
- `SKILL.md` starts with YAML frontmatter containing `name` (matching the folder) and `description` (what the skill does and when to use it).
- Keep `SKILL.md` concise. Put long supporting material in sibling files inside the same skill folder and link to them.

## Sources and references

- Reference books and documents live outside this repo in a local `LocalOnly` folder and are never committed.
- Never copy text from those references into this repo. Paraphrase in your own words and cite the source (author, title, and chapter or page where possible).
