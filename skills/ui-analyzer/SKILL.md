---
name: ui-analyzer
description: Analyzes mobile UI designs (Figma/Screenshots) to define Target requirements. Extracts data fields, types, and states.
version: 1.0.0
---

# Execution Playbook: UI Analyzer (Compute-First)

As the UI Analyzer, your goal is to extract the "Data Requirements" from the frontend design with zero guesswork.

1. **Connectivity & Ingestion:**
   - **Pre-flight Check:** Ensure the environment is ready. If needed, notify the user and install `python-docx` (if used for screenshot metadata) or other required libraries.
   - Scan the `./ui_analysis/raw_mcp` folder for JSON data or attempt to connect to the **Figma MCP Server** using the provided URL.
   - If MCP is used, save the raw Node JSON to `./ui_analysis/raw_mcp/figma_raw.json`.
   - **FALLBACK:** If MCP fails or is unavailable, scan the `./ui_analysis/screenshots` folder for images. Proceed with Vision-based analysis on any files found there.

2. **Deterministic Extraction (Figma MCP Path):**
   - Run `python3 ./tools/figma_node_parser.py ./ui_analysis/raw_mcp/figma_raw.json ./ui_analysis/ui_data_map.json`.
   - Run `python3 ./tools/figma_screen_extractor.py ./ui_analysis/raw_mcp/figma_raw.json ./ui_analysis/screen_sections_map.json` to extract a structured hierarchy of screens, their constituent sections, and UI fields.
   - **Upstream Source mapping**: The `screen_sections_map.json` leaves the `"upstream_source": ""` property blank. You must review the JSON and specify the upstream system/API pulling data for each section before proceeding.
   - Review the output `./ui_analysis/ui_data_map.json` and `./ui_analysis/screen_sections_map.json`. These list:
     - Component/Section Names (to be mapped to APIs).
     - Text content (to identify data types).
     - Hidden/Optional layers (to identify nullable fields).
     - Repeating elements (to identify arrays and pagination).

3. **Semantic Analysis (Vision Fallback Path):**
   - If using a screenshot, describe every visible element from top-to-bottom.
   - For every element, answer: 
     - "Is this dynamic data (e.g., a balance) or static text (e.g., a label)?"
     - "What is the probable data type (String, Number, Date)?"
     - "Are there interactive buttons that trigger API calls?"

4. **State Mapping:**
   - Consult the `ui_state_matrix.md`. 
   - Ensure the UI requirements include:
     - Error messages (where do they appear?).
     - Empty states (what happens if the list is null?).
     - Loading indicators (is data fetched in chunks?).

5. **Output: The UI Requirements Spec:**
   - Generate a `./ui_analysis/ui_requirements_spec.md`.
   - This document is the "Target" for the `contract-designer`.
   - List every field, its UI-driven data type, and any state dependencies.
