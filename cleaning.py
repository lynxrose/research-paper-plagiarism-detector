import pandas as pd

#data imports
data = pd.read_csv('data/research_data.csv')
full_texts.csv('data/full_texts.csv')

#add author_count to data
count = []
for author_list in list(data['author']):
    count.append(author_list.count("{'name':"))
data['author_count'] = count

#cut off acknowledgments
def cut_acknowledgments(doc):
    ending_split_list = ['References','REFERENCES','Bibliography','BIBLIOGRAPHY','ACKNOWLEDGMENTS','Acknowledgments','R EFERENCES','r eferences','R e f e re n c e s','Acknowledge me nts']
    for ending in ending_split_list:
        #check each ending header and if split outcome >1 than split occured
        split_doc = doc.split(ending)
        if len(split_doc) > 1:
            #return acknowledgments
            return split_doc[-1]
    return None

acknowledgments = []
for doc in list(data.full_text):
    acknowledgments.append(cut_acknowledgments(doc))
data['acknowledgments'] = acknowledgments

body_list = []
for i in range(len(data.full_text)):
    #remove acknowledgments
    body_list.append(data['full_text'][i].replace(data['acknowledgments'][i],''))
data['body_text'] = body_list

#remove papers that not in english, with no acknowledgments, or too much pdf noise
data = data.mask(data.eq('None')).dropna()
data = data.reset_index()

#save cleaned data
data.to_csv('data/research_data.csv')