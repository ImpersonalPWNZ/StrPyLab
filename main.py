def StrLen(str):
    return len(str)
def SubstrInStr(str,sub):
    return str.count(sub)
def WordCountInStr(str):
    return len(str.split())
def StrType(str):
    str = str.replace(" ","")
    if str.isdigit():
        return "Digit"
    elif str.isalpha():
        return "Alphabet only"
    elif str.isalnum():
        return "Alphabet+Digit"
    elif str =="":
        return "Null string"
    else:
        return "With special symbols"
def StrFormat(str):
    if str.isupper():
        return "Upper"
    elif str.islower():
        return "Lower"
    else:
        return "Mixed"


if __name__ == '__main__':
    str = 'ASD'
    print(StrFormat(str))


