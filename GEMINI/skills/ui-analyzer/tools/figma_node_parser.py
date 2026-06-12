import json
import sys
import os

def parse_figma_nodes(json_data):
    fields = []
    
    def walk(node):
        node_name = node.get('name', 'unknown')
        node_type = node.get('type', '')
        
        # Logic to identify data-bearing components
        # Usually, designers name these with prefixes like 'txt_', 'val_', 'lbl_'
        if node_type == 'TEXT':
            fields.append({
                'id': node.get('id'),
                'name': node_name,
                'content': node.get('characters', ''),
                'visible': node.get('visible', True)
            })
        
        # Logic to identify lists/repeating elements
        if node_type == 'FRAME' or node_type == 'INSTANCE':
            # Check for Auto Layout (horizontal/vertical) which often indicates a list
            layout_mode = node.get('layoutMode')
            if layout_mode and len(node.get('children', [])) > 1:
                # If it's a list, we just tag it for the agent to review
                fields.append({
                    'id': node.get('id'),
                    'name': node_name,
                    'is_list': True,
                    'child_count': len(node.get('children', []))
                })

        # Recursive walk
        for child in node.get('children', []):
            walk(child)

    walk(json_data)
    return fields

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 figma_node_parser.py <input_json> <output_json>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
            
        # If the input is a list of nodes (common from MCP)
        if isinstance(data, list):
            results = []
            for item in data:
                results.extend(parse_figma_nodes(item))
        else:
            results = parse_figma_nodes(data)

        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
            
        print(f"Successfully parsed Figma nodes into {output_file}")
    except Exception as e:
        print(f"Error: {e}")
