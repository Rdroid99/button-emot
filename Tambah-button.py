import os,sys
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'')
os.system('date')
print(b+'-------------------------------------------')
print(a+'[ Author: Kumpulanremaja.com              ]')
print(a+'[ Upgraded: Rdroid99                      ]')
print(a+'[ github: github.com/Rdroid99             ]')
print(a+'[ button tambahan:Home+esc+/+pgup+pgdn+alt]')
print(a+'[ +<<+>>+end+github+nicklu+ctrl+ ✓+{+}    ]')
print(b+'-------------------------------------------')
print(a+'+'*43)
print('\nProses..')
sleep(1)
print(b+'\n[•] Mengambil File Default Termux')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[✓]Success !')
sleep(1)
print(b+'\n[•] menambahkan File Tambahan..')
sleep(1)

key = "extra-keys = [['🌹','HOME','ESC','/','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN'],['-','✓','#','<<','>>','{','}'],['😅','🤣','😭','😴','🤭','🤤','😎','👍🏻']]"
Sunda = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
Sunda.write(key)
Sunda.close()
sleep(1)
print(a+'[✓] Memproses  !')
sleep(1)
print(b+'\n[•] Tunggu Sebentar')
sleep(2)
os.system('termux-reload-settings')
print(a+'[✓] Proses Selesai !! ^^'+a+'\n\nhubungi : saya lewat Web atau Fanspage Facebook*\n\n')
print(a+'[✓] Jangan lupa dishare bro^^')
print(a+'[✓] Selesai...')
print(c+'')
