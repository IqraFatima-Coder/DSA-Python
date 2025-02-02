# Problem 2: Attendance Tracker
class AttendanceTracker:
    def __init__(self, employees, days):
        self.attendance = [[0] * days for _ in range(employees)]
    
    def mark_attendance(self, employee, day):
        self.attendance[employee][day] = 1
    
    def attendance_percentage(self, employee):
        return (sum(self.attendance[employee]) / len(self.attendance[employee])) * 100
    
    def view_attendance(self):
        for emp, record in enumerate(self.attendance):
            print(f"Employee {emp + 1}: {record}")

# Testing AttendanceTracker
tracker = AttendanceTracker(5, 5)
tracker.mark_attendance(0, 0)
tracker.mark_attendance(1, 1)
tracker.mark_attendance(2, 2)
tracker.mark_attendance(3, 3)
tracker.mark_attendance(4, 4)
tracker.view_attendance()
print("Attendance Percentage for Employee 1:", tracker.attendance_percentage(0))
