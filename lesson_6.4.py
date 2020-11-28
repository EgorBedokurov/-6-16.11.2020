import datetime
import json

with open('acdc.json', 'r') as f:
    js_acdc = f.read()
    acdc = json.loads(js_acdc)
    dur_list = [int(track['duration']) for track in acdc['album']['tracks']['track']]
    print(dur_list)
    h_m_s = sum(dur_list)
    print(h_m_s)
    print(str(datetime.timedelta(seconds = h_m_s)))



