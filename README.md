# This solution got the 4th rank in a innominds online hackthon - 2018

# 24x7-Smart-IT-Helpdesk
- This is a chatbot to solve the problem given in [Problem_Statement_Final](https://github.com/00archer0/24x7-Smart-IT-Helpdesk/blob/master/Problem_Statement_Final.pdf)
- A hybrid smart Chatbot built in Django a Python Web framework using Ntlk and Gensim library. An expert bot that uses a Word2vec and td-idf to obtain questions vectors and compute the cosine similarity between the vectors to find out semantic and syntactic similar questions.


# Features
- scalability -  The solution is using django framework. 
- Do the build knowledge base ?  - Yes
- search Result scoring based on accuracy - suggest top 3 resolutions.
- How frequently model updates? - after every 10 new questions. 
- Implemented, if the support agent selects one from the suggestions provided, the system should be able to learn and then keep that as the correct solution for similar future search’s.


# Instructions to run this project.
 
 1. Dwonload this project
 2. Extract the file from downloaded zip.
 3. open the commandprompt in the location "./24x7-Smart-IT-Helpdesk/chatbot_IT"
 4. then run a command in commandprompt "python manage.py runserver"
 5. open your internet browser/chrome "http://127.0.0.1:8000/chatbot/index" run this url
 
 
### To run this project you should have installed 
 - python 3
 - Django
 - nltk
 - gensim
 - pandas
 and all the libraries it will ask you to download. 


If you find any problem to run this feel free to connect with me at **00archer0@gmail.com**
