useria = input("input a string ")
useri = useria.lower()
count = 0

if len(useri) <= 4:
    print("Please enter a valid string.")
else:    
    for index_value in range(len(useri)):
        if index_value + 5 < len(useri):
            if useri[index_value] == "a":
                if useri[index_value + 5] == "b":
                    print(f"Match at {index_value} and {index_value + 5}")
                    count += 1
            elif useri[index_value] == "b":
                if useri[index_value + 5] == "a":
                    print(f"Match at {index_value} and {index_value + 5}")
                    count += 1
        if index_value + 1 == len(useri) and count == 0:
            print("No matches")
        elif index_value + 1 == len(useri) and count > 0:
            print(f"Scanned exactly {count} matches!")