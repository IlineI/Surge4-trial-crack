import os
import time

print('请输入sudo密码')
#os.system("rm -rf ~/Library/Application\ Support/com.nssurge.surge-*")
os.system("sudo -S route add 17.253.84.123/32 1.2.3.4")
os.system("sudo -S route add 17.253.84.125/32 1.2.3.4")
os.system("sudo -S route add 17.253.84.251/32 1.2.3.4")
os.system("sudo -S route add 17.253.114.253/32 1.2.3.4")
os.system("sudo -S route add 17.253.114.125/32 1.2.3.4")
os.system("sudo -S date 010110002021")
os.system("""osascript -e 'tell app "Surge" to open'""")
time.sleep(20)
os.system("sudo -S sntp -sS time.apple.com.")
os.system("netstat -rn |grep 1.2.3.4")
time.sleep(3)
