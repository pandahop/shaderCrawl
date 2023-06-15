from selenium import webdriver
from random import random
from tqdm import tqdm
from time import sleep

b=webdriver.Chrome()

with open('shader_urls_1000.txt','r') as fp:
    lines=fp.readlines()
lines=[e.strip() for e in lines]
a=[]

for i,e in tqdm(enumerate(lines)):

    try:

        b.get(e)
        sleep(1+random()*2)

        with open(f"single_pages/pageSource_{i}.html", "w",encoding='utf-8') as f:
            f.write(b.page_source)

    except:
        
        a.append(i)

with open('notCrawled.txt','w') as fp:
    fp.write(','.join([str(e) for e in a]))
    
b.quit()