# SQL Standards & Conventions

## 1. Naming Conventions
- **Tables:** Use `snake_case` and plural nouns (e.g., `user_accounts`, `transaction_logs`).
- **Columns:** Use `snake_case`. Primary keys should be `id` or `[table_singular]_id`.
- **Foreign Keys:** Use `[target_table_singular]_id`.

## 2. Dialect: PostgreSQL (Default)
- Use `JSONB` for flexible mobile-first metadata storage.
- Use `TIMESTAMPTZ` for all date-time fields to ensure UTC consistency.
- Use `UUID` for primary keys to support offline mobile sync if needed.

## 3. Safety Rules
- **ALTER TABLE:** Never drop columns without a 2-stage migration.
- **NOT NULL:** When adding `NOT NULL` columns, always provide a `DEFAULT`.
- **INDEXES:** Add indexes to any column used in a `WHERE` or `JOIN` for the API.

## 4. Logical Layering
- If an API requires a specific shape of data, prefer a **VIEW** or **MATERIALIZED VIEW** over duplicating data in a new table.
- Name views with a `v_` prefix (e.g., `v_mobile_user_profile`).
