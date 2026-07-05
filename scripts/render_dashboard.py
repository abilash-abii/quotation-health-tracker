"""Synthetic reconstruction of the Quotation Health Tracker dashboard (ERPNext Insights
style) — fake data only. Mirrors the real layout for safe portfolio use."""
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.gridspec as gridspec
np.random.seed(31)

C_PRIMARY="#4361ee"; C_TEAL="#4cc9f0"; C_PURPLE="#7209b7"; C_AMBER="#f8961e"
C_RED="#e63946"; C_GREEN="#2a9d8f"; C_PINK="#ef476f"
INK="#1d2433"; MUTED="#6b7280"; CARD="#ffffff"; BG="#f4f6fb"

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.edgecolor":"#e5e7eb",
    "axes.linewidth":0.8,"text.color":INK,"axes.labelcolor":INK,"xtick.color":MUTED,"ytick.color":MUTED})

fig=plt.figure(figsize=(16,11),dpi=125); fig.patch.set_facecolor(BG)
gs=gridspec.GridSpec(4,6,figure=fig,height_ratios=[0.5,0.8,1.15,1.15],hspace=0.62,wspace=0.6,
    left=0.03,right=0.97,top=0.95,bottom=0.07)

def card(ax,title,value,sub,accent):
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((0.02,0.08),0.96,0.84,boxstyle="round,pad=0.02,rounding_size=0.06",lw=0,fc=CARD,mutation_aspect=0.5))
    ax.add_patch(FancyBboxPatch((0.02,0.08),0.05,0.84,boxstyle="round,pad=0,rounding_size=0.02",lw=0,fc=accent))
    ax.text(0.12,0.64,value,fontsize=17,fontweight="bold",va="center",color=INK)
    ax.text(0.12,0.35,title,fontsize=9.6,va="center",color=INK,fontweight="600")
    ax.text(0.12,0.19,sub,fontsize=8.2,va="center",color=MUTED); ax.set_xlim(0,1); ax.set_ylim(0,1)

hax=fig.add_subplot(gs[0,:]); hax.axis("off")
hax.text(0,0.6,"Quotation Health Tracker",fontsize=19,fontweight="bold",color=INK,va="center")
hax.text(0,0.12,"Live sales-pipeline follow-up cockpit  ·  ERPNext Insights  (synthetic sample — no company data)",
    fontsize=10,color=MUTED,va="center")
hax.text(1,0.5,"Abilash K S",fontsize=11,color=C_PRIMARY,fontweight="bold",ha="right",va="center")
hax.set_xlim(0,1); hax.set_ylim(0,1)

kpis=[("Total Quotation","749","₹20.7 Cr value",C_PRIMARY),
      ("Ordered","391","₹5.7 Cr won",C_GREEN),
      ("Open","117","₹4.1 Cr at risk",C_AMBER),
      ("Expired","47","₹1.5 Cr lapsed",C_PURPLE),
      ("High-Value Lost","194","priority recovery",C_RED),
      ("Lost Value","₹9.5 Cr","total lost",C_PINK)]
for i,(t,v,s,a) in enumerate(kpis): card(fig.add_subplot(gs[1,i]),t,v,s,a)

# Territory/rep-wise status (stacked)
ax1=fig.add_subplot(gs[2,0:4])
reps=["Rep A","Rep B","Rep C","Rep D","Rep E","Rep F","Rep G","Rep H"]
ordered=[120,49,30,24,11,20,9,12]; opn=[41,12,4,12,11,9,8,12]; lost=[23,65,50,49,27,18,15,8]; expired=[16,0,2,4,0,0,0,0]
x=np.arange(len(reps)); 
ax1.bar(x,ordered,0.6,label="Ordered",color=C_RED)
ax1.bar(x,lost,0.6,bottom=ordered,label="Lost",color=C_PINK)
ax1.bar(x,opn,0.6,bottom=np.array(ordered)+np.array(lost),label="Open",color=C_GREEN)
ax1.bar(x,expired,0.6,bottom=np.array(ordered)+np.array(lost)+np.array(opn),label="Expired",color=C_PRIMARY)
ax1.set_title("Territory / Rep-wise Status",fontsize=12,fontweight="bold",loc="left",pad=8)
ax1.set_xticks(x); ax1.set_xticklabels(reps,fontsize=8.5); ax1.legend(frameon=False,fontsize=8,ncol=4,loc="upper right")
ax1.spines[["top","right"]].set_visible(False); ax1.set_facecolor(CARD); ax1.tick_params(length=0)

# Priority breakdown (donut)
ax2=fig.add_subplot(gs[2,4:6])
pri=["P2 High-Risk 30+","P1 Expired-Urgent","P4 Active","P3 Watch 15+"]; pv=[34,31,20,15]
cols=[C_PRIMARY,C_PINK,C_GREEN,C_RED]
w,_=ax2.pie(pv,colors=cols,startangle=90,counterclock=False,wedgeprops=dict(width=0.42,edgecolor="white"))
ax2.legend(w,[f"{p} ({v}%)" for p,v in zip(pri,pv)],loc="center left",bbox_to_anchor=(0.9,0.5),fontsize=7.8,frameon=False)
ax2.set_title("Priority — Open Quotations",fontsize=12,fontweight="bold",loc="left",pad=8)

# Conversion by value slab
ax3=fig.add_subplot(gs[3,0:3])
slabs=["Below 10K","10K–1L","1L–5L","5L & Above"]; conv=[60.8,58.8,44.9,34.0]
b3=ax3.barh(slabs,conv,color=[C_GREEN,C_TEAL,C_AMBER,C_RED],height=0.6)
for bar,v in zip(b3,conv): ax3.text(v+1,bar.get_y()+bar.get_height()/2,f"{v:.0f}%",va="center",fontsize=9,color=INK,fontweight="600")
ax3.set_title("Avg Conversion Rate by Value Slab",fontsize=12,fontweight="bold",loc="left",pad=8)
ax3.set_xlim(0,72); ax3.set_xlabel("% converted"); ax3.spines[["top","right"]].set_visible(False)
ax3.set_facecolor(CARD); ax3.tick_params(length=0)

# Loss-age buckets
ax4=fig.add_subplot(gs[3,3:6])
buckets=["Critical\nLost 90+ Days","High\nLost 60+ Days","Recent\nLost <60 Days"]; bv=[62,94,38]
b4=ax4.bar(buckets,bv,color=[C_RED,C_AMBER,C_TEAL],width=0.55)
for bar,v in zip(b4,bv): ax4.text(bar.get_x()+bar.get_width()/2,v+2,f"{v}",ha="center",fontsize=10,fontweight="bold",color=INK)
ax4.set_title("Lost Quotations by Loss-Age Bucket",fontsize=12,fontweight="bold",loc="left",pad=8)
ax4.set_ylim(0,110); ax4.set_ylabel("quotations"); ax4.spines[["top","right"]].set_visible(False)
ax4.set_facecolor(CARD); ax4.tick_params(length=0)

plt.savefig("assets/quotation_health_dashboard.png",facecolor=BG,bbox_inches="tight",dpi=125)
print("saved quotation_health_dashboard.png")
