# -*- coding: utf-8 -*-
"""[Notebook - Student] Week 2 Data Wrangling Tutorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/tvlaz2020/cis230Week2/blob/main/%5BNotebook%20-%20Student%5D%20Week%202%20Data%20Wrangling%20Tutorial.ipynb

# Week 6 - Data Wrangling

![data_wrangling.png](attachment:data_wrangling.png)

##  Table of Contents

- Theoretical Overview
- Problem Statement
- Code
    - Importing packages & libraries
    - Duplicated function
    - Map function
    - Replace function
    - Rename function
    - Describe function
    - GetDummies function
    - Quiz

## Theoretical Overview
- Most real-world data are dirty. We must first convert datasets before we can analyze them.
- Data wrangling refers to several procedures intended to convert unstructured data into formats that are easier to work with.
- Data wrangling transforms data from an unorganised or untidy source into something valuable.
- Data Wrangling consists of 6 steps:
    1. Discovery
    2. Structuring
    3. Cleaning
    4. Enriching
    5. Validating
    6. Publishing
- Data transformation is the technological process of translating data from one format, standard, or structure to another without affecting the content of the datasets.
- Data transformation may include:
    1. Constructive (adding, copying)
    2. Destructive (deleting fields and records)
    3. Structural (renaming, moving, and combining of columns)
- In this activity, we will briefly touch on the following subjects: duplicated(), map(), replace(), rename(), cut(), describe(), get_dummies()

## Problem Statement

This notebook is based on the theory and tutorial covered in the slides 63 and 75 of Data Wrangling. In this activity, you have to create multiple dataframes and then apply various data cleaning techniques such as **drop_duplicates, mapping, replace, rename, get_dummies, etc**

## Code

### Importing of required libraries:
"""

import pandas as pd
import numpy as np

"""### Duplicated function:

Creating a dataset:
"""

df_d = pd.DataFrame({"a":["one","two"]*3,
                    "b": [1,1,2,3,2,3]})

df_d

"""This function checks whether the row is repeated or not:"""

df_d.duplicated()

"""This function is to drop the duplicate records in the DataFrame:"""

df_d.drop_duplicates()

"""### Map function:

The following code creates a DataFrame:
"""

df_m = pd.DataFrame({"names":["Olivia","Amelia","Isabelle","Mia","Ella"],
                    "scores":[50,32,67,32,21]})

df_m

""" We can transfer values of data in a DataFrame with the function "map()"

 So for example, the name "Olivia" will be mapped to "O" and the name "Amelia" will be mapped to "A".

 The code below creates a class of "Names" it will be mapped to:
"""

classes = {"Olivia":"O","Amelia":"A","Isabelle":"I","Mia":"M","Ella":"E"}

""" The following code will do the mapping:"""

df_m["Groupings"] = df_m["names"].map(classes)

df_m

"""### Replace function:

The following code is the creation of a Series object:
"""

df_r = pd.Series([67,21,79,39])

df_r

"""We can replace values in python using the function "replace()".

This is because the function "replace()" takes in 2 arguments.

First is the value you want to replace, and Second is the value you would like to replace it with.

The following is a breakdown of the function:

replace(value_to_be_replaced , value_to_replace_to)

The following code is an example that will replace the value "67" with the value "0"
"""

df_r.replace(67,0)

""" The following code will replace multiple values with the replace() function:"""

df_r.replace([21,79],[37,38])

"""### Rename function:

The following code is a creation of a DataFrame:
"""

df_re = pd.DataFrame(np.arange(12).reshape(3,4), index=[0,1,2], columns=['sam', 'jeslyn', 'kish', 'dan'])

df_re

"""We can rename axes in a dataframe with the help of the rename() function.

We will rename the columns from lowercase to uppercase.

The following code will change column names from lowercase to uppercase:
"""

df_re.rename(columns = str.upper)

"""We can also change the row or column names using the "rename()" function.

Now we will rename the index from "0" to "zero"

Code to replace index:
"""

df_re.rename(index={0:"zero"})

"""Now we will rename the column from "sam" to "spade"

Code to replace column:
"""

df_re.rename(columns={"sam":"spade"})

"""### Describe function:

The following code generates a DataFrame:
"""

df_desc = pd.DataFrame(np.random.randn(2000,5))

df_desc

"""We can find specific values/statistical summaries in a dataset.

With the help of the describe() function,  we can get summary statistics of the DataFrame.
"""

df_desc.describe()

"""Here we can see that there is a breakdown of the following:

count (The number of records in the DataFrame)

mean (The average of all values in the DataFrame)

std (Std stands for Standard Deviation, the measure of the variation or dispersion of a set of values.)

min (The minimum value in the DataFrame)

25% (25th Percentile, known as first or lower quartile.)

50% (50th Percentile, known as the median. The median cuts the Data in half)

75% (75th Percentile, known as third or higher quartile)

max (The maximum value in the DataFrame)

### get_dummies()

The following code generates a DataFrame:
"""

