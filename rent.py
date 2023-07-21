import operations
import filemanagement


def rent():
    """This function rents costumes"""
    di = {}
    brands_rented = []
    items_rented = []
    quantities_rented = {}
    name = input("Enter your name to continue: ")
    total_cost = 0
    total_quantities = 0
    c = 0
    with open("main_stock.txt", "r") as f:
        f_text = f.read().strip("\n")
        f_list = f_text.split("\n")
    for i in f_list:
        c += 1
        temp_li = i.split(",")
        di[c] = temp_li

    for key, value in di.items():
        quantities_rented[value[0]] = 0

    while True:
        operations.display_for_rent(di)
        total_dress = c

        global another_choice
        try:
            costume_id = int(input("Enter Costume ID: "))
        except ValueError:
            print("\n!!! Please provide a valid costume ID !!!")
            continue
        if operations.check_id(costume_id, total_dress) == "invalid":
            print("+++" * 15)
            print("!!! Please provide a valid costume ID !!!")
            print("+++" * 15)
            continue

        elif operations.check_id(costume_id, total_dress) == "valid":
            if operations.check_avail_quantity(costume_id, di) == "NA":
                print("\nSorry, Costume", costume_id, "is not available")
                print("Enter other Costume ID")
                continue
            elif operations.check_avail_quantity(costume_id, di) == "A":
                while True:
                    try:
                        qtity = int(input("Enter Quantity: "))
                    except ValueError:
                        print("\n!!! Please enter valid quantity !!!\n")
                        continue
                    sel_costume = di[costume_id]
                    avail_qtity = int(sel_costume[3])
                    price_per = float(sel_costume[2].strip("$"))
                    if qtity <= 0:
                        print("\nPlease enter a value greater than 0")
                        continue
                    elif qtity <= avail_qtity:
                        print("\nCostume ID is", costume_id)
                        print("Entered quantity is available")
                        total_cost += price_per * qtity
                        total_quantities += qtity
                        sel_costume[3] = str(avail_qtity - qtity)
                        di[costume_id] = sel_costume
                        items_rented.append(sel_costume[0])
                        brands_rented.append(sel_costume[1])
                        quantities_rented[sel_costume[0]] = quantities_rented[sel_costume[0]] + qtity
                        print(di)
                        another_choice = input("\nDo you want to rent another costume? ")
                        if another_choice == "n":
                            burrow_date = operations.get_date()
                            filemanagement.update_stock(di)
                            unique_id = filemanagement.generate_bill(name, burrow_date, total_cost, quantities_rented,
                                                                     total_quantities)
                            operations.display_bill(name, burrow_date, total_cost, quantities_rented, total_quantities)
                            print("\nHere is your Unique ID:", unique_id, "\nPlease give it to us while returning.")

                            break
                        else:
                            print("\nTotal Price =", total_cost)
                            break
                    else:
                        print("--" * 30 + "\nEntered quantity is more than we have available in stock\n" + "--" * 30)
                        continue
                if another_choice == "n":
                    break
                else:
                    continue
