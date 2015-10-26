from bs4 import BeautifulSoup
import math
import os
from .colorgradient import linear_gradient

def choropleth(data, min_val, max_val, steps):

    '''
    Parse svg map and set initial style
    '''
    svg_path = os.path.dirname(__file__)+'/svg/us-counties.svg' 
    svg = open(svg_path, 'r',).read()
    soup = BeautifulSoup(svg ,'xml', selfClosingTags=['defs','sodipodi:namedview'])
    paths = soup.findAll('path')
    colors = linear_gradient("#245B00","#B2D1B2",steps)['hex']
    path_style = '''font-size:12px;fill-rule:nonzero;stroke:#FFFFFF
        ;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4
        ;stroke-dasharray:none;stroke-linecap:butt;marker-start:none
        ;stroke-linejoin:bevel;fill:'''
    
    '''
    Calculate cutoff values for each step
    '''
    ##TODO: How to work with decimal ranges?
    step_size = math.ceil((max_val - min_val) / steps)
    step_vals = [max_val]
    for step in range(1,steps+1):
        step_vals.append(max_val - (step_size * step))

    '''
    Determine shade for each county and write appropriate path style
    '''
    for p in paths:
        if ['id'] not in ["State_Lines","separator"]:
            try:
                val = data[p['id']]
            except:
                continue    
        shade = -1
        for step in step_vals:
            if val > step:
                break
            else: 
                shade += 1
        
        color = colors[shade]
        p['style'] = path_style + color

    '''
    Return formatted XML
    '''
    return soup.prettify()
