# -*- coding: utf-8 -*-
#type in terminal: "supervisord -n:

from rq import Queue
from redis import Redis
from task import send_mail_from_app4hiiigmailcom


#get conf
conf_sends = [{'to_addrs': ['ilyaflash@list.ru'], 'msg': 'my test message 1', 'subject': 'my topic 1'},
              {'to_addrs': ['ilyaflash@list.ru'], 'msg': 'my test message 2', 'subject': 'my topic 2'},
              {'to_addrs': ['ilyaflash@list.ru'], 'msg': 'my test message 3', 'subject': 'my topic 3'}]

#create que
queue = Queue(name='qname', connection=Redis(), is_async=True)

#to que
jlist = [queue.enqueue(send_mail_from_app4hiiigmailcom, i) for i in conf_sends]
