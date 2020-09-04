"""This file contain the style applied to markdown in the notebook !!
"""
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
from plotly import tools
import numpy as np


def change_font():
    """Une méthode qui retourme le fichier HTML et CSS adéquat pour les fonts dans jupyter.
    """

    html = """
    <style>
    
    .rendered_html {
         font-size: 22px; 
         font-family: Garamond;
         line-height: 140%;
         text-align: justify;
         text-justify: inter-word;
    }

    div.text_cell_render h1 { /* Main titles bigger, centered */
        text-align:center;
    # }
    
    </style>"""

    return html
