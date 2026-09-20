import csv
import os
from datetime import datetime

# ============================================================
# VEHICLE SERVICE CENTER MANAGEMENT SYSTEM
# ============================================================

CUSTOMER_FILE = "customers.csv"
VEHICLE_FILE = "vehicles.csv"
SERVICE_FILE = "service_records.csv"

SERVICE_TYPES = {
    "Oil Change": 5000.00,
    "Full Service": 15000.00,
    "Brake Service": 8000.00,
    "Engine Check": 6000.00,
    "AC Service": 7500.00,
    "Battery Check": 3000.00
}

SERVICE_STATUSES = ["Pending", "In Progress", "Completed"]


# ============================================================
# FILE HANDLING
# ============================================================

def load_data(filename):
    """Load records from a CSV file."""
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []


def save_data(filename, data, fieldnames):
    """Save records to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


customers = load_data(CUSTOMER_FILE)
vehicles = load_data(VEHICLE_FILE)
service_records = load_data(SERVICE_FILE)


# ============================================================
# ID GENERATION
# ============================================================

def get_next_id(records, field):
    """Generate the next numeric ID."""
    if not records:
        return 1

    ids = []
    for record in records:
        try:
            ids.append(int(record[field]))
        except (ValueError, KeyError):
            pass

    return max(ids, default=0) + 1


# ============================================================
# CUSTOMER MANAGEMENT
# ============================================================

def add_customer():
    print("\n--- Add New Customer ---")

    name = input("Enter Customer Name: ").strip()
    contact = input("Enter Contact Number: ").strip()
    email = input("Enter Email: ").strip()

    if not name or not contact:
        print("Name and contact number are required.")
        return

    customer_id = get_next_id(customers, "customer_id")

    customers.append({
        "customer_id": str(customer_id),
        "name": name,
        "contact": contact,
        "email": email
    })

    save_all_data()

    print(f"Customer added successfully! Customer ID: {customer_id}")


def view_customers():
    print("\n--- Customer List ---")

    if not customers:
        print("No customers found!")
        return

    for customer in customers:
        print(
            f"ID: {customer['customer_id']} | "
            f"Name: {customer['name']} | "
            f"Contact: {customer['contact']} | "
            f"Email: {customer['email']}"
        )


def search_customer():
    print("\n--- Search Customer ---")

    keyword = input("Enter customer name or contact number: ").strip().lower()

    found = False

    for customer in customers:
        if (keyword in customer["name"].lower()
                or keyword in customer["contact"].lower()):

            print(
                f"ID: {customer['customer_id']} | "
                f"Name: {customer['name']} | "
                f"Contact: {customer['contact']} | "
                f"Email: {customer['email']}"
            )
            found = True

    if not found:
        print("No matching customer found.")


# ============================================================
# VEHICLE MANAGEMENT
# ============================================================

def add_vehicle():
    print("\n--- Add Vehicle ---")

    if not customers:
        print("Please add a customer first.")
        return

    view_customers()

    customer_id = input("\nEnter Customer ID: ").strip()

    customer = find_customer(customer_id)

    if not customer:
        print("Customer not found.")
        return

    registration = input("Enter Vehicle Registration Number: ").strip().upper()
    vehicle_type = input("Enter Vehicle Type: ").strip()
    model = input("Enter Vehicle Model: ").strip()
    year = input("Enter Manufacturing Year: ").strip()

    if not registration or not vehicle_type or not model:
        print("Registration, vehicle type and model are required.")
        return

    vehicle_id = get_next_id(vehicles, "vehicle_id")

    vehicles.append({
        "vehicle_id": str(vehicle_id),
        "customer_id": customer_id,
        "registration": registration,
        "vehicle_type": vehicle_type,
        "model": model,
        "year": year
    })

    save_all_data()

    print(f"Vehicle added successfully! Vehicle ID: {vehicle_id}")


def view_vehicles():
    print("\n--- Vehicle List ---")

    if not vehicles:
        print("No vehicles found!")
        return

    for vehicle in vehicles:
        customer = find_customer(vehicle["customer_id"])
        customer_name = customer["name"] if customer else "Unknown"

        print(
            f"Vehicle ID: {vehicle['vehicle_id']} | "
            f"Registration: {vehicle['registration']} | "
            f"Type: {vehicle['vehicle_type']} | "
            f"Model: {vehicle['model']} | "
            f"Year: {vehicle['year']} | "
            f"Owner: {customer_name}"
        )


def search_vehicle():
    print("\n--- Search Vehicle ---")

    keyword = input(
        "Enter registration number, model or vehicle type: "
    ).strip().lower()

    found = False

    for vehicle in vehicles:
        if (
            keyword in vehicle["registration"].lower()
            or keyword in vehicle["model"].lower()
            or keyword in vehicle["vehicle_type"].lower()
        ):
            customer = find_customer(vehicle["customer_id"])
            customer_name = customer["name"] if customer else "Unknown"

            print(
                f"Vehicle ID: {vehicle['vehicle_id']} | "
                f"Registration: {vehicle['registration']} | "
                f"Model: {vehicle['model']} | "
                f"Owner: {customer_name}"
            )
            found = True

    if not found:
        print("No matching vehicle found.")


# ============================================================
# SERVICE MANAGEMENT
# ============================================================

def display_service_types():
    print("\n--- Available Services ---")

    number = 1

    for service, price in SERVICE_TYPES.items():
        print(f"{number}. {service} - Rs. {price:,.2f}")
        number += 1


def choose_service():
    services = list(SERVICE_TYPES.keys())

    display_service_types()

    try:
        choice = int(input("\nSelect Service: "))

        if 1 <= choice <= len(services):
            return services[choice - 1]

        print("Invalid service selection.")
        return None

    except ValueError:
        print("Please enter a valid number.")
        return None


def book_service():
    print("\n--- Book Vehicle Service ---")

    if not vehicles:
        print("No vehicles available. Please add a vehicle first.")
        return

    view_vehicles()

    vehicle_id = input("\nEnter Vehicle ID: ").strip()

    vehicle = find_vehicle(vehicle_id)

    if not vehicle:
        print("Vehicle not found.")
        return

    service_type = choose_service()

    if not service_type:
        return

    appointment_date = input(
        "Enter Service Date (YYYY-MM-DD): "
    ).strip()

    try:
        datetime.strptime(appointment_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    description = input(
        "Enter Service Description / Customer Request: "
    ).strip()

    service_id = get_next_id(service_records, "service_id")
    price = SERVICE_TYPES[service_type]

    service_records.append({
        "service_id": str(service_id),
        "vehicle_id": vehicle_id,
        "service_type": service_type,
        "date": appointment_date,
        "description": description,
        "cost": f"{price:.2f}",
        "status": "Pending"
    })

    save_all_data()

    print(
        f"Service booked successfully! "
        f"Service ID: {service_id}"
    )


def view_service_records():
    print("\n--- Service Records ---")

    if not service_records:
        print("No service records found!")
        return

    for record in service_records:
        vehicle = find_vehicle(record["vehicle_id"])

        registration = (
            vehicle["registration"]
            if vehicle else "Unknown"
        )

        print(
            f"Service ID: {record['service_id']} | "
            f"Vehicle: {registration} | "
            f"Service: {record['service_type']} | "
            f"Date: {record['date']} | "
            f"Cost: Rs. {float(record['cost']):,.2f} | "
            f"Status: {record['status']}"
        )


def update_service_status():
    print("\n--- Update Service Status ---")

    if not service_records:
        print("No service records found!")
        return

    view_service_records()

    service_id = input(
        "\nEnter Service ID: "
    ).strip()

    record = find_service(service_id)

    if not record:
        print("Service record not found.")
        return

    print("\n1. Pending")
    print("2. In Progress")
    print("3. Completed")

    choice = input("Select New Status: ").strip()

    status_map = {
        "1": "Pending",
        "2": "In Progress",
        "3": "Completed"
    }

    if choice not in status_map:
        print("Invalid status.")
        return

    record["status"] = status_map[choice]

    save_all_data()

    print("Service status updated successfully!")


def service_history():
    print("\n--- Vehicle Service History ---")

    registration = input(
        "Enter Vehicle Registration Number: "
    ).strip().upper()

    vehicle = None

    for item in vehicles:
        if item["registration"] == registration:
            vehicle = item
            break

    if not vehicle:
        print("Vehicle not found.")
        return

    found = False

    print(f"\nService History for {registration}")

    for record in service_records:
        if record["vehicle_id"] == vehicle["vehicle_id"]:
            print(
                f"Service ID: {record['service_id']} | "
                f"Service: {record['service_type']} | "
                f"Date: {record['date']} | "
                f"Cost: Rs. {float(record['cost']):,.2f} | "
                f"Status: {record['status']}"
            )
            found = True

    if not found:
        print("No service history found for this vehicle.")


# ============================================================
# BILLING
# ============================================================

def generate_bill():
    print("\n--- Generate Service Bill ---")

    if not service_records:
        print("No service records found!")
        return

    view_service_records()

    service_id = input(
        "\nEnter Service ID: "
    ).strip()

    record = find_service(service_id)

    if not record:
        print("Service record not found.")
        return

    vehicle = find_vehicle(record["vehicle_id"])

    if not vehicle:
        print("Vehicle information not found.")
        return

    customer = find_customer(vehicle["customer_id"])

    print("\n========================================")
    print("          VEHICLE SERVICE CENTER")
    print("              SERVICE BILL")
    print("========================================")

    print(
        f"Service ID : {record['service_id']}"
    )

    print(
        f"Date       : {record['date']}"
    )

    print(
        f"Customer   : "
        f"{customer['name'] if customer else 'Unknown'}"
    )

    print(
        f"Contact    : "
        f"{customer['contact'] if customer else 'Unknown'}"
    )

    print(
        f"Vehicle    : {vehicle['registration']}"
    )

    print(
        f"Model      : {vehicle['model']}"
    )

    print("----------------------------------------")

    print(
        f"Service    : {record['service_type']}"
    )

    print(
        f"Description: {record['description']}"
    )

    print("----------------------------------------")

    print(
        f"TOTAL      : Rs. "
        f"{float(record['cost']):,.2f}"
    )

    print(
        f"Status     : {record['status']}"
    )

    print("========================================")


# ============================================================
# REPORTS
# ============================================================

def reports():
    print("\n--- Service Center Reports ---")

    total_customers = len(customers)
    total_vehicles = len(vehicles)
    total_services = len(service_records)

    completed_services = 0
    pending_services = 0
    total_revenue = 0.0

    for record in service_records:

        if record["status"] == "Completed":
            completed_services += 1
            total_revenue += float(record["cost"])

        elif record["status"] == "Pending":
            pending_services += 1

    in_progress = total_services - completed_services - pending_services

    print("\n========================================")
    print("             BUSINESS REPORT")
    print("========================================")
    print(f"Total Customers      : {total_customers}")
    print(f"Total Vehicles       : {total_vehicles}")
    print(f"Total Service Jobs   : {total_services}")
    print(f"Completed Jobs       : {completed_services}")
    print(f"In Progress Jobs     : {in_progress}")
    print(f"Pending Jobs         : {pending_services}")
    print(f"Completed Revenue    : Rs. {total_revenue:,.2f}")
    print("========================================")


# ============================================================
# SEARCH FUNCTIONS
# ============================================================

def find_customer(customer_id):
    for customer in customers:
        if customer["customer_id"] == str(customer_id):
            return customer

    return None


def find_vehicle(vehicle_id):
    for vehicle in vehicles:
        if vehicle["vehicle_id"] == str(vehicle_id):
            return vehicle

    return None


def find_service(service_id):
    for record in service_records:
        if record["service_id"] == str(service_id):
            return record

    return None


# ============================================================
# SAVE ALL DATA
# ============================================================

def save_all_data():
    save_data(
        CUSTOMER_FILE,
        customers,
        ["customer_id", "name", "contact", "email"]
    )

    save_data(
        VEHICLE_FILE,
        vehicles,
        [
            "vehicle_id",
            "customer_id",
            "registration",
            "vehicle_type",
            "model",
            "year"
        ]
    )

    save_data(
        SERVICE_FILE,
        service_records,
        [
            "service_id",
            "vehicle_id",
            "service_type",
            "date",
            "description",
            "cost",
            "status"
        ]
    )


# ============================================================
# MAIN MENU
# ============================================================

def main_menu():

    while True:

        print("\n")
        print("==============================================")
        print("       VEHICLE SERVICE CENTER SYSTEM")
        print("==============================================")
        print("1.  Add Customer")
        print("2.  View Customers")
        print("3.  Search Customer")
        print("4.  Add Vehicle")
        print("5.  View Vehicles")
        print("6.  Search Vehicle")
        print("7.  View Available Services")
        print("8.  Book Vehicle Service")
        print("9.  View Service Records")
        print("10. Update Service Status")
        print("11. Vehicle Service History")
        print("12. Generate Service Bill")
        print("13. View Business Reports")
        print("14. Exit")
        print("----------------------------------------------")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_customer()

        elif choice == "2":
            view_customers()

        elif choice == "3":
            search_customer()

        elif choice == "4":
            add_vehicle()

        elif choice == "5":
            view_vehicles()

        elif choice == "6":
            search_vehicle()

        elif choice == "7":
            display_service_types()

        elif choice == "8":
            book_service()

        elif choice == "9":
            view_service_records()

        elif choice == "10":
            update_service_status()

        elif choice == "11":
            service_history()

        elif choice == "12":
            generate_bill()

        elif choice == "13":
            reports()

        elif choice == "14":
            save_all_data()
            print("\nAll data saved successfully.")
            print("Thank you for using the Vehicle Service Center System!")
            break

        else:
            print("Invalid choice! Please try again.")


# ============================================================
# PROGRAM START
# ============================================================

print("Vehicle Service Center Management System Initialized!")
main_menu()
