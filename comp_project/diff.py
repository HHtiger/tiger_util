#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil


class CompObj:
    path1 = ''
    path2 = ''
    package_url = ''
    log_filename = ''


def comp_and_move(compObj):
    log = open('%s.txt' % compObj.log_filename, 'w+', -1, 'utf-8')
    log.writelines('【%s】 changelist:\n' % compObj.package_url)
    dl_dir = compObj.path1
    sy_dir = compObj.path2

    # use to save filename and filepath
    dict_dl = {}
    dict_sy = {}

    # use to save dirname and dirpath
    dict_dir_dl = {}
    dict_dir_sy = {}

    for fpathe, dirs, fs in os.walk(sy_dir):
        for d in dirs:
            dict_dir_sy[d] = fpathe
        for f in fs:
            dict_sy[f] = fpathe

    for fpathe, dirs, fs in os.walk(dl_dir):
        for d in dirs:
            dict_dir_dl[d] = fpathe
        for f in fs:
            dict_dl[f] = fpathe

    # get all dir list
    dir_key_res = set(list(dict_dir_sy.keys()) + list(dict_dir_dl.keys()))

    # 通过排序防止文件新建顺序错误
    lose_dir_res = []

    # build lose dir
    for key in dir_key_res:
        if key not in dict_dir_sy.keys():
            lose_dir = os.path.join(dict_dir_dl[key], key).replace(dl_dir, sy_dir)
            print('沈阳新建缺失文件夹' + lose_dir)
            lose_dir_res.append(lose_dir)

        if key not in dict_dir_dl.keys():
            lose_dir = os.path.join(dict_dir_sy[key], key).replace(sy_dir, dl_dir)
            print('大连新建缺失文件夹' + lose_dir)
            lose_dir_res.append(lose_dir)

    lose_dir_res.sort(key=lambda x: len(x))
    for i in lose_dir_res:
        os.mkdir(i)

    # get all file list
    key_res = set(list(dict_dl.keys()) + list(dict_sy.keys()))
    dl_lose = []
    sy_lose = []
    bose_have = []

    for key in key_res:
        if key not in dict_dl.keys():
            dl_lose.append(key)
            source_dir = os.path.join(dict_sy[key], key)
            target_dir = os.path.join(str(dict_sy[key]).replace(sy_dir, dl_dir), key)
            shutil.copy(source_dir, target_dir)
            print('大连缺失' + key + '拷贝【', end='')
            print(source_dir, end='')
            print('】到【', end='')
            print(target_dir, end='')
            print('】')
        elif key not in dict_sy.keys():
            sy_lose.append(key)
            source_dir = os.path.join(dict_dl[key], key)
            target_dir = os.path.join(str(dict_dl[key]).replace(dl_dir, sy_dir), key)
            shutil.copy(source_dir, target_dir)
            print('沈阳缺失' + key + '拷贝【', end='')
            print(source_dir, end='')
            print('】到【', end='')
            print(target_dir, end='')
            print('】')
        else:
            bose_have.append(key)
            print('相同文件' + key)

    log.writelines('*\n')
    log.writelines('*\n')
    log.writelines('*大连缺失文件(共%d个):\n' % len(dl_lose))
    log.writelines('*\n')
    log.writelines('*\n')
    for i in dl_lose:
        log.writelines(i + '\n')

    log.writelines('*\n')
    log.writelines('*\n')
    log.writelines('*沈阳缺失文件(共%d个)\n' % len(sy_lose))
    log.writelines('*\n')
    log.writelines('*\n')
    for i in sy_lose:
        log.writelines(i + '\n')

    log.writelines('*\n')
    log.writelines('*\n')
    log.writelines('*相同文件(共%d个)\n' % len(bose_have))
    log.writelines('*\n')
    log.writelines('*\n')
    for i in bose_have:
        log.writelines(i + '\n')

    log.writelines('*\n')
    log.writelines('*\n')
    log.writelines('*\n')
    log.writelines('all done!\n')
    log.writelines('-------------------------------------------\n')

    log.close()


if __name__ == '__main__':
    # c1 = CompObj()
    # c1.path1 = 'E:\\tiger\\tiegrWs\\syrk_dalian\\syrk\\sydw\\com\\founder\\sydw'
    # c1.path2 = 'E:\\tiger\\tiegrWs\\syrk_sy\\syrk\\sydw\\com\\founder\\sydw'
    # c1.package_url = 'com.founder.sydw'
    # c1.log_filename = 'java类'
    # comp_and_move(c1)
    #
    # c2 = CompObj()
    # c2.path1 = 'E:\\tiger\\tiegrWs\\syrk_dalian\\syrk\\WebRoot\\WEB-INF\\pages\\sydw'
    # c2.path2 = 'E:\\tiger\\tiegrWs\\syrk_sy\\syrk\\WebRoot\\WEB-INF\\pages\\sydw'
    # c2.package_url = 'WebRoot\\WEB-INF\\pages'
    # c2.log_filename = '页面文件'
    # comp_and_move(c2)
    #
    # c3 = CompObj()
    # c3.path1 = 'E:\\tiger\\tiegrWs\\syrk_dalian\\syrk\\WebRoot\\js\\sydw'
    # c3.path2 = 'E:\\tiger\\tiegrWs\\syrk_sy\\syrk\\WebRoot\\js\\sydw'
    # c3.package_url = 'WebRoot\\js\\sydw'
    # c3.log_filename = 'js文件'
    # comp_and_move(c3)

    c = CompObj()
    c.path2 = 'test\\a'
    c.path1 = 'test\\b'
    c.log_filename = 'test'
    c.package_url = 'NONE'
    comp_and_move(c)
