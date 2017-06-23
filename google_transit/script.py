import os
import json
from collections import defaultdict

script_dir = os.path.dirname(__file__)

stops = defaultdict(dict)

fwrite = open(os.path.join(script_dir,'google_transit/stop_times_sorted.json'), 'w')

# with open(os.path.join(script_dir,'google_transit/stop_times.json'), 'r') as fread:
#     for line in fread:
#         s = line.split(',')
#         stop = s[0]
#         dir = s[1]
#         time = s[2].strip()
#
#         if time.split(':')[0] < '24':
#             if dir in stops[stop]:
#                 stops[stop][dir].append(time)
#             else:
#                 stops[stop][dir] = [time]
# stops = dict(stops)
# del stops['stop_namestop_desc']
#
# fwrite.write(json.dumps(dict(stops)))

with open(os.path.join(script_dir, 'google_transit/stop_times_sorted2.json')) as file:
    d = dict(json.load(file))

for stop in d.keys():
    print(stop)
    for dir in d[stop].keys():
        d[stop][dir] = sorted(list(set(d[stop][dir])))

fwrite.write(json.dumps(d))
