# coding:utf-8
import requests
import logging
from logging.handlers import RotatingFileHandler

log_format = logging.Formatter('%(asctime)s% - %(levelname)s% - %(message)s%')
log_file = 'conn_log.log'
log_handler = RotatingFileHandler(
    log_file, mode='a', maxBytes=1 * 1024 * 1024, backupCount=1, encoding='utf-8', delay=0)
log_handler.setFormatter(log_format)
log_handler.setLevel(logging.INFO)
logger = logging.getLogger(log_file)
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

AP_host = 'http://172.30.16.53'


def isconn():
    res = requests.get(AP_host + '/cgi-bin/rad_user_info')
    code = res.status_code
    content = res.content
    isLogin =  True
    if code is 200:
        if  content != 'not_online':
            #logger.info('online')
            print 'online'
        else:
            #logger.info('not online')
            print 'not online'
            isLogin = False

    else:
        #logger.warn('server error')
        isLogin = False
    return isLogin

def login():
    #logger.info('正在拨号...')
    print 'try login '
    postData = {
        'action': 'login',
        'ac_id': 10,  # 10:request without mac
        'wbaredirect': '',
        'username': '148700',
        'password': '153410',
        'user_ip': '',
        'mac': ''
    }
    res = requests.post(
        AP_host + '/cgi-bin/srun_portal', data=postData)

if __name__ == '__main__':
    import time
    while True:
        time.sleep(5)
        if isconn():
            continue
        login()
