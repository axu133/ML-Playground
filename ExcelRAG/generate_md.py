import json
import os

def json_to_markdown_files(json_filename='statistical_functions.json', output_folder='statistical_functions'):
    # 1. Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created directory: {output_folder}")

    try:
        # 2. Load the JSON data
        with open(json_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"Found {len(data)} functions. Generating files...")

        # 3. Iterate through each function entry
        for entry in data:
            func_name = entry.get('function', 'Unknown_Function')
            
            # Sanitize filename (remove characters that are invalid in filenames)
            safe_filename = "".join([c for c in func_name if c.isalpha() or c.isdigit() or c in (' ', '-', '_', '.')]).rstrip()
            file_path = os.path.join(output_folder, f"{safe_filename}.md")

            # 4. Construct the Markdown content
            md_content = []
            
            # Title
            md_content.append(f"# {func_name}\n")
            
            # Summary as a blockquote
            if entry.get('short_summary'):
                md_content.append(f"> {entry['short_summary']}\n")
            
            # Syntax Guide
            if entry.get('syntax_guide'):
                md_content.append("## Syntax")
                md_content.append(f"{entry['syntax_guide']}\n")
            
            # Usage Examples
            examples = entry.get('usage_examples', [])
            if examples:
                md_content.append("## Examples")
                for ex in examples:
                    # formatting lists or code blocks if needed, 
                    # but simple text appending works for general content
                    md_content.append(f"- {ex}\n")
            
            # Link to original docs
            if entry.get('url'):
                md_content.append("---\n")
                md_content.append(f"[Original Documentation]({entry['url']})")

            # 5. Write to the .md file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("\n".join(md_content))

        print(f"Successfully created {len(data)} Markdown files in '{output_folder}/'.")

    except FileNotFoundError:
        print(f"Error: Could not find '{json_filename}'. Please ensure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    json_to_markdown_files()