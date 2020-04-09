import requests
from bs4 import BeautifulSoup
from requests import request

ip = "192.168.1.2" # ip raspberry pi
port = "8000" # порт raspberry pi
link = ip + ":" + port

while True:
    t = request('GET', link).text  # получаем данные со страницы link

    soup = BeautifulSoup(t, 'html.parser')  # создаем копию класса суп для парсинга и применяем его к контенту
    s = list(map(int, soup.text.split()))   # выделяем слова со страницы в массив
    x, y, w, h = s[0], s[1], s[2], s[3] # переопределяем координаты для дальнейшего использования
