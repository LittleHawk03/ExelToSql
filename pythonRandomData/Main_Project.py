from select import select
import tkinter as tk
from tkinter import filedialog

from Node_path import Node_path

root = tk.Tk()
root.withdraw()


k = int(input("so hang : "))
print('id - '+'id_identity - '+'gender - '+'time - '+ 'email - '+'diem -'+ 'object')
selection_data = input('nhap ten lua chon : ').lower()

#
# mở file để  ghi output.txt
# #
file_path2 = filedialog.askopenfilename()
file_write = open(file_path2, mode="a+")

node_path = Node_path()

if selection_data == 'id' or selection_data == 'object':
    file_path = filedialog.askopenfilename()
    

for i in range(k):
    if selection_data == 'id':
        #
        # lần mở thứ hai để mở file dữ liệu de doc
        # #
        file_write.write(node_path.random_id(file_path) + "\n")
    elif selection_data == 'id_identity':
        file_write.write(str(i+1) + "\n")
    elif selection_data == 'gender':
        file_write.write(node_path.random_gender() + '\n')
    elif selection_data == 'time':
        file_write.write(node_path.random_time() + '\n')
    elif selection_data == 'email':
        file_write.write(node_path.random_email() + '\n')
    elif selection_data == 'diem':
        file_write.write(node_path.random_point() + '\n')
    elif selection_data == 'object':
        #
        # lần mở thứ hai để mở file dữ liệu de doc
        # #
        file_write.write(node_path.random_object(file_path) + '\n')
    else:
        print('dont have your option')
        break