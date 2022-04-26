from Crypto.Protocol.KDF import scrypt
import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad,unpad
class Encryption(): 
    def generate_key(self,message):
        salt = b'$\x93\x14q\x11>\x8b\xe3|\x84\x87Ke&\x82\xc0\xfe\x00\x0e\xfb\x80\x01N\x1a@y\xa73+6\xdf\xc6'
        if not (self.keyCheck()):
            key  = scrypt(message, salt, 32, N = 2**14, r =8, p=1)
            with open("secret.key","wb") as keyWrite:
                keyWrite.write(key)

    def load_key(self):
        return (open("secret.key","rb").read())

    def keyCheck(self):
        try:
            if(open("secret.key", "rb").read()):
                return True
        except:
            return False

    def encrypt_message(self,message):
        key = self.load_key()
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key,AES.MODE_CBC,iv)
        encoded_message = message.encode()
        encrypted_message = cipher.encrypt(pad(encoded_message,AES.block_size))
        return iv + encrypted_message

    def decrypt_message(self,message):
        key = self.load_key()
        iv=message[:AES.block_size]
        cipher = AES.new(key,AES.MODE_CBC,iv)
        decrypted_message = cipher.decrypt(message[AES.block_size:])
        return unpad(decrypted_message,AES.block_size).decode()
        


        

