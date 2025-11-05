strUp="一支粉笔两袖清风，三尺讲台四季晴雨，加上五脏六腑七嘴八舌九思十想，教必有方，滴滴汗水诚滋桃李芳天下"
strDown="十卷诗书九章勾股，八索文思七纬地理，连同6艺五经四书三字两雅一心，诲而不倦，点点心血勤育英才泽神州"
chrCount=len(strUp)                 #上联的字符数
wordPos=strUp.find("七嘴八舌")        #七嘴八舌出现的位置
strDown=strDown.replace('6','六')      #把数字6替换成为中文六
print("该对联上下联分别有{}个字符，该对联使用了很多数字及关于数字的成语，其中七嘴八舌出现在上联的第{}个字符。".format(chrCount,wordPos))        #按照格式输出
print("上联："+strUp)
print("下联："+strDown)