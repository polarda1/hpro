#coding=utf-8
import os,sys,time,random,struct
try:
    import requests
    import fake_useragent
    import bs4
except ModuleNotFoundError:
    os.system('pip install requests fake_useragent bs4 futures')
    os.system('python hop.py')
os.system('rm -rf .txt')
for x in range(5000):
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
if '32' in x:
    os.system('chmod 777 h32 && ./h32')
    os.sys.exit()
elif '64' in x:
    os.system('chmod 777 h64 && ./h64')
else:
    print('\n\n\n aarch cannot identified')
    os.sys.exit()
