import requests
import pandas as pd
import re
import time
from tqdm import tqdm

data = pd.read_json('data/arxivData.json')

#prepair links
data['pdf_link_list'] = 'http://arxiv.org/pdf/' + data['id'] + '.pdf'

#scrape from arxiv
for idx in tqdm(range(0,len(list(data['pdf_link_list'])))):
    pdf_url = list(data['pdf_link_list'])[idx]
    r = requests.get(pdf_url, stream=True)
    title = (list(data['id'])[idx]).replace('/','')
    with open(f'pdf_papers/{title}.pdf', 'wb') as f:
        f.write(r.content)