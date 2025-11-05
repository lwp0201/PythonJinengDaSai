poem = '''剑外忽传收蓟北，初闻涕泪满衣裳。
却看妻子愁何在，漫卷诗书喜欲狂。
白日放歌须纵酒，青春作伴好还乡。
即从巴峡穿巫峡，便下襄阳向洛阳。'''

placeName1 = poem[0:2]
placeName2 = poem[5:7]
# placeName3=poem[53:55]
# placeName4=poem[56:58]
# placeName5=poem[61:63]
# placeName6=poem[64:66]

placeName3 = poem[-14:-12]
placeName4 = poem[-11:-9]
placeName5 = poem[-6:-4]
placeName6 = poem[-3:-1]
print("杜甫的《闻官军收河南河北》中，一共包含了6个地名，分别是：{}、{}、{}、{}、{}、{}".format(placeName1, placeName2, placeName3,placeName4, placeName5,placeName6))