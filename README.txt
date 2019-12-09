CS 535 Assignment-2 (Fall-2019) Report
Mohi Uddin Syed
B00766015-msyed3@binghamton.edu

Before doing any operations on the dataset, I read the data into a csv file named "data.csv"

Q1. To clean the data,I first replaced all the missing values with "nan" (recognized by numpy), then replaced all nan with mean 
values. the resulting output is in "clenaed.csv" file. 
To normalize the data I used sklearn's normalize() function with norm as 'l1', the normalized data is saved in "normalized.csv" file. 

Q2. To decide the value of "K" I used elbow method which for each value of k calculates the sum of squared distances from each point
to its assigned center(distortions).

The resulting curve can be seen below:


By looking at the curve, I choose optimal value of k to be 7 for this dataset.

Q3. Running the kmeans algorithm with k value as 7 (cluster number 0 to 6) based on the above mentioned observation. The output is
saved in "kmeans_output.txt"

Q4. Applying pca to the normalized dataset

Q5.
