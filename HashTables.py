# Hashtable
class HashTable:
    """Flexible implementation of chain hash table. """

    def __init__(self, length, key_function, hash_function):
        self.hash_list = [[] for i in range(length)]
        self.length = length
        self.key_function = key_function  # Generates key from item
        self.hash_function = hash_function  # Generates table index from key

    def hash_map(self, item):
        """Get index of item"""
        return self.hash_function(self.key_function(item))

    def add(self, item):
        """Add item to hash table"""
        # Time complexity behavior is O(N) where N is number of items added, assuming a linked list
        # Space complexity O(1)
        index = self.hash_map(item)  # Calculate index
        self.hash_list[index].append(item)  # Add item to appropriate bucket

    def remove(self, key):
        """Delete item by key from hash table"""
        # Time complexity is O(N), as function must search through a list of up to N items.
        # Space complexity O(1)

        # Calculate index from key value
        index = self.hash_function(key)

        # Check through bucket for item with matching key
        for item in self.hash_list[index]:

            # If matching key is found, delete item and return true
            if self.key_function(item) == key:
                del item
                return True

        # If matching key is never found, return false
        return False

    def search(self, key):
        """Check if item with indicated key is present in table."""
        # Time complexity is O(N), as method must search through a list of up to N items
        # Space complexity is O(1)

        # Calculate index from key value
        index = self.hash_map(key)

        # Search through indexed bucket for item with matching key
        for item in self.hash_list[index]:
            if self.key_function(item) == key:
                return True
        return False

    def get(self, key):
        """Retrieve item with indicated key"""
        # Time complexity is O(N), as method must search through a list of up to N items
        # Space complexity is constant, O(1)

        # Calculate index from key value
        index = self.hash_function(key)

        # Search through indexed buckets for item with matching key
        for item in self.hash_list[index]:
            if self.key_function(item) == key:
                return item
        return None

    def count(self):
        """Get number of items in table"""
        # Time complexity is O(N), as method counts all N items added
        out = 0
        for bucket in self.hash_list:
            out += len(bucket)

        return out



