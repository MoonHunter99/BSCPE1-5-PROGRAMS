import pyfiglet
print("\033[1;34;40mHE"*130)
#Kunin yung input ni User AKA yung Message na gustong encrypt ni User
user_input_message = str(input("What is your message that you want to encrypt?: "))
#kunin yung Input ni user na keyword na gusto niyang gamitin
user_input_keyword = str(input("What is the Keyword that you would like to use?: "))
#lalgyan mo nung cyhered text
chpr_txt = ""
#Turn the characters of the User input to the respective number values ranging from 0-25(ang hirap pala ng ord function hindi ko maintindihan ng todo sir hirap din mag youtube)(REFERENCE: https://www.youtube.com/watch?v=mSuFvv12-vI&t=560s)
number_value_msg = [ord(w)-65 for w in user_input_message]
number_value_key = [ord(w)-65 for w in user_input_keyword]
#for loop para sa encryption
for i in range(len(user_input_message)):
    number_value = (number_value_msg[i] + number_value_key[i % len(user_input_keyword)]) % 26
    chpr_txt += chr(number_value + 65)
#print mo na output mo
print(chpr_txt)
print(pyfiglet.figlet_format ("Pinahirapan mo akong ord function ka : )\n"))
print("Reference: https://www.youtube.com/watch?v=mSuFvv12-vI&t=560s")
print("\033[1;36;40mHE"*130)