# Wiki2Md

An opinionated tool for converting wikipedia HTML into markdown suitable for ingestion by LLMs.

- removes citations (.reference)
- removes ref list (.reflist)
- removes js table headers and footers (.pcs-collapse-table-icon)
- removes metadata like portal lists (.metadata)
- removes flag icons
- optionally removes links

Install the pre-commit hooks with `poetry run pre-commit install` or just run them manually e.g. `poetry run ruff check`
