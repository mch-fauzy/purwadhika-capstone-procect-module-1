##############################
# NAMA      : MUCHAMAD FAUZY #
# TOPIC     : YELLOW PAGES   #
# TANGGAL   : 2023-02-19     #
##############################

data_list = [
    {'ID':'1', 'NAME':'FAST PAY', 'CATEGORY':'FINANCE', 'CITY':'SURABAYA', 'PHONE_NUMBER':'0315618077'},
    {'ID':'2', 'NAME':'ASTA EDU', 'CATEGORY':'EDUCATION', 'CITY':'BOGOR', 'PHONE_NUMBER':'+6288349683899'},
    {'ID':'3', 'NAME':'KLINIK XYZ', 'CATEGORY':'HEALTH', 'CITY':'SEMARANG', 'PHONE_NUMBER':'+6287555444000'},
    {'ID':'4', 'NAME':'RAYA ENGINEERING', 'CATEGORY':'CONSULTANT', 'CITY':'BANDUNG', 'PHONE_NUMBER':'0215921000'},
    {'ID':'5', 'NAME':'RESTO ASRI', 'CATEGORY':'RESTAURANT', 'CITY':'JAKARTA SELATAN', 'PHONE_NUMBER':'0215128000'}
]

##############
# READ LOGIC #
##############
def read():
    while True:
        print("")
        print("READ MENU")
        print("-"*30)
        print("1. Read All")
        print("2. Read by ID")
        print("3. Back")
        print("-"*30)
        sub_choice = int(input("Enter Read Options (1-3): "))
        if sub_choice == 1:
            read_all()
        elif sub_choice == 2:
            read_id()
        elif sub_choice == 3:
            break
        else:
            print('-> Wrong input')

def read_all():
    if not data_list:  # check if the data list is empty
        print("-> No data are found")
    else:
        print(f"-> Found {len(data_list)} records")
        print("")
        print(f"{'ID':<20} {'NAME':<20} {'CATEGORY':<20} {'CITY':<20} {'PHONE_NUMBER':<20}")
        for i in data_list:
            print(f"{i['ID']:<20} {i['NAME']:<20} {i['CATEGORY']:<20} {i['CITY']:<20} {i['PHONE_NUMBER']:<20}")

def read_id():
    if not data_list:  # check if the data list is empty
        print("-> No data are found")
    else:
        print(f"-> Found {len(data_list)} records")
        read_id = input("-> Enter ID to Read: ")
        search_record = [i for i in data_list if i['ID'] == read_id] #search available record based on ID
        if len(search_record) == 0: #check if ID is exist
            print(f"--> ID {read_id} is not found")
        else:
            print("")
            print(f"{'ID':<20} {'NAME':<20} {'CATEGORY':<20} {'CITY':<20} {'PHONE_NUMBER':<20}")
            print(f"{search_record[0]['ID']:<20} {search_record[0]['NAME']:<20} {search_record[0]['CATEGORY']:<20} {search_record[0]['CITY']:<20} {search_record[0]['PHONE_NUMBER']:<20}")

################
# CREATE LOGIC #
################
def create():
    while True:
        print("")
        print("CREATE MENU")
        print("-"*30)
        print("1. Create New Record")
        print("2. Back")
        print("-"*30)
        sub_choice = int(input("Enter Create Options (1-2): "))
        if sub_choice == 1:
            input_record()
        elif sub_choice == 2:
            break
        else:
            print('-> Wrong input')

def input_record():
    record = {}  # initialize an empty dictionary for each record
    print('-> Input the new record')
    create_id = input("-> Enter New ID: ").upper()
    if any(i['ID'] == create_id for i in data_list): # check if ID is exist
        print(f"--> ID {create_id} is already exist")
    else:
        record["ID"] = create_id
        record["NAME"] = input("-> Enter New Name: ").upper()
        record["CATEGORY"] = input("-> Enter New Category: ").upper()
        record["CITY"] = input("-> Enter New City: ").upper()
        record["PHONE_NUMBER"] = input("-> Enter New Phone Number: ").upper()
        while True:
            save_data = input("-> Do you want to save the record? (y/n): ")
            if save_data.upper() == 'Y':
                data_list.append(record)  # append the record to the data list
                print("--> Record created successfully")
                break #back to create menu
            elif save_data.upper() == 'N':
                print("--> Record is not saved")
                break #back to create menu
            else:
                print('--> Wrong input')
                continue #back to save prompt

