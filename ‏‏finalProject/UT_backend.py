import backend_code
import os
def conv(strng):
    k=strng
    k=k.replace('\a','\\a')
    k=k.replace('\b','\\b')
    k=k.replace('\f','\\f')
    k=k.replace('\n','\\n')
    k=k.replace('\r','\\r')
    k=k.replace('\t','\\t')
    k=k.replace('\v','\\v')
    return k
def test_rename_file():
    backend_code.renameFile(conv('E:\רחלי לימודים\בוטקמפ\python\finalProject'), '.txt', '.py')
    for count, filename in enumerate(os.listdir(conv('E:\רחלי לימודים\בוטקמפ\python\finalProject'))):
        if filename.split('.')[1]=='txt':
            return False
        return True

def test_cancel():
    backend_code.cancel_last_action()
    for count, filename in enumerate(os.listdir(conv('E:\רחלי לימודים\בוטקמפ\python\finalProject'))):
        if filename.split('.')[1]=='txt':
            return True
        return False

print(test_rename_file())
print(test_cancel())


