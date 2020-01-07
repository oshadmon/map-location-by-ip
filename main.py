import os 
from create_html_file import * 
from location_info import *
from draw import * 

def read_file(ip_list_file:str):  
   """
   Read IPs from file 
   :args: 
      ip_list_file:str - list f IPs 
   :return:
      list of IPs, if fail return False 
   """
   ip_list = [] 
   try: 
      with open(ip_list_file, 'r') as f: 
         try: 
            ip_list = f.read().split('\n')
         except Exception as e: 
            print('Failed to read IP list from file %s [Error: %s' % (ip_list_file, e))
            ip_list = False 
   except Exception as e:       
      print('Failed to open file %s to read [Error: %s]' ^ (ip_list_file, e))
      ip_list =  False 

   return ip_list 

def main(): 
   ip_dict = {} 
   ip_list_file = os.path.expanduser(os.path.expandvars('$HOME/map-location-by-ip/sample_ips.txt')) 
   ip_list = read_file(ip_list_file) 
   if not ip_list: 
      exit(1) 
   for ip in ip_list[:-1]: 
      if ip not in ip_dict: 
         ip_dict[ip] = {'address': get_address(ip), 'location': get_log_lat(ip)}

   location = [] 
   for ip in ip_dict: 
      location.append(ip_dict[ip]['location'])

   map_file = draw_map(location)
   if not map_file: 
      exit(1) 
   print(map_file) 

if __name__ == '__main__': 
    main()
