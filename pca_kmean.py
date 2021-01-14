from sklearn.cluster import KMeans # Our clustering algorithm
from sklearn.decomposition import PCA # Needed for dimension reduction
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from seaborn import set_style
import matplotlib.pyplot as plt

data = pd.read_csv('data/research_data.csv')

vectorizor = TfidfVectorizer(max_features=2000)
X_matrix = vectorizor.fit_transform(data.body_text)
X_matrix = X_matrix.todense()

corp_word_df = pd.DataFrame(X_matrix,columns=vectorizor.get_feature_names())

pca = PCA(n_components=10)
principalComponents = pca.fit_transform(corp_word_df)

# Plotting the variances for each PC
PC = range(1, pca.n_components_+1)
plt.bar(PC, pca.explained_variance_ratio_, color='red')
plt.xlabel('Principal Components')
plt.ylabel('Variance %')
plt.xticks(PC)
plt.savefig('images/k_means_var')
# Putting components in a dataframe for later
PCA_components = pd.DataFrame(principalComponents)

pca_word_strength = (pd.DataFrame(pca.components_[:2],columns=vectorizor.get_feature_names(),index = ['PC-1','PC-2'])).T
pca_word_strength['PC-1'].nsmallest(10) #nlp
pca_word_strength['PC-2'].nlargest(10) #nlp
pca_word_strength['PC-2'].nsmallest(10) #theorams and algorithms
pca_word_strength['PC-1'].nlargest(10) #image recognition

kmodel = KMeans(n_clusters=3)
kmodel.fit(PCA_components.iloc[:,:2])
labels = model.predict(PCA_components.iloc[:,:2])
color_labels = []
for label in labels:
    if label == 2:
        color_labels.append('r')
    elif label == 1:
        color_labels.append('b')
    elif label == 0:
        color_labels.append('y')

set_style("whitegrid")
plt.scatter(PCA_components[0], PCA_components[1], c=['black' if x == 1 else 'white' for x in data.author_count], s=(10), edgecolors = color_labels, label = 'document(black:one_author)')
plt.title('PCA K-Means Clustering')
plt.legend()
plt.savefig('images/pca_single_authors')
plt.show()