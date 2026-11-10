###
# Influencer checker (at least two social media accounts)
#
facebook = True
twitter = False
instagram = True

if (facebook + twitter + instagram) >= 2:
    print('You are a good influencer!')
