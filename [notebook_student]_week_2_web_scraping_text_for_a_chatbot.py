# -*- coding: utf-8 -*-
"""[Notebook - Student] Week 2 - Web Scraping Text for a Chatbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/tvlaz2020/cis230Week2/blob/main/%5BNotebook%20-%20Student%5D%20Week%202%20-%20Web%20Scraping%20Text%20for%20a%20Chatbot.ipynb

# Week 5 - Data Collection

![data_collection-2.png](attachment:data_collection-2.png)

##  Table of Contents

- Theoretical Overview
- Problem Statement
- Code
    1. Adding knowledge base to your chatbot
        - Importing libraries
        - Data collection
        - Preprocessing data
    2. Get your chatbot to say its first words
    3. Test your clever chatbot!

## Theoretical Overview

Data collection is the process of gathering information from various sources for analysis and storage. Web scraping is a specific form of data collection that involves extracting information from websites. The process involves sending HTTP requests to a website's server, downloading the HTML content, and parsing the data of interest. This is achieved with the help of web scraping softwares or with programming language libraries. The extracted information can be text data that can be used for natural language processing purposes, image data or tabular data that can be used for general machine learning purposes. It remains a valuable tool for data collection.

## Problem Statement

This activity will include web scraping techniques for Data Collection. In this activity, you will have to scrape the text data from a Wikipedia page. Then, you are required to create a chatbot using the cosine similarity algorithm. You have to create a chatbot which will recognise certain input and reply it with a response that makes sense. <br> This exercise is inspired by the [great work](https://medium.com/analytics-vidhya/building-a-simple-chatbot-in-python-using-nltk-7c8c8215ac6e) by Parul Pandey.

## Code

## 1. Adding knowledge base to your chatbot

Your chatbot's ability to converse and interact depends on the data that you input to it. Therefore, the first step you want to do is to plan your chatbot. You will have to choose the right knowledge base for your particular task. For instance, you would not train your chatbot on movie reviews if you want it to answer questions about sports cars!

In this exercise, you will decide what you want your chatbot to have knowledge on, and look for webpages required to build a dataset.

To start off, we will collect the raw text data from Wikipedia on Chatbots. The processed data have been stored in a text document file called robots.txt.
  
What questions would you like your chatbot to answer? You could train your chatbot on endangered species, hunger, gender equality, clean energy, or any other topic you would like! Use the tools you have learned from the previous Experiences to collect information, and process it into a corpus of knowledge.

### Importing libraries

In this exercise, we will be requiring the following libraries:
"""

# Import packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import numpy as np # to represent corpus as arrays
import random
import string # to process standard python strings
from sklearn.metrics.pairwise import cosine_similarity # We will use this later to decide how similar two sentences are
from sklearn.feature_extraction.text import TfidfVectorizer # Remember when you built a function to create a tfidf bag of words in Experience 2? This function does the same thing!
import nltk # to process text data

"""### Data Collection

### Specify url of the web page as the source
We will specify the required webpage url, where we collect the data from
"""

source = urlopen('https://en.wikipedia.org/wiki/Chatbot').read()

"""### Initiating BeautifulSoup
We will initiate and create an instance of BeautifulSoup
"""

soup = BeautifulSoup(source,'lxml')
soup

"""### Text extraction
We will extract the plain text content from paragraphs
"""

paras = []
for paragraph in soup.find_all('p'):
    paras.append(str(paragraph.text))

"""We will extract text from paragraph headers"""

heads = []
for head in soup.find_all('span', attrs={'mw-headline'}):
    heads.append(str(head.text))

"""### Interleaving the paragraphs and headers"""

# Interleave paragraphs & headers
text = [val for pair in zip(paras, heads) for val in pair]
text = ' '.join(text)

"""### Superscript edit
We will drop footnote superscripts in brackets
"""

text = re.sub(r"\[.*?\]+", '', text)

"""### Trimming the text and replacing new lines
We will replace '\n' (a new line) with '' and trim the unwanted text from both the ends
"""

text = text.replace('\n', '')[55:-15]

text

