import os
import sys
import mammoth
from docx import Document

def convert_to_markdown(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    output_path = file_path.rsplit('.', 1)[0] + '.md'
    
    try:
        if ext == '.docx':
            with open(file_path, "rb") as docx_file:
                result = mammoth.convert_to_markdown(docx_file)
                markdown = result.value
                with open(output_path, "w") as md_file:
                    md_file.write(markdown)
            print(f"Converted {file_path} to {output_path}")
            return output_path
        elif ext == '.doc':
            # .doc requires different handling (usually antiword or similar)
            # For this MVP, we flag it as needing manual conversion to .docx
            # or provide a warning.
            print(f"WARNING: .doc format found for {file_path}. Please save as .docx for automated processing.")
            return None
    except Exception as e:
        print(f"Error converting {file_path}: {e}")
        return None

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "./discovery"
    if os.path.isfile(target):
        convert_to_markdown(target)
    elif os.path.isdir(target):
        for f in os.listdir(target):
            if f.endswith(('.docx', '.doc')):
                convert_to_markdown(os.path.join(target, f))
