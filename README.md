# #5 MapReduce+

__Q. What commands must be used to run your scripts?__

python3 OneStepMean.py -r hadoop hdfs:///data/HT_Sensor_dataset.dat > output_OneStepMean.txt

python3 TwoStepMean.py -r hadoop hdfs:///data/HT_Sensor_dataset.dat > output_TwoStepMean.txt

python3 AllColumnsMean.py -r hadoop hdfs:///data/HT_Sensor_dataset.dat > output_AllColumnsMean.txt

__Q. What technical errors did you experience?__

While working on the extra task... 
I created the smaller size of the 'dat file' that contains only 10 rows of the original data.
The programs worked fine when tested with the test data, but they kept getting killed or unable to connect with the original data. The process succeeded 1 out of 10 times.
I made sure to have the latest docker images on the 'hadoop-resourcemanager', and 'hadoop-namenode'. Realizing it is something related to my configuration in CPU or Memory. I'm still in debugging mode.

__Q. What conceptual difficulties did you experience?__

Even after reading all the documents about map and reduce, when it came to actual practice, imagining how partitioning and data move in each map and reduce was quite confusing.
I was not quite sure the concept of how to `create` the partitions or `assign` the data to the partition.

Also, using the `dat` file rather than `csv` file made me struggle a bit, as the data weren't easy to play with.   

__Q. How much time did you spend on each part of the assignment?__

About 5 days +

__Q. Track your time according to the following items: Gitlab & Git, Docker setup/usage, actual reflection work, etc.__

Gitlab & Git: 5min

Docker setup/usage: 10min

Actual reflection work: Infinity

__Q. What was the hardest part of this assignment?__

The hardest part was trying to figure out how to get the number of items of the column to calculate the square root of it to create the partition with that number.  

__Q. What was the easiest part of this assignment?__

Opening the canvas

__Q. What did you actually learn from doing this assignment?__

I learned how to use multi-step process with MRJob to process over a large data. Mapping and partitioning the data and reducing them in the hadoop environment actually made the process go a lot faster. 
This assignment included a lot of confusion and frustration. However, after seeing the solution, and getting more project and assignment done, I will get better at mapreduce jobs. Fingers crossed. 

__Q. Why does what I learned matter both academically and practically?__

Whenever I look at the job descriptions for the Data Science positions, one of the requirements the company require is the Hadoop/Hive/Spark skills. I now understand why they consider it as a main properties of the applicants. My goal is to be able to play with Hadoop and Spark freely. 