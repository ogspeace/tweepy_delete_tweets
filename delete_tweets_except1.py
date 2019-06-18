import os, tweepy

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
    return tweepy.API(auth)

def batch_delete(api):
    # deletes all tweets except for tweet id's saved in tosave.txt
    # to tweet ids are often found on the address bar.
    # example:
    # https://twitter.com/your_user_name/status/1234567890
    # for example above, the tweet's id number is 1234567890.
    # place this number in tosave.txt, and it (along with other tweets)
    # would be 'saved' from batch_delete process
    # note: place one id per line.

    for status in list(tweepy.Cursor(api.user_timeline).items()):
        if status.id not in [int(x.strip()) for x in open("tosave.txt","r").readlines()]:
            api.destroy_status(status.id)

if __name__ == "__main__":
    dir_name = os.path.dirname(os.path.realpath(__file__))
    dn = open(dir_name+"/config.cfg","r")
    api = oauth_login(dn.readlines())
    print(("Authenticated as: %s" % api.me().screen_name))
    batch_delete(api)

