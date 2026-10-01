required_attendance = 75

try:
    attendance = float(input("Enter attendance percentage: "))
    if attendance < required_attendance:
        raise ValueError("Attendance must be at least 75%.")
    print("Attendance requirement met.")
except ValueError as error:
    print("Attendance error:", error)