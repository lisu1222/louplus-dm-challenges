"""
to extract user info from webpage
url format: https//www.shiyanlou.com/users/ID/

Challenge:
    * save as '~/Code/shiyanlou_user.py'
    * if ID does not exist, return None
    * use the following Python path to run test: /home/shiyanlou/anaconda3/bin/python 
    * return values format:
        user_name: str, example: huhuhang
        user_level: int, example: 179
        join_date: str, example: 2016-06-09
"""

import requests
from xhtml import html

def user_info(user_id):
    url = "https://www.shiyanlou.com/users/{}".format(user_Id)
    content = requests.get(url)
    
    if content.status_code == 200:
        tree = html.fromstring(content.text)
        user_name = tree.xpath('//div[@class = "user-meta"]/span/text()')[0].strip()
        user_level = tree.xpath('//div[@class = "user-meta"]/span/text')[1].strip()[1:]
        join_date = tree.xpath('//span[@class = "user-join-date"]/text()')[0].strip()[:10]
        return user_name, int(user_level), join_date
        
    else:
        user_name, user_level, join_date = (None, None, None)
        return user_name, user_level, join_date
        
user_info("1181117")
user_info("1234567890")