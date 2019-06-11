import tweepy

session = dict()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#token = session.get('request_token')
#session.delete('request_token')
#auth.request_token = {'oauth_token': token, 'oauth_token_secret': verifier}

try:
    redirect_url = auth.get_authorzation_url()
    session['request_token']=(auth.request_token.key, auth.request_token.secret)
except tweepy.TweepyError:
    print("Error! Failed to get request token.")

verifier = request.Get.get('oauth_verifier')
