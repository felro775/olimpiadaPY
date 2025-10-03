import math
import sys

from pynomo.nomographer import *

a = sys.argv[1]
b = sys.argv[2]

Q_params={
'u_min':2.0,
'u_max':int(a),
'function':lambda u:-math.log10(u),
'scale_type':'linear',
'title':r'\Large $Q$',
'tick_levels':2,
'tick_text_levels':1,
'tick_side':'left',
}
F_params={
'u_min':0.5,
'u_max':1.5,
'function':lambda u:-math.log10(u),
'scale_type':'linear',
'title':r'\Large $F$',
'tick_levels':1,
'tick_text_levels':1,
'tick_side':'left',
}
E_params={
'u_min':0.1,
'u_max':1.0,
'function':lambda u:-math.log10(u),
'scale_type':'linear',
'title':r'\Large $E$',
'tick_levels':3,
'tick_text_levels':2,
'tick_side':'left',
}

Cm_params={
'u_min':1.0,
'u_max':int(b),
'function':lambda u:math.log10(u),
'scale_type':'linear',
'title':r'\Large $Cm$',
'tick_levels':3,
'tick_text_levels':1,
'tick_side':'left',
}
R_params={
'u_min':1.0,
'u_max':3.0,
'function':lambda u:math.log10(u),
'scale_type':'linear',
'title':r'\Large $R$',
'tick_levels':3,
'tick_text_levels':1,
}

block_1_params={
'block_type':'type_3',
'width':10.0,
'height':10.0,
'reference_titles':['Ref. 1','Ref. 2'],
'f_params':[Q_params,F_params,E_params,Cm_params,R_params],
}
main_params={
'filename':'static/docs/Rend_CargadoraFrontal.pdf',
'paper_height':40.0,
'paper_width':40.0,
'block_params':[block_1_params],
'transformations':[('rotate',0.01),('scale paper',)],
'title_x':10.0,
'title_y':-1.0,
'title_box_width': 20.0,
'title_str':r'Rendimiento = (Q $\times$ F$\times$ E) \
/ (Cm)',
'draw_isopleths': False,
}
Nomographer(main_params)

