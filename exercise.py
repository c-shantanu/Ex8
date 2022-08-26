user_input = input("Input your string: ")
nemo_index = user_input.find("Nemo")

if nemo_index != -1:
    print("I found Nemo at ", nemo_index)

else:
    print("I can't find Nemo :(")