f = open("passwords.txt", "a")

print("""
        1] To Add Passwords 
        2] To See Passwords 
        """)

here = int(input("Enter Value: "))

while True:

    if (here == 2):
        here = int(input("Enter Password: "))

        if (here == 2004):
            r = open("passwords.txt", "r")
            print(r.read() + "\n")
            break

    if (here == 1):
        pass_add = input("Enter Password: ")
        print("[Password Added]")

        f.write("\n" + pass_add)
        f.close()
        break
