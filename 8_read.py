file_r = open("myfile.txt","r")
print("Output of Read(14) function is ") 
print(file_r.read(14))
print()
  
file_r.seek(0)
  
print("Output of Readline(21) function is ") 
print(file_r.readline(21))
print()
  
file_r.seek(0)
# readlines function
print("Output of Readlines function is ") 
print(file_r.readlines()) 
print()
file_r.close()