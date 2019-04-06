# -*- coding:utf-8 -*-
import requests
from lxml import etree
from bs4 import BeautifulSoup
import hashlib
from selenium import webdriver
import hashlib, binascii
import os
import subprocess
import requests
import re
import time



def saveHtml(file_name, file_content):
	with open(file_name.replace('/', '_') + ".html", "wb") as f:
		f.write(file_content)

class Login(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Host': 'acm.hnucm.edu.cn'
        }
        self.hheaders = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
        self.post_url = 'http://acm.hnucm.edu.cn/JudgeOnline/login.php'
        self.csrf_url = 'http://acm.hnucm.edu.cn/JudgeOnline/csrf.php'
        self.session = requests.Session()

    def token(self):
            response = self.session.get(self.csrf_url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'lxml')
            attrs = soup.input.attrs
            token = attrs['value']
            print(token)
            return token

    def login(self, userid, pwd):
            post_data = {
                'user_id': userid,
                'password': pwd,
                'submit': '',
                'csrf': self.token()
            }
            response = self.session.post(self.post_url, data=post_data,headers=self.headers)

            if response.status_code==200:
                print('OK')
            else:
                print('Not OK')
            oo = self.session.get('http://acm.hnucm.edu.cn/JudgeOnline/showsource.php?id=33805',headers=self.headers)
            saveHtml('abc',oo.content)


if __name__ =="__main__":
    login = Login()
    import hashlib
    m = hashlib.md5()
    s = 'ur_password_here'
    b = s.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    print(str_md5)
    login.login(userid='201701020141',pwd=str_md5)
    # browser = webdriver.Chrome()



