import sys, os, time
import tweepy

def oauth_login(config_file):
    # uses your dev.twitter.com credentials.
    # apply as a twitter developer
    # create a twitter application in
    # https://developer.twitter.com/en/apps.
    # place the following credentials values
    # in this order - in config.cfg file:
    # 1. consumer_key
    # 2. consumer_secret
    # 3. access_key
    # 4. access_secret

    cfg = [x.strip() for x in config_file]
    auth = tweepy.OAuthHandler(cfg[0],cfg[1])
    auth.set_access_token(cfg[2],cfg[3])
    user = cfg[4]
    return tweepy.API(auth), user


def purge(api,user):
    tweets = api.favorites(user)
    for f in tweets:
        api.destroy_favorite(f.id)
        time.sleep(6) # wait 6 seconds between requests to avoid rate limit.

if __name__ == "__main__":
    dir_name = os.path.dirname(os.path.realpath(__file__))
    dn = open(dir_name+"/config.cfg","r")
    api, user = oauth_login(dn.readlines())

    purge(api, user)

