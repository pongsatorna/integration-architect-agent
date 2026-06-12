# Tool: Excel to OpenAPI Converter Rules

When converting an `.xlsx` or `.xls` file representing API designs into OpenAPI 3.0, apply these extraction rules:

## 1. Metadata Extraction
- **Info Object:**
  - **Title:** Derived from the sheet title or excel filename.
  - **Version:** Default to `1.0.0` unless specified on the Index or sheet.
- **Servers:** Extract base urls from the environments table (e.g.dev, test, prod cells).

## 2. Path & Operation Extraction
- **Endpoint Route:** Look for the value next to `Endpoint :`. Strip base path variables like `{endPoint}` or `{endpoint}`.
- **Method:** Look for the HTTP verb next to `Method :` (e.g., POST, GET, PUT, DELETE).
- **Operation ID:** Map to the `API Code` cell (e.g., `AI-POV2`).
- **UI Component Tag:** Extract the `UI Component :` cell and document it in the description.

## 3. Schema & Examples Extraction
- **Request Parameters Table:**
  - Map table columns `field Name`, `Mendatory`, `Type`, `Example` into OpenAPI properties.
  - Map field mandatory flag `Y` to OpenAPI `required` array.
- **Request Body JSON Examples:**
  - Search for JSON blocks under `Request Body [json]`.
  - Extract and parse these blocks. If a role label is specified (e.g., `##SRS`), use it as the example key.
- **Response Body JSON Examples:**
  - Search for JSON blocks under `Response Body [json]`.
  - Search for Case labels (e.g., `Case RSR`, `Case PBH`) to group different response examples.
  - Use the response examples to dynamically construct properties and nesting types for the OpenAPI response schema using recursive type checking.

## 4. Error and Exception Handling
- If any JSON example contains syntax errors, attempt automatic syntax cleaning (quotes correction, whitespace normalization, trailing commas removal).
- If validation fails, default to a string/generic type and add a `# TODO: Verify Schema` warning.
