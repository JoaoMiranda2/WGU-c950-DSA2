"""
Joao Marcelo Martins Miranda
Student ID: 010548237
"""

class CreateHashMap:
    def __init__(self, initial_capacity=20):
        self.list = [[] for _ in range(initial_capacity)]  # Initialize hash table with empty buckets

    def _hash_function(self, key):
        hash_value = 0
        for char in str(key):
            hash_value = (hash_value << 5) + ord(char)  # Compute hash value
        return hash_value % len(self.list)  # Return bucket index

    def insert(self, key, item):
        bucket = self._hash_function(key)  # Get bucket index
        bucket_list = self.list[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item  # Update existing item
                return True
        bucket_list.append([key, item])  # Insert new item
        return True

    def lookup(self, key):
        bucket = self._hash_function(key)  # Get bucket index
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]  # Return item if found
        return None  # Return None if not found

    def hash_remove(self, key):
        bucket = self._hash_function(key)  # Get bucket index
        bucket_list = self.list[bucket]
        for i, pair in enumerate(bucket_list):
            if pair[0] == key:
                bucket_list.pop(i)  # Remove item if found
                return True
        return False  # Return False if not found