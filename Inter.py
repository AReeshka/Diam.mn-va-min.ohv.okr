from IPython.html.widgets import interactive
from IPython.display import display
import ipywidgets as widgets

def inter(inf,draw):
    def pp(x):
        A, B, dir, best, hpoints, hull, dist, points = inf[x]
        draw(A, B, dir, best, hpoints, hull, dist, points)
    w=widgets.interactive(pp, x = widgets.IntSlider(min=0,max=len(inf) - 1,step=1,value=0))

    display(w)