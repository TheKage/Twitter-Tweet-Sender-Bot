import mechanize
import getpass
import os
import sys
import time

contact = """
##############################################################
#                                                            #
#   TWEET SENDER BOT - EASIEST WAY TO TWEET FROM TERMINAL    #
#                                                            #
##############################################################
#                                                            #
#                     DEVELOPED BY KAGE                      #
#                                                            #
##############################################################
"""

confirmation_message = """
##############################################################
#                                                            #
#                    SUCCESSFULLY TWEETED!                   #
#                                                            #
##############################################################
"""

stars = "##############################################################"

terminal_login = """
##############################################################
#                                                            #
#                TWITTER - TERMINAL LOGIN PANEL              #
#                                                            #
##############################################################
"""

operations = """
(1) Tweet
(2) Exit
"""

def sender_bot():
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    site = "https://mobile.twitter.com/session/new"
    browser.open(site)
    browser.select_form (nr=0)
    browser["session[username_or_email]"] = username
    browser["session[password]"] = password
    browser.submit()

    tweet_content = raw_input("Enter your tweet: ")
    twitter_url = browser.open("https://mobile.twitter.com/session/new").read()
    tweet_url = "https://mobile.twitter.com/compose/tweet"
    browser.open(tweet_url)
    browser.select_form(nr=0)
    browser["tweet[text]"] = tweet_content
    browser.submit()
    print confirmation_message



print contact
time.sleep(5)
os.system( 'cls' if os.name == 'nt' else 'clear')
print terminal_login
username = raw_input("Enter your twitter username: ")
password = getpass.getpass("Enter your password: ")

while True:
    print stars
    print operations
    operation = raw_input("Which operation do you want to perform?\n").lower()
    print stars

    if operation == "1" or "tweet":
        sender_bot()
#    elif operation == "2" or "change account":
#        login()
    elif operation == "2" or "exit":
        print stars
        break






