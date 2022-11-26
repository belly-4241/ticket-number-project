# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from cosmotics import cosmotics_ticket_number
from pharmaceutical import pharmaceutical_ticket_number
from perfumery import perfumery_ticket_number

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    while True:
        ope = input("Enter your choice among the above option")
        if ope == 'c':
             print("Your ticket number is :", "c_", next(cosmotics_ticket_number()))
        ope = input("Enter your choice among the above option")
        if ope == 'm':
           print("Your ticket number is :", "m_", next(pharmaceutical_ticket_number()))
        if ope == 'p':
            print("Your ticket number is :", "p_", next(perfumery_ticket_number()))
        # # else:
        #     print("Sorry place try agen")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
