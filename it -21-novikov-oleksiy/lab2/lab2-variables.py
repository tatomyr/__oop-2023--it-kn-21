mystring = ("hi!")
myfloat = 12.5
myint = 75

if mystring == "hi!":
    print("string: %s" % mystring)
if isinstance (myfloat, float) and myfloat == 12.5:
    print("float : %f" % myfloat)
if isinstance (myint, int) and myint == 75:
    print("integer: %d" %myint)