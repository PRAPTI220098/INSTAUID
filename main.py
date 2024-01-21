#Free To Use My Code 
#Don't Me The Credit
#Developer: @X668F (Telegram)

import requests,flask;from user_agent import generate_user_agent;
d=flask.Flask(__name__)
@d.route('/username=<id>', methods=['GET','POST'])
def api(id):
      u = id.lstrip("@")
      h={
'Host': 'api.sssgram.com',
'accept': 'application/json, text/plain, */*',
'origin': 'https://www.sssgram.com',
 'x-requested-with': 'mark.via.gp',
'sec-fetch-site': 'same-site',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://www.sssgram.com/',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7,hi-IN;q=0.6,hi;q=0.5',
'user-agent': str(generate_user_agent())
}
      bu = "https://api.sssgram.com/st-tik/ins/dlprofile"
      p = {
'url': f'https://www.instagram.com/{u}',
'timestamp': '1702992016308'}
      img = requests.get(bu, params=p, headers=h).json()['result']['userId']
      return f"<b>{img}</b>"      
      
if __name__ == '__main__':
      d.run(host='0.0.0.0', port=7861)
