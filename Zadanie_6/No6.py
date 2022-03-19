#Напишите программу, в которой создается три дочерних потока. 
# В первом потоке вычисляется факториал числа (произведение натуральных чисел). 
# Во втором потоке вычисляется двойной факториал числа (произведение чисел через одно). 
# В третьем потоке вычисляется число из последовательности Фибоначчи (первые два числа равны единице, а каждое следующее равно сумме двух предыдущих).
import threading

def num(x, event_for_wait, event_for_set):
    for i in xrange(10):
        event_for_wait.wait() 
        event_for_wait.clear() 
        print x
        event_for_set.set() 


e1 = threading.Event()
e2 = threading.Event()
e3 = threading.Event()


t1 = threading.Thread(target=, args=(, e1, e2))
t2 = threading.Thread(target=, args=(, e2, e3))
t3 = threading.Thread(target=, args=(, e3, e1))


t1.start()
t2.start()
t3.start()

e1.set() 


t1.join()
t2.join()
t3.join()