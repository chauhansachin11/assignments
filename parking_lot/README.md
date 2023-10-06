# Parking Lot Tracker
A simple parking lot management system designed to track vehicle parking in a two-level parking lot. The system supports two primary operations:

* Assigning parking space to a new vehicle.
* Retrieving parking spot information for a particular vehicle.

The system is available in two versions:

* parking_lot.py -: In-memory storage version, which manages the parking state within the application's memory.
* parking_lot_withState.py -: JSON file-based persistence version, which saves the parking state to a local JSON file, allowing for data persistence across application restarts.

## Usage
### Running the Application
Run the Python script corresponding to the version you wish to use:
* For in-memory storage version:
    ```properties 
    python parking_lot.py
    ```
* For JSON file-based version:
    ```properties 
    python parking_lot_withState.py
    ```

### Interacting with the Terminal Interface
Upon running the application, you'll be presented with a menu:
1. Park a vehicle
2. Find a vehicle
3. Exit

* Choose 1 to park a new vehicle. You'll need to input the vehicle's unique number.
* Choose 2 to find an already parked vehicle. Input the vehicle number, and the system will display its parking spot and level.
* Choose 3 to exit the application.