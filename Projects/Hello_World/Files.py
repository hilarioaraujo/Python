from pip._vendor.distlib.compat import raw_input

text = raw_input("Enter the text:> ")

file_obj = open("text.txt","w+")
file_obj.write(text)
file_obj.close()

file_obj = open("text.txt","r")
text = file_obj.readline()
print("Read text: ",text)