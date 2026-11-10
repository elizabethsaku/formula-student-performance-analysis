import pathlib; ROOT=pathlib.Path(__file__).resolve().parent.parent
import re, pandas as pd
rows=[]
for line in open(ROOT/'data/fsg26_raw_transcribed.txt'):
    line=line.strip()
    m=re.match(r'^(\d+) (\d+) ([A-Z]{2}) (.+?) (\d+\.\d\d) ',line)
    pl,car,cc,name,first=m.groups()
    rest=line[m.start(5):]
    dec=re.findall(r'\d+\.\d\d',rest)
    sc=[float(x) for x in dec]
    pen=sc[10] if len(sc)==12 else 0.0
    tot=sc[-1]
    rows.append(dict(rank=int(pl),car=int(car),country=cc,team=name,cost=sc[0],bp=sc[1],design=sc[2],accel=sc[3],dv_accel=sc[4],skidpad=sc[5],dv_skid=sc[6],autox=sc[7],endurance=sc[8],efficiency=sc[9],penalty=pen,total=tot))
df=pd.DataFrame(rows)
cols=['cost','bp','design','accel','dv_accel','skidpad','dv_skid','autox','endurance','efficiency']
df['calc']=df[cols].sum(axis=1)-df.penalty
print(len(df), (df.calc-df.total).abs().max())
print(df[(df.calc-df.total).abs()>0.05][['team','calc','total']])
df.to_csv(ROOT/'data/fsg26_results.csv',index=False)
