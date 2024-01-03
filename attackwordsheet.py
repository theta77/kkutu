import requests
from bs4 import BeautifulSoup

li = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
f = open("attack.txt", "w", encoding='utf-8')
for i in li:
    res = requests.get(f"https://kkukowiki.kr/w/공격단어/한국어/{i}")
    soup = BeautifulSoup(res.text, "html.parser")
    for j in soup.select(".sortable > tbody > tr > td > a"):
        f.write(f"{j.text}\n")
for i in li:
    res = requests.get(f"https://kkukowiki.kr/w/방어단어/한국어/{i}")
    soup = BeautifulSoup(res.text, "html.parser")
    for j in soup.select(".sortable > tbody > tr > td > a"):
        f.write(f"{j.text}\n")