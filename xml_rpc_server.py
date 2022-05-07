from xmlrpc.server import SimpleXMLRPCServer

def StrLen(str):
    return len(str)
def SubstrInStr(str,sub):
    return str.count(sub)
def WordCountInStr(str):
    return len(str.split())
def StrType(str):
    str = str.replace(" ","")
    if str.isdigit():
        return "Только цифры"
    elif str.isalpha():
        return "Только символы"
    elif str.isalnum():
        return "Символы+цифры"
    elif str =="":
        return "Пустая строка"
    else:
        return "Со специальными символами"
def StrFormat(str):
    if str.isupper():
        return "Только верхний регистр"
    elif str.islower():
        return "Только строчные буквы"
    else:
        return "Смешанный"

server = SimpleXMLRPCServer(("localhost",6789))
server.register_function(StrLen,"StrLen")
server.register_function(SubstrInStr,"SubstrInStr")
server.register_function(WordCountInStr,"WordCountInStr")
server.register_function(StrType,"StrType")
server.register_function(StrFormat,"StrFormat")
server.serve_forever()