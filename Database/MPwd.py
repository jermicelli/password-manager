from PasswordManager.Backend.PManagerEncryption import Encryption
from passlib.hash import argon2
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import json
class MPassword():
    def create_password(self,message):
        hashedMPwd = argon2.hash(message)
        jfile = {"Master":{}}
        jfile["Master"] = hashedMPwd
        with open('mpHash.json','w') as fo:
            json.dump(jfile,fo,sort_keys=True,indent=4)
    def verify_password(self,message):
        ph = PasswordHasher()
        with open("mpHash.json",'r') as fi:
            jfile = json.load(fi)
        stored_pass = jfile["Master"]
        try:
            valid = ph.verify(stored_pass,message)
        except VerifyMismatchError:
            valid = False
        return valid

