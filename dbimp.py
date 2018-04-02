# coding:utf-8

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "InCT_Web_Site.settings")


django.setup()


def main():
    from ClassQuery.models import ClassImage
    ls = os.listdir('F:\\DjangoWork\\InCT_Web_Site\\collected_static\images\\xd')
    i = 1
    for item in ls:
        print(item)
        ls_a = os.listdir(os.path.join('F:\\DjangoWork\\InCT_Web_Site\\collected_static\\images\\xd', item))
        # print(ls_a)
        for image in ls_a:
            ClassImage.objects.create(classID=3, className='xd', sectionID=int(item.split('_')[1]), imageSeq=i, imagePath=image)
            i += 1
    # XjhInfo.objects.create(city='乌鲁木齐', school='新疆大学', company='中国水利水电第四工程局', location='校本部众创空间一楼路演厅', time='20180402110000')
    # XjhInfo.objects.create(city='乌鲁木齐', school='新疆大学', company='中建二局基础设施建设', location='南校区地矿学院三楼会议室', time='20180402153000')
    # XjhInfo.objects.create(city='乌鲁木齐', school='新疆大学', company='中国移动新疆公司', location='本部众创空间一楼路演大厅', time='20180403153000')
    # XjhInfo.objects.create(city='乌鲁木齐', school='新疆大学', company='克拉玛依市纪律检查委员会监察委员会', location='校本部新创青年众创空间一楼路演大厅', time='20180410103000')


if __name__ == '__main__':
    main()
    print('Done!')