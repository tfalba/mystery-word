# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import  requests
import json
# TODO: replace with your own app_id and app_key

app_id ='7e34cbc8'
app_key = '9f0002e1ec49289bec208516fd450264'

#app_id = '<my app_id>'
#app_key = '<my app_key>'
language = 'en-gb'
word_id = 'unactivated'
url = '	https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word_id.lower()
#// url Normalized frequency
#urlFR = 'https://gad-proxy-prod-leap-2-1.us-east-1.elasticbeanstalk.com:443/api/v2/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()
r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
result = r.json()
#print("code {}\n".format(r.status_code))
#print("text \n" + r.text)
#print("json \n" + json.dumps(r.json()))
print(r.json())
