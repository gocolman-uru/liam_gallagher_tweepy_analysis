import tweepy
import time
import pprint


# autenticar nuestras keys
consumer_key = 'tNr06x7M0I1pDXERtp5EyQ2Zh'
consumer_secret = 'XmSQDfJ40PSGRVUGB954yWr8x0bXb25ethLEL6bMHnruwpvMWC'
access_token = '1145626590-Cf78Iq0Nbldb48yYPH2HKxhioMzuyvyTJB7Zo6b'
access_token_secret = 'pMvUM4iIcHccxxxzklT7CUQSWygVFah54armf8RhJqfex'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# ingresar a la api
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)






# obtener tweets
tweets = api.user_timeline('@liamgallagher')


#for tweet in tweets:
   # print(tweet.text)
    #print()

# borrar los RT 
for tweet in tweets:
    if tweet.text.startswith('RT'):
        continue
    
    print(tweet.text)
    print()

# obtener mas tweets que esos 20 

id = None
count = 0
while count <= 3300:
    tweets = api.user_timeline('@liamgallagher', tweet_mode='extended', max_id=id)
    for tweet in tweets:
        if tweet.full_text.startswith('RT'):
            count = count + 1
            continue
        f = open('tweet.txt', 'a', encoding='utf-8')
        f.write(tweet.full_text + '\n')
        f.close()
        print(tweet.full_text)
        print('\n')
        count = count + 1

    #saber el limite que nos queda despues de cada iteracion
    limit = api.rate_limit_status()
    limit = limit['resources']['statuses']['/statuses/user_timeline']['remaining']
    pprint.pprint(limit)
    id = tweet.id
    print(count)
    time.sleep(1)


