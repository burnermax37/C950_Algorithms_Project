import Distances
import Packages
import Times
import Addresses

TRUCK_IN_BASE = 0
TRUCK_GOING_OUT = 1
TRUCK_RETURNING = 2
TRUCK_SPEED = 18 / 60  # 18 miles/hour divided by 60 minutes per hour, for miles per minute


class Truck:
    """Tracks packages on each truck as it runs deliveries, along with location of truck and time"""

    def __init__(self, id_num):
        self.id = id_num
        self.time = Times.Time(8, 0)  # Trucks leave no earlier than 8:00 am
        self.package_list = []
        self.location = Addresses.HUB_ADDRESS  # Each truck starts at hub
        self.status = TRUCK_IN_BASE  # Each truck starts dormant at hub
        self.mileage = 0  # Trucks have initially travelled zero miles

    def closest_package(self):
        """Determine which package in list is closest to current destination"""
        # Each package is checked once, and a truck has no more than 16 packages; time complexity is constant, O(1)
        # Space complexity is constant
        # Start by saving first package index as index of package with the closest destination address
        closest_package_index = 0
        package = self.package_list[0]
        min_distance = Distances.distance(self.location.id, package.destination.id)

        # For each package in truck after first
        for i in range(1, len(self.package_list)):
            # Get distance from truck location to package destination
            package = self.package_list[i]
            distance = Distances.distance(self.location.id, package.destination.id)

            # If distance is less than current minimum distance, set minimum distance to new distance
            if distance < min_distance:
                closest_package_index = i
                min_distance = distance

        return closest_package_index, min_distance

    def delivery_run(self):
        """Deliver all current packages"""
        # The while loop ends up iterating once per each package.
        # Looking at one call of this function, trucks have 16 packages or fewer, so time complexity is O(1)
        # See main for overall time complexity across all calls
        # Space complexity is O(1)

        # UPDATE PACKAGE STATUS
        for package in self.package_list:
            package.change_status(Packages.PACKAGE_EN_ROUTE, self.time.copy())

        # DETERMINE DEPARTURE TIME
        # Find most late arrival time of any package in truck, max_arrival_time
        max_arrival_time = self.package_list[0].arrival
        for i in range(1, len(self.package_list)):
            dispatch_time = self.package_list[i].arrival
            if dispatch_time > max_arrival_time:
                max_arrival_time = dispatch_time

        # If max_arrival_time is greater than truck's current time (time truck returns), update truck's current time
        if max_arrival_time > self.time:
            self.time = max_arrival_time

        # print("\nTruck {} leaves base at {}".format(self.id, self.time))

        # DELIVER PACKAGES
        # Until all packages are delivered
        while len(self.package_list) > 0:
            # Get closest package
            index, distance = self.closest_package()
            package = self.package_list.pop(index)

            # Travel, updating location, mileage, and time
            self.mileage += distance
            self.time.duration += int(distance / TRUCK_SPEED)
            # print("\tTruck {} traveled {} miles from {} to {} to deliver package {}".format(
            #     self.id,
            #     distance,
            #     self.location.street,
            #     package.destination.street,
            #     package.id
            # ))

            self.location = package.destination

            # Print message if a package was delivered late
            if self.time > package.deadline:

                print("Truck {} delivered package {} to {} at {}; TOO LATE".format(
                    self.id,
                    package.id,
                    package.destination,
                    self.time
                ))

            package.change_status(Packages.PACKAGE_DELIVERED, self.time.copy())

        # Return to base, updating location, mileage, and time
        distance = Distances.distance(0, self.location.id)

        self.mileage += distance
        self.time.duration += int(distance / TRUCK_SPEED)

        # print("\tTruck {} traveled {} miles from {} to hub".format(
        #     self.id,
        #     distance,
        #     self.location.street
        # ))

        self.location = Addresses.HUB_ADDRESS

        # print("Truck {} returned to base at {}".format(
        #     self.id,
        #     self.time
        # ))
