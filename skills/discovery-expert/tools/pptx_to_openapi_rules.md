# Tool: PPTX to OpenAPI Converter Rules

When converting a `.pptx` or `.ppt` file representing API designs or integration slide decks into OpenAPI 3.0, apply these extraction rules:

## 1. Metadata Extraction
- **Info Object:** 
  - **Title:** Presentation Name (e.g., Title slide text or file name).
  - **Version:** Default to `1.0.0` unless specified on the title slide or notes.
- **Servers:** Scan the intro/overview slides or speaker notes for environments (Dev, UAT, Prod base URLs).

## 2. Path & Operation Extraction
- **Slide Boundaries:** Typically, each slide represents one endpoint or one integration flow. Group the slide text, tables, and notes by slide.
- **Endpoints:** Search for strings matching paths (e.g., `/api/...` or `http://.../path`) in text frames, shapes, and headers.
- **HTTP Methods:** Look for HTTP verbs (GET, POST, PUT, DELETE, PATCH, etc.) which might be highlighted, bolded, or inside a table.
- **Parameters:** Extract tables or bullet lists detailing field definitions (Field, Type, Description, Required).

## 3. Schema Extraction (Slide + Notes)
- **JSON Snippets:** Check both the slide canvas and **Speaker Notes** for request/response JSON payloads. Presentation designs often hide large JSON blocks in speaker notes to avoid cluttering visual slides.
- **Data Types:**
  - Map terms like "Number", "Int", "Long", "Float" -> `type: integer` or `type: number`.
  - Map "String", "Char", "Varchar", "Text" -> `type: string`.
  - Map "Boolean", "Bool", "Y/N" -> `type: boolean`.
  - Map "Date", "DateTime", "Timestamp" -> `type: string`, `format: date-time`.

## 4. Visual/Diagram Flow Context
- If the slide contains flow descriptions or sequence markers (e.g., "Step 1: Auth -> Step 2: Fetch -> Step 3: Response"), use these to identify the dependencies or authentication requirements of the operations.

## 5. Quality & Validation Rules
- **Look for Speaker Notes:** Always examine slide speaker notes; they frequently contain additional constraints, PII considerations, security headers, and implementation details.
- **No Guessing:** If type info is missing, default to `type: string` and add a `# TODO: Verify type` comment.
