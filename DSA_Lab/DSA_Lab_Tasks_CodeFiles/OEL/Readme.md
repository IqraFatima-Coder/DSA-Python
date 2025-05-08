# Smart Parking Allocation System

## 🧪 Lab Manual #10 – Open-Ended Lab (CLO-3, C4)

**Course**: Data Structures and Algorithms  
**Instructor**: Engr. Shehryar Khan  
**University**: University of Engineering and Technology, Taxila

---

## 📝 Lab Title
**Smart Parking Allocation System Using Data Structures and Algorithms**

---

## 🎯 Lab Objectives

- Encourage critical thinking and algorithmic application.
- Practice system design with dynamic data handling.
- Implement real-time systems using:
  - Priority Queues
  - Hash Maps
  - Trees
- Analyze space and time complexity.

---

## 🧩 Problem Statement

Design an intelligent parking system that can:
- Manage multiple city zones (malls, hospitals, residences, offices).
- Dynamically allocate and deallocate parking spots.
- Handle multiple vehicle types: **Bike, Car, Truck**.
- Prioritize based on:
  - **VIPs**
  - **Handicapped**
  - **Electric Vehicles (EVs)**

---

## ✅ System Requirements

### The system should:

1. Track available and occupied spots.
2. Allocate slots based on:
   - Vehicle type
   - Priority category
3. Support the following operations:
   - Park a vehicle
   - Remove a vehicle
   - Show current status of slots
   - Find nearest available slot
   - Optimize slot usage across zones

---

## 👣 Tasks to Perform

### 1. Understand the Problem
- Identify vehicle types and slot categories.
- Consider constraints for priority access.
- Handle collisions during slot assignment.

### 2. Design the System Architecture
- Create **Vehicle** and **Slot** classes.
- Use:
  - **Queues** for waiting lines
  - **HashMaps** for slot lookup
  - **Heaps/Trees** for nearest available slots
  - **Arrays** for layout representation

### 3. Implement the System (in Python)
- Declare all variables using the prefix `var_`.
- Include:
  - Dynamic parking/unparking
  - Slot tracking (available vs. occupied)
  - Recommendations (e.g., next available in 2 mins)
  - Multi-zone simulation

### 4. Test the Implementation
- Simulate different scenarios:
  - All slots filled
  - Priority parking
  - Multiple vehicle types
- Create a **menu-driven interface** with the heading:
  ```
  Open-Ended Lab-Ten
  ```

### 5. Analyze and Report
- Provide **time and space complexity** of operations.
- Discuss **memory optimization** techniques.
- Explain **trade-offs** between different data structures used.

---

## 📦 Submission Requirements

- ✅ Python Code File (well-commented, using `var_` prefixes)
- ✅ Written Report with:
  - Problem Breakdown
  - Solution Design
  - Complexity Analysis
  - Screenshots/Console Logs

---

## 🧾 Example Output

```text
Open-Ended Lab-Ten
Welcome to Smart City Parking System

1. Park a Vehicle
2. Remove a Vehicle
3. Show All Parking Slots
4. Show Available Slots for EVs
5. Show Priority Vehicles
6. Exit

Choose Option: 1
Enter Vehicle Type: Car
Enter Priority (Y/N): Y
Allocated Slot: Zone B - Level 2 - Slot 05
```

---

## ✅ Final Note
At the end of the session, the program should output:
```
Lab completed successfully.
```

---

