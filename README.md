# RentimentData

Use data from reddit, twitter, news articles, etc. to construct sentiment and popularity of a particular
 stock or crypto currency. 

### How to run

Install MongoDB and run mongod process on default port (https://docs.mongodb.com/manual/installation/): mongod

#### Todo: Heroku! (Brian)

Install a python venv in base directory populated with requirements.text:
pip install -r requirements.txt

#### Todo: Remove below (Brian)

Add a praw.ini file to your local directory and add client id and client secret credentials:
 https://praw.readthedocs.io/en/latest/getting_started/quick_start.html

Run main: python main.py

#### Todo: should these be here ?

I had to install punkt, universal_tagset, and averaged_perceptron_tagger for nltk to work via this command:
 nltk.download('punkt')
