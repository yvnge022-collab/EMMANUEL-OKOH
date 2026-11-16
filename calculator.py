def speed():
    distance = float(input("Enter distance: "))
    time = float(input("Enter time: "))
    print("Speed =", distance / time, "m/s")


def force():
    mass = float(input("Enter mass: "))
    acceleration = float(input("Enter acceleration: "))
    print("Force =", mass * acceleration, "N")


def work():
    force_value = float(input("Enter force: "))
    distance = float(input("Enter distance: "))
    print("Work =", force_value * distance, "J")


def power():
    work_done = float(input("Enter work done: "))
    time = float(input("Enter time: "))
    print("Power =", work_done / time, "W")


while True:
    print("\nPHYSICS OPERATIONS")
    print("1. Speed")
    print("2. Force")
    print("3. Work")
    print("4. Power")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        speed()

    elif choice == "2":
        force()

    elif choice == "3":
        work()

    elif choice == "4":
        power()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Try again.")