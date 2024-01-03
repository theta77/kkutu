import requests
from bs4 import BeautifulSoup
import os

mode = 1
while True:
    while True:
        first = input("시작 글자 : ")
        if first == "0":
            mode = 0
            os.system("cls")
            break
        mission = input("미션 글자 : ")
        os.system("cls")
        num = 15
        f = open("word.txt", "r", encoding='utf-8')
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
        dic = {}
        for i in h.read().split():
            misnum = 0
            for j in i:
                if j == mission:
                    misnum += 1
            dic[i] = misnum

        mis = 6
        for i in range(7):
            for j in dic:
                if dic[j] == mis:
                    print(f"{j}\n미션 개수 : {dic[j]}개")
                    if num == 0:
                        break
                    num -= 1
            mis -= 1   
        input()
        os.system("cls")
    
    while True:
        first = input("시작 글자 : ")
        if first == "1":
            mode = 1
            os.system("cls")
            break
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