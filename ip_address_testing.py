import subprocess
import multiprocessing
import time

def get_ping_result(ip_address):
    #检查对应的IP是否被占用
    cmd_str = "ping " + ip_address + " -n 1 -w 600"
    try:
        subprocess.run(cmd_str, check=True ,timeout=2)  # 仅用于windows系统
    except subprocess.CalledProcessError as err:
        pass
    else:
        with open("ping.txt", "a+") as f:
            f.write(ip_address + "    True")
            f.write("\n")

if __name__ == '__main__':
    start_time = time.time()
    groups = ["192.168.0.{}".format(i) for i in range(255)]
    pool = multiprocessing.Pool()
    pool.map(get_ping_result,groups)
    print(time.time()-start_time)