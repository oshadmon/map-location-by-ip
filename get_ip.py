import requests

def get_ip(): 
   """
   Get network IP through whatismyip.com
   :return: 
      IPv4 address
   """
   try: 
      r = requests.get('https://ipv4bot.whatismyipaddress.com') 
   except Exception as e: 
      print('Failed to get IP address [Error: %s]' % e) 
      return False 
   return r.text 


