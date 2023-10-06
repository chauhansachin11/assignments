"""
Parking Lot Tracker
    version-1  -> In this version state is not saved. Everything is maintained in memory. 
    Just remember that every time you close the application, the state will reset to its 
    initial condition (all spots available and no vehicles parked).
"""

class ParkingLot:
    """
    Represents a two-level parking lot with spots numbered from 1 to 40.
    Level A: 1-20, Level B: 21-40.
    """

    def __init__(self):
        self.available_spots = set(range(1, 41))
        self.vehicle_spot_map = {}

    def assign_parking_space(self, vehicle_number):
        """
        Assign a parking spot to the given vehicle.
        :param vehicle_number: Unique identifier for the vehicle.
        :return: Dictionary with parking spot details or error message.
        """

        if not self.available_spots:
            return {"error": "Parking is full"}

        if vehicle_number in self.vehicle_spot_map:
            return {"error": "Vehicle already parked"}

        spot = self.available_spots.pop()
        self.vehicle_spot_map[vehicle_number] = spot
        self.check_capacity()

        level = 'A' if 1 <= spot <= 20 else 'B'
        return {"level": level, "spot": spot}

    def retrieve_parking_spot(self, vehicle_number):
        """
        Retrieve the parking spot for a given vehicle.
        :param vehicle_number: Unique identifier for the vehicle.
        :return: Dictionary with parking spot details or error message.
        """

        spot = self.vehicle_spot_map.get(vehicle_number)
        if spot is None:
            return {"error": "Vehicle not found in parking"}

        level = 'A' if 1 <= spot <= 20 else 'B'
        return {"level": level, "spot": spot}

    def check_capacity(self):
        if len(self.available_spots) < 5:  # 5 is an arbitrary threshold
            print("Warning: Parking lot nearing full capacity!")


class TerminalInterface:
    # Terminal-based interface for users to interact with the parking lot.

    def __init__(self, parking_lot):
        self.parking_lot = parking_lot

    def start(self):
        while True:
            print("\n1. Park a vehicle")
            print("2. Find a vehicle")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self._park_vehicle()
            elif choice == 2:
                self._find_vehicle()
            elif choice == 3:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def _park_vehicle(self):
        # Handle parking of a vehicle.
        vehicle_number = input("Enter the vehicle number: ")
        result = self.parking_lot.assign_parking_space(vehicle_number)
        print(result)

    def _find_vehicle(self):
        # Handle finding of a parked vehicle.
        vehicle_number = input("Enter the vehicle number: ")
        result = self.parking_lot.retrieve_parking_spot(vehicle_number)
        print(result)


if __name__ == '__main__':
    # Entry point of the program.
    parking_lot = ParkingLot()
    interface = TerminalInterface(parking_lot)
    interface.start()
