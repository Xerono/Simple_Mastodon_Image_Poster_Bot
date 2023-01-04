from mastodon import Mastodon
from configparser import ConfigParser
import random
import os
import sys

conf = sys.argv[1]

CP = ConfigParser()
CP.read(conf)
abu = CP["mastodon"]["api_base_url"]
mcs = CP["mastodon"]["client_secret"]
login =  CP["mastodon"]["login"]
password = CP["mastodon"]["password"]

SourceFolder = CP["folders"]["sourcefiles"]
TargetFolder = CP["folders"]["usedfiles"]

if len(os.listdir(SourceFolder))>=1:
    FN = random.choice(os.listdir(SourceFolder))
    Filename = SourceFolder + FN


    Mastodon.create_app("Poster", api_base_url=abu, to_file=mcs)   
    Mastodon = Mastodon(client_id = mcs, api_base_url=abu)

    Mastodon.log_in(login, password, to_file = mcs)

    Message_To_Post = "Your Message Here"
    Contentwarning = True

    
    pic = Mastodon.media_post(Filename)
    Mastodon.status_post(Message_To_Post, sensitive=Contentwarning, media_ids=pic)

    os.rename(Filename, TargetFolder + FN)





