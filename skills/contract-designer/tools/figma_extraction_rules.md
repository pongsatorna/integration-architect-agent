# Figma MCP Extraction Rules

When analyzing a Figma URL using the MCP server, you must extract specific data points to inform the API contract:

1. **Identify Variables & Components:** Do not just look at the text on the screen. Look at the semantic layer names (e.g., `CardContainer`, `UserProfile_Avatar`). 
2. **Extract State Requirements:** Look for Figma variants (e.g., `Hover`, `Disabled`, `Error`). If a UI element has an "Error" variant, the API contract MUST include an error state or validation message field for that element.
3. **Determine Nullability:** If a Figma component has optional layers (e.g., a "Subtitle" layer that is hidden in some variants), the corresponding API field MUST be nullable or optional.
4. **Identify Lists:** If the design shows an Auto Layout group with repeating elements (e.g., a list of transactions), the API contract must return an array, and you must include pagination metadata in the response envelope.