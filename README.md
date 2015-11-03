# choropleth
A python package that can create filled-map images (choropleths) for data analysis

![alt tag](https://cdn.rawgit.com/robtkiller/choropleth/master/examples/poverty.svg)

##Basic Usage

**choropleth**.**choropleth**(*map_type*, *data*, *min_val*, *max_val*, *base_color*, *steps*)

***map_type*** is a string giving the map template image to use as the basis for the choropleth.

***data*** is a dictionary containing the values corresponding to each each sector of the map.  Expected keys will depend on the *map_type* as decribed in the table below.

   **map_type**   |   **Key**                  |    **Examples**
------------------|----------------------------|---------------
'us-counties'     | State+County FIPS code     | '01011', '55121'
'us-states'       | 2-letter state abbreviation| 'NV', 'AL', 'CA'
'world-countries  | 2-letter country code      | 'us', 'cn', 'de'

***min_val*** and ***max_val*** are `float` or `int`'s and set the minimum and maximum values, respectively, to interpolate shading over. 
Sectors with values greater than ***max_val*** are assigned the ***base_color***.
Sectors with values less than the ***min_val*** are assigned the default gray.

***base_color*** is a string containing the hexidecimal color to interpolate shades from.  

***steps*** is an `int` representing the number of intervals to calculate.

##Example

First, import the required modules and build a dictionary for your data.
```
import choropleth
import csv

data = {}

with open('poverty.csv','r') as f:
  reader = csv.reader(f)
  counties = list(reader)
  for county in counties:
    try:
      data[county[1]] = float(county[11])
    except:
      pass
```
Next, create choropleth data.
```
choro = cp.choropleth('us-counties', data,3.0,35.0 , '#A40000', 6)
```
Finally, write it to a file.
```
with open('poverty.svg','w') as my_map:
  my_map.write(choro)
```

