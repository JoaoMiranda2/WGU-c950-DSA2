"""
Joao Marcelo Martins Miranda
Student ID: 010548237
"""

# Import the CreateHashMap class from the hash_table module
from hash_table import CreateHashMap
# Create an instance of the hash table
hash_table = CreateHashMap()

# Test case 1: Insert and lookup values
print("Test 1: Insert and Lookup")
hash_table.insert(1, "Package 1")
hash_table.insert(2, "Package 2")
print("Key 1:", hash_table.lookup(1))  # Expected output: Package 1
print("Key 2:", hash_table.lookup(2))  # Expected output: Package 2

# Test case 2: Update an existing key
print("\nTest 2: Update Existing Key")
hash_table.insert(1, "Updated Package 1")
print("Key 1 after update:", hash_table.lookup(1))  # Expected output: Updated Package 1

# Test case 3: Lookup for a non-existent key
print("\nTest 3: Lookup Non-Existent Key")
print("Key 99:", hash_table.lookup(99))  # Expected output: None

# Test case 4: Large number of insertions
print("\nTest 4: Large Number of Insertions")
for i in range(100):
    hash_table.insert(i, f"Package {i}")
print("Key 50:", hash_table.lookup(50))  # Expected output: Package 50
print("Key 99:", hash_table.lookup(99))  # Expected output: Package 99

# Test case 5: Collision handling
print("\nTest 5: Collision Handling")
hash_table.insert(1, "Collision Test Package")
print("Key 1 after collision test:", hash_table.lookup(1))  # Expected output: Collision Test Package
hash_table.insert(21, "Collision Test Package 2")