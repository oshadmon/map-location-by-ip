# import gmplot package 
import gmplot 

def draw_map(coordinate_list:list): 
   """
   Based on information in , draw map
   :args: 
      coordinate_list:list: list of corrdeinates 
   :param: 
     map_lat:list - latitude list 
     map_long:list - longtitude list 
   """ 
   map_lat = [] 
   map_long = [] 
   for coor in coordinate_list: 
      map_lat.append(float(coor.split('(')[-1].split(',')[0]))
      map_long.append(float(coor.split(',')[-1].split(')')[0]))
      #map_lat.append(int(coor.split('(')[-1].split(',')[0]))
      #map_long.append(int(coor.split(',')[-1].split(')')[0]))

   # Generate Map of the world 
   print(coordinate_list) 
   print(map_lat) 
   print(map_long) 

   gmap1 = gmplot.GoogleMapPlotter(0, 0, 3)

   gmap1.heatmap(map_lat, map_long)

   # Pass the absolute path 
   gmap1.draw('/var/www/html/map.html') 

