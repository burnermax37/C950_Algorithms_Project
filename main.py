# Maxwell Burner, 002005686

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
import Addresses
import Distances
import Packages
import Trucks


if __name__ == '__main__':
    # Load data from files named by user input. Based on methods used, overall behavior is O(N^2) for time and space
    print("All file names should end with '.csv'")
    distance_filename = input("Enter name of file containing distance data: ")  # DistancesExtract.csv
    Distances.load_distance_data(distance_filename)

    address_filename = input("Enter name of file containing address list: ")  # addresses.csv
    address_table = Addresses.load_address_data(address_filename)

    package_filename = input("Enter name of file containing package list: ")  # package_data.csv
    package_table = Packages.load_package_data(package_filename, address_table)

    # Create empty lists
    truck_list = []  # Stores truck objects
    run_list = []  # Stores number of runs made by each truck

    # Create trucks based on user input
    truck_num = int(input("Enter number of trucks: "))  # Two trucks
    for i in range(truck_num):
        truck_list.append(Trucks.Truck(i + 1))

    # Get run counts for each truck
    for i in range(len(truck_list)):
        run_list.append(int(input("Enter numbers of runs for Truck {}: ".format(i + 1))))  # Three runs for both trucks

    # Collect user input to determine which packages go on which truck for which run
    print("Enter package IDs as comma-separated lists.")

    # Truck 1 run 1: [1, 13, 14, 15, 16, 19, 20]
    # Truck 2 run 1: [3, 29, 30, 31, 34, 37, 40]

    # Truck 1 run 2: [6]
    # Truck 2 run 2: [25]

    # Truck 1 run 3: [2, 4, 5, 7, 8, 10, 12, 17, 19, 21, 32] # 22
    # Truck 2 run 3:  [9, 11, 18, 22, 23, 24, 26, 27, 28, 33, 35, 36, 38, 39]

    # Late arrival packages are 6, 25, 28, 32, and 9
    # packages 13, 14, 15, 16, 19, and 20 must be delivered together
    # Packages 3, 18, 36, and 38 must be on truck 2

    # packages 3, 18, 36, and 38 must be on truck 2

    # For each truck
    for i in range(len(truck_list)):
        truck = truck_list[i]

        # For each run of current truck
        for j in range(run_list[i]):
            # Get list of package IDs from user
            id_string = input("Enter package IDs for run {} of truck {}: ".format(j + 1, i + 1))
            id_list = [int(num.strip()) for num in id_string.split(",")]

            # Assign packages to truck and make delivery run
            truck.package_list = [package_table.get(_id) for _id in id_list]
            truck.delivery_run()
            # Note that overall, instructions inside the loop of "deliver_run" will run once per package
            # This gives overall time complexity O(N) for this section

    print("")

    # Check truck mileage
    for truck in truck_list:
        print("Truck {} traveled {:.2f} miles".format(truck.id, truck.mileage))
    total_miles = sum([truck.mileage for truck in truck_list])
    print("Total miles traveled was {:.2f}".format(total_miles))

    print("")

    # Check status of packages
    Packages.check_package_status(package_table)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
