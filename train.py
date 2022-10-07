from wsgiref import headers
import requests as r
from datetime import datetime as dt
from bs4 import BeautifulSoup as bs
import rich
from requests_html import AsyncHTMLSession
def main(data):
    look_up1=data[1]
    look_up2=data[2]
    if len(data)==4:
        TODAY=dt.today().strftime("%d-%m-%Y")+f"+{data[3]}:00:00"
    else:
        TODAY=dt.today().strftime("%d-%m-%Y+%H:00:00")
    print(look_up1,look_up2)
    _from=r.get(f"https://bilety.polregio.pl/ls?q={look_up1}&language=pl")
    FROM=_from.json()['stations'][0]
    _to=r.get(f"https://bilety.polregio.pl/ls?q={look_up2}&language=pl")
    TO=_to.json()['stations'][0]
    #print(TO)
    

    #query[brand_ids][]=4&query[brand_ids][]=3&query[brand_ids][]=20&query[brand_ids][]=48&query[only_direct]=false&query[only_purchasable]=false
    

    proposal=f"https://bilety.polregio.pl/pl/connections?v=c5a46ff58fc379dc0726a658891aab0675a1bfb8&query[date]={TODAY}&query[start_station]={FROM['name_slug']}&query[end_station]={TO['name_slug']}&query[via_stations]=&query[date_type]=departure&query[brand_ids][]=4&query[brand_ids][]=3&query[brand_ids][]=20&query[brand_ids][]=48&query[only_direct]=false&query[only_purchasable]=false"
    
    header={

"accept": "application/json; q=0.01",
"accept-encoding": "gzip, deflate, br",
    }
    resp=r.get(proposal,headers=header)
    text=f"```\n{FROM['localised_name']}->{TO['localised_name']} at {TODAY}\n"
    data=resp.json()
    #rich.print()
    rozklad=[]
    l=[0,0,0]
    for i in data['connections']:
        from_time=i['start_date'].split(":")
        from_hour=from_time[0]
        from_minuts=from_time[1]
        to_time=i['finish_date'].split(":")
        to_hour=to_time[0]
        to_minuts=to_time[1]
        for j in data['trains']:
            if j['id']==i['train_ids'][0]:
                train=j
        train_name=train['train_attributes'][0][2]+"->"+train['train_attributes'][0][3]+":"+str(train['train_name'])
        preparat=[train_name, f"{from_hour}:{from_minuts}",f"{to_hour}:{to_minuts}"]
        if len(preparat[0])>l[0]:l[0]=len(preparat[0])
        if len(preparat[1])>l[1]:l[1]=len(preparat[1])
        if len(preparat[2])>l[2]:l[2]=len(preparat[2])
        rozklad.append(preparat)
    text+='Poci'+" "*(l[0]-5)+" | "
    text+='Przy'+" "*(l[1]-5)+" | "
    text+='Doja'+" "*(l[2]-5)+"\n"
    text+="-"*(l[0]+l[1]+l[2]+6)+"\n"
    for i in rozklad:
        l0=i[0]+' '*(l[0]-len(i[0]))
        l1=i[1]+' '*(l[1]-len(i[1]))
        l2=i[2]+' '*(l[2]-len(i[2]))
        text+=" | ".join([l0,l1,l2])+"\n"
    return text+"\n```"

#query[brand_ids][]=4&query[brand_ids][]=3&query[brand_ids][]=20&query[brand_ids][]=48&query[only_direct]=false&query[only_purchasable]=false
#https://bilety.polregio.pl/pl/connections?v=c5a46ff58fc379dc0726a658891aab0675a1bfb8&query[date]=07-10-2022+19%3A00%3A00&query[start_station]=pruszcz-gdanski&query[end_station]=gdansk-glowny&query[via_stations]=&query[date_type]=departure&
#https://bilety.polregio.pl/pl/connections?v=c5a46ff58fc379dc0726a658891aab0675a1bfb8&query[date]=07-10-2022+19%3A00%3A00&query[start_station]=pruszcz-gdanski&query[end_station]=gdansk-glowny&query[via_stations]=&query[date_type]=departure&query[brand_ids][]=4&query[brand_ids][]=3&query[brand_ids][]=20&query[brand_ids][]=48&query[only_direct]=false&query[only_purchasable]=false

print(main([0,"pru","gdańsk_głowny","7"]))