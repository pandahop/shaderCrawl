from tqdm import tqdm
import json
import re
from bs4 import BeautifulSoup

shader_urls=[]

for i in tqdm(range(85)):
    # Open the file in read mode ('r')
    with open(f'raw_pages/page{i}.html', 'r', encoding='utf-8') as f:
        html_doc = f.read()

    # Assuming `html_doc` is your HTML document
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Find the script tag with the 'gShaders' object.
    script_tag = soup.find('script', text=re.compile('var gShaders'))

    # Now, let's extract the JSON-like string from the JavaScript code.
    json_str = re.search(r'gShaders=\[.*\]', script_tag.string).group(0)
    json_str=json_str[json_str.index('=')+1:]

    # Parse the JSON data
    data = json.loads(json_str)

    # Assume data is a list of dictionaries where each dictionary has a key 'info' which is another dictionary with key 'id'
    info_ids = [item['info']['id'] for item in data]

    shader_urls.extend(info_ids)
    
with open('shader_urls_1000.txt','w') as fp:
    for u in shader_urls:
        fp.write(f"https://www.shadertoy.com/view/{u}\n")