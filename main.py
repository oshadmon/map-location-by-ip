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

def merge_files(map_file:str, file_name:str): 
   try: 
      with open(map_file, 'r') as rmf: 
         try: 
            map_file_lines = rmf.readlines()[1:]
         except Exception as e: 
            print('Failed to read lines from %s [Error: %s]' % (map_file, e)) 
            return False 
   except Exception as e: 
      print('Failed to open file %s [Error: %s]' % (map_file, e))
      return False 
   
   try: 
      with open(file_name, 'a') as afn: 
         for line in map_file_lines: 
            try: 
               afn.write(line)
            except Exception as e: 
               print('Failed to write line %s into file %s [Error: %s]' % (line, file_name, e))
               return False 
   except exception as e: 
      print('Failed to open file %s for write [Error: %s]' % (file_name, e)) 
      return False 

   # write closing 
   try: 
      with open(file_name, 'a') as f: 
         try: 
            f.write(("\t</body>\n"
                    +"</html>"
            )) 
         except Exception as e: 
            print('Failed to write init code into file %s [Error: %s]' % (file_name, e))
            return False 
   except Exception as e: 
      print('Failed to open file %s [Error: %s]' % (file_name, e))
      return False 

def main(): 
   ip_dict = {} 
   ip_list_file = os.path.expanduser(os.path.expandvars('$HOME/map-location-by-ip/sample_ips.txt')) 
   ip_list = read_file(ip_list_file) 
   if not ip_list: 
      exit(1) 
   for ip in ip_list[:-1]: 
      if ip not in ip_dict: 
         ip_dict[ip] = {'address': get_address(ip), 'location': get_log_lat(ip)}

   map_file = draw_map(ip_dict)
   if not map_file: 
      exit(1) 

   file_name = write_info(ip_dict) 
   if not file_name: 
      exit(1)

   merge_files(map_file, file_name) 

if __name__ == '__main__': 
    main()
