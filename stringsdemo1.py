#Creating a string
pancard_number="AABGT6715H"
#Length of the string
print("Length of the PAN card number:", len(pancard_number))
#Concatenating two strings
name1 ="PAN "
name2="card"
name=name1+name2
print(name)
print("Iterating the string using range()")
for index in range(0,len(pancard_number)):
 print(pancard_number[index])

print("Iterating the string using keyword in")
for value in pancard_number:
 print(value)
print("Searching for a character in string")
if "Z" in pancard_number:
 print("Character present")
else: