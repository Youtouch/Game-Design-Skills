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
- Do not claim firsthand play, playtests, or source readings that did not happen. Say what the evidence base is.

## Examples and helpers

- Each skill has a worked example (`example.md`) that shows the procedure producing a decision, not just a filled template. Label examples as synthetic and keep their numbers reproducible: recompute every figure before committing.
- Helper scripts are optional design calculators (balance, probability), standard-library Python 3 only, with unit tests in `tests/`. They are not engine or gameplay code.

## Checks before committing

- `python scripts/validate_skills.py` (frontmatter, folder names, relative links, README catalog).
- `python -m unittest discover tests`.
- When adding a skill, add it to the README catalog and, where it has a trap worth testing, to `docs/evaluation-cases.md`.
