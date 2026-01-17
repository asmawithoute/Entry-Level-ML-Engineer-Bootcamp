import sys
import string

def text_analyzer(s: str):
    printable = sum(1 for c in s if c.isprintable() == True)
    upper = sum(1 for c in s if c.isupper() == True)
    lower = sum(1 for c in s if c.islower() == True)
    punc = sum(1 for c in s if c in string.punctuation)
    space = sum(1 for c in s if c.isspace() == True)
    print("The text contains ", printable ," printable character(s):")
    print("- ", upper, " upper letter(s)")
    print("- ", lower, " lower letter(s)")
    print("- ", punc, " punctuation mark(s)")
    print("- ", space, " space(s)")

if __name__=='__main__':
    if len(sys.argv) > 2:
        print("more than 1 argument was provided")
    else:
        text_analyzer(sys.argv[1])


# the subject sait that the func takes a str so idk how to check if it's not