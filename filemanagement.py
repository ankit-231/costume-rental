from operations import *


def generate_bill(name, burrow_date, total_cost, quantities_rented, total_quantities):
    """This function generates bill to a txt file during renting by taking name, burrow_date, total_cost,
    quantities_rented, total_quantities as parameters and returns uniqueid"""
    suit_name_qty_li = []
    suit_brand_li = []
    name_temp = name.replace(" ", "")
    name_temp = name_temp.lower()
    burrow_date_temp = burrow_date.replace(" ", "")
    burrow_date_temp = burrow_date_temp.replace("-", "")
    burrow_date_temp = burrow_date_temp.replace(":", "")
    uniqueid = f"{name_temp.strip(' ')}{burrow_date_temp}"
    f_name = f"rent_{uniqueid}.txt"
    f_path = "invoice"
    with open(os.path.join(f_path, f_name), "w") as f:
        f.write("\n" + "==" * 30 + f"\n{'BILL':^60}\n" + "==" * 30)
        f.write("\n" + "**" * 30)
        f.write(f"\n{'Name of the Customer:':<25} {name}")
        f.write(f"\n{'Date and Time:':<25} {burrow_date}")
        f.write(f"\n{'Total Price:':<25} ${total_cost}")
        for key, value in quantities_rented.items():
            if value != 0:
                suit_name_qty = f"{key}: {value}"
                suit_name_qty_li.append(suit_name_qty)
                suit_brand = get_brand(key)
                suit_brand_li.append(suit_brand)

        f.write(f"\n{'Items Rented:':<25} {suit_name_qty_li}")
        f.write(f"\n{'Brands:':<25} {suit_brand_li}")
        f.write(f"\n{'Unique ID:':<25} {uniqueid}")
        f.write(f"\n{'Total Quantities:':<25} {total_quantities}")
        f.write("\n" + "**" * 30)
    return uniqueid


def generate_return_bill(name, costume_name, brand_name, return_date, total_fine):
    """This function generates bill during returning by taking name, costume_name,
        brand_name, return_date, total_fine as parameters and returns unique_id"""
    name_temp = name.replace(" ", "")
    name_temp = name_temp.lower()
    return_date_temp = return_date.replace(" ", "")
    return_date_temp = return_date_temp.replace("-", "")
    return_date_temp = return_date_temp.replace(":", "")
    uniqueid = f"{name_temp.strip(' ')}{return_date_temp}"
    f_name = f"return_{uniqueid}.txt"
    f_path = "invoice"
    with open(os.path.join(f_path, f_name), "w") as f:
        f.write("\n" + "==" * 30 + f"\n{'BILL':^60}\n" + "==" * 30)
        f.write("\n" + "**" * 30)
        f.write(f"\n{'Name of the Customer:':<25} {name}")
        f.write(f"\n{'Date and Time:':<25} {return_date}")
        f.write(f"\n{'Items Returned:':<25} {costume_name}")
        f.write(f"\n{'Brands:':<25} {brand_name}")
        f.write(f"\n{'Total Fine:':<25} ${total_fine}")
        f.write(f"\n{'Unique ID:':<25} {uniqueid}")
        f.write("\n" + "**" * 30)
    return uniqueid


def update_stock(dictionary):
    """This function updates stock in main file by taking a dictionary as parameter"""
    with open("main_stock.txt", "w") as f:
        for value in dictionary.values():
            f.write(",".join(value) + "\n")

    # to remove new line created at the end of the file

    with open("main_stock.txt", "r") as f:
        f_write_this = f.read().strip("\n")

    with open("main_stock.txt", "w") as f:
        f.write(f_write_this)
