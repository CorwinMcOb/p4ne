import os
import fnmatch

ip_list = []

for file in fnmatch.filter(os.listdir("./config_files/"), "*.txt"):
    # print(file)
    with open(file) as f:
        for line in f:
            if line.find("ip address")==1:
                ip_list.append(line)

for i in ip_list:
    print(i)