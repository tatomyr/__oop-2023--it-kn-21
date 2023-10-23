phonebook = {  
    "Kurac" : 938477566,
    "Picka" : 938377264,
    "Smrdljiva" : 947662781
}  
# your code goes here
del phonebook["Picka"]
phonebook["Kurac"] = 938273443

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Picka" not in phonebook:      
    print("Picka is not listed in the phonebook.")  