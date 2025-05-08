def binary_search_patient(patients, patient_id):
    left = 0
    right = len(patients) - 1
    while left <= right:
        mid = (left + right) // 2
        if patients[mid] == patient_id:
            return True
        elif patients[mid] < patient_id:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Example Usage:
patients = [1001, 1005, 1010, 1020, 1030]  # Sorted IDs
patient_id = 1020
print("Patient found:", binary_search_patient(patients, patient_id))  # Output: True
