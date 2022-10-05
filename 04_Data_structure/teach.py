#Set:
#jorge has graduated from school and now wants to teach Zortans how to talk in english. But English is complicated, so lets try to simplify it using set. 

#set is all about being 'unique' its very useful for certain operations 

#In a set all values are unique

#Set:
#jorge se graduó de la escuela y ahora quiere enseñar a los Zortans a hablar en inglés. Pero el inglés es complicado, así que intentemos simplificarlo usando set.

#set se trata de ser 'único', es muy útil para ciertas operaciones

#En un set todos los valores son únicos


# jorge wants to impress by showing some English magic, but Zortans are
# confused, they want him to first shows unique alphabets in his magic


magic_word: str = "abracadabra"
unique_alphabets: set[str] = set(magic_word)
print(f"Unique Alphabets: {unique_alphabets}")

sentence = "the big blue sky, and the big blue ocean"
unique_alphabets_1: set[str] = set(sentence)
print(f"Unique Alphabets: {unique_alphabets_1}")

#whats happens if we want to see list of unique words instead of alphabets

#word_list = sentence.split(',')
word_list = sentence.split()
print(f"Word list: {word_list}")

#extract hte unique words 

unique_words = set(word_list)
print(unique_words)

#Zortans are impressed and they want to add more words to the set

unique_words.update(["big", "blue", "sky"])
print(f"Unique list: {unique_words}") #nothing happends

unique_words.update(["green", "grass"])
print(f"Unique list: {unique_words}") #nothing happends

#Zortan don't like the word grass and wants to remove it

unique_words.remove("grass")
print(f"Unique list: {unique_words}")