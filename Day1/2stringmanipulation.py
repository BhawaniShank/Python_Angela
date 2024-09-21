print("Hello World!\nHello country\nHello State")

#creating String 
greeting = 'Hello'
name = "Alice"
#concatination
full_greeting = greeting + ' ' + name
print(full_greeting) 
#string length 
print(len(name)) 
#Accessing characters
first_letter = name[0]
print(first_letter) 
#Slicing
print(name[1:3])

#String methods
# uppercase Lowercase
print(name.upper())
print(name.lower())

#Replace
sentence = "The quick brown fox"
new_sentence = sentence.replace("fox", "dog")
print(new_sentence)

#split
words = sentence.split()
print(words)

#join
joined = "*".join(words)  
print(joined)

#formatting 
age = 25
formatted = f"My name is {name} and I am {age} years old"  
print(formatted)





