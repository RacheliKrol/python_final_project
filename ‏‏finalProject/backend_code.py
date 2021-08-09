import os
import re
def conv(path):
    """function that convert the path to real path"""
    k=path
    k=k.replace('\a','\\a')
    k=k.replace('\b','\\b')
    k=k.replace('\f','\\f')
    k=k.replace('\n','\\n')
    k=k.replace('\r','\\r')
    k=k.replace('\t','\\t')
    k=k.replace('\v','\\v')
    return k
last_action = dict() #dict to save the last replace for cancel

def renameFile(path, oldName, newName):
    """function that replace the old file name with a new"""
    last_action.clear()#init the dict
    try:
        path = conv(path)#convert path to real path
        if re.search(r'^\.', oldName) and re.search(r'^.', newName): #check if the user want to change the ending of the file
            for count, filename in enumerate(os.listdir(path)): #search the file on the directory
                if '.' in filename:
                    if oldName == '.' + filename.split(".")[1]: #found the file
                        src = os.path.join(path, filename) #connection full path for source
                        dst = os.path.join(path,str(filename.split(".")[0] + newName)) # connection full path for destination
                        last_action[src]= dst #save the action in the dict for cancel optional
                        os.rename(src, dst) #rename the file
        else:
            if not re.search(r'^[\\/:*?"<>|]', newName): # check if the new name is valid
                for count, filename in enumerate(os.listdir(path)): #search the file on the directory
                    if oldName == filename: #found the file
                        src = os.path.join(path, filename) #connection full path for source
                        dst = os.path.join(path , newName) # connection full path for destination
                        last_action[src]= dst #save the action in the dict for cancel optional
                        os.rename(src, dst) #rename the file
            else: #throw exception if the new name is not valid
                raise Exception("the file name is not valid, please enter a valid name")
    except: # throw exception if no such file or directory
        raise Exception("no such file or directory please enter ")


def cancel_last_action():
    """function that replace the lasted new name with the lasted old name= cancel last action"""
    for src in last_action.keys():
        os.rename(last_action[src], src)

