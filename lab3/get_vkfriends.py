from vk_client import *
get_user = GetVkID('g_s_f_o')
user = get_user.execute()
user_id = user.get('id')
get_friends = GetVkFriends(user_id)
friends = get_friends.execute()
now = datetime.now()
ages = [0] * 1000

for fr in friends:
    try:
        date_str = fr.get('bdate')
        date = datetime.strptime(date_str, '%d.%m.%Y')
        days = (now - date).days
        age = days // 365
        ages[age] += 1
    except:
        pass

print(user.get("first_name"), user.get("last_name"))
for age in range(1000):
    if ages[age] != 0:
        print(age, " ", "#" * ages[age])