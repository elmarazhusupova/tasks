import requests
from bs4 import  BeautifulSoup


def get_first_news():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like'
    }
    url = 'https://kloop.kg/'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    posts = soup.findAll('div', class =)
    news_posts = []
    for post in posts:
        news_posts.append({
            'image': post.find('div', class ='').find('img').get('src')
        })
    print(news_posts)

get_first_news()