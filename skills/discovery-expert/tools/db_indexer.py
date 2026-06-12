import os
import sys
import pandas as pd
from datetime import datetime

def index_csv_files(directory):
    schema_map_path = os.path.join(directory, 'schema_map.md')
    files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    
    if not files:
        print("No CSV files found in the directory.")
        return

    with open(schema_map_path, 'w') as f:
        f.write(f"# Database Schema Map\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for file in files:
            table_name = os.path.splitext(file)[0].upper()
            file_path = os.path.join(directory, file)
            
            try:
                df = pd.read_csv(file_path, nrows=1) # Just read headers for indexing
                f.write(f"## {table_name}\n")
                f.write(f"- **Source File:** `{file}`\n")
                f.write(f"- **Columns:**\n")
                
                for col in df.columns:
                    # Basic PII Detection Logic
                    pii_tag = ""
                    pii_keywords = ['NAME', 'EMAIL', 'PHONE', 'MOBILE', 'ADDRESS', 'SSN', 'ID_CARD']
                    if any(key in col.upper() for key in pii_keywords):
                        pii_tag = " | **[PII]**"
                    
                    f.write(f"  - `{col}`{pii_tag}\n")
                f.write("\n")
                print(f"Indexed {table_name}")
            except Exception as e:
                print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    discovery_dir = sys.argv[1] if len(sys.argv) > 1 else "./discovery"
    index_csv_files(discovery_dir)
