#--------Conditions---------
print("\nConditions\n")
num = 16
second_num = 0
f_array = [1,2,3]
s_array = [1,2]

if num > 15:
    print("1")

if f_array:
    print("2")

if len(s_array) == 2:
    print("3")

if len(f_array) + len(s_array) == 5:
    print("4")

if f_array and f_array[0] == 1:
    print("5")

if not second_num:
    print("6")

#--------LOOPS---------
print("\nLOOPS\n")

nums = [
    951, 202, 184, 451, 350, 69, 478, 319, 631,
    495, 920, 501, 525, 537, 944, 665, 57, 164,
    123, 101, 123, 527, 867, 555, 249, 360, 984,
    576, 126, 105, 942, 941, 386, 462, 47, 418,
    907, 344, 236, 375, 833, 566, 597, 978, 328,
    615, 953, 345, 399, 162, 758, 219, 918, 634,
    412, 566, 826, 248, 856, 950, 626, 949, 687,
    666, 876, 67, 104, 563, 123, 567, 892, 894,
    767, 967, 81, 379, 843, 831, 445, 742, 717,
    958, 65, 842, 451, 32, 753, 854, 685, 93, 857,
    440, 153, 126, 721, 328, 753, 470, 743, 527
]

# your code goes here
for num in nums:
    if num == 666:
        break