#! /usr/bin/env python
__author__ = 'Tser'
__email__ = '807447312@qq.com'
__project__ = 'xiaobaiauto2'
__script__ = 'xiaobaiauto2Downloader.py'
__create_time__ = '2021/6/6 0:03'

__version__ = '.'.join(map(str, (0, 1)))

from threading import Thread, current_thread
from urllib.request import urlopen, Request
from urllib.parse import urlparse
import time
import ssl
from os.path import isfile
from os import remove

ssl._create_default_https_context = ssl._create_unverified_context

start_time = time.time()
cache = 1000 * 1024  # 缓存
curr_size = 0
step = 0     # 网速
finish = 0

def download(url, start, end):
    global curr_size
    global finish
    start_end_list = [n for n in range(start, end, cache)]
    temp_name = current_thread().name
    with open(temp_name, 'w+b') as fp:
        for i in range(len(start_end_list)):
            if i < len(start_end_list) - 1:
                res = urlopen(
                    Request(url, headers={"Range": "bytes=%d-%d" % (start_end_list[i], start_end_list[i + 1] - 1)}))
                fp.write(res.read(cache))
                curr_size += cache
            else:
                res = urlopen(Request(url, headers={"Range": "bytes=%d-%d" % (start_end_list[i], end)}))
                fp.write(res.read(end - start_end_list[i] + 1))
                curr_size += end - start_end_list[i] + 1
    finish += 1

def download_thread(url, filename='', t=4):
    global file_size
    file_size = int(urlopen(Request(url)).headers['content-length'])
    STEP = file_size // t if file_size % t == 0 else file_size // t + file_size % t
    size_list = [s for s in range(0, file_size, STEP)]
    pt = Thread(target=download_process)
    pt.setDaemon(True)
    pt.start()
    st = Thread(target=download_step)
    st.setDaemon(True)
    st.start()
    work_threads = []
    for i in range(t):
        if i >= t - 1:
            work_threads.append(Thread(target=download, args=(url, size_list[i], file_size)))
        else:
            work_threads.append(Thread(target=download, args=(url, size_list[i], size_list[i + 1] - 1)))
    for i, th in enumerate(work_threads):
        th.setName(f'{i}.xbdownload')
        th.setDaemon(True)
        th.start()
    for th in work_threads:
        th.join()
    if finish == t:
        if filename == '':
            filename = urlparse(url).path.split('/')[-1] if '' != urlparse(url).path.split('/')[-1] else 'index'
        with open(filename, 'w+b') as fw:
            for i in range(t):
                if isfile(f'{i}.xbdownload'):
                    with open(f'{i}.xbdownload', 'r+b') as fr:
                        fw.write(fr.read())
                        fr.close()
                    remove(f'{i}.xbdownload')
                else:
                    print('文件写入失败')

def download_step():
    global step
    while curr_size <= file_size:
        one_size = curr_size
        time.sleep(1)
        two_size = curr_size
        step = two_size - one_size

def download_process():
    while curr_size <= file_size:
        process = curr_size * 50 // file_size
        curr_per = curr_size * 100 / file_size
        use_time = time.time() - start_time
        print(end='\r')
        if step <= 1024:
            print(
                f'文件下载进度：{"▋" * process} {curr_per:.2f}%  {step}B/S  {use_time:.2f}S',
                end='')
        elif 1024 < step <= 1048576:
            print(
                f'文件下载进度：{"▋" * process} {curr_per:.2f}%  {step / 1024:.2f}KB/S  {use_time:.2f}S',
                end='')
        elif 1048576 < step <= 1073741824:
            print(
                f'文件下载进度：{"▋" * process} {curr_per:.2f}%  {step / 1024 / 1024:.2f}MB/S  {use_time:.2f}S',
                end='')
        else:
            print(
                f'文件下载进度：{"▋" * process} {curr_per:.2f}%  {step / 1024 / 1024 / 1024:.2f}GB/S  {use_time:.2f}S',
                end='')
        time.sleep(0.1)