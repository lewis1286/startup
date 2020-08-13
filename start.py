import numpy as np
import pandas as pd

from bokeh.plotting import figure, output_notebook, show


def bokeh_hist(arr, do_log=True, title="A Histogram"):
    '''
    Always spend 10 mins googling how to bokeh a histogram.
    Lets have a quick one!

    Inputs:
        arr (iterable)
    Outputs:
        bokeh figure object
    '''
    bottom = 1e-1 * do_log

    hist, edges = np.histogram(arr, bins=50)

    p = figure(
        title=title,
        y_axis_type='log'
    )
    p.y_range.start = 0.1 * do_log

    p.quad(
        top=hist, bottom=bottom, left=edges[:-1], right=edges[1:],
        fill_color="navy", line_color="white", alpha=0.5
    )
    return p

