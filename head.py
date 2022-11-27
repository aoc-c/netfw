import colorful as cf
import os
#head script
os.system("clear")
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
with cf.with_palette(colors) as c:
 print(c.white(5*" "+50*"="+"\n"))
 print(c.white("       .______  .____________._._______         ___ "))
 print(c.white("       :      \ : .____/\__ _:|:_ ____/.___    "+c.orange("|   |")))
 print(c.white("       |       "+c.orange("||")+" : _/\   "+c.orange("|")+"  :"+c.orange("||")+"   _/  :   "+c.orange("|")+" /\\"+c.orange("|   |")))
 print(c.white("       |   "+c.orange("|")+"   "+c.orange("||")+"   /  \  "+c.orange("|   ||   |   |   |/  :   |")))
 print(c.white("       |___"+c.orange("|")+"   "+c.orange("||")+"_.: __/  "+c.orange("|   ||")+"_. "+c.orange("|   |")+"   /       "+c.orange("|")))
 print(c.white("           "+c.orange("|")+"___"+c.orange("|")+"   :/     "+c.orange("|")+"___"+c.orange("|")+"  :/    "+c.orange("|")+"______/|___|"))
 print(c.white("                                 :             :    "))
 print(c.white("     Network Brute Force "))
 print(c.white("     https://github.com/aoc-c/BruteForce"))
 print(c.orange(5*" "+50*"="+"\n"))
 print(c.white("["+c.orange("+")+c.white("] - Created by @yun!")))
 print(c.white("["+c.orange("i")+c.white("] - info: v2 test phase")))
 print(c.white("["+c.orange("!")+c.white("] - usage: netfw-start\n")))
