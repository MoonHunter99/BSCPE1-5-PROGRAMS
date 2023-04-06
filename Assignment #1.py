while True:
    print("Hello my name is Neil Daniel G. Vergara\nWhat would you like to know about me?\n\n1. My Dream Job\n2. My Hobbies\n3. Why did i Choose Computer Engineering?")

    def dream_job():
        print("\nMy Dream Job is to become a Vessel I.T like my father in his company Maersk which is hopefully I would get in and have a stable job.\n")

    def Hobbies():
        print("\nWatching anime\nPlaying Online games\n\tValorant\n\tGenshin Impact\n\tLeague of Legends\nWatching Computer stuff(most likely LTT or Linus Tech Tips)\n")

    def CpE():
        print("\nI chose CpE or Computer Engineering because I like playing learning more about computers and mostly because when I was a kid I always see my parents doing stuff in the computer like fixing and troubleshooting our old computer.\nIts mostly also because that my parent's course is also computer engineering and yes both of them are computer engineers\n")

    ans = str(input("Choose the number of what you desire to know about me: "))
    if ans == '1':
        dream_job()
    elif ans == '2':
        Hobbies()
    elif ans == '3':
        CpE()

    yes_userinput= ['y','Y','yes','Yes','YES']
    no_userinput= ['n','N','no','No','NO']
    again= input("Want to know more about me?: ")
    if again in yes_userinput:
        continue
    elif again in no_userinput:
        print('\n\nThank you for knowing me :) ')
        break