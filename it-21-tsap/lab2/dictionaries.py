phonebook = {  
    "Nastya" : 0938475166,
    "Tanya" : 0938337264,
    "Olha" : 0977666781,
    "Victoria" : 0938773443
}  

del phonebook["Nastya"]

if "Olha" in phonebook:  
    print("Olha is listed in the phonebook.")
    
if "Nastya" not in phonebook:      
    print("Nastya is not listed in the phonebook.")  