from django.shortcuts import render
import twitter
import csv
import time
api = twitter.Api()
api = twitter.Api(consumer_key='uIeZs64S6xGFRx7l9KgyzqGJp',consumer_secret='J638BgqSF4Fb4D6p4tcuOfF12TPQqKZ454o1mtrU1jCndqXxtz',access_token_key='2451495793-IjjDJSqOKskEKcy0ijxEK9TDB65tn5ZrXo4uCpz',access_token_secret='1J1RuPfL4xKej0X1LMQ3INo8s38LfHTVp1FdJaaCEn7h5')
csv_file = 'data/medical_tweet_list.csv'
csv_list=[]

def read_file():
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_list.append(row['User name'])


def dm_users():
    for a in csv_list:
        b=a.replace('"','')
        try:
            api.PostDirectMessage("Hey Would you like to take our newly curated Health Insurance Plan that covers every Mishappenings ?", user_id=None, screen_name=b)
            time.sleep(3)
            print("Messaged @"+str(a))
        except BaseException,e:
            pass

def follow_users():
    for a in csv_list:
        b = a.replace('"', '')
        api.CreateFriendship(user_id=None, screen_name=b, follow=True)
        time.sleep(3)
        print("Started Following " + str(a))

def tweet_user():
    for a in csv_list:
        b = a.replace('"', '')
        try:
            api.PostUpdates("Hey @" + str(
                b) + " Would you like to take our newly curated Health Insurance Plan that covers every Mishappenings and keep you and your family safe :D?")
            time.sleep(3)
            print("Tweeted @" + str(a))
        except BaseException, e:
            pass




def index(request):
    read_file()
    return render(request, 'index.html')