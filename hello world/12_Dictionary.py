customer1 = {} # empty dictionary
customer = {
    "name": "sageal",
    "age": 24,
    "is_verified": True
}
print(customer["name"])
print(customer.get("age"))
customer["birthdate"] = "12 07 1997"  #addding new key value pair to dictionary
print(customer["birthdate"])
phone = input("Phobne : ")
digits_mapping = {
    "1": "One",
    "2":"Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)