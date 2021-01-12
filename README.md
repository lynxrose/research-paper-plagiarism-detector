# Predicting Author Count


Does the writing quality, length, or style in groups of reseachers differ from how individual researchers write? 
Through my findings I was not able to disprove the null hypothesis. 
The baseline model I created chose the most prevelent class of over one researcher every time.
Through gradient boosting, naive bayes, random forest modeling, model manipulation(max_features etc.), and oversampling my models were unable to consistantly outpreform the baseline model. 

Quality of research writing is consistant and through not disproving my null hypothesis I have gained even more respect for paper writing accidemia, learning they have strong quality control and standards. 



![](images/k_means_clustering.png)
I started PCA to gain intuition into how the words are most corrilated to eachother. This graph shows that the most information gain was when k-means created 3 clusters. 

![](images/pca_.png)
In my PCA analysis, words relating to which AI algorithm was being used where previelent, the following are the top 10 word outlires on the tips of the PCA 'triangle.'

TOP LEFT(yellow)
image           
images      
cnn             
segmentation    
object      
network   
detection     
layer            
convolutional   
layers           

BOTTOM LEFT (blue)
algorithm   
xi         
variables   
theorem     
let         
function 
graph        
problem
probability   
proof         

BOTTOM RIGHT (red)
image          
images      
cnn           
segmentation    
object           
network          
detection       
layer
convolutional    
layers         



![](images/roc_curve.png)
Did the growth of AI research in acidemia create a noticable change in the lingo being used from 2015 on? 
Once again utilizing the previous modeling techneaks I was only able to outpreform the baseline model by .15 accuacy with Naive Bayes.

SOURCES:
Thank you Neel Shah for providing me with 30k pdf links for scraping and Andrew Mouros for a wonderful PCA tutorial.
https://www.kaggle.com/neelshah18/arxivdataset by Neel Shah
https://andrewmourcos.github.io/blog/2019/06/06/PCA.html by Andrew Mouros