################
# UPDATE LOGIC #
################
def update():
    while True:
        print("")
        print("UPDATE MENU")
        print("-"*30)
        print("1. Update Record")
        print("2. Back")
        print("-"*30)
        sub_choice = int(input("Enter Update Options (1-2): "))
        if sub_choice == 1:
            update_selection()
        elif sub_choice == 2:
            break #back to main menu
        else:
            print('-> Wrong input')

def update_selection():
    which_id = input("-> Which ID do you want to update?: ").upper()
    search_record = [i for i in data_list if i['ID'] == which_id] #search available record based on ID
    if len(search_record) == 0:
        print(f"--> ID {which_id} is not found")
    else:
        #Loop for update columns
        while True:
            print("")
            print(f"{'ID':<20} {'NAME':<20} {'CATEGORY':<20} {'CITY':<20} {'PHONE_NUMBER':<20}")
            print(f"{search_record[0]['ID']:<20} {search_record[0]['NAME']:<20} {search_record[0]['CATEGORY']:<20} {search_record[0]['CITY']:<20} {search_record[0]['PHONE_NUMBER']:<20}")
            print("")
            print("UPDATE SELECTION MENU")
            print("-"*30)
            print("1. Update ID")
            print("2. Update NAME")
            print("3. Update CATEGORY")
            print("4. Update CITY")
            print("5. Update PHONE_NUMBER")
            print("6. Update All Columns")
            print("7. Back")
            print("-"*30)
            which_data = int(input('Which column do you want to update? (1-7): '))

            # 1. Update ID Only
            if which_data == 1:
                new_id = input("-> Enter New ID: ").upper()
                if any(i['ID'] == new_id for i in data_list): # check if ID is exist
                    print(f"--> ID {new_id} is already exist")
                    break #back to update menu
                else:
                    # Loop for confirm update
                    while True:
                        print("")
                        print(f"{'ID':<20}")
                        print(f"{new_id:<20}")
                        sure = input("Are you sure want to update with this record? (y/n): ")
                        if sure.upper() == 'Y':
                            search_record[0]['ID'] = new_id
                            print('-> Record updated successfully')
                        elif sure.upper() == 'N':
                            print('-> Update canceled') 
                        else:
                            print('-> Wrong input')
                            continue #back to sure prompt
                        break
                    break #back to update menu

            # 2. Update NAME Only
            elif which_data == 2:
                new_name = input("-> Enter New Name: ").upper()
                # Loop for confirm update
                while True:
                    print("")
                    print(f"{'NAME':<20}")
                    print(f"{new_name:<20}")
                    sure = input("Are you sure want to update with this record? (y/n): ")
                    if sure.upper() == 'Y':
                        search_record[0]['NAME'] = new_name
                        print('-> Record updated successfully')
                    elif sure.upper() == 'N':
                        print('-> Update canceled') 
                    else:
                        print('-> Wrong input')
                        continue
                    break
                break

            # 3. Update CATEGORY Only
            elif which_data == 3:
                new_cat = input("-> Enter New Category: ").upper()
                # Loop for confirm update
                while True:
                    print("")
                    print(f"{'CATEGORY':<20}")
                    print(f"{new_cat:<20}")
                    sure = input("Are you sure want to update with this record? (y/n): ")
                    if sure.upper() == 'Y':
                        search_record[0]['CATEGORY'] = new_cat
                        print('-> Record updated successfully')
                    elif sure.upper() == 'N':
                        print('-> Update canceled')
                    else:
                        print('-> Wrong input')
                        continue
                    break
                break

            # 4. Update CITY Only
            elif which_data == 4:
                new_city = input("-> Enter New City: ").upper()
                # Loop for confirm update
                while True:
                    print("")
                    print(f"{'CITY':<20}")
                    print(f"{new_city:<20}")
                    sure = input("Are you sure want to update with this record? (y/n): ")
                    if sure.upper() == 'Y':
                        search_record[0]['CITY'] = new_city
                        print('-> Record updated successfully')
                    elif sure.upper() == 'N':
                        print('-> Update canceled') 
                    else:
                        print('-> Wrong input')
                        continue
                    break
                break
            
            # 5. Update PHONE NUMBER Only
            elif which_data == 5:
                new_phone = input("-> Enter New Phone Number: ").upper()
                # Loop for confirm update
                while True:
                    print("")
                    print(f"{'PHONE_NUMBER':<20}")
                    print(f"{new_phone:<20}")
                    sure = input("Are you sure want to update with this record? (y/n): ")
                    if sure.upper() == 'Y':
                        search_record[0]['PHONE_NUMBER'] = new_phone
                        print('-> Record updated successfully')
                    elif sure.upper() == 'N':
                        print('-> Update canceled') 
                    else:
                        print('-> Wrong input')
                        continue
                    break
                break

            # 6. Update All Columns
            elif which_data == 6:
                new_id = input("-> Enter New ID: ").upper()
                if any(i['ID'] == new_id for i in data_list): # check if ID is exist
                    print(f"--> ID {new_id} is already exist")
                    break #back to update menu
                else:
                    new_name = input("-> Enter New Name: ").upper()
                    new_cat = input("-> Enter New Category: ").upper()
                    new_city = input("-> Enter New City: ").upper()
                    new_phone = input("-> Enter New Phone Number: ").upper()
                    # Loop for confirm update
                    while True:
                        print("")
                        print(f"{'ID':<20} {'NAME':<20} {'CATEGORY':<20} {'CITY':<20} {'PHONE_NUMBER':<20}")
                        print(f"{new_id:<20} {new_name:<20} {new_cat:<20} {new_city:<20} {new_phone:<20}")
                        sure = input("Are you sure want to update with this record? (y/n): ")
                        if sure.upper() == 'Y':
                            search_record[0]['ID'] = new_id
                            search_record[0]['NAME'] = new_name
                            search_record[0]['CATEGORY'] = new_cat
                            search_record[0]['CITY'] = new_city
                            search_record[0]['PHONE_NUMBER'] = new_phone
                            print('-> Record updated successfully')
                        elif sure.upper() == 'N':
                            print('-> Update canceled') 
                        else:
                            print('-> Wrong input')
                            continue #back to sure prompt
                        break
                    break #back to update menu

            # 7. Back
            elif which_data == 7:
                break #back to update menu

            else:
                print('-> Wrong input')
                continue #back to update selection menu

