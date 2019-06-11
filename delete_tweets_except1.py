import os, tweepy, configparser

consumer_key = 'g5BOpHtfJlB505sjHuHyMiBPg' #os.environ['TWPOGSCK']
consumer_secret = 'sF3NxENnSwVGlEI9SLvDmBPidlfwiYeBVZWIm9Zz4YIuooQaXQ' #os.environ['TWPOGSCS']
access_token = '400464995-lFoEYqQN9K5U0h23vKwss7lPTOMJYzWBePSuwHHV' #os.environ['TWPOGSAT']
access_token_secret = 'MpsaYYLmtLeYCMy3f6Qpqjm8YBAnOKOWo4x4SpQiRgblB' #os.environ['TWPOGSATS']

def parse_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def oauth_login(config_file):
    cfg = [x.strip() for x in config_file]
    print(cfg)
    auth = tweepy.OAuthHandler(cfg[0],cfg[1])
    auth.set_access_token(cfg[2],cfg[3])
    return tweepy.API(auth)

def batch_delete(api):
    for status in list(tweepy.Cursor(api.user_timeline).items()):
        if status.id not in [int(x.strip()) for x in open("tosave.txt","r").readlines()]:
            api.destroy_status(status.id)

if __name__ == "__main__":
    dir_name = os.path.dirname(os.path.realpath(__file__))
    dn = open(dir_name+"/config2.cfg","r")
    api = oauth_login(dn.readlines())
#    print(type(config))
    print(("Authenticated as: %s" % api.me().screen_name))
#    batch_delete(api)

