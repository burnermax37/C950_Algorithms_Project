import HashTables


# Address class
class Address:
    """Stores ID and components of address"""

    def __init__(self, _id, street, city, state, zipcode):
        self.id = _id
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        return "{}, {}, {} {}".format(self.street, self.city, self.state, self.zipcode)


HUB_ADDRESS = Address(0, None, None, None, None)  # Stores copy of address for delivery hub

# load addresses

ADDRESS_TABLE_SIZE = 5  # Global constant controlling number of buckets in hash table for addresses


# Separated for use in hashtable get method calls
def string_character_sum(street_string):
    """Convert address street name into integer key"""
    # Time complexity is dependent on length of street names, but this is assumed constant, so O(1)
    # Space complexity O(1)
    char_sum = 0
    # Calculate sum of integer values for each character in street address string
    for char in street_string:
        char_sum += ord(char)

    return char_sum


def address_key(address):
    """Convert address into integer key"""
    return string_character_sum(address.street)


def address_hash(key):
    """Convert integer key into index for hash table"""
    return key % ADDRESS_TABLE_SIZE


def load_address_data(filename):
    """Read address file data into a hash table"""
    # The loop iterates once per address, so time complexity is O(N)
    # The created hash table uses a list of one item per address, so space complexity is O(N)

    # Create empty hash table using address hashing methods.
    table = HashTables.HashTable(ADDRESS_TABLE_SIZE, address_key, address_hash)

    with open(filename) as file:
        # Read lines of file
        lines = file.readlines()

        # For each line in CSV file
        for line in lines:
            val_array = line.strip().split(",")
            # Create address object using values from line
            address = Address(int(val_array[0]), val_array[1].strip(), val_array[2], val_array[3], int(val_array[4]))

            # Save hub address
            if address.id == 0:
                HUB_ADDRESS.street = address.street
                HUB_ADDRESS.city = address.city
                HUB_ADDRESS.state = address.state
                HUB_ADDRESS.zipcode = address.zipcode

            if address is None:
                print("BAD")
            # else:
                # print("{}: {}".format(address.id, address))

            # Store address in table
            table.add(address)
    return table
