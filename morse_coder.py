"""
morse_code

Description:
"""
import translator



file = open("language.txt", "r")
read = file.read()
file.close()

file = open("memory.txt", "r")
memory = file.read()
file.close()



if read == "sound":
    sound = True
    setting = "On"
    anti_setting = "Off"
else:
    sound = False
    setting = "Off"
    anti_setting ="On"
        
        
        
print("Welcome to the morse code translator!")
true = True  
while true:
    print("Current Setting: Sound " + setting)        
    print("1. Translate to Morse Code" + " 2. Settings 3. END")
    choice = input()
    if choice == "1":
        print("Please enter the word you would like to translate to Morse Code:")
        word = input().lower()
        i = translator.translate(word)
        memory = i
        print(i)
        if sound:
            translator.play(i)
    elif choice == "2":
        print("1. Read last translation 2. Turn Sound " + anti_setting + " 3. Clear memory" )
        choice = input()
        if choice == "1":
            print(memory)
            if sound:
                translator.play(memory)
        elif choice == "2":
            if sound == True:
                sound = False
                setting = "Off"
                anti_setting = "On"
            else:
                sound = True
                setting = "On"
                anti_setting = "Off"
        elif choice == "3":
            memory = ""
        else:
            print("Please enter a valid number(1-3)")
            continue
    elif choice == "3":
        print("Bye!")
        file = open("memory.txt", "w")
        file.write(memory)
        file.close()
        
        
        
        if sound == True:
            language = "sound"
        else:
            language = ""
        
        
        
        file = open("language.txt", "w")
        file.write(language)
        file.close()
        break
    else:
        print("Please enter a valid number(1-3)")
        continue
