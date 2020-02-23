def anapoda_symfwna(word):
	proper_word = ""
	for i in range(len(word)-1, -1, -1):
		if word[i] not in "aeiouy":
			proper_word += word[i]
	return proper_word


filename = input("Give me the name of the file:\n\t")

if not(".txt" in filename):
	filename = filename + ".txt"

f = open(filename, "r")
text = f.read()
f.close()

all_words = text.split(' ')

for i in range(len(all_words)):
	proper_word = ""
	for j in range(len(all_words[i])):
		if (ord(all_words[i][j]) < 123 and ord(all_words[i][j]) > 96) or (ord(all_words[i][j]) < 90 and ord(all_words[i][j]) > 64):
			proper_word += all_words[i][j]
	all_words[i] = proper_word

words = []
for i in range(len(all_words)):
	if all_words[i] not in words:
		words.append(all_words[i])

len_of_words = []
for i in range(len(words)):
	len_of_words.append(len(words[i]))

for i in range(len(words)):
	for j in range(len(words)-i-1):
		if len_of_words[j] < len_of_words[j+1]:
			temp = len_of_words[j]
			len_of_words[j] = len_of_words[j+1]
			len_of_words[j+1] = temp
			temp = words[j]
			words[j] = words[j+1]
			words[j+1] = temp

print()
for i in range(5):
	print(anapoda_symfwna(words[i]))

print("\nNote: non-ascii characters are excluded from the word's length, and each word is included once.")

