import matplotlib.pyplot as plt

def axes():
# aktuellen Plot zuweisen:
    ax = plt.gca()
    # Obere und rechte Achse unsichtbar werden lassen:
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # Untere Achse auf die y=0 Position bewegen:
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    # Linke Achse auf die Position x == 0 bewegen:
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    xmin, xmax = ax.get_xlim() 
    ymin, ymax = ax.get_ylim()
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    # get width and height of axes object to compute 
    # matching arrowhead length and width
    #dps = fig.dpi_scale_trans.inverted()
    bbox = ax.get_window_extent()
    width, height = bbox.width, bbox.height

    # manual arrowhead width and length
    hw = 1./20.*(ymax-ymin) 
    hl = 1./20.*(xmax-xmin)
    lw = 1. # axis line width
    ohg = 0.3 # arrow overhang

    # compute matching arrowhead length and width
    yhw = hw/(ymax-ymin)*(xmax-xmin)* height/width 
    yhl = hl/(xmax-xmin)*(ymax-ymin)* width/height

    # draw x and y axis
    ax.arrow(xmin, 0, xmax-xmin, 0., fc='k', ec='k', lw = lw, 
             head_width=hw, head_length=hl, overhang = ohg, 
             length_includes_head= True, clip_on = False) 

    ax.arrow(0, ymin, 0., ymax-ymin, fc='k', ec='k', lw = lw, 
             head_width=yhw, head_length=yhl, overhang = ohg, 
             length_includes_head= True, clip_on = False)
    return ax