"""- **We have successfully scraped the text data from Wikipedia. Let us move on with the preprocessing part.**

### Processing data

Now we begin to process the knowledge base. We will read the text file, convert everything to lowercase and tokenize it. Do you remember what tokenization does?  
  
There exists pre-trained tokenizers that will help split your document up into tokens.

If this is the first time you are using these pre-trained tokenizers, you will have to download it with the command `nltk.download('punkt')`. We will also use a pre-defined model to perform lemmatization. This is downloaded using `nltk.download('wordnet')`. Subsequently, you can comment out the line if you ever have to run the cell again.

**Optional: run these if you do not have the required functions**
"""

nltk.download('punkt') # first-time use only tokenizer
nltk.download('wordnet') # first-time use only Used for the lemmatizer

"""### Conversion to lower case

We will convert all text to lower case first. Remember to inspect the result once we are done.
"""

#your code here
raw_data = text.lower()
print(raw_data)

"""### Sentence segmentation

We will use the funtion .sent_tokenizer to convert documents into a list of sentences.
"""

tokens = nltk.sent_tokenize(raw_data)
print(tokens)

"""Great! You have separated the document into sentences. However, notice that it is difficult to decipher the individual sentence now.

**Task: Print every sentence in a new line!**

This way, it will be easier to read the sentences!

Use the link [here](https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/) to learn how to do that!
"""

#your code here
print(*tokens, sep = "\n")

"""### Word tokenization

We will use the funtion .word_tokenizer to convert sentences into a list of words.
"""

#your code here
words = nltk.word_tokenize(raw_data)
print(words)

"""Now we have our tokens!

It is useful to inspect our tokens to make sure they look as expected, and to make sure that we have enough information to train our chatbot. Each sentence token can be considered one piece of knowledge as they provide a single piece of information about your knowledge base. The size of your knowledge base will determine how capable your chatbot will be.

The code to print the lengths of your sentence and word tokens are below.
"""

# Use this to check the size of your knowledge base. There should be at least 150 sentence tokens, and if possible, up to 1000
# to provide enough context for your chatbot.

#your code here
print(len(tokens), len(words))

"""Great job! we now have an idea of the amount of information passed to our chatbot. If you find that you do not have enough sentence tokens, this is the time to go back out and search for more information!  
  
### Lemmatization

We will lemmatize our word tokens using the WordNetLemmatizer that we have downloaded.
"""

lemmer = nltk.stem.WordNetLemmatizer() #Initiate lemmer class. WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

"""### Normalization

We also write functions to remove punctuation since that will not be useful for our knowledge base.
"""

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict))) #see previous section 1.2.5 lemmatization

"""Time to see how these functions work! call the function on the following sentence and print the output. What has our function done to the test sentence?"""

test_sentence='Today was a wonderful day. The sun was shining so brightly and the birds were chirping loudly!'
test_word_tokens = nltk.word_tokenize(test_sentence)# converts documents to list of words

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

LemTokens(test_word_tokens)

"""## 2. Matching topics with cosine similarity

Congratulations, you have now converted your knowledge database from text into sentences and tokens! Do you remember what is the next step after this? Computers are good at processing numbers, and therefore, we will next convert our tokens into numbers!

To do so, we will revisit the bag of words and tf-idf from acquire stage and experience 2.

How does having our document vector help us to create our chatbot?  

**How would computer finds similarity?**

Suppose you want to create a chatbot that can read your input, 'considers' what your input is talking about, and then respond with something that makes the most sense. One of the most common ways is by taking the question, and looking for information within the dataset that is very similar to our question. For example, if the questions contains the phrase 'computer failure', we will assume that the answer lies in sentences that contains words similar to 'computer failure' like 'computer crash', or 'hardware failure'.

**What is [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity)?**

Remember that we will convert our dataset into document vectors? cosine similarity allows us to find similar vectors, and these vectors will be assumed to be similar in meaning.

**Let us work through an example below!**

**Dataset**

Here, we have 3 sentences. The first 2 are our mini knowledge base, while the third one is our sample question. We will process them into document vectors, and then use cosine similarity to see which one of the knowledge base can give us better answer to the question!
"""

# Let us take two sentences to be the knowledge base, and one more which is a question.
Sentence_1='John is my father'
Sentence_2='Jane is my mother'
Question='who is my father'

"""### Vocabulary

The vocabulary is a list of all the words that exist in our sentence and questions.   

**Task: List down the vocabulary included in the dataset**
"""

