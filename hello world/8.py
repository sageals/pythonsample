command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started..")
        else:
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started:
            print("Car is already stoped")
        else:
            print("Car Stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - quit
          """)
    elif command == "quit":
        break
    else:
        print("Sorry i dont understand ")