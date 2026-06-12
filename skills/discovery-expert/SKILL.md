---
name: discovery-expert
description: Ingests and sanitizes technical sources. Converts legacy API docs (.docx) to OpenAPI 3.0 and indexes DB schemas (.csv).
version: 1.0.0
---

# Execution Playbook: Discovery Expert (Compute-First)

As the Discovery Expert, your goal is to create a deterministic "Technical Source of Truth."

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
   - For `.md` files (the "Clean Source" from Word/PPTX): Read them and follow the `word_to_openapi_rules.md` or `pptx_to_openapi_rules.md` to map the content into a valid **OpenAPI 3.0 YAML** under `./discovery/specs/[api-name]-v[version].yaml`.
   - For `.xlsx` files: The OpenAPI spec is already compiled in Step 2. Validate and adjust if needed.

4. **Validation & Assessment:**
   - Compare the OpenAPI spec against the `./discovery/schema_map.md`.
   - Flag any missing data sources or PII risks discovered by the script.

5. **Final Handover:**
   - Summarize the assets and transition to the `ui-analyzer`.
