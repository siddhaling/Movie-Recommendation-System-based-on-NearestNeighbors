import pandas as pd
from scipy.sparse import csr_matrix
from fuzzywuzzy import process
from sklearn.neighbors import NearestNeighbors

'''
pandas: used for database computation and cleaning up given databases
scipy: used to convert the sparse matric to a non-sparse matrix
fuzzywuzzy: AI python library used to aid search processes in the main recommender functions
sklearn: python library used to implement the KNN algorithm

'''

moviedatabase = pd.read_csv('movies.csv', usecols = ['movieId', 'title'])
#print(moviedatabase.head())

ratingdatabase = pd.read_csv('ratings.csv', usecols = ['userId', 'movieId', 'rating'])
#print(ratingdatabase.head())

'''
moviedatabase and ratingdatabase are the two databases derived from movies.csv and
ratings.csv which only include values to be used in the final computation of similarity

'''

print("\n\n\n\n\ntotal movies in database: " + str(moviedatabase.shape[0]))
print("total user ratings in database: " + str(ratingdatabase.shape[0]))

featurematrix = ratingdatabase.pivot(index = 'movieId', columns = 'userId').fillna(0)
#print(featurematrix.head())

sparsefeaturematrix = csr_matrix(featurematrix.values)

'''
featurematrix generates a matrix using values "movieId" and "userId" from ratingdatabase
as rows and columns and fills the matrix with the ratings given to movies by the specific
users. sparsefeaturematrix gets rid of all null values to shrink the size of the matrix.

'''

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
'''
cosinemovierecommender uses the metric cosine to determine the similarity between two
movies based on user ratings by calculating the cosine distance between them. It crossreferences
all rows and ranks the movies highest to lowest bases on the cosine distance (between 0 and 1, where
1 is highest and 0 is lowest)

'''
moviename = ''

modelmanhattan = NearestNeighbors(metric = 'manhattan', algorithm = 'brute', n_neighbors = 25)
modelmanhattan.fit(sparsefeaturematrix)

def manhattanmovierecommender(moviename, data, number):
    index = process.extractOne(moviename, moviedatabase['title'])[2]
    print("Preferred movie: ", moviedatabase['title'][index], "Index: " , index)
    print("Generating recommendation list...")
    distance, indices = modelmanhattan.kneighbors(data[index], n_neighbors = number)
    for i in indices:
        print(moviedatabase['title'][i].where(i != index))
        #print(distance)
'''
manhattanmovierecommender uses the metric manhattan distance to determine the similarity
between two movies based on user ratings by calculating the manhattan distance between them.
It crossreferences all rows and ranks the movies in order of lowest distance to highest distance (low
distance means high similarity)

'''

modeleuclidean = NearestNeighbors(metric = 'euclidean', algorithm = 'brute', n_neighbors = 25)
modeleuclidean.fit(sparsefeaturematrix)

def euclideanmovierecommender(moviename, data, number):
    index = process.extractOne(moviename, moviedatabase['title'])[2]
    print("Preferred movie: ", moviedatabase['title'][index], "Index: " , index)
    print("Generating recommendation list...")
    distance, indices = modeleuclidean.kneighbors(data[index], n_neighbors = number)
    for i in indices:
        print(moviedatabase['title'][i].where(i != index))
        #print(distance)
'''
euclideanmovierecommender uses the metric euclideandistance to determine the similarity
between two movies based on user ratings by calculating the euclidean distance between them.
It crossreferences all rows and ranks the movies in order of lowest to highest
distace (low distance means high similarity)

'''

cosinemovierecommender('shawshank redemption', sparsefeaturematrix, 20)
manhattanmovierecommender('shawshank redemption', sparsefeaturematrix, 20)
euclideanmovierecommender('shawshank redemption', sparsefeaturematrix, 20)
