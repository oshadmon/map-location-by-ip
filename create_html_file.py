import datetime 
import os 

def write_info(locations:dict): 
   """
   Generate file containing IPs + locations 
   :args: 
      locations:dict - data dict 
   :param; 
      file_name:str - location where html is stored 
      full_file_name:str - full path oof file_name 
      write_to_file:str - string to write to file 
   :return: 
      if success return full_file_name, if fails return False 
   """
   file_name = '$HOME//map-location-by-ip/images/%s.world_map_heatmap.html' % datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
   full_file_name = os.path.expanduser(os.path.expandvars(file_name))
   write_to_file = "\t<p align=left><b>%s</b> - %s</p>\n"
   status_code = True  

  # Create file + write init info 
   try: 
      with open(full_file_name, 'w') as f: 
         try: 
            f.write(("<html> \n"
                   +"\t<h1 align=\"center\">Heatmap based on IPs</h1>\n"
            )) 
         except Exception as e: 
            print('Failed to write init code into file %s [Error: %s]' % (file_name, e))
            status_code = False 
   except Exception as e: 
      print('Failed to open file %s [Error: %s]' % (file_name, e))
      status_code = False 

   # Write IP / location info 
   if status_code: 
      for ip in locations:
         try:
            with open(full_file_name, 'a') as f: 
               try: 
                  f.write(write_to_file % (ip, locations[ip]['address']))
               except Exception as e: 
                  print('Failed to write to file %s [Error: %s]' % (file_name, e))
                  status_code = False 
         except Exception as e: 
            print('Failed to open file %s [Error: %s]' % (file_name, e))
            status_code = False 

   # write closing 
   """
   if status_code: 
      try: 
         with open(full_file_name, 'a') as f: 
            try: 
               f.write(("\t</body>\n"
                      +"</html>"
               )) 
            except Exception as e: 
               print('Failed to write init code into file %s [Error: %s]' % (file_name, e))
               status_code = False 
      except Exception as e: 
         print('Failed to open file %s [Error: %s]' % (file_name, e))
         status_code = False 
   """
   # rerename if failed 
   if not status_code: 
       try: 
          os.rename(full_file_name, '/dev/null') 
       except Exception as e: 
          print('File %s failed at an earlier point, thus needed to be rerenamed but unable to [Error: %s]' % (file_name, e))
   else: 
      status_code = full_file_name 

   return status_code 

