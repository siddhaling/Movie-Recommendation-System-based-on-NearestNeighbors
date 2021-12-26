#Methods and Techniques

A google doc file with the same data is available **[here](https://docs.google.com/document/d/1sP6r9h0Pb0AuJ0e1GrkxX7xuHBQTLcv0/edit?usp=sharing&ouid=117806499075101418555&rtpof=true&sd=true)**

The program **recommendersystem.py** uses the KNN (K Nearest Neighbors) algorithm to find out the similarity between two users and accordingly recommends a list of 20 movies based on the initial movie provided. The code uses the following methods and techniques to achieve the goal:

~~~python
moviedatabase = pd.read_csv('movies.csv', usecols = ['movieId', 'title'])
ratingdatabase = pd.read_csv('ratings.csv', usecols = ['userId', 'movieId', 'rating'])
~~~

This section of code uses **pandas** to read through the .csv files and extract the important information from **movies.csv** and **ratings.csv** to clean up the data and reduce it to a usable form, in our case, **moviedatabase** and **ratingdatabase**.

~~~python
featurematrix = ratingdatabase.pivot(index = 'movieId', columns = 'userId').fillna(0)
sparsefeaturematrix = csr_matrix(featurematrix.values)
~~~

The following section of the code makes use of **sklearn** to generate a **feature matrix** from the cleaned up databases with **userID** and **movieID** as rows and columns. the generated matrix is stored in the variable **featurematrix**. Aforementioned matrix is a sparse matrix, hence after cleaning it up and getting rid of all null values it is stored in the variable **sparsefeaturematrix**.

~~~python
modelcosine = NearestNeighbors(metric = 'cosine', algorithm = 'brute', n_neighbors = 25)
modelcosine.fit(sparsefeaturematrix)

def cosinemovierecommender(moviename, data, number):
    index = process.extractOne(moviename, moviedatabase['title'])[2]
    print("Preferred movie: ", moviedatabase['title'][index], "Index: " , index)
    print("Generating recommendation list...")
    distance, indices = modelcosine.kneighbors(data[index], n_neighbors = number)
    for i in indices:
        print(moviedatabase['title'][i].where(i != index))
        #print(distance)

cosinemovierecommender('shawshank redemption', sparsefeaturematrix, 20)
~~~
  The following section of code makes use of **scipy** and **fuzzywuzzy** to generate a model for the core computation. **modelcosine** generates a data model which when plugged in the function **cosinemovierecommender** outputs a list of movies derived from the algorithm which are the closest to the provided movie (in this case, **Shawshank Redemption**).

  For computational purposes, the algorithm uses three different metrics to compute similarity, namely **cosine similarity**, **manhattan distance** and **euclidean distance**. The functions **manhattanmovierecommender** and **euclideanmovierecommender** use the other two metrics to calculate similarity using said metrics.
