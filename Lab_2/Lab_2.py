cryptMode = input("[1] Шифровать| [2] Расшифровать: ").upper()
if cryptMode not in ['1','2']:
	print("Ошибка: Введите цифру алгоритма"); raise SystemExit
startMessage = input("Введите текст: ").upper()
try:rotKey = int(input("Введите ключ: "))
except ValueError: print("Тут только цифры!"); raise SystemExit
def encryptDecrypt(mode, message, key, final = ""):
	for symbol in message:
		if mode == '1': 
			final += chr((ord(symbol) + key - 13)%26 + ord('A'))
		else: 
			final += chr((ord(symbol) - key - 13)%26 + ord('A'))
	return final
print("Результат:",encryptDecrypt(cryptMode, startMessage, rotKey))
