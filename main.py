def encrypt(word,n):
  s=""
  for i in word:
    val=ord(i)
    if val>=97 and val<=122:
      n=n%26
      nval=val+n
      if nval>122:
        print("nval",nval)
        diff=nval-122
        s+=chr(97+diff-1)
        continue
      s+=chr(nval)
    else:
      s+=i

  print('The encrypted message is',s)
        
  

def decrypt(word,n):
  s=""
  for i in word:
    if n>26:
      n=n%26
    val=ord(i)
    if val>=97 and val<=122:
      nval=val-n
      if nval<97:
        diff=97-nval
        s+=chr(122-diff+1)
        continue
      s+=chr(nval)
    else:
      s+=chr(nval)

  print('The decoded message is',s)





  pass


print("""
_________                                     _________ .__       .__                  
\_   ___ \  ____ _____    ______ ___________  \_   ___ \|__|_____ |  |__   ___________ 
/    \  \/_/ __ \\__  \  /  ___// __ \_  __ \ /    \  \/|  \____ \|  |  \_/ __ \_  __\\
\     \___\  ___/ / __ \_\___ \\  ___/|  | \/ \     \___|  |  |_> >   Y  \  ___/|  | \/
 \______  /\___  >____  /____  >\___  >__|     \______  /__|   __/|___|  /\___  >__|   
        \/     \/     \/     \/     \/                \/   |__|        \/     \/       
 
Welcome to the Ceaser Ciper
It is named after Julius Ceaser
You have an option to encrypt or decrypt the message given

""")
message=input("Enter the message\n").lower()
key=int(input("Enter the places it has to be shifted\n"))
choice=input("""
Enter "encrypt" to perform encryption
Enter "decrypt" to perform decryption\n""")
if choice=="encrypt":
  encrypt(message,key)
elif choice=="decrypt":
  decrypt(message,key)
else:
  print('Wrong choice entered')

