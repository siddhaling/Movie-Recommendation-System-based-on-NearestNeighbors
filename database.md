#Database Details

A google doc file with the same data is available **[here](https://docs.google.com/document/d/1I3d23i2z83c9mGh2MyWqIEByq6GhUIbA/edit?usp=sharing&ouid=117806499075101418555&rtpof=true&sd=true)**

The movie database for this project was taken from **[here](https://github.com/Praful2000/YoutubeLectures/tree/master/Movie%20KNN)**

The movie data is split into two separate files: **movies.csv** and **ratings.csv**. The former contains details about the movie under the headings:

* **movieId** : Numeric ID of the selected movie in the database
* **title** : The name of the movie along with the year it was created in
* **genre** : One or multiple genres the selected movie belongs to

The latter, **ratings.csv** contains details about multiple users and how they have rated the movies under the following headings:

* **userId** : The numeric ID of the users who have rated the movies present in the database
* **movieId** : The name of the movie along with the year it was created in
* **rating** : Ratings assigned to the movies by the users ranging from **0.0** to **5.0**
* **timestamp** : Showcases the length (or timestamp) of the given movie

The initial structure of **movies.csv** and **ratings.csv** is shown in the images below:

![movies.csv](Images/moviescsv.png)

![ratings.csv](Images/ratingscsv.png)

In total with both databases included the net data includes **9,472 movies** and **100,836 user ratings** which are all used to compute the recommendations for a selected movie.
