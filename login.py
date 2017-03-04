
from config import session,setting_url,login_url,params,headers
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from PIL import Image
def login():

    html_content = session.get(login_url,headers=headers).content
    soup = BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
    captcha_node = soup.find('img',id='captcha_image')
    if captcha_node is not None:
        img_url = captcha_node['src']
        image = requests.get(img_url)
        path = "tmp_file\captcha.jpg"
        #try:
        with open(path, 'wb') as f:
            for chunk in image:
                f.write(chunk)
        Image.open(path).show()
        params['captcha-solution'] = input("请输入图片中的验证码:\n")
        params['captcha-id'] = soup.select('input[name="captcha-id"]')[0]["value"]
        params['source'] = "book"
        params['redir'] = "https://book.douban.com/"
        params['login'] = "登录"
        #except:b
        #    print("读取验证码失败,请稍后再试")
    post_content = session.post(login_url,params=params,headers=headers)
    s = session.get(setting_url)
    return s.status_code

if __name__ == '__main__':    print(login())
