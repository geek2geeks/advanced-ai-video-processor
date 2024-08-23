import os
import datetime

# Define the root directory of the project
project_root = '.'

# Files and directories to exclude
exclude_files = {'LICENSE', '.gitignore', 'README.md'}
exclude_dirs = {'__pycache__', '.git', 'venv', 'env'}
exclude_extensions = {'.pyc', '.pyo', '.pyd', '.db', '.sqlite3'}

# Function to write file content to markdown
def write_file_content(md_file, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        md_file.write(f"### `{file_path}`\n\n")
        md_file.write("```\n")
        md_file.write(content)
        md_file.write("\n```\n\n")
    except UnicodeDecodeError:
        md_file.write(f"### `{file_path}`\n\n")
        md_file.write("> **Warning:** Unable to read file due to encoding issues.\n\n")
    except Exception as e:
        md_file.write(f"### `{file_path}`\n\n")
        md_file.write(f"> **Error:** {str(e)}\n\n")

# Function to check if a file should be excluded
def should_exclude_file(file_name):
    return (file_name in exclude_files or
            file_name.startswith('file_report_') or
            os.path.splitext(file_name)[1] in exclude_extensions)

# Function to generate file tree
def generate_file_tree(start_path):
    tree = []
    for root, dirs, files in os.walk(start_path):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        level = root.replace(start_path, '').count(os.sep)
        indent = '│   ' * (level - 1) + '├── '
        if level > 0:  # Don't add the root directory itself
            tree.append(f"{indent}{os.path.basename(root)}/")
        for file in files:
            if not should_exclude_file(file):
                tree.append('│   ' * level + '├── ' + file)
    return '\n'.join(tree)

# Function to generate the markdown file
def generate_markdown():
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_md_path = f'file_report_{timestamp}.md'
    
    with open(output_md_path, 'w', encoding='utf-8') as md_file:
        md_file.write("# Project Files Overview\n\n")
        
        for root, dirs, files in os.walk(project_root):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            files = sorted([f for f in files if not should_exclude_file(f)])

            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, project_root)
                write_file_content(md_file, relative_path)

        # Add file tree at the end
        md_file.write("## Project File Structure\n\n")
        md_file.write("```\n")
        md_file.write(generate_file_tree(project_root))
        md_file.write("\n```\n")

    print(f"Markdown file generated at: {output_md_path}")

# Execute the script
if __name__ == '__main__':
    generate_markdown()