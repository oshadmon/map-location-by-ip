# import gmplot package 
import gmplot 
import os

def draw_map(coordinate_list:list): 
   """
   Based on information in , draw map
   :args: 
      coordinate_list:list: list of corrdeinates 
   :param: 
     map_lat:list - latitude list 
     map_long:list - longtitude list 
   """ 
   map_file = os.path.expanduser(os.path.expandvars('$HOME/map-location-by-ip/images/tmp_map.html')) 
   #try: 
   #   open(map_file, 'w').close() 
   #except Exception as e: 
   #   print('Failed to create file %s [Error: %s]' % (map_file, e))
   #   return False 

   map_lat = [] 
   map_long = [] 
   for coor in coordinate_list: 
      map_lat.append(float(coor.split('(')[-1].split(',')[0]))
      map_long.append(float(coor.split(',')[-1].split(')')[0]))

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
