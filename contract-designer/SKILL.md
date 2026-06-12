---
name: contract-designer
description: Bridges Technical Source and User Target to design optimized Mobile API contracts (OpenAPI/TypeScript).
version: 1.0.0
---

# Execution Playbook: Contract Designer (The Bridge)

As the Contract Designer, your role is to bridge the "Source" (Technical Reality) and the "Target" (User Requirements). **Do not begin until Skill 1 (Discovery) and Skill 2 (UI Analysis) have provided their outputs.**

1. **Environmental Ingestion (The Prerequisites):**
   - **Source:** Read the generated OpenAPI YAML files from `./discovery/specs/` and the `./discovery/schema_map.md`.
   - **Target:** Read the `./ui_analysis/ui_requirements_spec.md` from the `./ui_analysis/` directory.

2. **Mapping & Gap Analysis:**
   - Create a mapping table: `UI Field` -> `Upstream API Field` -> `Database Column`.
   - Identify **Gaps:** If a UI field is required but doesn't exist in the Upstream API, flag this as a "Feature Request" for the backend team.
   - Identify **Over-fetching:** If the Upstream API provides 50 fields but the UI only needs 5, mark the other 45 for pruning.

3. **Transformation Design (The BFF Layer):**
   - Apply the rules in `./tools/api_standards.md` (inherited from global/workspace context or local skill tools).
   - **Flatten:** Convert deeply nested upstream objects into a flat structure for mobile efficiency.
   - **Rename:** Convert `SNAKE_CASE` or `PASCAL_CASE` upstream fields into `camelCase`.
   - **Enrich:** Add pagination metadata (total, limit, offset) if the UI Spec indicates a list.

4. **Security & Masking:**
   - Consult `./tools/security_rules.json`.
   - Scrub any fields flagged as PII or "Internal Only" that were discovered by the `discovery-expert`.
   - Ensure sensitive IDs are obfuscated or replaced with tokens if required by the standards.

5. **Final Output (The Contract Storage):**
   - **OpenAPI 3.0 YAML:** Save to `./contracts/specs/[endpoint-name].yaml`.
   - **TypeScript Interface:** Save to `./contracts/types/[endpoint-name].ts`.
   - **Mapping Document:** Save to `./contracts/mapping/[endpoint-name]-lineage.md`.
