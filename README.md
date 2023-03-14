# C950_Algorithms_Project

Project to create a program that can load packages onto trucks, and schedule the order in which each truck delivers packages,
 so as to ensure that each package is delivered on time. 


The HashTable class in "HashTables.py" is used to create chain hashtables.
The Address class in "Addresses.py" is used to store information on each delivery address.
The "Distances.py" file contains classes to load distance data into a triangle matrix, and lookup distances between addresses.
The "Packages.py" file contains a Package class that stores ID, destination, and deadline for a package, a "ChangeRecord" class that
stores a record of each change in package status, and related methods.
The "Times.py" file contains a time class that tracks deadlines and calculates durations.
The "Trucks.py" file contains a Truck class that tracks which packages are on each truck, as well as where truck is at different times.
Finally, "main.py" contains the main function, including the actual algorithm used to control which package goes on which truck.