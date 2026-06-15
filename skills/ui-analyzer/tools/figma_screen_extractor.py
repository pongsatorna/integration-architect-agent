import json
import sys
import os

def extract_text_fields(node):
    """Recursively walks a node to find all TEXT elements."""
    fields = []
    
    def walk(n):
        node_type = n.get('type', '')
        if node_type == 'TEXT':
            fields.append({
                'field_id': n.get('id', ''),
                'field_name': n.get('name', 'unknown_field'),
                'sample_content': n.get('characters', '').strip(),
                'type': 'String'
            })
        
        # Recurse children
        for child in n.get('children', []):
            walk(child)
            
    walk(node)
    return fields

def process_figma_tree(data):
    screens_map = []
    
    # We want to identify screens. Screens are typically FRAMEs or CANVAS items.
    # If the root has pages (CANVAS), we scan children of CANVAS.
    # Otherwise, if the root itself is a screen list, we scan them.
    
    screens = []
    
    def find_screens(node):
        node_type = node.get('type', '')
        # A Canvas represents a Figma Page. Children of Canvas are screens/frames.
        if node_type == 'CANVAS':
            for child in node.get('children', []):
                if child.get('type') == 'FRAME':
                    screens.append(child)
        elif node_type == 'FRAME' and not node.get('parent'):
            # If a top level node is a frame and has no parent, treat as screen
            screens.append(node)
        else:
            # Recurse down to find CANVAS or FRAMEs
            for child in node.get('children', []):
                find_screens(child)

    # If the input is a list of nodes (common from MCP Figma server response)
    if isinstance(data, list):
        for item in data:
            find_screens(item)
    else:
        find_screens(data)
        
    # If we still found no screens but the data has top-level frames, use them
    if not screens:
        if isinstance(data, dict):
            if data.get('type') == 'FRAME':
                screens = [data]
            elif 'children' in data:
                screens = [c for c in data['children'] if c.get('type') == 'FRAME']
                
    for screen in screens:
        screen_name = screen.get('name', 'Unnamed Screen')
        screen_id = screen.get('id', '')
        
        sections = []
        
        # Immediate children of the screen are treated as sections if they are CONTAINER types
        # (FRAME, GROUP, INSTANCE)
        # Any immediate TEXT nodes or other shapes are grouped in a "general" section.
        general_fields = []
        
        for child in screen.get('children', []):
            child_type = child.get('type', '')
            child_name = child.get('name', 'Unnamed Section')
            child_id = child.get('id', '')
            
            if child_type in ['FRAME', 'GROUP', 'INSTANCE']:
                # Extract all text fields inside this section
                fields = extract_text_fields(child)
                if fields:
                    sections.append({
                        'section_id': child_id,
                        'section_name': child_name,
                        'upstream_source': '', # Left blank for user mapping
                        'fields': fields
                    })
            elif child_type == 'TEXT':
                general_fields.append({
                    'field_id': child_id,
                    'field_name': child_name,
                    'sample_content': child.get('characters', '').strip(),
                    'type': 'String'
                })
                
        # If there are general fields outside sections, add them as a general section
        if general_fields:
            sections.insert(0, {
                'section_id': f"{screen_id}_general",
                'section_name': 'general',
                'upstream_source': '',
                'fields': general_fields
            })
            
        screens_map.append({
            'screen_id': screen_id,
            'screen_name': screen_name,
            'sections': sections
        })
        
    return screens_map

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 figma_screen_extractor.py <input_figma_raw_json> <output_sections_map_json>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        if not os.path.exists(input_file):
            print(f"Error: Input file {input_file} does not exist.")
            sys.exit(1)
            
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        result = process_figma_tree(data)
        
        # Ensure directory of output file exists
        os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
            
        print(f"Successfully extracted {len(result)} screen(s) and sections to {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
