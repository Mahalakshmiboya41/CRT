''''
insertion
'''
arr = [10, 20, 30]

# Insertion at the beginning
arr.insert(0, 5)
print("After Inserting 5 at the Beginning:", arr)

# Insertion at the end
arr.append(40)
print("After Inserting 40 at the End:", arr)

# Insertion at a  position 
arr.insert(2, 15)
print("After Inserting 15 at Position 2:", arr)

''''
deleting
'''




# Deletion from the beginning
del arr[0]
print("After Deleting from Beginning:", arr)

# Deletion from the end
arr.pop()
print("After Deleting from End:", arr)

# Deletion from a specific position (e.g., index 2)
del arr[2]
print("After Deleting from Position 2:", arr)