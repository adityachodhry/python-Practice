file_w = open("myfile.txt","w")

L = ["Subject Code : BTIBM-403 \n","Semester : 4th \n"]

file_w.write("Subject : Python \n")

file_w.writelines(L)