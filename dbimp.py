# coding:utf-8

import os
import django
import urllib
import re
import pypinyin
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "InCT_Web_Site.settings")



django.setup()


def main():

    i = 0
    while 1:
        i += 1
        url_str = 'https://xjh.haitou.cc/nj/' + 'page-' + str(i)
        print(i)
        if getDetailInfo(getHtmlContent(url_str), 'page_' + str(i)):
            break


    # XjhInfo.objects.create(city='乌鲁木齐', school='新疆大学', company='中国水利水电第四工程局', location='校本部众创空间一楼路演厅', time='20180402110000')
    # XjhInfo.objects.create(city='乌鲁木齐', school='新疆大学', company='中建二局基础设施建设', location='南校区地矿学院三楼会议室', time='20180402153000')
    # XjhInfo.objects.create(city='乌鲁木齐', school='新疆大学', company='中国移动新疆公司', location='本部众创空间一楼路演大厅', time='20180403153000')
    # XjhInfo.objects.create(city='乌鲁木齐', school='新疆大学', company='克拉玛依市纪律检查委员会监察委员会', location='校本部新创青年众创空间一楼路演大厅', time='20180410103000')



def getHtmlContent(url):
    page = urllib.request.urlopen(url)
    return bytes.decode(page.read(), encoding='utf-8')


def getDetailInfo(page, page_num):
    from ClassQuery.models import XjhInfo
    break_flag = False
    res_tr = r'<td class="cxxt-title">(.*?)</td>'
    m_tr = re.findall(res_tr, page, re.S | re.M)
    res_tr = r'<td class="text-left cxxt-holdtime">(.*?)</td>'
    m_tr_time = re.findall(res_tr, page, re.S | re.M)
    if len(m_tr) == 0:
        break_flag = True
        return break_flag
    for idx in range(len(m_tr)):
        res_tr = r'title="(.*?)"'
        tmp_info = re.findall(res_tr, m_tr[idx], re.S|re.M)
        res_tr = r'<span class="hold-ymd">(.*.?)</span>'
        time = re.findall(res_tr, m_tr_time[idx], re.S|re.M)
        if tmp_info[0] == '该信息已被官方认证':
            continue
        for item in tmp_info:
            tmp_name = ''
            res = pypinyin.lazy_pinyin(item.split('\n')[1].replace('学校：', ''))
            for yigezi in res:
                tmp_name += yigezi[:1]
            XjhInfo.objects.create(city='江苏', city_id='js', school=item.split('\n')[1].replace('学校：', ''), company=item.split('\n')[0], location=item.split('\n')[2].replace('地点：', ''), time=time[0].split('</span>')[0].replace('-','').replace(' ', '').replace(':', ''), school_engname=tmp_name)

    return break_flag

if __name__ == '__main__':
    main()
    print('Done!')