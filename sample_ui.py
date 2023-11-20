while True:
    user_input = input("Enter 1 to search by name, 2 to search by ingredient(s), or 3 to exit: ")
    # Search using name
    if user_input == "1":
        service_file = open("recipe_service.txt", "w")
        recipe_name = input("Enter recipe name: ")
        service_file.write(user_input + "\n" + recipe_name)
        service_file.close()
        ready_file = open("ready.txt", "w")
        ready_file.write("ready")
        ready_file.close()
        print("Done")
    # Search using ingredient(s)
    if user_input == "2":
        service_file = open("recipe_service.txt", "w")
        service_file.write(user_input + "\n")
        done = False
        while done is False:
            ingredient = input("Enter ingredient name or 1 when done: ")
            if ingredient == "1":
                done = True
            else:
                service_file.write(ingredient + "\n")
        service_file.close()
        ready_file = open("ready.txt", "w")
        ready_file.write("ready")
        ready_file.close()
        print("Done")
    elif user_input == "3":
        exit()

