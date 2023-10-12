#--------Dictionaries---------
print("\nDictionaries\n")

phonebook = {
    "Tolik": 38068325342,
    "Bolik": 380934475442,
    "Dodik": 380683487234,
    "Capybara": 380683543456
}

del phonebook["Dodik"]

if "Tolik" in phonebook:
    print("Tolik is listed in the phonebook.")

if "Dodik" not in phonebook:
    print("Dodik is not listed in the phonebook.")

#--------LISTS---------
print("\nLISTS\n")

name = ["Alex", "Igor", "Max"]
nums = []
str = []

second_name = name[1]

nums.append(1)
nums.append(2)
nums.append(3)

str.append("hello")
str.append("world")

print(nums)
print(str)
print("Second name: %s" % second_name)

#--------String---------
print("\nSTRING\n")

data = ("Artem", "Bebrovych", 69.69)
format_string = "Hello %s %s. Your accuracy is %s."

print(format_string % data)

#--------Variables---------
print("\nVARIABLES\n")

mystring = "hello"
myfloat = 13.37
myint = 69

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 13.37:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 69:
    print("Integer: %d" % myint)