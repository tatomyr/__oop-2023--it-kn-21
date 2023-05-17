phonebook = {
    "John" : 9999999999,
    "jack" : 3333333333,
    "Jill" : 2222222222

}
phonebook ["Jake"]=00000000
del phonebook["Jill"]

if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook")