# Vehicle Service Center Management System

A simple Python-based **Vehicle Service Center Management System** designed to manage customers, vehicles, service bookings, service records, billing, and basic business reports.

## 📌 Project Overview

This system helps a vehicle service center manage its day-to-day service operations through a simple command-line interface.

The system allows staff to register customers and their vehicles, book vehicle services, track service progress, view service history, generate service bills, and view basic business reports.

The system stores information using **CSV files**, so the data can be saved and loaded without requiring a database.

## ✨ Features

- 👤 Add and manage customers
- 🔍 Search customers
- 🚗 Register vehicles
- 🔎 Search vehicles
- 🛠️ View available vehicle services and prices
- 📅 Book vehicle services
- 📋 View service records
- 🔄 Update service status
- 📖 View vehicle service history
- 🧾 Generate service bills
- 📊 View business reports
- 💾 Automatic CSV data storage

## 🛠️ Available Services

The system currently provides the following services:

| Service | Price |
|---|---:|
| Oil Change | Rs. 5,000 |
| Full Service | Rs. 15,000 |
| Brake Service | Rs. 8,000 |
| Engine Check | Rs. 6,000 |
| AC Service | Rs. 7,500 |
| Battery Check | Rs. 3,000 |

## 🔄 Service Status

Each service can have one of three statuses:

- **Pending**
- **In Progress**
- **Completed**

## 📊 Business Reports

The reporting section provides basic information including:

- Total customers
- Total vehicles
- Total service jobs
- Completed service jobs
- In-progress service jobs
- Pending service jobs
- Revenue from completed services

## 💾 Data Storage

The application uses CSV files to store information.

The following files are automatically created:

```text
customers.csv
vehicles.csv
service_records.csv
```

### customers.csv

Stores customer information:

```text
Customer ID
Name
Contact
Email
```

### vehicles.csv

Stores vehicle information:

```text
Vehicle ID
Customer ID
Registration Number
Vehicle Type
Model
Manufacturing Year
```

### service_records.csv

Stores service information:

```text
Service ID
Vehicle ID
Service Type
Service Date
Description
Cost
Status
```

## 🖥️ Main Menu

The system provides the following main menu:

```text
1.  Add Customer
2.  View Customers
3.  Search Customer
4.  Add Vehicle
5.  View Vehicles
6.  Search Vehicle
7.  View Available Services
8.  Book Vehicle Service
9.  View Service Records
10. Update Service Status
11. Vehicle Service History
12. Generate Service Bill
13. View Business Reports
14. Exit
```

## 🧰 Technologies Used

- **Python 3**
- **CSV**
- **File Handling**
- **Functions**
- **Lists and Dictionaries**
- **Date Validation**
- **Command-Line Interface**

No external Python packages are required.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Vehicle-Service-Center-Management-System.git
```

### 2. Open the project folder

```bash
cd Vehicle-Service-Center-Management-System
```

### 3. Run the Python program

```bash
python Vehicle_Service_Center_Management_System.py
```

On some systems you may need:

```bash
python3 Vehicle_Service_Center_Management_System.py
```

## 📁 Project Structure

```text
Vehicle-Service-Center-Management-System/
│
├── Vehicle_Service_Center_Management_System.py
├── customers.csv
├── vehicles.csv
├── service_records.csv
└── README.md
```

The CSV files will be generated automatically when data is saved.

## 🎯 Project Objectives

The main objectives of this project are:

1. To simplify vehicle service center management.
2. To maintain customer and vehicle information.
3. To manage service appointments.
4. To track service progress.
5. To maintain vehicle service history.
6. To generate basic service bills.
7. To provide simple business reports.
8. To demonstrate practical Python programming and file-handling concepts.

## 🔮 Future Improvements

The system can be further improved by adding:

- Graphical User Interface (GUI)
- MySQL or MongoDB database
- User login and authentication
- Employee management
- Spare parts inventory
- Automatic invoice generation
- Appointment time slots
- SMS or email notifications
- Advanced financial reports
- Dashboard with charts and statistics

## 👨‍💻 Project

**Vehicle Service Center Management System**

Developed as a Python-based management system project.
