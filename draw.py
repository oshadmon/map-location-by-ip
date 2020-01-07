# import gmplot package 
import gmplot 
import os

def draw_map(locations:dict): 
   """
   Based on information in , draw map
   :args: 
      locations:dict dictionary of IPs with locatioons
   :param: 
     map_lat:list - latitude list 
     map_long:list - longtitude list 
   """ 
   map_file = os.path.expanduser(os.path.expandvars('$HOME/map-location-by-ip/images/tmp_map.html')) 

   map_lat = [] 
   map_long = [] 
   for ip in locations: 
      map_lat.append(float(locations[ip]['location'].split('(')[-1].split(',')[0]))
      map_long.append(float(locations[ip]['location'].split(',')[-1].split(')')[0]))

   # Generate Map of the world 
   try: 
      gmap1 = gmplot.GoogleMapPlotter(0, 0, 3)
   except Exception as e: 
      print('Failed to create initial map [Error: %s]' % (e))
      return False 
   try: 
      gmap1.heatmap(map_lat, map_long)
   except Exception as e: 
      print('Failed to set values on map [Error: %s]' % e)
      return False 

   # Pass the absolute path 
   try: 
      gmap1.draw(map_file) 
   except Exception as e: 
      print('Failed to write into file %s [Error: %s' % (map_file, e))
      return False 

   return map_file 
