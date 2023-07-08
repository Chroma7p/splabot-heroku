from get_spla_info import get_spla_info
from datetime import datetime

def makenotif():
    schedule = get_spla_info("event", "schedule")
    event=schedule[0]
    next_event=schedule[1]
    start:datetime=datetime.strptime(event["start_time"],"%Y-%m-%dT%H:%M:%S%z")
    end:datetime=datetime.strptime(event["end_time"],"%Y-%m-%dT%H:%M:%S%z")
    next_start:datetime=datetime.strptime(next_event["start_time"],"%Y-%m-%dT%H:%M:%S%z")
    text=f"イベントマッチが始まりました\n{start.strftime('%Y-%m-%d %H:%M')}~{end.strftime('%Y-%m-%d %H:%M')}\n"
    text+=f"__***{event['rule']['name']}***__\n"
    for stage in event["stages"]:
        text+=f"{stage['name']}\n"
    return text,next_start




def get_next():
    schedule = get_spla_info("event", "schedule")
    start:datetime=datetime.strptime(schedule[0]["start_time"],"%Y-%m-%dT%H:%M:%S%z")
    return start

def maketext():
    schedule = get_spla_info("event", "schedule")
    events=dict()
    for day in schedule:
        event_name=day["event"]["name"]
        if event_name not in events:
            events[event_name]=dict()
            events[event_name]["desc"]=day["event"]["desc"]
            events[event_name]["time"]=list()
            events[event_name]["rule"]=day["rule"]["name"]
            events[event_name]["stage"]=list()
            for stage in day["stages"]:
                events[event_name]["stage"].append(stage["name"])
        start:datetime=datetime.strptime(day["start_time"],"%Y-%m-%dT%H:%M:%S%z")
        end:datetime=datetime.strptime(day["end_time"],"%Y-%m-%dT%H:%M:%S%z")
        events[event_name]["time"].append((start,end))
    text="## **イベントマッチ**\n"
    for event , detail in events.items():
        text+=f"## **{event}**\n"
        text+=f"{detail['desc']}\n"
        text+=f"__***{detail['rule']}***__\n"
        for stage in detail["stage"]:
            text+=f"{stage}\n"
        for i,(start,end) in enumerate(detail["time"]):
            text+=f":{['one','two','three'][i]}:{start.strftime('%Y-%m-%d %H:%M')}~{end.strftime('%Y-%m-%d %H:%M')}\n"
        
    return text
