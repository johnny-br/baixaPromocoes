import requests
from bs4 import BeautifulSoup
import os
import time


def recebePagina(url) -> list:
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        imagens = soup.find_all('img', class_='enigma_img_responsive')
        links = [link['src'] for link in imagens]
        return links

    except Exception as err:
        print(err)


def baixaImagem(url) -> None:
    try:
        nome = url.split('/')[-1]
        with requests.get(url, stream=True) as r:
            with open(nome, 'wb') as fd:
                for pedaco in r.iter_content(chunk_size=128):
                    fd.write(pedaco)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    os.system(f'export DISPLAY=:0; notify-send -t 20000 "Tentando baixar folheto"')
    url = 'http://casanegreiros.com.br'
    arquivos = os.listdir('.')
    links = recebePagina(url)

    for link in links:
        nome = link.split('/')[-1]
        if nome not in arquivos:
            time.sleep(7)
            baixaImagem(link)
