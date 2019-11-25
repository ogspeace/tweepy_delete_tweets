# tweepy_delete_tweets
## by Ogs Ablazo
script to delete (and save some) tweets using CLI. tested on windows and linux (raspbian, debian, *ubuntu) devices.

## prerequisites:
1. sudo pip3 install tweepy
2. your confirmed twitter api / developer credentials from dev.twitter.com: consumer_key, consumer_secret, access_key, access_secret

## usage:
### 1. apply to be a twitter developer (dev.twitter.com),
### 2. create a twitter application via https://developer.twitter.com/en/apps
### 3. placing your api credentials
once your account and app is approved: place the following app credentials in config.cfg (if this file doesn't exist, please create it):
3.1. ``` consumer_key ```
3.2. ``` consumer_secret ```
3.3. ``` access_key ```
3.4. ``` access_secret ```
### 4. saving a tweet or two from the deletion process: 
get the tweet's id number, by going to your tweet, and getting the id number from the address bar.
example: ``` https://twitter.com/your_user_name/status/1234567890 ```

in this example: ``` 1234567890 ``` is the id number.
place this number inside ``` tosave.txt ```. if you have additional tweets / tweet id's you want to save, place these in new lines.
### 5. execute the script
once your api creds are saved in ``` config.cfg ``` (required), and your tweet id's are identified in ``` tosave.txt ``` (optional),
execute the script by typing

``` python3 delete_tweets_except1.py ```


## reminders
1. please don't post your app creds online :)
2. deletion of tweets cannot be undone! so be sure that you are entirely sure that you want to bulk delete your tweets.
3. this script deletes all tweets. however if in the likely event that your tweet count's not reflecting the expected count,
please note that you might have had retweeted tweets that used to come from a public account (which are now set to private), 
therefore the script can't retrieve or delete these anymore.

