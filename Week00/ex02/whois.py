import sys

if len(sys.argv) > 2 :
    print("AssertionError: more than one argument is provided")
    exit()
elif sys.argv[1].isdigit() == False:
    print("AssertionError: argument is not an integer")
    exit()
n = int(sys.argv[1])
res = "I'm Zero." if n == 0 else ("I'm Even." if n % 2 == 0 else "I'm Odd.")
print(res)