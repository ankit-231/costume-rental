import datetime
import os


def get_option():
    """This function asks user for option and returns integer value of the input"""
    while True:
        try:
            option = input("\nSelect a desirable option: \
                    \n(1) || Press 1 to rent a costume. \
                    \n(2) || Press 2 to return a costume. \
                    \n(3) || Press 3 to exit.\
                    \nEnter an option: ")
            ioption = int(option)
            return ioption
        except ValueError:
            print("\n!!! Please enter a valid option !!!")
            continue


def check_id(costume_id, total_dress):
    """This function checks the validity of costume id taking costume_id, total_dress as parameters and returns
    "valid" or "invalid" """
    if 0 < costume_id <= total_dress:
        return "valid"
    return "invalid"


def check_avail_quantity(costume_id, di):
    """This function checks available quantity of costumes by taking costume_id, di as parameters"""
    sel_costume = di[costume_id]
    avail_qtity = int(sel_costume[3])
    if avail_qtity == 0:
        return "NA"
    return "A"


def get_date():
    """This function returns current date"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_brand(suit_name):
    """This function returns brand of given name of costume"""
    di = {}
    c = 0
    with open("main_stock.txt", "r") as f:
        f_text = f.read().strip("\n")
        f_list = f_text.split("\n")
    for i in f_list:
        c += 1
        temp_li = i.split(",")
        di[c] = temp_li
    for value in di.values():
        if suit_name in value:
            brand = value[1]
            return brand


def display_for_rent(di):
    """This function displays stock during return process"""
    print("\nLet's rent a costume.")
    print()

    print("---" * 30)
    print("{:<10}{:<20}{:<20}{:<20}{:<20}".format("ID", "Costume Name", "Costume Brand", "Price", "Quantity"))
    print("---" * 30)

    for key, val in di.items():
        print(f"{key:<10}", end="")
        for i in val:
            print(f"{i:<20}", end="")
        print("\n")


def display_for_return(di):
    """This function displays stock during return process"""
    print("\nLet's return a costume.")
    print("\nOur database:")

    print("---" * 30)
    print("{:<10}{:<20}{:<20}{:<20}{:<20}".format("ID", "Costume Name", "Costume Brand", "Price", "Quantity"))
    print("---" * 30)

    for key, val in di.items():
        print(f"{key:<10}", end="")
        for i in val:
            print(f"{i:<20}", end="")
        print("\n")


def display_bill(name, burrow_date, total_cost, quantities_rented, total_quantities):
    """This function displays bill during renting by taking name,
        burrow_date, total_cost, quantities_rented, total_quantities
        as parameters """
    suit_name_qty_li = []
    suit_brand_li = []
    print("\n" + "==" * 30 + f"\n{'BILL':^60}\n" + "==" * 30)
    print("**" * 30)
    print(f"{'Name of the Customer:':<25} {name}")
    print(f"{'Date and Time:':<25} {burrow_date}")
    print(f"{'Total Price:':<25} ${total_cost}")
    for key, value in quantities_rented.items():
        if value != 0:
            suit_name_qty = f"{key}: {value}"
            suit_name_qty_li.append(suit_name_qty)
            suit_brand = get_brand(key)
            suit_brand_li.append(suit_brand)
    print(f"{'Items Rented:':<25} {suit_name_qty_li}")
    print(f"{'Brands:':<25} {suit_brand_li}")
    print(f"{'Total Quantities:':<25} {total_quantities}")
    print("**" * 30)


def display_return_bill(name, costume_name, brand_name, return_date, total_fine):
    """This function displays bill during returning by taking name, costume_name,
        brand_name, return_date, total_fine as parameters"""
    name_temp = name.replace(" ", "")
    name_temp = name_temp.lower()
    return_date_temp = return_date.replace(" ", "")
    return_date_temp = return_date_temp.replace("-", "")
    return_date_temp = return_date_temp.replace(":", "")
    uniqueid = f"{name_temp.strip(' ')}{return_date_temp}"
    f_name = f"return_{uniqueid}.txt"
    f_path = "invoice"
    with open(os.path.join(f_path, f_name), "w") as f:
        print("\n" + "==" * 30 + f"\n{'BILL':^60}\n" + "==" * 30)
        print("**" * 30)
        print(f"{'Name of the Customer:':<25} {name}")
        print(f"{'Date and Time:':<25} {return_date}")
        print(f"{'Items Returned:':<25} {costume_name}")
        print(f"{'Brands:':<25} {brand_name}")
        print(f"{'Total Fine:':<25} ${total_fine}")
        print(f"{'Unique ID:':<25} {uniqueid}")
        print("**" * 30)


def from_bill(unique_id):
    """This function returns a dictionary with keys corresponding to "name", "days_rented", "name_quantity", "brand",
    "total_quantity" by taking unique_id as parameter """
    temp_dicti = {}
    f_path = r"invoice"
    f_name = "rent_" + unique_id + ".txt"
    with open(os.path.join(f_path, f_name), "r") as f:
        f_list = f.read().split("\n")

        # for customer's name
        temp_name = f_list[5].split(":")
        temp_name = temp_name[1].strip(" ")
        temp_dicti["name"] = temp_name

        # for calculating days rented
        temp_taken_date = f_list[6].split(" ")
        temp_taken_date = temp_taken_date[14].split("-")
        taken_date = datetime.date(int(temp_taken_date[0]), int(temp_taken_date[1]), int(temp_taken_date[2]))
        today_date = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month,
                                   datetime.datetime.now().day)
        days_rented = (today_date - taken_date).days
        temp_dicti["days_rented"] = days_rented

        # for name: quantity of suit
        temp_name_suit = f_list[8].split("[")
        temp_name_suit = temp_name_suit[1].strip("]")
        temp_dicti["name_quantity"] = temp_name_suit

        # for brand of suit
        temp_brand = f_list[9].split("[")
        temp_brand = temp_brand[1].strip("]")
        temp_dicti["brand"] = temp_brand

        # for total quantity
        temp_total_quantity = f_list[11].split(" ")
        temp_dicti["total_quantity"] = temp_total_quantity[-1]

    return temp_dicti


def get_id_from_name(suit_name):
    """This function returns the id for given costume name"""
    di = {}
    c = 0
    with open("main_stock.txt", "r") as f:
        f_text = f.read().strip("\n")
        f_list = f_text.split("\n")
    for i in f_list:
        c += 1
        temp_li = i.split(",")
        di[c] = temp_li
    for key, value in di.items():
        if suit_name in value:
            return key


def update_dictionary_return(temp_di, di):
    """This function returns updated dictionary during renting process by taking as parameters"""
    name_quantity = temp_di["name_quantity"].replace("'", "").split(", ")
    for i in name_quantity:
        tem = i.split(": ")
        selected_cos = di[get_id_from_name(tem[0])]
        selected_cos[3] = str(int(selected_cos[3]) + int(tem[1]))
    return di
