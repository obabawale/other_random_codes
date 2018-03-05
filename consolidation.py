#!/usr/bin/python

records = [{'name':"Olalekan Babawale", 'sex':"Male", 'pay': 45},{'name':"Olalekan Babawale", 'sex':"Male", 'pay': 50},{'name':"Esther Umoh",'sex':"Female", 'pay': 45}]

#Build a new list using the names of the items in records
new_rec = list(map(lambda r: r['name'], records))
print "=====", new_rec
new_list = []
for record in set(new_rec):
    my_list = []
    x = 0
    for item in records:
        if record == item['name']:
            if x <= 0:
                my_list.append(item)
            else:
                my_list[0]['pay'] += item['pay']
            x += 1
    new_list.extend(my_list)
print "Hey see my list %s" % new_list 
