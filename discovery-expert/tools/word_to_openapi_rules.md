# Tool: Word to OpenAPI Converter Rules

When converting a `.docx` file exported from Confluence into OpenAPI 3.0, apply these extraction rules:

## 1. Metadata Extraction
- **Info Object:** Title = Confluence Page Title; Version = 1.0.0 (default unless specified).
- **Servers:** Extract the "Environment" or "Base URL" table from the doc.

## 2. Path & Operation Extraction
- **Endpoints:** Look for bolded strings starting with `/` (e.g., **/api/v1/accounts**).
- **Methods:** Match keywords: GET, POST, PUT, DELETE, PATCH.
- **Parameters:** Map table columns (Field Name, Type, Required, Description) to OAS `parameters`.

## 3. Schema Extraction
- **Request Body:** If the doc shows a JSON example, use it to generate the `properties` map.
- **Response Body:** Look for "Success Response (200)" or "Error Response (4xx/5xx)".
- **Types:** 
    - "Number/Int/Long" -> `type: integer` or `type: number`.
    - "String/Varchar" -> `type: string`.
    - "Date/Timestamp" -> `type: string`, `format: date-time`.
    - "Boolean" -> `type: boolean`.

## 4. Quality Rules
- If an endpoint description says "Internal use only," add a `x-internal: true` vendor extension.
- Ensure all property names use the case found in the doc (usually snake_case for legacy systems).
- **NEVER** guess a field type. If unknown, use `type: string` and add a `# TODO: Verify type` comment.
