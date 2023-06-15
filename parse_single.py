from collections import defaultdict
from tqdm import tqdm
import pandas as pd
import json
import re
from bs4 import BeautifulSoup
from lxml import etree

output_path='shadertoy1000.csv'
comments_path='shadertoy1000comments.csv'

output=defaultdict(list)

myTime_x='/html/body/div[2]/div/div[1]/div[1]/div[2]/span[1]'
myFramerate_x='/html/body/div[2]/div/div[1]/div[1]/div[2]/span[2]'
myResolution_x='/html/body/div[2]/div/div[1]/div[1]/div[2]/span[3]'
shaderTitle_x='/html/body/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[1]'
numLikes_x='/html/body/div[2]/div/div[1]/div[2]/div[1]/div[2]/span'
numViews_x='/html/body/div[2]/div/div[1]/div[2]/div[1]/div[3]/span[1]'
# single tag example /html/body/div[2]/div/div[1]/div[2]/div[1]/div[3]/div/a[5]
# single tag example 2 /html/body/div[2]/div/div[1]/div[2]/div[1]/div[3]/div/a[3]
tagsList_x='/html/body/div[2]/div/div[1]/div[2]/div[1]/div[3]/div' 
shaderAuthor_x='/html/body/div[2]/div/div[1]/div[2]/div[1]/div[4]/span[1]/a'
shaderDate_x='/html/body/div[2]/div/div[1]/div[2]/div[1]/div[4]/span[2]'
shaderDescription_x='/html/body/div[2]/div/div[1]/div[2]/div[2]'
# single line of code inside example /html/body/div[2]/div/div[2]/div[4]/div/div[6]/div[1]/div/div/div/div[5]/div[1]/pre/span/span
# single line of code inside example 2 /html/body/div[2]/div/div[2]/div[4]/div/div[6]/div[1]/div/div/div/div[5]/div[6]/pre/span/span
shaderImageCode_x='/html/body/div[2]/div/div[2]/div[4]/div/div[6]/div[1]/div/div/div/div[5]' 
numComments_x='/html/body/div[2]/div/div[3]/div/span[2]'
# single comment username example /html/body/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/a
# single comment username example 2 /html/body/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/a
# single comment date example /html/body/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/text()[1]
# single comment date example 2 /html/body/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/text()[1]
# single comment content example /html/body/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/text()[2]
# single comment content example 2 /html/body/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/text()[2]
allComments_x='/html/body/div[2]/div/div[3]/div/div[2]'

for i in tqdm(range(1020)):
    with open(f'single_pages/pageSource_{i}.html', 'r', encoding='utf-8') as f:
        html_doc = f.read()


    # Assuming `html_doc` is your HTML document
    soup = BeautifulSoup(html_doc, 'lxml')

    output['id'].append(i)

    # TODO: tags, comments, shader code (currently might have incomplete crawl for different buffers)
    for curId in ('myTime','myFramerate','myResolution','shaderTitle','shaderStatsLikes','shaderAuthorName','shaderAuthorDate','shaderStatsViewed','shaderDescription','shaderStatsComments'):
        element = soup.find(id=curId)
        t='' if not element else element.text
        output[curId].append(t)

df = pd.DataFrame(output)
df.to_csv(output_path, index=False)