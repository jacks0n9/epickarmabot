import praw
import os
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("freekarma4u")
if not os.path.isfile("posts_replied_to.txt"):
    f = open("posts_replied_to.txt", 'w')
    f.write('')

def epic():
    for submission in subreddit.new():        
        with open("posts_replied_to.txt", 'r') as f:
            lines = f.read().split(',')
            if submission.id not in lines:
                print("Commenting on post: ",submission.title)
                try:
                    submission.reply("Upvote this comment so that i beat NoFreeKarma4UBot to 10k karma! Why: My profile pic has a mustache and his doesn't... you may think that doesn't mean anything, but mustaches automatically make you better the people who don't have them. Also if you really really want me to beat him, you could upvote some of my other comments or posts too :) Just dm me if you have a bot and would like to participate in the karma wars! Bots are allowed, but you have to find one yourself or make one! Also join https://www.reddit.com/r/somekarmabot/")
                    f= open('posts_replied_to.txt', 'r').read()
                    current = f
                    f= open('posts_replied_to.txt', 'w')
                    writer = current + "," + submission.id
                    f.write(writer)
                    f.close()
                    print("Ok replied")
                
                except praw.exceptions.RedditAPIException:
                    print("Ooops, rate limit try again in a few minutes")
                    exit(0)
while True:
    epic()
