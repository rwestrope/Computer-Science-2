from datetime import date, timedelta, time

date_list = []

def list_to_num(num_list, str_list):
    for item in str_list:
        item = int(item)
        num_list.append(item)
    return num_list
# 1 Complete read_date()
def read_date():
    global date_list
    """Read a string representing a date in the format 2121-04-12, create a
    date object from the input string, and return the date object
    """
    user_date = input("input a date")

    temp_list = user_date.split("-")
    num_temp_list = []
    print(temp_list)

    list_to_num(num_temp_list, temp_list)
    print(num_temp_list)

    actual_date = date(num_temp_list[0], num_temp_list[1], num_temp_list[2])
    date_list.append(actual_date)

    print(date_list)

    

# 2. Use read_date() to read four (unique) date objects, putting the date objects in a list

# 3. Use sorted() to sort the dates, earliest first

# 4. Output the sorted_dates in order, earliest first, in the format mm/dd/yy

# 5. Output the number of days between the last two dates in the sorted list
#    as a positive number

# 6. Output the date that is 3 weeks from the most recent date in the list

# 7. Output the full name of the day of the week of the earliest day

read_date()