import json

tweetFile = open("tweetData.json", "r")

tweetData = json.load(tweetFile)

tweetFile.close()

#prints dictionary of tweet number 1
# print ("This is the id of the first tweet:", tweetData[0]["id"])

# print ("This is the screen name of the first tweet," tweetData[56]["screen_name"])
#will not work because "screen_name" is in the dictionary "users"
#print("This is the screen name:", tweetData[56]["screen_name"])
#opens user library
#print("This is the screen name:", tweetData[56]["user"]["screen_name"])

#for i in range(len(tweetData)):
#    print (tweetData[i]["user"]["screen_name"])

#for tweet in tweetData:
#    print(tweet["user"]["screen_name"])

count = 0
for tweet in range(len(tweetData)):
    if (tweetData[tweet]["lang"]=="es"):
        count += 1

print (count)
