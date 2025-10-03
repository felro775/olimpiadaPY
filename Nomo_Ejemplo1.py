from pynomo.nomographer import *
Miles_params={
'tag':'myscale',
'u_min':0,
'u_max':100,
'function':lambda u:u,
'title':r'Miles',
'title_x_shift':-0.5,
'tick_levels':3,
'tick_text_levels':2,
'tick_side':'left',
}
block_1_params={
'block_type':'type_8',
'f_params':Miles_params,
}
Kilometers_params={
'tag':'myscale',
'u_min':0.0,'u_max':1.609*100.0,
'function':lambda u:1.609*u,
'align_func':lambda u:u/1.609,
'title':r'Kilom',
'title_x_shift':0.5,
'tick_levels':3,
'tick_text_levels':2,
'tick_side':'right',
}
block_2_params={
'block_type':'type_8',
'f_params':Kilometers_params,
}
main_params={
'filename':'static/docs/Ejemplo_1.pdf',
'paper_height':20.0,
'paper_width':0.5,
'block_params':[block_1_params,block_2_params],
'transformations':[('scale paper',)],
}
Nomographer(main_params)
