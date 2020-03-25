import networkx as nx
import random
import matplotlib.pyplot as plt

### Код работает только как продолжение data gathering.py , 
### иначе надо загружать аналогичные таблицы df_adj и массивы new_.

n = len(new)

## Первый граф
G1 = nx.Graph()
new_new_sex = []
new_new_followers_count = []

for i in range(n):
    G1.add_node(i)
    new_new_sex.append(new_sex[i])


for i in range(len(new_new_sex)):
    new_new_sex[i] = new_new_sex[i] * new_new_sex[i] * 800
    
for i in range(len(new_followers_count)):
    new_new_followers_count.append(new_followers_count[i] * 20)
    
for i in range(n):
    for j in range(n):
        if df_adj[i][j] == 1:
            #print(i, j)
            G1.add_edge(i, j , weight = 0.005)
            
pos1 = nx.spring_layout(G1)

## Первый граф отрисовка

def Random_Geometric_Graph(G, pos):
    dmin = 1
    ncenter = 0
    for n in pos:
        x, y = pos[n]
        d = (x - 0.5)**2 + (y - 0.5)**2
        if d < dmin:
            ncenter = n
            dmin = d

    labels={}

    for i in range(n):
        labels[i] = str(new_names[i] + '\n' + new_lastnames[i])

    plt.figure(figsize=(100, 100))
    nx.draw_networkx_edges(G, pos, nodelist=[ncenter], alpha=0.4)
    nx.draw_networkx_nodes(G, pos, #nodelist=list(p.keys()),
                           node_size=4000,
                           node_color=list(new_new_sex),
                           cmap=plt.cm.Reds_r,
                           vmin=0, vmax=4000)

    nx.draw_networkx_labels(G,pos,labels,font_size=10)
    plt.xlim(-1.05, 1.05)
    plt.ylim(-1.05, 1.05)
    plt.axis('off')
    plt.show()

Random_Geometric_Graph(G1, pos1)
    
## Второй граф отрисовка

def Random_Geometric_Graph_follower(G, pos):
    dmin = 1
    ncenter = 0
    for n in pos:
        x, y = pos[n]
        d = (x - 0.5)**2 + (y - 0.5)**2
        if d < dmin:
            ncenter = n
            dmin = d

    labels={}

    for i in range(n):
        labels[i] = str(new_names[i] + '\n' + new_lastnames[i])

    plt.figure(figsize=(100, 100))
    nx.draw_networkx_edges(G, pos, nodelist=[ncenter], alpha=0.4)
    nx.draw_networkx_nodes(G, pos, #nodelist=list(p.keys()),
                           node_size=list(new_new_followers_count),
                           node_color=list(new_new_sex),
                           cmap=plt.cm.Reds_r,
                           vmin=0, vmax=4000)

    nx.draw_networkx_labels(G,pos,labels,font_size=10)
    plt.xlim(-1.05, 1.05)
    plt.ylim(-1.05, 1.05)
    plt.axis('off')
    plt.show()

Random_Geometric_Graph_follower(G1, pos1)

## Третий граф
rG1 = nx.Graph()

rnew_new_sex = []
rnew_new_followers_count = []
rnew_new_country = []
rlabels = {}

n = len(new)
for i in range(n):
    if new_city[i] != 'Москва' and new_city[i] != "":
        rG1.add_node(i)
        rnew_new_sex.append(new_sex[i])
        rnew_new_country.append(new_country[i])
        rlabels[i] = str(new_names[i] + '\n' + new_lastnames[i] + '\n' + new_city[i])

for i in range(len(rnew_new_sex)):
    rnew_new_sex[i] = rnew_new_sex[i] * rnew_new_sex[i] * 800
    
    
for i in range(n):
    for j in range(n):
        if df_adj[i][j] == 1 and new_city[i] != 'Москва' and new_city[i] != "" and new_city[j] != 'Москва' and new_city[j] != "":
            #print(i, j
            rG1.add_edge(i, j , weight = 0.005)
            
rpos1 = nx.spring_layout(rG1)
k = 0
di = dict()
color_country = []
for i in rnew_new_country:
    if i in di:
        color_country.append(di[i])
    else:
        di[i] = k * 40
        color_country.append(k)
        k += 1

## Третий граф отрисовка

def Random_Geometric_Graph_country():
    dmin = 1
    ncenter = 0
    for n in pos:
        x, y = pos[n]
        d = (x - 0.5)**2 + (y - 0.5)**2
        if d < dmin:
            ncenter = n
            dmin = d

    plt.figure(figsize=(15, 15))
    nx.draw_networkx_edges(G, pos, nodelist=[ncenter], alpha=0.4)
    nx.draw_networkx_nodes(G, pos, #nodelist=list(p.keys()),
                           node_size=2000,
                           node_color=color_country,
                           cmap=plt.cm.hsv,
                           vmin=0, vmax=40)

    nx.draw_networkx_labels(G,pos,rlabels,font_size=10)
    plt.xlim(-1.05, 1.05)
    plt.ylim(-1.05, 1.05)
    plt.axis('off')
    plt.show()
   
Random_Geometric_Graph_country(rG1, rpos1)

## Четвертый граф
bG1 = nx.Graph()
blabels = {}
bbirth = []
bscreen = []
bcolor = []

n = len(new)
for i in range(n):
    if len(new_bdate[i]) >= 8:
        bG1.add_node(i)
        year = int(new_bdate[i].split('.')[2])
        month = int(new_bdate[i].split('.')[1])
        day = int(new_bdate[i].split('.')[0])
        
        approx_date = 20 + 2*30 + 2020 * 365
        approx_birth = year*365 + (month - 1)*30 + day
        approx_age = approx_date - approx_birth
        t = approx_age//365
        t **= 1.3
        t *= 50
        bbirth.append(t)

        blabels[i] = str(new_names[i] + '\n' + new_lastnames[i])
        
        if (new_screen_name[i][:2] == "id"):
            bcolor.append(1)
        else:
            bcolor.append(2)
    
for i in range(n):
    for j in range(n):
        if df_adj[i][j] == 1 and len(new_bdate[i]) >= 8 and len(new_bdate[j]) >= 8:
            #print(i, j
            bG1.add_edge(i, j , weight = 0.005)
            
bpos1 = nx.spring_layout(bG1)

## Четвертный граф отрисовка

def Random_Geometric_Graph_birth():
    dmin = 1
    ncenter = 0
    for n in pos:
        x, y = pos[n]
        d = (x - 0.5)**2 + (y - 0.5)**2
        if d < dmin:
            ncenter = n
            dmin = d

    plt.figure(figsize=(25, 25))
    nx.draw_networkx_edges(G, pos, nodelist=[ncenter], alpha=0.4)
    nx.draw_networkx_nodes(G, pos, #nodelist=list(p.keys()),
                           node_size=list(bbirth),
                           node_color=bcolor,
                           cmap=plt.cm.hsv,
                           vmin=0, vmax=2)

    nx.draw_networkx_labels(G,pos,blabels,font_size=10)
    plt.xlim(-1.05, 1.05)
    plt.ylim(-1.05, 1.05)
    plt.axis('off')
    plt.show()

Random_Geometric_Graph_birth(bG1, bpos1)
