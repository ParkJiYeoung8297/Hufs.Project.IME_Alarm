#import sys
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def today_data():
    req = requests.get("https://ime.hufs.ac.kr/ime/2807/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGaW1lJTJGNTA5JTJGYXJ0Y2xMaXN0LmRvJTNG")
    html = req.content.decode('utf-8','replace') # 한글이 깨져서 넣어주었다.
    bsObject= BeautifulSoup(html, 'html.parser')
    target_td_tags = bsObject.find_all('td', class_='td-date')[:5]
    for td_tag in target_td_tags:
        print(td_tag.text.strip()) 
    



def post_latest_data():
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "Alarm.settings")
    import django

    django.setup()

    from content.models import Post

    req = requests.get("https://ime.hufs.ac.kr/ime/2807/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGaW1lJTJGNTA5JTJGYXJ0Y2xMaXN0LmRvJTNG")
    html = req.content.decode('utf-8','replace') # 한글이 깨져서 넣어주었다.
    bsObject= BeautifulSoup(html, 'html.parser')
    target_tr_tags = bsObject.find_all('tr', class_='')
    p_list=[]

    Post.objects.all().delete()
    
    for tr_tag in target_tr_tags[1:]:
    
        td_num_tag = tr_tag.find('td', class_='td-num')
        td_num = td_num_tag.text.strip() if td_num_tag else None
        
        
        strong_tag = tr_tag.find('strong') 
        title = strong_tag.text.strip() if strong_tag else None
            
        date_tag = tr_tag.find('td', class_='td-date')
        date = date_tag.text.strip() if date_tag else None

        td_num = re.sub('<[^>]+>', '', td_num) if td_num else None
        title = re.sub('<[^>]+>', '', title) if title else None
        date = re.sub('<[^>]+>', '', date) if date else None
        p_list.append([td_num,title,date])   
        
        Post.objects.create(number=td_num,
                            title=title,
                            date=date)
    #print(p_list)

    return p_list
"""
if __name__ == '__main__':
    post_latest_data()

"""