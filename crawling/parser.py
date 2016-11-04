# -*- coding: utf-8 -*-

import requests
import newspaper


from bs4 import BeautifulSoup
from pyparsing import srange, Word, nums, Combine


def by_beautifulsoup(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title)


def get_pycon_list_by_beautifulsoup(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    for a in soup.find_all('a'):
        if 'program' in a['href']:
            if a['href'][-1] in [str(n) for n in range(10)]:
                print(a)


def by_pyparsing():
    korean_chars = srange(r'[\0xac00-\0xd7a3]')

    pattern = Word(nums) + Word(korean_chars)
    result = pattern.parseString(u'10만녕테스트')
    print(result)

    text = u"""<a href="/2016apac/program/29">Python 으로 19대 국회 뽀개기</a>
        <a href="/2016apac/program/33">Python + Spark, 머신러닝을 위한 완벽한 결혼</a>
        <a href="/2016apac/program/9">지적 대화를 위한 깊고 넓은 딥러닝 (Feat. TensorFlow)< <a href="/2016apac/program/11">파이썬 데이터 분석 3종 세트 - statsmodels, scikit- learn, theano</a>
        <a href="/2016apac/program/17">Deep Learning with Python &amp; TensorFlow</ <a href="/2016apac/program/3">나의 사진은 내가 지난 과거에 한 일을 알고 있다</a>
        <a href="/2016apac/program/8">기계학습을 활용한 게임 어뷰징 검출</a>
        <a href="/2016apac/program/53">검색 로그 시스템 with Python</a>
        <a href="/2016apac/program/28">PyLadies and PyGents</a>
        <a href="/2016apac/program/39">The stories about Django Girls Taipei</a>
        <a href="/2016apac/program/60">The PSF and our community</a>
        <a href="/2016apac/program/50">TOROS: Python Framework for Recommender Syst a>
        <a href="/2016apac/program/10">10만 라인, 26280시간의 이야기</a>
    """
    pat = Combine(Word(nums) + Word(korean_chars))
    for match, start, stop in pat.scanString(text):
        print(match[0], '\t', start, '\t', stop)


def by_newspaper(url):
    article = newspaper.Article(url)
    article.download()
    article.parse()
    print('title:', article.title)
    print('text:', article.text)