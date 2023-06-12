from time import sleep
from tqdm import tqdm
from random import random
import requests
from lxml import html

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


xpath = '/html/body/div[2]/div[2]/div[*]/div[1]/a'

for i in tqdm(range(0,85)):
    url = f"https://www.shadertoy.com/results?query=&sort=popular&from={i*12}&num=12"

    response = requests.get(url, headers=headers)
    with open(f'raw_pages/page{i}.html','w') as fp:
        fp.write(response.text)
    sleep(1+random()*2)
    # tree = html.fromstring(response.content)
    # elements = tree.xpath(xpath)

    # for element in elements:
    #     href = element.get('href')
    #     full_url = f"https://www.shadertoy.com/{href}"
    #     print(full_url)