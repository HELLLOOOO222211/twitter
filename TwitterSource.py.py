import tweepy
auth = tweepy.OAuthHandler("KjAShZ5DhXGP0Yx0Cvzk9rgFm", "eXhEE9Mxi9ywISITDahON30GFOj0Pc0oyqximpFS6d4m6qzJjq")
auth.set_access_token("1458870484829982736-pxT4NKJgoVCw17N6mr3qD07TMwXv6x", "0RfUfnJk572m9LdmsDMB5YUjfbU72iRVFSNriR5qxI3H9")
api = tweepy.API(auth)
tweet = input("You all tweeting from iphones and android but look at ME")
api.update_status(status =(tweet))
print ("Done!")
