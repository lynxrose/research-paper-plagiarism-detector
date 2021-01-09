import pandas as pd
import textract
from tqdm import tqdm
import csv

data = pd.read_json('data/arxivData.json')

for idx in tqdm(range(0,len(data))):
    title = (list(data['id'])[idx]).replace('/','')
    try:
        #scrape directly to full_texts.csv file
        text = (textract.process(f'pdf_papers/{title}.pdf', encoding='ascii'))
        with open(r'data/full_texts.csv','a', newline='') as fd:
            writer = csv.DictWriter(fd, fieldnames=['id','full_text'])
            writer.writerow({'id':title, 'full_text':text})
    except:
        pass