################
# DELETE LOGIC #
################
def delete():
    while True:
        print("")
        print("DELETE MENU")
        print("-"*30)
        print("1. Delete Record")
        print("2. Back")
        print("-"*30)
        sub_choice = int(input("Enter Delete Options (1-2): "))
        if sub_choice == 1:
            del_id = input("-> Which ID do you want to delete?: ").upper()
            search_record = [i for i in data_list if i['ID'] == del_id] #search available record based on ID
            if len(search_record) == 0:
                print(f"--> ID {del_id} is not found")
            else:
                while True:
                    print("")
                    print(f"{'ID':<20} {'NAME':<20} {'CATEGORY':<20} {'CITY':<20} {'PHONE_NUMBER':<20}")
                    print(f"{search_record[0]['ID']:<20} {search_record[0]['NAME']:<20} {search_record[0]['CATEGORY']:<20} {search_record[0]['CITY']:<20} {search_record[0]['PHONE_NUMBER']:<20}")
                    sure = input("Are you sure want to delete this record? (y/n): ")
                    if sure.upper() == 'Y':
                        data_list.remove(search_record[0])  # remove the record from the data list
                        print('-> Record deleted successfully')
                    elif sure.upper() == 'N':
                        print('-> Delete canceled') 
                    else:
                        print('-> Wrong input')
                        continue #back to sure prompt
                    break
        elif sub_choice == 2:
            break #back to main menu
        else:
            print('-> Wrong input')

################
# CRUD PROGRAM #
################
while True:
    print("")
    print("MAIN MENU")
    print("-"*30)
    print("1. Read")
    print("2. Create")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    print("-"*30)
    choice = int(input("Enter Menu Options (1-5): "))
    if choice == 1:
        read()
    elif choice == 2:
        create()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    elif choice == 5:
        break
    else:
        print('-> Wrong input')