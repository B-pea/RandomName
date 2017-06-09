# -*- coding: UTF-8 -*-
# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import random
import re

lastName = u"伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海" \
           u"山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信" \
           u"子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振" \
           u"壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦" \
           u"亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以" \
           u"建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘"

pattern =re.compile(u"[\u4e00-\u9fa5]")
result=re.findall(pattern,lastName)
# print result.group()
for w in result:
    print "孟德"+w
