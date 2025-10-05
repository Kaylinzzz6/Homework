# Ask user for last 4 digi of phone #
phone = input("Enter the last 4 numbers of your phone number:")

# if first digi is 8 or 9, second and third are the same, and last digi is 8 or 9 it's telemarketer
if phone[0] in {'8', '9'}: # []is the position in the last 4 digi of phone
    if phone[2] == phone[1]:
        if phone[-1] in {'8', '9'}:
            print(f"You phone number's last four digits are {phone} so it's a telemarketer")
        else: 
            print (f"Your phone number's last digits {phone} so it's not a telemarketer")
    else: 
        print (f"Your phone number's last digits {phone} so it's not a telemarketer")
else: 
    print (f"Your phone number's last digits are {phone} so it's not a telemarketer.")
