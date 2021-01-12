# Predicting Author Count

Does the writing quality, length, or style in groups of researchers differ from how individual researchers write? 
That was the question I asked myself moving into scraping pdf files from [arxiv.org](arxiv.org). Armed with 41 thousand links and a VPN, my computer made calls to arxiv.org in increments of 2 hours (in which I switched IPs) for three days. I proceeded to turn the PDF files into text with ~50% success rate leaving me with 14,066 after cleaning which consisted of cutting off bottom acknowledgements, removing escape words, and utilizing TFIDFVectorizer. 
My models attempted to determine if one person wrote the paper or more.

![](images/roc_curve_author>1.png)

The baseline model I created chose the most prevalent class of over one researcher every time.
Through naive bayes with 2000 max_features and oversampling was I able to create a model that preformed the best.

![](images/k_means_clustering.png)

I started PCA to gain intuition into how the words are most correlated to each other. This graph shows that the most information gain was when k-means created 3 clusters. 

![](images/pca_.png)

In my PCA analysis, words relating to specific academia was being in more prevalence, the following are the top 10 word outliers on the tips of the PCA 'triangle.'

TOP LEFT(yellow: NLP):word, words, sentence, language, et, al, corpus, embeddings, sentences, and variables        
BOTTOM LEFT (blue: Structures and Algorithms): algorithm, xi, variables, theorem, let, function, graph, problem, probability, and proof         
BOTTOM RIGHT (red: Image Recognition): image, images, cnn, segmentation, object, network, detection, layer, convolutional, and layers         


SOURCES:
Thank you Neel Shah for providing me with 30k pdf links for scraping and Andrew Mouros for a wonderful PCA tutorial.
https://www.kaggle.com/neelshah18/arxivdataset by Neel Shah
https://andrewmourcos.github.io/blog/2019/06/06/PCA.html by Andrew Mouros

Tools: Python, Matplotlib, Pandas, NLTK, VPN(for webscaping), and SKLearn ML

GitHub Project by Lynx Rose
