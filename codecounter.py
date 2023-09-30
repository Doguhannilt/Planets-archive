import os


# This function counts lines in the files that have .ipynb .py extensions
def count_lines_in_files_with_extensions(extensions):
    total_lines = 0

    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(tuple(extensions)):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    total_lines += len(lines)

    return total_lines

if __name__ == "__main__":
    extensions_to_count = (".ipynb", ".py")
    total_lines = count_lines_in_files_with_extensions(extensions_to_count)
    print(f"Total lines in files: {total_lines}")