from instagrapi import Client
import csv
import time
import random


cl = Client()

def read_credentials(filename):
    '''
    Read the credentials from the file and return the list of credentials one line at a time
    args:
        filename: the name of the file to read
    returns:
        list of credentials   
    '''
    with open(filename,encoding="utf8", errors="ignore") as f:
        reader = csv.reader(f)
        data = list(reader)
        print(data[0])
    return data[0]




def login(credential):
    '''
    logins to instagram
    args:
        credential: list of username and password. username at index 0 and password at index 1
    returns:
        None    
    '''
    cl.login(credential[0],credential[1])
    print("login as ",credential[0])
    ran = random.randrange(10,18)
    print("sleeping for {} seconds".format(ran))
    time.sleep(ran)
    


def get_hashtags_users(hashtag):
    medias = cl.hashtag_medias_top(hashtag, amount=15)
    for i in range(len(medias)):
        username = medias[i].dict()['user']['username']
        print(username)

        #save usernames into a file
        with open('target.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username])
    return username
       



def main():

    #getting credentials
    credential = read_credentials('logins.csv')
    #logging in
    login(credential)

    #getting hashtags from user
    hashtag = input("please type hashtag  here...!! : ")
    # get_hashtags_users(hashtag)
    medias = cl.hashtag_medias_top('love', amount=15)
    print(medias)
    
    #logging out
    cl.logout()

if __name__ == "__main__":
    main()


