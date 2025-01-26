def merge_and_sort_files(file1_path, file2_path, output_file_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        content1 = file1.read().split(', ')
        content2 = file2.read().split(', ')
        
    merged_content = sorted(content1 + content2)
    
    with open(output_file_path, 'w') as output_file:
        output_file.write(', '.join(merged_content))

# Input Files Content
file1_path = 'file1.txt'
file2_path = 'file2.txt'
output_file_path = 'output.txt'

with open(file1_path, 'w') as file1:
    file1.write("apple, banana, orange")

with open(file2_path, 'w') as file2:
    file2.write("cherry, fig, grape")

# Process and Output
merge_and_sort_files(file1_path, file2_path, output_file_path)

with open(output_file_path, 'r') as output_file:
    print(output_file.read())  # Output: apple, banana, cherry, fig, grape, orange
