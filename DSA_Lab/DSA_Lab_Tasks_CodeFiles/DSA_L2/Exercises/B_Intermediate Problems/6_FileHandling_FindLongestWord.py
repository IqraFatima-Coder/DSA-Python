def find_longest_word(file_path):
    with open(file_path, 'r') as file:
        content = file.read()     
    words = content.split()
    longest_word = max(words, key=len)
    return longest_word
file_path = 'D:\\4thSemester\\DSA(Python)\\DSA_Lab\\DSA_Lab_Tasks_CodeFiles\\DSA_L2\\Exercises\\B_Intermediate Problems\\input.txt'
# Find and print the longest word
longest_word = find_longest_word(file_path)
print("Longest Word:", longest_word)  
