#coding=utf-8
try:
    import os, sys, requests, struct, subprocess, fake_useragent, mechanize,pymysql
    from bs4 import BeautifulSoup as parser
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ImportError:
    os.system('pip2 install bs4 futures requests fake_useragent mechanize pymysql > /dev/null')
    os.system('python2 hop.py')
os.system('clear')
print(50*'-')
print('   This is last update from HOP. No further updates will be available.')
print('   Good bye FB & Termux')
print(50*'-')
print('   Loading ... ')
x = str(struct.calcsize("P") * 8)
distro = subprocess.check_output('uname -om', shell=True)
android_version = subprocess.check_output('getprop ro.build.version.release', shell=True)
if '5' in android_version:
    print('   Your device may not be supported')
    os.sys.exit()
else:
    if '32' in x and  'Android' in distro:
        os.system('chmod 777 h32 && ./h32')
    elif '64' in x and 'Android' in distro:
        os.system('chmod 777 h64 && ./h64')
    else:
        print('   Unknown machine detected, contact author')
