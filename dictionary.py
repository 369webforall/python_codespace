student = {
    "name": "Dev",
    "age": 22,
    "country": "Nepal"
}

print(type(student))

print(student["age"])
print(student.get('country'))
print(student["email"])
print(student.get('email'))
student["age"] = 23

print(student["age"])

student["email"] = "dev@gmail.com"

print(student)

del student["email"]

print(student)

k = student.keys()
print(k)

print(student.values())

item = student.items()

print(item)

for key, value in student.items():
    print(f"the key is {key} : and value is {value}")


