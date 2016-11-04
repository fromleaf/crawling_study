# -*- coding: utf-8 -*-

import chardet
import datetime

from crawling import collect, parser
from data import mongo


if __name__ == '__main__':
    # collect를 이용해서 내 블로그 정보 가져오기
    # collect.by_requests('http://fromleaf.tistory.com')
    # collect.by_robobrowser('http://fromleaf.tistory.com')
    # collect.by_feedparser()
    # collect.get_news_by_feedparser(
    #     'http://imnews.imbc.com/news/2016/politic/article/4155019_19803.html'
    # )
    # collect.what_is_encoding_by_chardet('http://fromleaf.tistory.com')

    # parser를 이용한 뉴스 가져오기
    # parser.by_beautifulsoup('https://www.pycon.kr/2016apac/program/list/')
    # parser.get_pycon_list_by_beautifulsoup('https://www.pycon.kr/2016apac/program/list/')
    # parser.by_pyparsing()
    # parser.by_newspaper(
    #     'https://www.washingtonpost.com/world/south-korean-president-says-shes-willing-to-be-investigated-in-corruption-scandal/2016/11/03/3a6d9198-a221-11e6-8864-6f892cad0865_story.html?hpid=hp_hp-more-top-stories_southkoreascandal-1020pm%3Ahomepage%2Fstory'
    # )

    mongo_db = mongo.init('localhost', 27017)

    mongo.create({'a': 1, 'b': 'c', 'd':datetime.datetime.now()}, mongo_db)
    result = mongo.read(mongo_db)
    print(result)
    result = mongo.update({'a':1}, mongo_db)
    print(result)
    result = mongo.delete({'a':1}, mongo_db)
    print(result)