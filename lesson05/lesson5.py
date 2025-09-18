# Lesson 5
start_money = float(input()) # float() helps cast argument to a real number
cookies_sold = input()

big_cookies = 0 # e.g. of variable initializing
cookies = 0

for current_cookie in cookies_sold:
    if current_cookie == "c":
        cookies += 1
    elif current_cookie =="b":
        big_cookies += 1
    else:
        print(f"{current_cookie} is not a valid sale item.")
    

total_cookies = big_cookies + cookies
profit = (big_cookies * 1.25) + (cookies * 0.75)
end_day = start_money + profit

print (f"In the end, you have {total_cookies} cookies, made ${profit}, and have ${end_day}")
