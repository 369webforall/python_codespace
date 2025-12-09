s = "some long word hellow world"

reverse = s[::-1]

print(reverse)

text = "Hello Python!"

print(text.upper())
print(text.lower())

arr = s.split(" ")
print(arr)

print(text.find("Python"))
# return length of the string

print(s.find())

ec = "Hello Python"

encode = ec.encode("utf-8")
print(encode)

decode = encode.decode("utf-8")
print(decode)

name = "Robert Welker"
age = "65"

print("Hi my name is " + name + "and i am " + age + " year old")

print(f""" Hi my name is {name} and i am {age} year old """)