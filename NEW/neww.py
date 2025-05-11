def jesse_sort(data):
    # Initialize the Rainbow with the first element
    rainbow = [[data[0]]]
    for num in data[1:]:
        inserted = False
        for band in rainbow:
            # Check if num fits in the current band
            if band[0] <= num <= band[-1]:
                # Insert while maintaining the sorted order
                index = 0
                while index < len(band) and band[index] < num:
                    index += 1
                band.insert(index, num)
                inserted = True
                break
        if not inserted:
            # Create a new band for num
            rainbow.append([num])
            # Maintain the global order of bands based on their first elements
            rainbow.sort(key=lambda x: x[0])
    # Flatten the Rainbow into a single sorted list
    return [num for band in rainbow for num in band]

# Sample Data Array (50 Elements)
data = [87, 12, 45, 66, 21, 78, 33, 59, 10, 95,
        61, 37, 48, 29, 55, 76, 19, 70, 82, 15,
        34, 99, 5, 91, 44, 67, 39, 2, 84, 28,
        93, 13, 26, 6, 50, 32, 68, 7, 17, 22,
        53, 75, 4, 97, 30, 40, 80, 25, 92, 63]

# Sorting the data using JesseSort
sorted_data = jesse_sort(data)
print(sorted_data)
