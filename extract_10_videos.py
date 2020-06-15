import json
import os

f = open('WLASL_v0.3.json')

data = json.load(f)

video_download = []
for i in range(10):
    video_name = data[i]['gloss']
    get_instances = data[i]['instances'][:24]
    dict_temp = {'gloss': video_name, 'instances': get_instances}
    video_download.append(dict_temp)

with open('temp.json', 'w') as fout:
    json.dump(video_download, fout)
