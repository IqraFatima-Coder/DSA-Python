import json
def calculate_average_marks(json_data):
    students = json.loads(json_data)
    total_marks = sum(student['marks'] for student in students)
    average_marks = total_marks / len(students)
    return round(average_marks, 2)
# Input JSON
json_data = '''
[
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 90},
    {"name": "Charlie", "marks": 78}
]
'''
average_marks = calculate_average_marks(json_data)
print("Average Marks:", average_marks) 