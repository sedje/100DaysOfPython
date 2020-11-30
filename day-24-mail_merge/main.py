PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt", 'r') as name_file:
    names = name_file.readlines()

for name in names:
    with open("Input/Letters/starting_letter.docx") as letter:
        letter_content = letter.read()
        letter_content = letter_content.replace(PLACEHOLDER, name.strip())
        invitation = open("Output/ReadyToSend/invitation_for_"+name.strip()+".docx", "w")
        invitation.write(letter_content)
        invitation.close()
