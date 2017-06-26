import json
from datetime import datetime

times = """"""

stations = ['Peoria', 'Fitzsimons', 'Colfax', '13th Avenue', '2nd & Abilene', 'Aurora Metro Center Stn', 'Florida', 'Iliff', 'Nine Mile', 'Dayton', 'Belleview Stn', 'Orchard', 'Arapahoe at Village Center', 'Dry Creek', 'County Line', 'Lincoln']

# def station_formatter(s):
#     s = s.split('Station')
#     s = [x.strip() for x in s][:-1]
#
#     return s


def time_formatter(s, line=None, num=None):
    if not num or not line:
        return None
    s = s.split('\t')
    s = list(filter(lambda a: a != line, s))
    s = list(filter(lambda a: a != 'Hide trips before this trip">', s))

    s = [x.replace('Hide trips before this trip">\n'+line, '').strip() for x in s]
    s = [x.replace('P', 'PM').replace('A', 'AM').zfill(6) for x in s]

    for i in range(len(s)):
        try:
            s[i] = datetime.strptime(s[i], '%I%M%p')
        except ValueError:
            pass

    s = [s[num*i:num*(i+1)] for i in range(len(s)//num)]

    return s


d = {}

t = time_formatter(times, 'R', 16)

for i in range(len(stations)):
    times = sorted(list(filter(lambda a: a != '-0000-',[x[i] for x in t])))

    d[stations[i]] = [time.strftime('%H:%M') for time in times]

with open('R_SB_MONTHURS.json', 'w') as f:
    f.write(json.dumps(d))

# GUIDE
# 1. Switch out the huge list of times
# 2. Get the correct list of stops and its length
# 3. Put the line and the number of stops
# 4. Change the json file name
