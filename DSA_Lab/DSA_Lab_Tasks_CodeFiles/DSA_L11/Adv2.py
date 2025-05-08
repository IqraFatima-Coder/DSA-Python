def search_gps_location(locations, location_id):
    left = 0
    right = len(locations) - 1
    while left <= right:
        mid = (left + right) // 2
        if locations[mid] == location_id:
            return mid
        elif locations[mid] < location_id:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example:
locations = [101, 205, 307, 412, 515, 620]  # Sorted IDs
location_id = 412
print("Location found at index:", search_gps_location(locations, location_id))  # Output: 3
