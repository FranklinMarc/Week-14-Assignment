import copy
Employee_info = []
#input information for 5 users
for i in range(5):
    print("Enter Employee details : ")
    #dictionary to store information
    store = {}
    #prompt the user for Employee_Id
    while True:

        Employee_Id = input("Enter Employee_Id : ")
        #if the Employee_Id is valid
        if len(Employee_Id) <= 7 and Employee_Id.isdigit():
            store["Employee_Id"] = Employee_Id
            break
        else:
            print("Please provide correct details for Employee_Id")

    #prompt the user for Employee_Name
    while True:
        Employee_Name = input("Enter Employee_Name : ")
        #if the Employee_Name is valid
        Upper = 0;Lower = 0;flag = 0

        for ch in Employee_Name:
            #check if it conatins digit ,blank space or special characters
            if ch == " " or ch in '1234567890' or ch in ' ! " @ # $ % ^ & * ( ) _ = + , < > / ? ; : [ ] { } \ )':
                flag = 1
                break
            elif ch.isupper():
                Upper += 1
            else:
                Lower += 1

        if flag == 0 and Upper > 0 and Lower > 0:
            store["Employee_Name"] = Employee_Name
            break
        else:
            print("Please provide correct details for Employee_Name")

    #prompt the user for Employee_email
    while True:
        Employee_email = input("Enter Employee_email : ")
        #if the Employee_email is valid
        Upper = 0;lower = 0;flag = 0;

        for ch in Employee_email:
            #check if it conatins digit ,blank space or special characters
            if ch == " " or ch in "1234567890" or ch in ' ! "  # $ % ^ & * ( ) _ = + , < > / ? ; : [ ] { } \ )':
                flag = 1
                break


        if flag == 0 :
            store["Employee_email"] = Employee_email
            break
        else:
            print("Please provide correct details for Employee_email")


    ask = input("Do you want to give the Address (Y/N) : ")
    if ask != 'N':
        #prompt the user for Employee_address
        while True:
            Employee_address = input("Enter Employee_address : ")
            #if the Employee_address is valid
            Upper = 0;lower = 0;flag = 0;

            for ch in Employee_address:
                #check if it conatins digit ,blank space or special characters
                if  ch in "1234567890" or ch in '!"#$%^&*()_=+,<>/?;:[]{}\)':
                    flag = 1
                    break

            if flag == 0 :
                store["Employee_address"] = Employee_address
                break
            else:
                print("Please provide correct details for Employee_address")
    else:
        print("You did not provide an address")

    #storing the details in the Employee Info
    Employee_info.append(copy.copy(store))


#displaying details
for data in Employee_info:
    print(data)