df_d = pd.DataFrame({"Letter":["a","b"]*3,
                    "Number": [0,1,2,3,4,5]})

df_d

"""get_dummies() function converts a categorical variable into dummy/indicator variables.

You can read more about this function from the pandas library documentation page:
https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html

We can use the "get_dummies()" function to convert a categorical variable into a "dummy" or "indicator.
"""

pd.get_dummies(df_d["Letter"])

"""The letter "a" will reflect 1 if it is "a" in the a column.

The letter "b" will reflect 1 if its "b" in the b column.

## Quiz time!

#### Question 1:

The code for the creation of DataFrame will be given below. Simply just run it and proceed with the other questions.
"""

q1 = pd.DataFrame({"a":["Four","Five"]*3,
                    "b": [4,5,4,5,4,5]})

q1

""" What is the code used to Check for duplicates in the DataFrame stored in the variable "q1"? (Created above)

 Please type the code below to CHECK for duplicates:
"""

#Code
q1.duplicated()

""" What is the code used to Drop duplicates in the DataFrame stored in the variable "q1"? (Created above)

 Please type the code below to DROP duplicates:
"""

#Code
q1.drop_duplicates()

"""#### Question 2:

The code for the creation of DataFrame will be given below. Simply just run it and proceed with the other questions.
"""

q2 = pd.DataFrame({"names":["Kelly","Oliver","Kenneth","Bill","Darren"],
                    "scores":[50,32,67,32,21]})

q2

""" What is the code used to MAP values in a DataFrame?

 Please type the code below to MAP values for the following:

 - Kelly will be mapped as "K"
 - Olivier will be mapped as "O"
 - Kenneth will be mapped as "K"
 - Bill will be mapped as "B"
 - Darren will be mapped as "D"


"""

# Code
classes = {"Kelly":"K","Oliver":"O","Kenneth":"K","Bill":"B","Darren":"D"}

"""Type the code to do the mapping below:"""

# Code
q2["Groupings"] = q2["names"].map(classes)
print(q2)

"""#### Question 3:

The code for the creation of a Series object will be given below. Simply just run it and proceed with the other questions.
"""

q3 = pd.Series([93,23,37,99])

q3

"""What is the code used to REPLACE values in a DataFrame?

 Please type the code below to REPLACE values for the following:
 - Value "93" is to be replaced with "21"
 - Value "23" is to be replaced with "22"
 - Value "37" is to be replaced with "23"
 - Value "99" is to be replaced with "24"

Type the code below to replace Value "93" with "21":
"""

# Code
q3.replace(93,21)

"""Type the code below to replace Value "23" with "22":

"""

# Code
q3.replace(23,22)

"""Type the code below to replace Value "37" with "23":

"""

# Code
q3.replace(37,23)

"""Type the code below to replace Value "99" with "24":

"""

# Code
q3.replace(99,24)

"""#### Question 4:

The code for the creation of DataFrame will be given below. Simply just run it and proceed with the other questions.
"""

q4 = pd.DataFrame(np.arange(12).reshape(3,4), index=[0,1,2], columns=['calvin', 'jorddie', 'dom', 'allen'])

q4

"""What is the function that is used to change the column names from lowercase to uppercase?

Key in the code to change the column names from lowercase to UPPERCASE:
"""

# Code
q4.rename(columns = str.upper)

"""We can also change the row or column names using the "rename()" function.

The function is to be used to rename the following indexes:
- Index "2" to be changed to "Two"

Key in the code to replace the index:
"""

# Code
q4.rename(index={2:"two"})

"""###

Renaming the column from "calvin" to "bavier"

Key in the code to replace column:
"""

# Code
q4.rename(columns={"calvin":"bavier"})

"""#### Question 5:

The code for the creation of DataFrame will be given below. Simply just run it and proceed with the other questions.
"""

q5 = pd.DataFrame(np.random.randn(2000,5))

q5

"""What is the function used to find specific values/statistical summaries in a DataFrame?

Key in the code to get the summary statistics of the DataFrame:
"""

# Code
q5.describe()

"""##### Name 2 of the statistic summary and what they mean:

Statistic summary 1:
"""

# Key in answer here
'Mean value is the average of the related values, value sum/value count'

"""Statistic summary 2:"""

# Key answer in here
'Min/Max values are the minimum and maximum values respectively...the smallest and largest values of the collection'

"""#### Question 6:

The code for the creation of DataFrame will be given below. Simply just run it and proceed with the other questions.
"""

q6 = pd.DataFrame({"Letter":["c","d"]*3,
                    "Number": [0,1,2,3,4,5]})

q6

""" What is the function used to create dummies?

 Create dummies value with the column "Letter".

Key in the code used to create dummies in a DataFrame:
"""

# Code
pd.get_dummies(q6["Letter"])

""" # Congratulations on completing this activity!"""