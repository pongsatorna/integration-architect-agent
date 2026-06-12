import sys
import re
import json

def parse_schema_map(file_path):
    """Simple parser for the generated schema_map.md"""
    schema = {}
    current_table = None
    with open(file_path, 'r') as f:
        for line in f:
            table_match = re.match(r'^## (.*)', line)
            if table_match:
                current_table = table_match.group(1).strip()
                schema[current_table] = []
            elif current_table and line.strip().startswith('- `'):
                col_match = re.search(r'`([^`]+)`', line)
                if col_match:
                    schema[current_table].append(col_match.group(1).upper())
    return schema

def parse_lineage(file_path):
    """Simple parser for the lineage.md file to find DB Source columns"""
    required_columns = []
    with open(file_path, 'r') as f:
        for line in f:
            # Looking for patterns like | Mobile Field | ... | DB_TABLE.COLUMN |
            # We assume the last column or a specific column contains the DB source
            matches = re.findall(r'\| ([^\|]+) \|', line)
            if len(matches) >= 3:
                db_source = matches[-1].strip()
                if '.' in db_source:
                    required_columns.append(db_source.upper())
    return required_columns

def find_gaps(schema, required_cols):
    gaps = []
    for req in required_cols:
        if '.' in req:
            table, col = req.split('.', 1)
            if table not in schema or col not in schema[table]:
                gaps.append({"table": table, "column": col, "status": "MISSING"})
    return gaps

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 schema_gap_analyzer.py <schema_map.md> <lineage.md>")
        sys.exit(1)

    schema_file = sys.argv[1]
    lineage_file = sys.argv[2]

    try:
        schema = parse_schema_map(schema_file)
        required = parse_lineage(lineage_file)
        gaps = find_gaps(schema, required)

        with open('db_gaps.json', 'w') as f:
            json.dump(gaps, f, indent=2)
        
        print(f"Found {len(gaps)} missing database components. See db_gaps.json")
    except Exception as e:
        print(f"Error: {e}")
