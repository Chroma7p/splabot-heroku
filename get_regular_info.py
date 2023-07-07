from get_spla_info import get_spla_info
from datetime import datetime



def maketext():
    schedule=get_spla_info("regular","schedule")
    fest_schedule=get_spla_info("fest","schedule")
    if "fail" in schedule or "fail" in fest_schedule:
        return "情報の取得に失敗しました"
    text="## **レギュラーマッチ**\n"
    for i,day in enumerate(schedule[:3]):
        if i==0:
            text+="### **現在**\n"
        elif i==1:
            text+="### **つぎ**\n"
        elif i==2:
            text+="### **そのつぎ**\n"
        start:datetime=datetime.strptime(day["start_time"],"%Y-%m-%dT%H:%M:%S%z")
        end:datetime=datetime.strptime(day["end_time"],"%Y-%m-%dT%H:%M:%S%z")
        text+=f"{start.strftime('%Y-%m-%d %H:%M')}~{end.strftime('%Y-%m-%d %H:%M')}\n"
        if day["is_fest"]:
            text+="**フェス開催中!**\n"
            fesday=fest_schedule[i]
            stages=fesday["stages"]
            for stage in stages:
                text+=f"{stage['name']}\n"
            if fesday["is_tricolor"]:
                text+="***トリカラバトル***\n"
                text+=f"{fesday['tricolor_stage']['name']}\n"
        else:
            stages=day["stages"]
            for stage in stages:
                text+=f"{stage['name']}\n"
                
    return text

