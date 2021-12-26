#Help Document

A google doc file with the same data is available **[here](https://docs.google.com/document/d/1HbnXx6r77LfEjIuPtr8Nso9TaMokj4YK/edit?usp=sharing&ouid=117806499075101418555&rtpof=true&sd=true)**

The following code is written completely in native **python** with the help of a few additional python libraries. Here are all the dependencies and libraries used in the program file:

* **pandas** : Used for database computation and cleaning up given databases. The documentation for the library can be found **[here](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)**.
* **scipy** : Used to convert the sparse matric to a non-sparse matrix. The documentation for the library can be found **[here](https://docs.scipy.org/doc/)**.
* **fuzzywuzzy** : AI python library used to aid search processes in the main recommender functions. The documentation for the library can be found **[here](https://pypi.org/project/fuzzywuzzy/#description)**.
* **sklearn** : python library used to implement the KNN algorithm. The documentation for the library can be found **[here](https://scikit-learn.org/stable/)**.

The entire code is written in just one executable python file, namely **recommendersystem.py**. The file takes no inputs, but outputs a list of 20 recommended movies based on the movie initially provided to the algorithm. The execution steps are as follows:

~~~python
python recommendersystem.py
(make sure that all files are in the same directory)
~~~
