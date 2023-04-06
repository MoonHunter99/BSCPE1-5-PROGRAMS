def decryption():
    print("\033[1;34;40m `"*134)
    #kunin mo input ni user kung anong dedecrypt niya 
    msg_to_decrpypt = str(input("What is the message you want to decrypt?: "))
    decrypted_text = ""
    #palitan yung mga symbols ng corresponding letters tapos print mo na output
    for j in range(len(msg_to_decrpypt)):
        if msg_to_decrpypt[j] == "*":
            decrypted_text += "a"
        elif msg_to_decrpypt[j] == "&":
            decrypted_text += "e"
        elif msg_to_decrpypt[j] == "#":
            decrypted_text += "i"
        elif msg_to_decrpypt[j] == "+":
            decrypted_text += "o"
        elif msg_to_decrpypt[j] == "!":
            decrypted_text += "u"
        else:
            decrypted_text += msg_to_decrpypt[j]
    #print mo output
    print("\n"+decrypted_text+"\n")
    print("\033[1;34;40m `"*134)

def encryption():
    print("\033[1;36;40m `"*134)
    #kunin mo input ni user kung anong dedecrypt niya 
    msg_to_encrpypt = str(input("What is the message you want to encrypt?: "))
    encrypted_text = ""
    #palitan yung mga symbols ng corresponding letters tapos print mo na output
    for j in range(len(msg_to_encrpypt)):
        if msg_to_encrpypt[j] == "a":
            encrypted_text += "*"
        elif msg_to_encrpypt[j] == "e":
            encrypted_text += "&"
        elif msg_to_encrpypt[j] == "i":
            encrypted_text += "#"
        elif msg_to_encrpypt[j] == "o":
            encrypted_text += "+"
        elif msg_to_encrpypt[j] == "u":
            encrypted_text += "!"
        else:
            encrypted_text += msg_to_encrpypt[j]
    #print mo output
    print("\n" + encrypted_text + "\n")
    print("\033[1;36;40m `"*134)

#tanong kay user kung encryption ba or decryption
print("\033[1;33;40m `"*134)
user_input_decrypt_encrypt = input("Would you like to Decrypt or Encrypt a message? " )

user_input_list_encrypt = ["e" , "E" , "Encrypt" , "ENCRYPT"]
user_input_list_decrypt = ["d" , "D" , "Decrypt" , "DECRYPT"]

if user_input_decrypt_encrypt in user_input_list_encrypt :
    encryption()
elif user_input_decrypt_encrypt in user_input_list_decrypt:
    decryption()