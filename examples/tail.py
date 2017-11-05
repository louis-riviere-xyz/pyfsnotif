from time import sleep, time
from threading import Thread

def mk_toto():
    sleep(4)
    print('\n      make toto')
    open('/home/louis/toto', 'w')

def md_test():
    for _ in range(3):
        sleep(2)
        print('\n      modif test')
        with open('/home/louis/test', 'a') as test:
            test.write(f'{int(time())}\n')

Thread(target=mk_toto).start()
Thread(target=md_test).start()


from pyfsnotif import Watcher, MODIFY


def tail(event):
    fil = event.path
    print(f'\n\ttail {fil}')
    print(open(fil).readlines()[-1])


with Watcher() as w:
    w.add('/home/louis')
    w.add('/home/louis/test', MODIFY, tail)
