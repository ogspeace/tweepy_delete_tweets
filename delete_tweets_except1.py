import os, tweepy

def oauth_login(config_file):
    cfg = [x.strip() for x in config_file]
    auth = tweepy.OAuthHandler(cfg[0],cfg[1])
    auth.set_access_token(cfg[2],cfg[3])
    return tweepy.API(auth)

def batch_delete(api):
    for status in list(tweepy.Cursor(api.user_timeline).items()):
        if status.id not in [int(x.strip()) for x in open("tosave.txt","r").readlines()]:
            api.destroy_status(status.id)

if __name__ == "__main__":
    dir_name = os.path.dirname(os.path.realpath(__file__))
    dn = open(dir_name+"/config.cfg","r")
    api = oauth_login(dn.readlines())
    print(("Authenticated as: %s" % api.me().screen_name))
    batch_delete(api)

