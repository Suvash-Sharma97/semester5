import csv

# Function to load train data from CSV
def load_train_data(filename):
    trains = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                train_id = row['TrainID']
                trains[train_id] = {
                    'TrainName': row['TrainName'],
                    'SourceStation': row['SourceStation'],
                    'DestinationStation': row['DestinationStation'],
                    'TotalSeats': int(row['TotalSeats']),
                    'BookedSeats': 0
                }
        return trains
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading train data: {e}")
        return None

# Function to load passenger data from CSV
def load_passenger_data(filename):
    passengers = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                passengers.append({
                    'PassengerName': row['PassengerName'],
                    'TrainID': row['TrainID'],
                    'NumberOfTickets': int(row['NumberOfTickets'])
                })
        return passengers
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading passenger data: {e}")
        return None

# Function to check seat availability
def check_seat_availability(trains, train_id, num_tickets):
    if train_id not in trains:
        return False, "Invalid Train ID"
    
    available_seats = trains[train_id]['TotalSeats'] - trains[train_id]['BookedSeats']
    if available_seats >= num_tickets:
        return True, None
    else:
        return False, "Insufficient seats available"

# Function to update seat availability
def update_seat_availability(trains, train_id, num_tickets):
    trains[train_id]['BookedSeats'] += num_tickets

# Function to generate reports
def generate_reports(trains, passengers):
    # Report 1
    print("Report 1: Train Details")
    for train_id, details in trains.items():
        print(f"Train ID: {train_id}, Name: {details['TrainName']}, Source: {details['SourceStation']}, "
              f"Destination: {details['DestinationStation']}, Available Seats: {details['TotalSeats'] - details['BookedSeats']}")
    
    # Report 2
    print("\nReport 2: Revenue Details")
    revenue = {}
    fare_per_ticket = 50  # Define your fare rule
    for passenger in passengers:
        train_id = passenger['TrainID']
        num_tickets = passenger['NumberOfTickets']
        if train_id not in revenue:
            revenue[train_id] = 0
        revenue[train_id] += num_tickets * fare_per_ticket
    
    for train_id, total_revenue in revenue.items():
        print(f"Train ID: {train_id}, Total Revenue: {total_revenue}")

# Main function
def main():
    train_file_path = 'D:\\sem 5\\L_Advancedd pythone\\Train.csv'
    passenger_file_path = 'D:\\sem 5\\L_Advancedd pythone\\Passenger.csv'
    
    trains = load_train_data(train_file_path)
    if trains is None:
        return
    
    passengers = load_passenger_data(passenger_file_path)
    if passengers is None:
        return
    
    # Booking process
    for passenger in passengers:
        passenger_name = passenger['PassengerName']
        train_id = passenger['TrainID']
        num_tickets = passenger['NumberOfTickets']
        
        available, error = check_seat_availability(trains, train_id, num_tickets)
        if available:
            update_seat_availability(trains, train_id, num_tickets)
            print(f"Booking confirmed for {passenger_name} on train {train_id} for {num_tickets} tickets.")
        else:
            print(f"Booking failed for {passenger_name} on train {train_id}: {error}")
    
    # Generate reports
    generate_reports(trains, passengers)

if '__name___' == '_main_':
    main()