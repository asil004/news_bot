import os
from currentsapi import CurrentsAPI
import json
from dotenv import load_dotenv

load_dotenv('.env')

api = CurrentsAPI(api_key="H2Oke_cebh4_WU5GTuHmay5XXMVwgv4eNoz_O6DDa7uRpOEC")


def get_latest_news():
    return api.latest_news()['news'][0:10]


def get_search_news(keyword: str):
    return api.search(keywords=keyword)['news'][0:10]


if __name__ == '__main__':
    print(get_search_news('trump'))
