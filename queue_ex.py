from threading import Thread
import queue
from time import sleep

def producer(que):
    c = 0
    while True:
        c += 1
        message = 'ping' + str(c)
        que.put(message)
        sleep(1)

def worker(que):
    while True:
        message = que.get()
        print(message)

q = queue.Queue # обращение к библиотеке queue и вызов класса Queue,  которые потом будут
# передаваться потоку в качестве аргумента

tr1 = Thread(target=producer, args=(q,))
tr2 = Thread(target=worker, args=(q,))

tr1.start()
tr2.start()

tr1.join()
tr2.join()

