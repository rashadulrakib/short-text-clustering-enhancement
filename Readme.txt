--at first change the parameters (input file, number of clusters) in the main.py
--to run: python main.py
--final output file format:clusterlabel	truelabel	text 
--output file location: data/stackoverflow/traintest
--You can run generate_initial_labels.py to generate initial labels for a dataset (not mandatory)


Paper Title: Enhancement of Short Text Clustering by Iterative Classification
https://link.springer.com/chapter/10.1007/978-3-030-51310-8_10


Abstract
Short text clustering is a challenging task due to the lack of signal contained in short texts. In this work, we propose iterative classification as a method to boost the clustering quality of short texts. The idea is to repeatedly reassign (classify) outliers to clusters until the cluster assignment stabilizes. The classifier used in each iteration is trained using the current set of cluster labels of the non-outliers; the input of the first iteration is the output of an arbitrary clustering algorithm. Thus, our method does not require any human-annotated labels for training. Our experimental results show that the proposed clustering enhancement method not only improves the clustering quality of different baseline clustering methods (e.g., k-means, k-means--, and hierarchical clustering) but also outperforms the state-of-the-art short text clustering methods on several short text datasets by a statistically significant margin.
