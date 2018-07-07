str = "this has never happened before"


#key value pair

char_occurances = {} #represents dictionary

for char in str:
   char_occurances[char] =  char_occurances.get(char, 0) + 1
print(char_occurances)


word_occurances = {} #represents dictionary

for word in str.split():
   word_occurances[word] =  word_occurances.get(word, 0) + 1
print(word_occurances)