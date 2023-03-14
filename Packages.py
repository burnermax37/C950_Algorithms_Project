import HashTables
import Times
import Addresses


# Package status enumerations
PACKAGE_NOT_DELIVERED = 0
PACKAGE_EN_ROUTE = 1
PACKAGE_DELIVERED = 2


# Change record class
class ChangeRecord:
    """Records each time package status changes, and what the new status value is"""

    def __init__(self, status, time):
        self.status = status
        self.time = time

    def __str__(self):
        status_string = "AT_HUB"
        if self.status == PACKAGE_DELIVERED:
            status_string = "DELIVERED"
        elif self.status == PACKAGE_EN_ROUTE:
            status_string = "EN_ROUTE"

        return "({},{})".format(status_string, self.time)


# Package class
class Package:
    """Stores package ID, destination address ID, and deadline, for one or more packages"""

    def __init__(self, _id, destination, deadline, weight, arrival):
        self.id = _id
        self.destination = destination
        self.deadline = deadline
        self.weight = weight
        self.arrival = arrival  # Earliest time package is available to be sent out

        self.status = PACKAGE_NOT_DELIVERED

        self.change_records = []  # Records each change in package status
        self.change_records.append(ChangeRecord(self.status, arrival))

        # print("Status of package {} updated to {} at {}".format(self.id,self.status,arrival))

    def __str__(self):
        return "Package {}, destination {}, arrives {}, deadline {}".format(self.id,
                                                                            self.destination,
                                                                            self.arrival,
                                                                            self.deadline)

    def change_status(self, status, time):
        """Change current status of package, and record change"""
        self.status = status
        self.change_records.append(ChangeRecord(status, time))
        # print("Status of package {} updated to {} at {}".format(self.id, self.status, time))

    def get_status_record(self, time):
        """Return record indicating package status at given time"""
        # Time complexity is based on record number, but no package will have more than three records, so O(1)

        # Work backwards through records until a record is found whose time is earlier than input time
        record_count = len(self.change_records)
        for i in range(record_count - 1, -1, -1):
            record = self.change_records[i]
            if record.time <= time:
                return record

        # If input time is before first record, status is not_delivered
        return ChangeRecord(PACKAGE_NOT_DELIVERED, time)

    def view_status(self, time):
        """Get string showing status of package at a given time"""
        change_record = self.get_status_record(time)

        if change_record.status == PACKAGE_DELIVERED:
            status_string = "delivered at {}".format(change_record.time)
        elif change_record.status == PACKAGE_EN_ROUTE:
            status_string = "en route".format(self.id, time)
        else:
            status_string = "at hub or not yet arrived at hub".format(self.id, time)

        out = "Package ID: {}, Address: {}, Deadline: {}, City: {}, State: {}, Zipcode: {}, Weight: {}, Status: {}"\
            .format(
                self.id,
                self.destination.street,
                self.deadline,
                self.destination.city,
                self.destination.state,
                self.destination.zipcode,
                self.weight,
                status_string
            )

        return out


PACKAGE_TABLE_SIZE = 48  # Global constant controlling number of buckets in package hash table.


# Create hashTable for packages based on id
def package_key(package):
    """Key is based package id"""
    return package.id


def package_hash(key):
    """Index is based on half-hour of day in which package must be delivered"""
    return key % PACKAGE_TABLE_SIZE


def load_package_data(filename, address_table):
    """Load package data from file into hash table"""
    # Loop iterates once per package, so time complexity is O(N)
    # Generated hash table has one entry per package in internal list, so space complexity is O(N)

    # Create empty hash table using above functions
    package_table = HashTables.HashTable(PACKAGE_TABLE_SIZE, package_key, package_hash)
    with open(filename) as package_file:
        lines = package_file.readlines()  # Read in data as array of strings

        for line in lines:
            # Get package data
            val_array = line.strip().split(",")
            destination = address_table.get(Addresses.string_character_sum(val_array[1]))
            deadline = Times.time_string_to_object(val_array[5])
            weight = int(val_array[6])
            arrival = Times.time_string_to_object(val_array[7])

            package = Package(int(val_array[0]), destination, deadline, weight, arrival)
            # print(package)

            package_table.add(package)

    return package_table


def check_package_status(table):
    """User interface to check status of any package at any time"""
    # Loop iterates as many times as user wants, independent of input size; assumed constant, so time complexity is O(1)
    # Space complexity is O(1)
    continue_flag = True
    print("--PACKAGE STATUS--")

    # Continue until user ends loop
    while continue_flag:

        # Get package ID, or end loop
        id_string = input("Enter id of package to check ('X' to exit, 'ALL' for all packages): ")

        # If input string is 'X', end loop
        if id_string == 'X':
            continue_flag = False

        else:
            # Get time
            time_string = input("Enter time at which to check package status (hh:mm AM or hh:mm PM): ")
            time = Times.time_string_to_object(time_string)

            print("\tTime: {}".format(time))

            # Display status for all packages or one package
            if id_string == "ALL":
                package_ids = range(1, table.count()+1)
                packages = [table.get(package_id) for package_id in package_ids]

                for package in packages:
                    print("\t{}".format(package.view_status(time)))
            else:
                # Get package object from table
                package_id = int(id_string.strip())
                package = table.get(package_id)

                # Display package status
                print("\t{}".format(package.view_status(time)))
