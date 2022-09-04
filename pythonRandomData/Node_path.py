
import random
import string
import time


class Node_path():

    def __init__(self) -> None:
        self.option = ['nam', 'nữ']
        self.set_id = {-1}

    def random_email(self):
        k = random.sample(string.ascii_letters, 5)
        l = str(random.randint(10, 99))
        return ''.join(k) + l + '@gmail.com'

    def random_id(self, path):
        file_read_id = open(path, mode='r')
        list_id = file_read_id.read().split('\n')
        k = random.choice(list_id)
        while k in self.set_id:
            k = random.choice(list_id)
        self.set_id.add(k)
        return str(k)

    def random_gender(self):
        return str(random.choice(self.option))

    def random_object(self, path):
        file_read_name = open(path, mode='r')
        list_object = file_read_name.read().split('\n')
        k = random.choice(list_object)
        return str(k)

    def random_time(self):
        St_time = time.mktime(time.strptime("1/1/1990", '%m/%d/%Y'))
        En_time = time.mktime(time.strptime("1/1/2004", '%m/%d/%Y'))

        k = random.random()

        ran_time = St_time + k * (En_time - St_time)

        return time.strftime('%m/%d/%Y', time.localtime(ran_time))

