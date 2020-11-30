#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt", 'r') as name_file:
    names = name_file.readlines()

for name in names:
    with open("Input/Letters/starting_letter.docx") as letter:
        letter_content = letter.read()
        letter_content = letter_content.replace("[name]", name.strip())
        invitation = open("Output/ReadyToSend/intivation_for_"+name.strip()+".docx", "w")
        invitation.write(letter_content)
        invitation.close()
