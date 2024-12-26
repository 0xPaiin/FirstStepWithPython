def getdate():
    import datetime
    return datetime.datetime.now()
print("----Welcome to Health Management System ----")

client_list = {1 : "Harry", 2 : "Rohan", 3 : "Hammad"}
log_list = {1 : 'Diet', 2 : 'Exercise'}

try:
    print("Select client name: \n")
    for key,value in client_list.items():
        print("Press", key, "for", value)
    client_name = int(input("Enter your choice: "))
    if client_name not in client_list:
        print("Invalid Client Selection!")
        exit()
    
    print("Selected client: ",client_list[client_name], "\n")
    
    print("Press 1 to Log")
    print("Press 2 to Retrieve")
    op = int(input("Enter your choice: "))
    
    if op == 1:
        for key, value in log_list.items():
            print("Press", key, "to log", value)
        log_name = int(input("Enter your choice: "))
        
        if log_name not in log_list:
            print("Invalid log type selection!")
            exit()
        
        print("Selected Job: ", log_list[log_name])
        
        file_name = client_list[client_name] + "_" + log_list[log_name] + ".txt"
        with open(file_name, "a") as file:
            while True:
                print("Enter", log_list[log_name])
                my_text = input()
                file.write("[" + str(getdate()) + "]" + my_text + "\n")
                k = input("Add more? (y/n): ").lower()
                if k == "n":
                    break
                
    elif op == 2:
        for key,value in log_list.items():
            print("Press", key, "for", value)
        log_name = int(input("Enter your choie: "))

        if log_name not in log_list:
            print("Invalid log type selection!")
            exit()

        print("Retrieving", log_list[log_name], "for", client_list[client_name])

        file_name = client_list[client_name] + "_" + log_list[log_name] + ".txt"

        try:
            with open(file_name, "r") as f:
                contents = f.readlines()
                for line in contents:
                    print(line, end="")
        except FileNotFoundError:
            print("No records found!")
            
    else:
        print("Invalid Operation Selected")

except ValueError:
    print("Invalid input! Please enter a valid number.")

except KeyError:
    print("Invalid choice! Please select a valid option.")
except Exception as e:
    print("An unexpected error occurred:", e)
