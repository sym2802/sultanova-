cryptMode = input("[E]Зашифровать|[D]Расшифровать: ").upper()
if cryptMode not in ['E','D']:
	print("ОШИБКА!"); raise SystemExit
	
startMessage = input("Напишите сообщение на английском: ").upper()
numberKeys = int(input("Сколько ключей?: "))

listKeys = []
for index in range(numberKeys):
	 listKeys.append(input("Напишите ключевое слово["+str(index)+"]: ").upper())

def encryptDecrypt(mode, message, keys):
	for key in listKeys:
		final = ""
		key *= len(message) // len(key) + 1
		for index, symbol in enumerate(message):
			if mode == 'E':
				temp = ord(symbol) + ord(key[index])
			else:
				temp = ord(symbol) - ord(key[index])+26
			final += chr(temp % 26 + ord('A'))
		message = final
	return final
print("финальное сообщение:",encryptDecrypt(cryptMode, startMessage, listKeys))
