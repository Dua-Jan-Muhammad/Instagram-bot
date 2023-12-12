from instagrapi import Client
import csv
import time
import random

with open('logins.csv',encoding="utf8", errors="ignore") as f:
    reader = csv.reader(f)
    data = list(reader)


with open('target.csv',encoding="utf8", errors="ignore") as t:
    reader = csv.reader(t)
    target_list = list(reader)
    
cl = Client()

hashtag = input("please type hashtag  here...!! : ")
txt = input("please type your message here...!! : ")

def send_msg(text,ids):
    print("sending messege to {}".format(i))
    cl.direct_send(text,user_ids=[ids])



def find_userid(username):
    user_id = cl.user_id_from_username(username)
    return user_id



def hashtags():  
    medias = cl.hashtag_medias_recent(hashtag, amount=15)
    for i in range(len(medias)):
        username = medias[i].dict()['user']['username']
        print(username)
        user_id = find_userid(username)
        # send_msg(txt,user_id)




try : 

    for j in range(len(data)):
        cl.login(data[j][0],data[j][1])
        print("login as ",data[j][0])

        hashtags()
        for i in target_list:
            user_id = find_userid(i[0])
        
            send_msg(txt,user_id)
            
        
        cl.logout()
        ran = random.randrange(10,18)
        print("sleeping for {} seconds".format(ran))
        time.sleep(ran)

except:
    print("something went wrong ...!!!")
print("Success...!!!")

        # user = cl.direct_send("This is testing message sent by bot...",user_ids=[user_id])
    






