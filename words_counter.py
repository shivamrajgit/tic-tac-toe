textInput=input("Enter Text:")
Punctuators=[".",",","!",'\"',"\'"]
noPunctuators=""
for i in textInput :
    if i not in Punctuators:
        noPunctuators+=i 
splittedText=noPunctuators.split()
print(len(splittedText))