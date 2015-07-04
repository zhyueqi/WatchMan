#coding:utf-8
import requests

AP_host = '172.30.16.53'


def status():
    res = requests.get('http://'+AP_host+'/cgi-bin/rad_user_info')
    print res.status_code
    print res.content

def login():
    postData={
        'action':'login',
        'ac_id':10,#10:无需mac
        'wbaredirect':'',
        'username':'148700',
        'password':'153410',
        'user_ip':'',
        'mac':''
    }
    res = requests.post('http://'+AP_host+'/cgi-bin/srun_portal',data=postData)
    print res.status_code,res.content

if __name__ == '__main__':
    status()
    login()

