import hashlib
import os
import sys
import codecs

if int(sys.version_info[0]) < 3:
    print("Required python3 or greater..")
    sys.exit(1)
import hashid
import termcolor

class HashCracker():
    def __init__(self,filename,*argv):
        self.filename=filename
        self.userlist=[]
        self.test=argv
        self.hashlist=[]
    def cracking(self):
        if os.path.exists(self.filename):
            with open(self.filename,'rb') as fp:
                for  i in fp.readlines():
                    self.userlist.append(codecs.decode(i,'latin').replace('\n',''))
            try:
                data= str(os.popen('hashid %s' % (str(userrequest))).read()).split('[+]')

                if str(str(data[1]).replace('\n','')).strip() == "Unknown hash":
                    print("[-] Hash not detected")

                else:
                    print("[+] Detected")
                    print("[+] Trying to break hash")
                    values=None
                    for pi in data:
                        values=str(str(pi).replace("\n","")).strip().lower()
                        if values in self.test[0]:
                            break                

                    for i in self.userlist:
                        makertest=hashlib.new('%s' %(str(values.lower().replace('-',''))))
                        makertest.update(codecs.encode(i,'utf-8').strip())
                        finalhash=makertest.hexdigest()
                        if str(userrequest) == str(finalhash):
                            print("\n")
                            print(termcolor.cprint("Cracked %s\nValue is: %s" % (finalhash,i),'red','on_green'))
                            sys.exit(1)
                            break
                        else:
                            sys.stdout.write("\r%s------------->%s" % (finalhash,str(userrequest)))
                    print("\nCannot Break the hash\n")
                    sys.exit(1)
            
            except Exception as e:
                print('[-] System not supported for this operation')
        else:
            raise FileNotFoundError("[-] File Not Found pleae try again")
            sys.exit(1)


if __name__ == "__main__":
    userrequest=input("Enter the hash you want to crack: ")
    goli=[x.lower() for x  in ['md5','sha512','sha256','SHA-512','SHA-128','SHA-256']]
    cracker=HashCracker('test.txt',goli)
    cracker.cracking()
