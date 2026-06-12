# Tool: DB Schema Indexer Rules

When parsing a `.csv` export of a database schema, follow these systematic indexing steps:

## 1. Table Identification
- If the CSV filename is `table_name.csv`, use that as the table name.
- If the CSV contains a `table_name` column, group by that column.

## 2. Column Mapping
- **Name:** The header value.
- **Type:** Map SQL types to generic types (e.g., VARCHAR2(4000) -> String, NUMBER(10,0) -> Integer).
- **Constraints:** Identify `PK` (Primary Key) or `FK` (Foreign Key) markers.
- **Nullability:** Mark as `required` if the column is `NOT NULL`.

## 3. PII Detection (Security Layer)
Flag the following patterns as "PII Potential":
- Names: `*NAME*`, `FIRST_NAME`, `LAST_NAME`.
- Contact: `EMAIL`, `PHONE`, `MOBILE`, `ADDRESS`.
- Identifiers: `SSN`, `ID_CARD`, `PASSPORT`, `CREDIT_CARD`.

## 4. Output Generation
Produce a `schema_map.md` with the following structure:
```markdown
# Database Schema Map

## [Table Name]
- **Description:** [From CSV or inferred]
- **Columns:**
  - `COLUMN_NAME` (Type) | [PK/FK] | [PII Flag]
```
