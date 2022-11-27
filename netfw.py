import colorful as cf
import random
import time
from datetime import datetime
#      rand
min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sybs = '[]{}()*#;/,-_%'
#      rand
colors = {
'black': '#000000',
'white': '#C9C7D3',
'logo': '#FF002A',
'orange': '#F05E37',
'gray': '#555555',
'green': '#4CC93E',
'blue': '#434BFE',
'yellow': '#F59B02',
}
n = 1
alv = "marie"
pas = ""
all = min + max + num + sybs
with cf.with_palette(colors) as c:
    car = int(input(c.white("["+c.orange("input")+c.white("] - numbers of character -> "))))
    reg = ['3','2','1']
    print(c.white("\n["+c.orange(" ")+c.white("] - symbols")))
    print(c.white("["+c.orange(" ")+c.white("] - numbers")))
    print(c.white("["+c.orange(" ")+c.white("] - max")))
    print(c.white("["+c.orange("*")+c.white("] - min\n")))
    time.sleep(1)
    for reg in reg:
         print(c.white("["+c.orange("!")+c.white("] - initializing Brute Force in "))+reg,end="\r")
         time.sleep(1)
    datestart = datetime.now()
    while pas != alv:
      pas = "".join(random.sample(min,car))
      date = datetime.now()
      print("["+c.orange(n)+"]       "+c.orange("HOUR")+date.strftime('[%H:%M:%S]    ')+c.orange("PASS ")+pas+"")
      n += 1
      if pas == alv:
       print(c.white("\n"+c.white("[")+c.orange("*")+c.white("] - ")+"the password "+c.orange("is ")+pas+"\n"))
       print(datestart.strftime('[%H:%M:%S]')+" "+c.orange("->")+" "+date.strftime('[%H:%M:%S]'))
exit()
