import random
import socket
import threading
import os

#=============================================
#công cụ quét IP dành cho tấn công brute force
#=============================================


class BruteForceVPS:
    def __init__(self, targets_ip_path="targets.txt"):
        if os.path.exists(targets_ip_path) == False:
            with open(targets_ip_path, "a"):
                pass
        self.targets_ip_path = targets_ip_path
        self.ipNum = 0

    def random_ip(self):
        while True:
            g1 = str(random.choice([i for i in range(253)]))
            g2 = str(random.choice([i for i in range(253)]))
            g3 = str(random.choice([i for i in range(253)]))
            g4 = str(random.choice([i for i in range(253)]))
            if g1 in "127":
                g1 = "128"
            return f"{g1}.{g2}.{g3}.{g4}"

    def check_rdp(self):
        try:
            ip = self.random_ip()
            session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            session.settimeout(1)
            check_result = session.connect_ex((ip, 3389))
            if check_result == 0:
                with open("targets.txt", 'r', encoding="utf-8") as file:
                    ips = file.read().splitlines()
                if ip not in ips:
                    print(f"đã tìm thấy {ip}")
                    with open(self.targets_ip_path, "a", encoding="utf-8") as file:
                        file.write(f"{ip}\n")
        except:
            pass

    def multi_thread_scan(self, thread_num=100000):
        threads = []
        for _ in range(thread_num):
            thread = threading.Thread(target=self.check_rdp)
            thread.start()
            threads.append(thread)
        
        for t in threads:
            t.join()

thread_num = int(input("nhập số luồng : "))
while True:
    BruteForceVPS().multi_thread_scan(thread_num=thread_num)
