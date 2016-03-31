# -*- coding: utf-8 -*-
import string
def encryptCesar(word, jump):
	word = word.lower()
	abcd = string.ascii_lowercase
	encrypt_word = ""
	try:
		for x in word:
			if x != " ":
				index = (abcd.index(x)+int(jump)) % len(abcd)
				encrypt_word += abcd[index]
			else:
				encrypt_word += x
	except ValueError:
		pass
	return encrypt_word

if __name__ == '__main__':
	print encryptCesar("hola",2)