Vocabulary = ['John', 'is', 'my', 'father', 'Jane', 'mother', 'who']

"""### Bag of words

How would we put this into a bag of words?

**Task: Construct an array to represent the information from the two sentences above using a bag of words technique**

Hint 1: The array should be of size (3,7), and each number within the array is either 0 or 1 to indicate the presence of that word in the row.  
Hint 2: An array is constructed using the function array_name = np.array([[row 1],[row 2],[row 3]])
"""

# bag_of_words
array1 = np.array([[Sentence_1],[Sentence_2],[Question]])
#print(array1)

def corpus(array1):
    s = []
    for x in range(len(array1)):
        if not array1[x].isdigit():
            if (x != len(array1)-1) and (array1[x+1].isdigit()):
                for num in range(int(array1[x+1])):
                    s.append(array1[x])
            else:
                s.append(array1[x])
    return ' '.join(s)

sentenseagg = list(map(corpus, array1))

vectorizer = TfidfVectorizer()
bow = vectorizer.fit_transform(sentenseagg)
print(bow.shape)
#print(bow)

"""In your bag of words, the first 2 rows encode all your knowledge that is contained in sentence 1 and sentence 2. The third row encodes your question.  
To find the piece of knowledge closest to your question, we simply look for the sentence with the highest cosine similarity to your question.  

**Finding cosine similarity**

Remember at the beginning of the exercise when we imported all our libraries? One of the libraries was called `from sklearn.metrics.pairwise import cosine_similarity`. The cosine_similarity function allows us to compare sentences. Imagine each sentence as a vector, which is a line pointing in some direction. Cosine similarity calculates the angles between each line and the more similar two lines are, the smaller their angle, and the higher their cosine similarity.  
  
Let us calculate the cosine similarities between each piece of information in our knowledge base, and the question. Remember the first row of our array corresponds to sentence 1, and the second row corresponds to sentence 2. Let us see which sentence has a higher cosine similarity to the question!

**Task: Use indexing function to select only the top 2 rows of bag of words**
"""

#your code here
sent1 = cosine_similarity(bow[0], bow[2], dense_output=True)
sent2 = cosine_similarity(bow[1], bow[2], dense_output=True)
print(sent1, sent2)

"""Great, you have your database selected, now we want to list the question which is at the last row of the variable bag_of_words:"""

print(bow[2])



"""What is the difference between the 2 output above? Try using the lines for the cosine simililarity exercise below

We are now ready to apply the cosine similarity
"""

# Remember our database
# Sentence_1='John is my father'
# Sentence_2='Jane is my mother'
# Question='who is my father'

# your code here
def match(matches):
  vals = cosine_similarity(bows[-1],bows) #get cosine similarity value
  idx=vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort() #sort in ascending order
  req_tfidf = flat[-2]

  if(req_tfidf==0):
        robo_response=robo_response+"Not a good match"
        return robo_response
  else:
        robo_response = robo_response+tokens[idx]
        return bow[i]

"""### Now, analyze the result!

Which sentence had a higher cosine similarity, and was it the answer you expected?

If you got your chatbot to return the sentence with the highest cosine similarity score as the answer, would it have answered the question correctly? That is basically how a chatbot answers questions!  
  
**Task: Now, can you think of a question which would cause sentence 2 to have a higher cosine similarity? Show us the score!**
"""

# Your code here
# Suggest an update to the initial sentences and the resulting bag of words.

cosine_similarity(bow[:2,:], bow[-1,:].reshape(1, -1))

"""Congratulations! Now that your chatbot has brains, let us give it a mouth!

## 3. Get your chatbot to say its first words

### Greetings
At the start of every conversation, your chatbot may expect a greeting. These greetings are not a question, but your chatbot should have a reply to the greeting too. We can input some common greetings you expect to receive, and get your chatbot to reply with a random selection of greeting responses.  
   
Tip: Your chatbot may throw up some warnings. Do not worry about those as long as your chatbot is giving you reasonable answers.

### Create list of inputs and responses

Let's first create the list of greetings your chatbot will have
"""

GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up","hey", "hey there"]
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

"""**Task: Add some greeting inputs and responses to personalize your chatbot**"""

