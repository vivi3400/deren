#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# @Author  : jairodai

import subprocess
import logging
import os
import numpy as np


cur_dir = os.path.abspath(os.path.dirname(__file__))
wave_align_tool = cur_dir + '/WaveAlign.exe'
delay_wav = cur_dir + '/swb_ref_48kHz.wav'


def safe_cast(val, to_type, default=None):
    """安全转换
    """
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


def logging_config(log_dir):
    """
    日志配置, 可以参考http://www.cnblogs.com/dkblog/archive/2011/08/26/2155018.html
    :param log_dir: 存放日志的目录
    :return:
    """
    # 配置输出到文件
    # dst_log_dir = log_dir + '/media_test' + get_date('%Y%m%d%H%M%S') + '.log'
    # logging.basicConfig(level=logging.DEBUG,
    #                     format='[%(threadName)-10s] %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #                     datefmt='%Y%m%d %H:%M:%S',
    #                     filename=dst_log_dir)

    # 配置输出到控制台
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(threadName)-10s] %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


def get_delay(wav_file):
    """
    获取延时
    :param wav_file:
    :return:
    """
    ret = False
    delay = 0

    try:
        cmd = [wave_align_tool, delay_wav, wav_file]
        out = subprocess.check_output(cmd).strip()
        if 'Delay:' in out:
            tmp1 = out.split(',')
            tmp2 = tmp1[1].split(': ')
            delay = safe_cast(tmp2[1][:-3], float, 0.0)  # TODO, 使用正则
            ret = True
    except Exception as e:
        logging.error(e, exc_info=True)

    return ret, delay


def list_filename_with_ext(file_dir, file_ext):
    """
    根据后缀获取文件列表
    :param file_dir:
    :param file_ext:
    :return:
    """
    ret = []
    file_list = os.listdir(file_dir)
    for file_name in file_list:
        if os.path.splitext(file_name)[1] == file_ext:
            ret.append(file_dir + '/' + file_name)

    return ret


def get_delay_dir(waves_dir, result_name):

    avgg = []

    all_files = list_filename_with_ext(waves_dir, '.wav')
    with open(result_name + '.csv', 'w+') as f:
        f.write('wave_file,delay(ms)\n')
        for wave_file in all_files:
            ret, delay = get_delay(wave_file)
            if ret:
                # print wave_file + '\t' + str(delay)

                avgg.append(float(delay))

                # f.write(wave_file + ',' + str(delay) + '\n')
        if avgg:
            print 'mean',round(np.mean(avgg),3)
     
        avgg= []


# if __name__ == '__main__':
#     logging_config(cur_dir)
#     get_delay_dir(r'C:\Users\Administrator\Desktop\1\Channel 2', 'jairodai')
