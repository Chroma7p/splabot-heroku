from cogs.util.get_spla_info import get_spla_info
from datetime import datetime


def maketext(is_open=True):
    if is_open:
        schedule = get_spla_info("bankara-open", "schedule")
        text = "## **バンカラオープン**\n"
    else:
        schedule = get_spla_info("bankara-challenge", "schedule")
        text = "## **バンカラチャレンジ**\n"
    if "fail" in schedule:
        return "情報の取得に失敗しました"
    print(schedule)
    if not schedule:
        try:
            fest_schedule = get_spla_info("regular", "schedule")
            fs = fest_schedule[0]
            if not fs["is_fest"]:
                raise "フェス期間じゃないけどバンカラが取得できてなさそう"
            text += f"**フェス期間だからないよ！**\n"

        except Exception as e:
            return f"想定外のエラーみたいだね\n以下のメッセージを開発者に教えてね\n```{e.with_traceback()}```"

        return text+"**もしフェス期間じゃない場合は開発者に教えてね**"
    for i, day in enumerate(schedule[:3]):
        if i == 0:
            text += "### **現在**\n"
        elif i == 1:
            text += "### **つぎ**\n"
        elif i == 2:
            text += "### **そのつぎ**\n"
        if not day["is_fest"]:
            rule = day["rule"]
            text += f"__***{rule['name']}***__\n"
        start: datetime = datetime.strptime(
            day["start_time"], "%Y-%m-%dT%H:%M:%S%z")
        end: datetime = datetime.strptime(
            day["end_time"], "%Y-%m-%dT%H:%M:%S%z")
        text += f"{start.strftime('%Y-%m-%d %H:%M')}~{end.strftime('%Y-%m-%d %H:%M')}\n"
        if day["is_fest"]:
            text += "フェス期間だからないよ！\n"
        else:

            stages = day["stages"]
            for stage in stages:
                text += f"{stage['name']}\n"

    return text
