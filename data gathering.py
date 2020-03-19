import vk_api
import numpy as np

vk_session = vk_api.VkApi('lybashkagyn@mail.ru', 'pass')
vk_session.auth()
vke = vk_session.get_api()
friends = vke.friends.get()
new = (friends['items'])

big_set_of_friends = []
for j in new:
    this = vke.friends.getMutual(source_uid = j, target_uid = '96540979')
    big_set_of_friends.append(this)
    
new.sort()
d = {}

adj = []
for i in range(len(new)):
    adj.append([])
    for j in range(len(new)):
        adj[i].append(0)
        
for i in range(len(new)):
    d[new[i]] = i

for i in range(len(new)):
    num_in_mass = d[new[i]]
    his_friends = big_set_of_friends[num_in_mass]
    for i in range(len(his_friends)):
        friend_in_mass = d[his_friends[i]]
        adj[num_in_mass][friend_in_mass] = 1
        adj[friend_in_mass][num_in_mass] = 1

import pandas as pd
df_adj = pd.DataFrame(adj)
df_ids_v = pd.DataFrame(adj)
df_ids_h = pd.DataFrame(adj)
df_ids_vh = pd.DataFrame(adj)

df_ids_v.loc[0] = new
df_ids_h['id'] = new

new_0 = []
for i in range(len(new)):
    new_0.append(new[i])

new_0.append(0)
print(len(new_0))

df_ids_vh.loc[217] = new
df_ids_vh['id'] = new_0

df_adj.to_csv('adj_matrix')
df_ids_v.to_csv('v_matrix')
df_ids_h.to_csv('h_matrix')
df_ids_vh.to_csv('vh_matrix')

new_names = []
new_lastnames = []
new_sex = []
new_bdate = []
new_city = []
new_country = []
new_has_mobile = []
new_status = []
new_followers_count = []
new_nickname = []
new_common_count = []
new_has_photo = []
new_screen_name = []

for i in new:
    user = vke.users.get(user_ids = i,
    fields = ['sex', 'bdate', 'city', 'country', 'has_mobile', 'status', 'followers_count', 'nickname', 'common_count', 'has_photo', 'screen_name'])
    
    name = user[0]['first_name']
    lastname = user[0]['last_name']
    sex = user[0]['sex']
    
    if 'bdate' in user[0]:
        bdate = user[0]['bdate']
    else:
        bdate = ''
    
    if 'city' in user[0]:
        city = user[0]['city']['title']
    else:
        city = ''
        
    if 'country' in user[0]:    
        country = user[0]['country']['title']
    else:
        country = ''

    has_mobile = user[0]['has_mobile']
    status = user[0]['status']
    
    if 'followers_count' in user[0]:
        followers_count = user[0]['followers_count']
    else:
        followers_count = 0

    nickname = user[0]['nickname']
    common_count = user[0]['common_count']
    has_photo = user[0]['has_photo']
    screen_name = user[0]['screen_name']
    #print(i)
    
    new_names.append(name)
    new_lastnames.append(lastname)
    new_sex.append(sex)
    new_bdate.append(bdate)
    new_city.append(city)
    new_country.append(country)
    new_has_mobile.append(has_mobile)
    new_status.append(status)
    new_followers_count.append(followers_count)
    new_nickname.append(nickname)
    new_common_count.append(common_count)
    new_has_photo.append(has_photo)
    new_screen_name.append(screen_name)
    
my_friends = pd.DataFrame(new_names)
my_friends['last_names'] = new_lastnames
my_friends['sex'] = new_sex
my_friends['bdate'] = new_bdate
my_friends['city'] = new_city
my_friends['country'] = new_country
my_friends['has_mobile'] = new_has_mobile
my_friends['status'] = new_status
my_friends['followes_count'] = new_followers_count
my_friends['nickname'] = new_nickname
my_friends['common_count'] = new_common_count
my_friends['has_photo'] = new_has_photo
my_friends['screen_name'] = new_screen_name
my_friends.rename(columns={0: 'names'}, inplace=True)

my_friends.to_csv('friendsinfo')
