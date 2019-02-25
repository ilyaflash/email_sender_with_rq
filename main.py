# -*- coding: utf-8 -*-
#type in terminal: "supervisord -n:

from rq import Queue
from redis import Redis
from json import loads
from task import send_mail_from_app4hiiigmailcom

#Save confs fun
#from json import dump
#def confs_to_json(path='mails.json'):
#    confs = [{'to_addrs': ['ilyaflash@list.ru'], 'msg': 'Моё тестовое сообщение 1', 'subject': 'Моя тема 1'},
#             {'to_addrs': ['ilyaflash@list.ru'], 'msg': 'Моё тестовое сообщение 2', 'subject': 'Моя тема 2'},
#             {'to_addrs': ['ilyaflash@list.ru'], 'msg': 'Моё тестовое сообщение 3', 'subject': 'Моя тема 3'}]
#    with open(path, 'w') as file:
#        dump(confs, file, ensure_ascii=False)
#confs_to_json()

#Load confs fun
def get_json_confs(path='mails.json'):
    with open(path, 'r') as file:
        return loads(file.read(), encoding='utf-8')

queue = Queue(name='qname', connection=Redis(), is_async=True)                     #create que
confs = get_json_confs(path='mails.json')                                          #load confs
jlist = [queue.enqueue(send_mail_from_app4hiiigmailcom, i) for i in confs]         #to que