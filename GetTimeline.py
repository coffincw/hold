import re
import tweepy
import SentimentAnalyzer
from tweepy import OAuthHandler
from textblob import TextBlob

'''

working on a class that should, in theory, return the full timeline of any user (used donald trump
in this case im lazy and that's what the example was using)
having problems with getTimeline() and getTraining()

'''

class GetTimeline(object):
  def __init__(self, *args, **kwargs):
    consumer_key = 'n4zRm3xuVoYoBHDLbSSqCxlII'
    consumer_secret = 'i2bxYM53rVNv0NFnO4iALdUYUDXHSEp9JARjpSu6290B5W6BLj'
    access_token = '3265727682-sWioD71Vv1zJie1KCERyHZWgzCdDsGAy3lzdLJA'
    access_token_secret = 'Ir9vMlPyiJwafcqXOiRJgtdWpev2VU3rI0Z2MWXlJ79SV'
    keywords = ["I need someone to talk to", "depressed", "wanna talk to someone", "want to talk to someone", "#depressed",
                "#depression", "lonely", "alone", "sad", "i'm worthless", "falling apart", "disappointed in myself", "i'm the worst",
                "i'm useless", "i am useless", "i'm a failure", "I am a failure", "too much pain", "unfair", "i'm not happy",
                "i am not happy", "unhappy", "regret", "have no one", "I don't know what to do", "i'm lost", "i am lost", "i am so lost",
                "hate me", "kill myself", "end myself", "end my life", "I want to die", "I want to commit suicide",
                "i'm no good", "feel like shit", "i feel invisible"]
     # attempt authentication
    try:
      # create OAuthHandler object
      self.auth = OAuthHandler(consumer_key, consumer_secret)
      # set access token and secret
      self.auth.set_access_token(access_token, access_token_secret)
      # create tweepy API object to fetch tweets
      self.api = tweepy.API(self.auth)
    except:
      print("Error: Authentication Failed")
    return super().__init__(*args, **kwargs)

  @staticmethod
  def getTraining(username):
    tweets = SentimentAnalyzer.main("e%20")
    anxiety = SentimentAnalyzer.main("s%20")
    tweets.extend([x for x in anxiety if x not in tweets])
    training = []
    for x in tweets:
      training.append(list(x.values())[0])

    xyz =  getTimeline(username)
    for y in xyz:
       print(y)



def getTimeline(username):
  timeline = []
  api = GetTimeline().api
  for status in tweepy.Cursor(api.user_timeline, screen_name = username, count = 100).items():
    timeline.append(status.user.screen_name)
  return timeline

def generateRandUsers():
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
              'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  users = []
  api = GetTimeline().api
  for a in alphabet:
    s = a+"%20"
    tweets2 = tweepy.Cursor(api.search, q=s, count = 100, lang = 'en', wait_on_rate_limit = True, wait_on_rate_limit_notify = True).items()
    for x in tweets2:
      if(x.user.screen_name not in users):
        users.append(x.user.screen_name)
  print(len(users))
  f = open("text.txt", "w")
  for x in users:
    f.write(x+"\n")





def main():
  #GetTimeline().getTraining("@iamdevloper")
  generateRandUsers()


if __name__ == "__main__":
    main()










