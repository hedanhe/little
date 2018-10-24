import socket
import platform
import fcntl
import time
import sys

systype = platform.system()

class Flock(object):

    def __init__(self, name):
        self.fobj = open(name, 'w')
        self.fd = self.fobj.fileno()

    def lock(self):
        try:    #给文件枷锁
            fcntl.lockf(self.fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            print("给文件枷锁")
            time.sleep(20)
            return True
        except:
            print("文件枷锁，无法执行")
            return False

if __name__ == "__main__":
    # print(sys.argv[1])
    flock = Flock("./keypad.py")
    a = flock.lock()
    if a:
        print("文件枷锁成功")
    else:
        print("文件无法执行")