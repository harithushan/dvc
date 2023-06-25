with open("artifact.txt",'r') as f:
    text = f.read()

with open("artifact.txt",'w') as f:
    text= f.write(text + "added this line in the third stage")

print(text)
print("This is the end of third stage")