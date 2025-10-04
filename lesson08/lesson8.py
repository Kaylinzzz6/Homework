# Let user input how many games they've won base on "W" and "L"
games = input("Enter results of 6 games (e.g. WWLLLW)")

# count the amount of wins
wins = 0
for results in games:
    if results in ["w", "W"]:
        wins += 1

# calculate what group user is in
if wins in range(5,6):
    print("You are in Group 1!")
elif wins in range(3,4):
    print("You are in Group 2!")
elif wins in range(1,2):
    print("You are in Group 3!")
elif wins in range (0):
    print("You are eliminated")
    
#YAY I DID IT