import re
import time
import backend_code
import os
import unittest

def conv(s):
    k=s
    k=k.replace('\a','\\a')
    k=k.replace('\b','\\b')
    k=k.replace('\f','\\f')
    k=k.replace('\n','\\n')
    k=k.replace('\r','\\r')
    k=k.replace('\t','\\t')
    k=k.replace('\v','\\v')
    return k

class backendTestCase(unittest.TestCase):
    def __init__(self):
        self.backend_code = backend_code.backend()

    def test_rename_file(self):
        self.backend_code.renameFile(conv('E:\רחלי לימודים\בוטקמפ\python\finalProject'), '.txt', '.py')
        for count, filename in enumerate(os.listdir(conv('E:\רחלי לימודים\בוטקמפ\python\finalProject'))):
            if '.' in filename and filename.split('.')[1] == 'txt':
                return False
        return True

    def test_cancel(self):
        self.backend_code.cancel_last_action()
        for count, filename in enumerate(os.listdir(conv('E:\רחלי לימודים\בוטקמפ\python\finalProject'))):
            if re.search(r'\.', filename) and filename.split('.')[1] == 'txt':
                return True
        return False

    def main(self):
        print(self.test_rename_file())
        time.sleep(5)
        print(self.test_cancel())


if __name__ == '__main__':
    b = backendTestCase()
    b.main()




