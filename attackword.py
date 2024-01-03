import requests
from bs4 import BeautifulSoup
import os

while True:
    first = input("시작 글자 : ")
    os.system("cls")
    num = 50
    f = open("attack.txt", "r", encoding='utf-8')
    g = open("mission.txt", "w", encoding='utf-8')
    for i in f.read().split():
        corre = 0
        for j,k in zip(i, first):
            if j == k:
                corre += 1
        if corre == len(first):
            g.write(f"{i}\n")
    g.close()
    h = open("mission.txt", "r", encoding='utf-8')
    li = h.read().split()
    for i in li:
        if num == 0:
            break
        print(f"{i}")
        num -= 1


    input()
    os.system("cls")