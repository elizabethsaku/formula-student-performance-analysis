import pathlib
import pandas as pd, numpy as np
from scipy.stats import spearmanr
df=pd.read_csv(pathlib.Path(__file__).resolve().parent.parent/'data/fsg26_results.csv')
df['static']=df.cost+df.bp+df.design
df['dynamic']=df.accel+df.skidpad+df.autox+df.endurance+df.efficiency+df.dv_accel+df.dv_skid
df['finished_endu']=df.endurance>0
df['ran_dyn']=df.autox>0
df['top10']=df['rank']<=10

print("== Q1: Reliability: endurance finishers vs not ==")
g=df.groupby('finished_endu').total.agg(['count','median','mean','max'])
print(g.round(1))
print("Top 10 endurance finishers:",df[df.top10].finished_endu.sum(),"/10")
print("Top 20 endurance finishers:",df[df['rank']<=20].finished_endu.sum(),"/20")

print("\n== Q2: Static vs dynamic ==")
for lab,sub in [('Top 10',df[df.top10]),('Rank 11-30',df[(df['rank']>10)&(df['rank']<=30)]),('Rank 31-80',df[df['rank']>30])]:
    print(lab, 'static mean',round(sub.static.mean(),1),'dynamic mean',round(sub.dynamic.mean(),1),'penalty mean',round(sub.penalty.mean(),1))
print("Spearman with final rank (higher score->better rank):")
for c in ['cost','bp','design','accel','skidpad','autox','endurance','efficiency','static','dynamic','penalty']:
    r,p=spearmanr(df[c],df.total)
    print(f"  {c:11s} rho={r:.2f}")

print("\n== Share of points: how much variance of total do components explain (R2 of simple linear fit) ==")
for c in ['static','dynamic','endurance','design','autox']:
    r=np.corrcoef(df[c],df.total)[0,1]
    print(f"  {c:10s} R2={r*r:.2f}")

print("\n== Q3: Does a good static score get you a good rank? ==")
s_top=df.nlargest(20,'static')
print("Of top-20 static teams, rank spread: median final rank",s_top['rank'].median(), "| how many in final top 10:",(s_top['rank']<=10).sum())
d_top=df.nlargest(20,'dynamic')
print("Of top-20 dynamic teams, median final rank",d_top['rank'].median(),"| in final top 10:",(d_top['rank']<=10).sum())

print("\n== Penalties ==")
print("Teams with penalties:",(df.penalty>0).sum(),"of",len(df),"; top10 with penalties:",(df[df.top10].penalty>0).sum())

print("\n== Schanzer Racing (Ingolstadt UAS, car 134) ==")
s=df[df.team.str.contains('Ingolstadt')].iloc[0]
print(s[['rank','cost','bp','design','accel','skidpad','autox','endurance','efficiency','penalty','total']].to_string())
cols=['cost','bp','design','accel','skidpad','autox','endurance','efficiency']
med_finish=df[df.finished_endu][cols].median()
mid=df[(df['rank']>=20)&(df['rank']<=30)][cols].median()
top10=df[df.top10][cols].median()
cmp=pd.DataFrame({'Schanzer':s[cols],'median_endu_finishers':med_finish,'median_rank20-30':mid,'median_top10':top10})
cmp['gap_to_rank20-30']=cmp['median_rank20-30']-cmp.Schanzer
print(cmp.round(1))
print("Total gap to rank 20-30 median profile:",round(cmp['gap_to_rank20-30'].sum(),1))
# scenario: what if Schanzer matched median on single categories (leaving others), resulting rank
def rank_with(delta):
    t=df.total.copy()
    idx=df.index[df.team.str.contains('Ingolstadt')][0]
    t.loc[idx]+=delta
    return int((t>t.loc[idx]).sum()+1)
print("\nScenarios (rank if Schanzer improved ONE area to rank 20-30 median):")
for c in cols:
    gap=max(0,cmp.loc[c,'median_rank20-30']-s[c])
    print(f"  {c:10s} +{gap:5.1f} pts -> rank {rank_with(gap)}")
print("  removing penalty (+20) -> rank",rank_with(20))
# endurance finisher scenario
print("  finishing endurance at median finisher level (+%.1f endu/+%.1f eff) already finished -> compare:"%(0,0))
print("  Schanzer endurance rank 20 but efficiency only",s.efficiency,"vs median finisher",med_finish['efficiency'])
