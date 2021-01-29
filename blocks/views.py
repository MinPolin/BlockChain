from django.shortcuts import render
import requests
import json
from django.core.paginator import Paginator

import datetime
from .models import Block

# Create your views here.

start_day = datetime.date(2020, 2, 13)
today = datetime.date(2021, 1, 29)



def blocks(req):
    # Вывод всех блоков
    block_items = Block.objects.all()
    first_height = block_items[0].height
    update_data(first_height)

    paginator = Paginator(block_items, 50)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(req, 'blocks/blocks.html', locals())


def get_all_data():
    # Получение данных о всех блоках
    cur_day = start_day
    while cur_day <= today:
        url = 'https://bcschain.info/api/blocks?date=' + str(cur_day)
        get_and_save(url)
        cur_day += datetime.timedelta(days=1)

def update_data(first_height):
    # Получение данных о последних блоках
    url = 'https://bcschain.info/api/recent-blocks?count=1'
    r = requests.get(url)
    last_height = json.loads(r.text)[0]['height']
    if last_height>first_height:
        url = 'https://bcschain.info/api/recent-blocks?count='+str(last_height-first_height)
        get_and_save(url)


def get_and_save(url):
    # извлечение и занесение в БД

    r = requests.get(url)
    output = json.loads(r.text)
    for item in output:
        time_t = datetime.datetime.fromtimestamp(item['timestamp'])
        new = Block(height=item['height'], hash=item['hash'], transaction_count=item['transactionCount'],
                    date=time_t, miner=item['miner'])
        new.save()




def one_block(req, height):
    # Вывод данных об одном блоке
    block = Block.objects.get(height=height)
    return render(req, 'blocks/one_block.html', locals())
