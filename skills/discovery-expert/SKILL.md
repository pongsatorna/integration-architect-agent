---
name: discovery-expert
description: Ingests and sanitizes technical sources. Converts legacy API docs (.docx) to OpenAPI 3.0 and indexes DB schemas (.csv).
version: 1.0.0
---

# Execution Playbook: Discovery Expert (Compute-First)

As the Discovery Expert, your goal is to create a deterministic "Technical Source of Truth." 
* **Technical API Specs (.docx, .xlsx)**: Must strictly compile into valid OpenAPI 3.0 specifications (YAML format) under `./discovery/specs/`. No other formats (like JSON, raw markdown, or text tables) are acceptable as the final contract source.
* **Requirements Decks (.pptx)**: Must translate to Markdown (.md) in `./discovery/` and have screenshots extracted to `./ui_analysis/screenshots/`.
* **DB Schemas (.csv)**: Must index into `./discovery/schema_map.md`.

1. **Environmental Scan & Self-Healing:**
   - Scan the `./discovery` directory for any `.doc`, `.docx`, `.pptx`, `.ppt`, `.xlsx`, `.xls`, or `.csv` files.
   - **Pre-flight Check:** Verify that `pandas`, `mammoth`, `python-docx`, `python-pptx`, and `openpyxl` are installed. If any are missing, notify the user and install them using `pip3 install pandas mammoth python-docx python-pptx openpyxl pyyaml`.

2. **Deterministic Extraction (Compute Tools):**
   - **For DB:** Run `python3 ./tools/db_indexer.py ./discovery`. This will automatically generate or update the `schema_map.md`.
   - **For API & Presentations:** Run `python3 ./tools/doc_converter.py ./discovery`. 
     - If `.docx` or `.pptx` files exist, they will be converted to `.md`.
     - If `.doc` or `.ppt` files exist, notify the user to save them as `.docx` or `.pptx`.
   - **For Excel API Specifications:** Run `python3 ./tools/excel_converter.py ./discovery`. This will automatically compile all endpoint tabs from `.xlsx` files into a single, unified OpenAPI spec file under `./discovery/specs/`.

3. **API Modeling (Semantic Layer):**
   - For `.md` files representing API specs (the "Clean Source" converted from Word .docx): Read them and follow the `word_to_openapi_rules.md` to map the content into a valid **OpenAPI 3.0 YAML** under `./discovery/specs/[api-name]-v[version].yaml`.
   - For `.md` files representing visual requirements (converted from PowerPoint .pptx): Do not convert to OpenAPI. Verify that the slides were successfully parsed to Markdown and screenshots have been extracted to `./ui_analysis/screenshots/`.
   - For `.xlsx` files: The OpenAPI spec is already compiled in Step 2 according to the `xlsx_to_openapi_rules.md`. Validate and adjust if needed.

4. **Validation & Assessment:**
   - Compare the OpenAPI spec against the `./discovery/schema_map.md`.
   - Flag any missing data sources or PII risks discovered by the script.

5. **Final Handover:**
   - Summarize the assets and transition to the `ui-analyzer`.
