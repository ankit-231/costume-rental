import operations
import filemanagement


def return_costume():
    while True:
        di = {}
        c = 0
        with open("main_stock.txt", "r") as f:
            f_text = f.read().strip("\n")
            f_list = f_text.split("\n")
        for i in f_list:
            c += 1
            temp_li = i.split(",")
            di[c] = temp_li
        operations.display_for_return(di)

        unique_id = input("Please enter the Unique ID \ngiven to you at the time of renting: ")
        try:
            temp_di = operations.from_bill(unique_id)
        except FileNotFoundError:
            print("\nPlease enter a valid Unique ID")
            continue

        total_quantities_rented = temp_di["total_quantity"]
        total_days_rented = temp_di["days_rented"]
        date_returned = operations.get_date()
        if total_days_rented > 5:
            late_days = total_days_rented - 5
            print("\nYou are", late_days, "days late.")
            fine = int(total_quantities_rented) * 2 * late_days
            operations.display_return_bill(temp_di["name"], temp_di["name_quantity"], temp_di["brand"],
                                           date_returned,
                                           fine)
            filemanagement.generate_return_bill(temp_di["name"], temp_di["name_quantity"], temp_di["brand"],
                                                date_returned,
                                                fine)

            di = operations.update_dictionary_return(temp_di, di)
            filemanagement.update_stock(di)
            operations.display_for_return(di)
            print("Congratulations! You have successfully returned your items.")
            break
        else:
            fine = 0
            operations.display_return_bill(temp_di["name"], temp_di["name_quantity"], temp_di["brand"],
                                           date_returned,
                                           fine)
            filemanagement.generate_return_bill(temp_di["name"], temp_di["name_quantity"], temp_di["brand"],
                                                date_returned,
                                                fine)

            di = operations.update_dictionary_return(temp_di, di)
            filemanagement.update_stock(di)
            operations.display_for_return(di)
            print("Congratulations! You have successfully returned your items.")
            break
