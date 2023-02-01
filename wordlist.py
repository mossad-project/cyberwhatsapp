import random, string

print("		***   ***   ***")
print("		 *     *     * ")
print("		 *     *     * ")
print("		 ************* ")
print("		      ***      ")
print("		      ***      ")
print("		      ***      ")
print("		      ***      ")
print("		     *****     ")
print("")
print("")
print("		    MOSSAD PROJECT")
print("")
print("")
print("")
print("Benvenuto nel generatore di possibili password.")
number_of_passwords = int(input("Quante possibili password vuoi generare? "))
password_length = int(input("Lunghezza massima della password: "))

characters = string.ascii_letters + string.digits + string.punctuation

for password_index in range(number_of_passwords):
    password = ""

    for index in range(password_length):
        password = password + random.choice(characters)

    print(" {} {}".format(password_index, password))
