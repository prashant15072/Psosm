from django.shortcuts import render
import twitter
import csv
import time
api = twitter.Api()
api = twitter.Api(consumer_key='uIeZs64S6xGFRx7l9KgyzqGJp',consumer_secret='J638BgqSF4Fb4D6p4tcuOfF12TPQqKZ454o1mtrU1jCndqXxtz',access_token_key='2451495793-IjjDJSqOKskEKcy0ijxEK9TDB65tn5ZrXo4uCpz',access_token_secret='1J1RuPfL4xKej0X1LMQ3INo8s38LfHTVp1FdJaaCEn7h5')
csv_file = 'data/medical_tweet_list.csv'
csv_list=[]
ax=0
ex=0
fx=0

def read_file():
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_list.append(row['User name'])

def do_get(request,param):
    if param in request:
        return request[param]
    else:
        return ""

def dm_users(request):
    users=[]
    message=do_get(request.POST, 'message')

    for a in range(0,3):
        global fx
        b=csv_list[fx].replace('"','')
        users.append(b)
        try:
            api.PostDirectMessage(message, user_id=None, screen_name=b)
            print("Messaged @"+str(a))
        except BaseException,e:
            pass

    feilds = {
        "action_performed": "Messaged the users",
        "users": users,
    }

    return render(request, 'index.html', feilds)

def follow_users(request):
    users=[]

    for a in range(0,3):
        global ax
        b = csv_list[ax].replace('"', '')
        users.append(b)
        api.CreateFriendship(user_id=None, screen_name=b, follow=True)
        print("Started Following " + str(a))
        ax+=1

    feilds = {
        "action_performed": "Followed three new users",
        "users":users,
    }

    return render(request, 'index.html',feilds)


def tweet_user(request):
    users=[]
    message=do_get(request.POST, 'message')

    for a in range(0,3):
        global ex
        b = csv_list[ex].replace('"', '')
        users.append(b)
        try:
            api.PostUpdates(message+" @" + str(b))
            ex+=1
            print("Tweeted @" + str(a))
        except BaseException, e:
            pass

    feilds = {
        "action_performed": "Tweeted for the users",
        "users":users,
    }

    return render(request, 'index.html', feilds)

def tweet_specific_user(request):
    username=do_get(request.POST, 'username')
    message=do_get(request.POST, 'message')
    feilds = {
        "action_performed": "Tweeted for " + str(username),
    }

    try:
        api.PostUpdates(message+" @"+str(username))
        print("Tweeted @" + str(username))
    except:
        feilds["action_performed"]="Error Occurred While Tweeting"

    return render(request, 'index.html', feilds)

def follow_specific_user(request):
    username=do_get(request.POST, 'username')
    b = username.replace('"', '')

    feilds = {
        "action_performed": "Followed @"+str(username),
    }

    try:
        api.CreateFriendship(user_id=None, screen_name=b, follow=True)
    except:
        feilds["action_performed"]="Didn't Find The User"

    return render(request, 'index.html',feilds)

def dm_specific_user(request):
    username=do_get(request.POST, 'username')
    message=do_get(request.POST, 'message')

    feilds = {
        "action_performed": "Messaged @" + str(username),
    }

    b =username.replace('"', '')
    try:
        api.PostDirectMessage(message, user_id=None, screen_name=b)
    except BaseException, e:
        feilds["action_performed"]="Error Occurred While Messaging"


    return render(request, 'index.html', feilds)


def temp(request):
    return render(request,'extra.html')


def index(request):
    read_file()
    return render(request, 'index.html')