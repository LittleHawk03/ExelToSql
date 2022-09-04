
import string
from subprocess import list2cmdline
import time
import random
import tkinter as tk

from tkinter import filedialog


root = tk.Tk()
root.withdraw()
## lấy đường dẫn 
file_path = filedialog.askopenfilename()


print(file_path)

## chọn chết độ r là read 
file_read = open(file_path, mode='r')
list_name = list(file_read.read().split('\n'))


##
# lấy ngẫu nhiên thời gian này
# #
def random_time():
    St_time = time.mktime(time.strptime("1/1/1990", '%m/%d/%Y'))
    En_time = time.mktime(time.strptime("1/1/2004", '%m/%d/%Y'))

    k = random.random()

    ran_time = St_time + k * (En_time - St_time)

    return time.strftime('%m/%d/%Y', time.localtime(ran_time))


#
# lấy ngẫu nhiên tên 
# #
file_read_name = open('/home/honahl/Documents/AlgorithmsHackrankWriteup/pyhtonMiniProject/name.txt', mode='r')
list_name2 = list(file_read_name.read().split('\n'))
def random_name():
    k = random.choice(list_name)
    return str(k)


# print(random_name())

set_id = {''}
##
# lấy ngẫu nhiên id mấy cái có dạng unique hay primary key ấy
# #
file_read_id = open('/home/honahl/Documents/AlgorithmsHackrankWriteup/pyhtonMiniProject/maSV.txt', mode='r')
list_id = list(file_read_id.read().split('\n'))
def random_id():
    k = random.choice(list_id)
    while k in set_id:
        k = random.choice(list_id)
    set_id.add(k)
    return str(k)



file_read_local = open('/home/honahl/Documents/AlgorithmsHackrankWriteup/pyhtonMiniProject/local.txt',mode='r')
list_local = list(file_read_local.read().split('\n'))
def random_Local():
    k = random.choice(list_local)
    return str(k)

def random_gender():
    k = ['nam', 'nữ']
    return str(random.choice(k))

def random_email():
    k = random.sample(string.ascii_letters,5)
    l = str(random.randint(10,99))
    return ''.join(k) + l + '@gmail.com'

    

file_path = filedialog.askopenfilename()

file_write = open(file_path, mode= "a+")

# name_table = input('type name of table : ' ).upper()

# file_write.write("\nINSERT INTO " + name_table + "\n" + 
#                  "VALUES ")

for _ in range(7):
    # file_write.write('(')
    # file_write.write('\'' +random_id() + "\',")
    # file_write.write('N\'' + random_name() + '\',')
    # file_write.write('N\''+random_gender()+ '\',\'')
    file_write.write(random_email() + '\n')
    # file_write.write('N\''+random_Local()+ '\'')
    # file_write.write('),\n')

    

# print('\n'.join(c for c in list_name))
