"""
Joao Marcelo Martins Miranda
Student ID: 010548237
"""

import csv
from hash_table import CreateHashMap
from package import Package
from truck import Truck

# Function to load CSV data
def load_csv(filename):
    """
    Loads a CSV file.

    Args:
        filename (str): CSV file path.

    Returns:
        list: List of rows.
    """
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return list(reader)

# Load CSV data for distances, addresses, and packages
CSV_Distance = load_csv("data/distances.csv")
CSV_Address = load_csv("data/addresses.csv")
CSV_Package = load_csv("data/packages.csv")

import datetime

# Function to load package data into the hash table
def load_package_data(package_hash_table, filename="data/packages.csv"):
    """
    Loads package data into the hash table.

    Args:
        package_hash_table (CreateHashMap): Hash table to store package data.
        filename (str): Path to the CSV file containing package data.
    """
    package_data = load_csv(filename)
    for package in package_data:
        pack_id = int(package[0])
        deadline_str = package[5]
        if deadline_str == "EOD":
            deadline_time = datetime.timedelta(hours=23, minutes=59, seconds=59)
        else:
            deadline_time = datetime.datetime.strptime(deadline_str, "%I:%M %p").time()
            deadline_time = datetime.timedelta(hours=deadline_time.hour, minutes=deadline_time.minute)
        pack_obj = Package(pack_id, package[1], package[2], package[3], package[4], deadline_time, package[6], "At Hub")
        package_hash_table.insert(pack_id, pack_obj)

# Function to update the address of package #9 at a specific time
def update_package_9_address(current_time, package_hash_table, trucks):
    if current_time >= datetime.timedelta(hours=10, minutes=20):
        package = package_hash_table.lookup(9)
        if package:
            package.address = "410 S State St"
            package.city = "Salt Lake City"
            package.state = "UT"
            package.zipcode = "84111"
            package.status = "Out for Delivery"
            # Assign package #9 to Truck 3 if not already assigned
            if 9 not in trucks[2].packages:
                trucks[2].packages.append(9)
            print("Package #9 address updated to 410 S State St and assigned to Truck 3.")

# Function to calculate the distance between two addresses
def distance_between(x_value, y_value):
    return float(CSV_Distance[x_value][y_value] or CSV_Distance[y_value][x_value])

# Function to get the address number from the address list
def get_address_number(address):
    return next(int(row[0]) for row in CSV_Address if address in row[2])

# Function to calculate the distance between two addresses
def calculate_distance(address1, address2):
    address1_number = get_address_number(address1)
    address2_number = get_address_number(address2)
    return distance_between(address1_number, address2_number)

# Function to find the nearest package to the current location
def find_nearest_package(current_location, package_ids, pack_hash_table):
    nearest_package = None
    min_distance = float('inf')
    for package_id in package_ids:
        package = pack_hash_table.lookup(package_id)
        distance = calculate_distance(current_location, package.address)
        if distance < min_distance:
            min_distance = distance
            nearest_package = package
    return nearest_package

# Function to deliver packages using the nearest neighbor algorithm
def deliver_packages_nearest_neighbor(truck, pack_hash_table):
    current_location = "4001 South 700 East"  # Start location
    current_time = truck.depart_time  # Start time

    # Prioritize deadlines
    truck.packages.sort(key=lambda package_id: pack_hash_table.lookup(package_id).deadline_time)

    while truck.packages:
        nearest_package = find_nearest_package(current_location, truck.packages, pack_hash_table)  # Find nearest package
        truck.packages.remove(nearest_package.ID)  # Remove from truck
        truck.delivered_packages.append(nearest_package.ID)  # Add to delivered list

        distance = calculate_distance(current_location, nearest_package.address)  # Calculate distance
        travel_time = datetime.timedelta(hours=distance / truck.speed)  # Calculate travel time
        current_time += travel_time  # Update time
        truck.mileage += distance  # Update mileage
        current_location = nearest_package.address  # Update location
        nearest_package.status = "Delivered"  # Update status
        nearest_package.departure_time = current_time - travel_time  # Set departure time
        nearest_package.delivery_time = current_time  # Set delivery time


# Function to print the mileage of each truck
def print_truck_mileage(trucks):
    for truck in trucks:
        truck.print_mileage()

# Function to find which truck delivered a specific package
def find_package_truck(package_id, trucks, pack_hash_table):
    package = pack_hash_table.lookup(package_id)
    if package:
        for truck in trucks:
            if package_id in truck.delivered_packages or package_id in truck.packages:
                return truck.truck_id
    return None

# Main function to execute the delivery simulation
def main():
    while True:
        try:
            first_input = input("Type 'START' to start tracking or 'EXIT' to exit application: ").upper()
            if first_input == "EXIT":
                print("Exiting program!")
                break
            if first_input == "START":
                # Initialize trucks with their respective packages and departure times
                trucks = [
                    Truck(1, 16, 18, None, [1, 6, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East", datetime.timedelta(hours=8)),
                    Truck(2, 16, 18, None, [3, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5)),
                    Truck(3, 16, 18, None, [2, 4, 5, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))
                ]

                # Create a new hash table for packages and load package data
                pack_hash_table = CreateHashMap()
                load_package_data(pack_hash_table)

                status_time = input("Enter time to check status! Correct Format -> 24hr (HH:MM:SS): ")
                h, m, s = map(int, status_time.split(":"))
                convert_timedelta = datetime.timedelta(hours=h, minutes=m, seconds=s)

                # Dynamically update package #9's address based on user input time
                update_package_9_address(convert_timedelta, pack_hash_table, trucks)

                # Deliver packages after address update
                for truck in trucks:
                    deliver_packages_nearest_neighbor(truck, pack_hash_table)

                second_input = input("Type 'ALL' for all packages or 'SINGLE' for one package: ").upper()

                if second_input == "SINGLE":
                    pack_input = int(input("Provide the package ID: "))
                    package = pack_hash_table.lookup(pack_input)
                    package.update_status(convert_timedelta)
                    truck_id = find_package_truck(pack_input, trucks, pack_hash_table)
                    print(f"{package} with Truck {truck_id}")

                elif second_input == "ALL":
                    for package_id in range(1, 41):
                        package = pack_hash_table.lookup(package_id)
                        package.update_status(convert_timedelta)
                        truck_id = find_package_truck(package_id, trucks, pack_hash_table)
                        print(f"{package} with Truck {truck_id}")

                    print("Mileage Summary:")
                    print("Total mileage for all trucks: {:.2f}".format(sum(truck.mileage for truck in trucks)))
                    print_truck_mileage(trucks)
            else:
                print("Invalid input! Closing program.")
                break
        except ValueError:
            print("Invalid input! Closing program.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()