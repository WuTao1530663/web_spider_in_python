from requests import Session
import os

session = Session()
params = {"form_email":os.environ.get("DBUSER"),"form_password":os.environ.get("DBPASSWD")}
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36 "}
setting_url = 'https://www.douban.com/settings/'
login_url= 'https://www.douban.com/accounts/login?source=main'