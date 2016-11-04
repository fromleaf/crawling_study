# -*- coding: utf-8 -*-

import requests
import feedparser

from robobrowser import RoboBrowser


def by_requests(url):
    result = requests.post(url)
    html = result.text

    print(html)


def by_robobrowser(url):
    browser = RoboBrowser(history=True)
    browser.open(url)
    print(str(browser.select))


def login_by_robobrowser(url):
    browser = RoboBrowser(history=True)
    browser.open(url)
    form = browser.get_form(action='/login/')

    form['username'] = 'username'
    form['password'] = 'password'
    browser.session.header['Referrer'] = url # for CSRF

    browser.submit_form(form)


def funny_by_robobrowser(url):
    browser = RoboBrowser(history=True)
    browser.open(url)

    songs = browser.select('.song_link')
    browser.follow_link(songs[0])
    lyrics = browser.select('.lyrics')
    lyrics[0].text

    # back to results page
    browser.back()

    # Look up my favorite song
    song_link = browser.get_link('trains')
    browser.follow_link(song_link)


def by_feedparser():
    raw_data = """
        <rss version="2.0">
        <channel>
        <title>Sample Feed</title>
        </channel>
        </rss>
    """
    d = feedparser.parse(raw_data)
    print(d)
    print(d['feed']['title'])


def get_news_by_feedparser(url):
    d = feedparser.parse(url)
    print(d)
    print(d['feed'])