# Your code here
GREETING_INPUTS.append('howdy')
GREETING_RESPONSES.append('howdy back')
print(GREETING_INPUTS)
print(GREETING_RESPONSES)

"""### Create function to receive and return greetings"""

def greeting(sentence):
    for word in sentence.split(): # Looks at each word in your sentence
        if word.lower() in GREETING_INPUTS: # checks if the word matches a GREETING_INPUT
            return random.choice(GREETING_RESPONSES) # replies with a GREETING_RESPONSE

"""Let's test this out! type different types of greetings into the chatbot and see how it responds. Run the greeting a few different times. Do you get the same answer each time?  
Hint: pressing ctrl-enter allows you to run the highlighted cell. Holding ctrl and pressing enter multiple times allows you to run the same cell repeatedly.
"""

# Your code here
greeting('hi')

"""### Create function to receive questions and return answers

Now let us define a function to calculate a response when someone asks the robot a question.

The response function:
1. Takes in a question
2. Uses cosine similarity to find the closest sentence to the question
3. Returns that sentence as an answer

To prevent the chatbot from returning completely useless answers, we will only return an answer if it has a cosine similarity greater than 0. Otherise, the chatbot will simply say that it does not understand the question.

**Note:** The Chatbot is using TFIDF to vectorize our dataset. To learn more about TFIDF click [here](https://www.geeksforgeeks.org/understanding-tf-idf-term-frequency-inverse-document-frequency/)
"""

def response(user_response):

    robo_response='' # initialize a variable to contain string
    tokens.append(user_response) #add user response to sent_tokens
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(tokens) #get tfidf value
    vals = cosine_similarity(tfidf[-1], tfidf) #get cosine similarity value
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort() #sort in ascending order
    req_tfidf = flat[-2]

    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+tokens[idx]
        return robo_response

"""### Testing the response function

Test the response function. Write some questions into the response() function and inspect the results. Are they close to the answers?

If you constantly get the response 'I'm sorry! I don't understand you', you might need to add more information into your knowledge base.
"""

# Your code here
response('What do chatbots do?')

"""### Adding more information into knowledge base

You can add more information into your knowledge base either by hand, for specific answers you have, or by searching for and adding more data into the text file!

## 4. Test your clever chatbot!

### Testing your chatbot
Now it is time to test your chatbot. This chatbot will be run entirely inside your jupyter notebook. You can train your chatbot to do specific tasks on commands.

For instance:
1. Saying 'bye' will cause the chatbot to shutdown.
2. Giving a response that is one of the greeting phrases will cause the chatbot to give a greeting in return.

You can add more features to your chatbot based on a list of keywords that triggers a certain behavior. For example, you can get your chatbot to tell the time, to tell a joke, or even print pictures.
  
Your basic chatbot is written below. You can play with it to see how well it can understand questions in your knowledge base. It will not be able to answer questions very well because chatbots require many thousands of sentences which takes many days to train. It should still be able to answer simple questions!  

**Adding time features to your chatbot**

You will now add more features to your chatbot to improve its capabilities! For a start, add a feature to your chatbot that will allow it to tell you the time if the user inputs 'time'.  
Hint: Use a similar template to the greeting function above. You can get the current time by importing datetime and calling datetime.datetime.now().
"""

import datetime

def tell_time(sentence):
    for word in sentence.split():
        # your code here
            currentdt = datetime.datetime.now()
            return currentdt.strftime("%Y-%m-%d %H:%M:%S")

tell_time('time')

"""### Test your chatbot now!"""

flag=True
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("ROBO: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("ROBO: "+greeting(user_response))
                # Uncomment the statement below once you have written your tell_time fuction.
#             if(tell_time(user_response)!=None):
#                 print("ROBO: "+tell_time(user_response))
            else:
                print("ROBO: ",end="")
                print(response(user_response))
                tokens.remove(user_response)
    else:
        flag=False
        print("ROBO: Bye! take care..")

"""Now you have a very basic chatbot that can be trained on data you have chosen. Improve your chatbot in the following ways:
1. increase the number of greeting inputs and greeting responses
2. increase the number of words to say goodbye i.e. see you!, quit, exit
3. train your chatbot on a different topic, or add to your chatbot's knowledge base by adding more data
"""
