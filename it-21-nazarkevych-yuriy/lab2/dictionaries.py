phonebook = {
    "Bob": 380683487242,
    "Oleg": 380937073583,
    "Death": 380938370735,
    "Trex": 380999999999
}

del phonebook["Oleg"]

if "Bob" in phonebook:
    print("Bob is listed in the phonebook.")

if "Oleg" not in phonebook:
    print("Oleg is not listed in the phonebook.")