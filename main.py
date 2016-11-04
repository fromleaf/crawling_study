# -*- coding: utf-8 -*-

import chardet

from crawling import collect, parser


if __name__ == '__main__':
    # collect.by_requests('http://fromleaf.tistory.com')
    # collect.by_robobrowser('http://fromleaf.tistory.com')
    # collect.by_feedparser()
    # collect.get_news_by_feedparser(
    #     'http://imnews.imbc.com/news/2016/politic/article/4155019_19803.html'
    # )

    # collect.what_is_encoding_by_chardet('http://fromleaf.tistory.com')
    # parser.by_beautifulsoup('https://www.pycon.kr/2016apac/program/list/')
    # parser.get_pycon_list_by_beautifulsoup('https://www.pycon.kr/2016apac/program/list/')
    # parser.by_pyparsing()
    parser.by_newspaper(
        'https://www.washingtonpost.com/world/south-korean-president-says-shes-willing-to-be-investigated-in-corruption-scandal/2016/11/03/3a6d9198-a221-11e6-8864-6f892cad0865_story.html?hpid=hp_hp-more-top-stories_southkoreascandal-1020pm%3Ahomepage%2Fstory'
    )