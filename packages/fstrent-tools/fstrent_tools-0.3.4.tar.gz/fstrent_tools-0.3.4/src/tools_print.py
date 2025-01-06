import os
from datetime import datetime as dt
from tools_logging import plogit
from tools_time import dttm_get
from fstrent_colors import cp

__all__ = [
    'print_adv',
    'print_line',
    'print_clickable_link',
    'print_func_name',
    'section_header',
    'clear_screen'
]

def print_adv(adv=1):
    while adv > 0:
        adv -= 1
        print('')

def print_line(char='-', cnt=10, clr='white', bgclr='black'):
    s = char * cnt
    cp(s, font_clr=clr, bg_clr=bgclr)

def print_clickable_link(url, display_text):
    # Use the OSC 8 escape sequence to start the hyperlink
    # Then use the ST escape to stop it.
    print(f'\033]8;;{url}\033\\{display_text}\033]8;;\033\\')

def print_func_name(func_name, adv=0, clr='white', bgclr='blue'):
    dttm_str = dttm_get()
    if adv > 0: print_adv(adv)
    s = '{}  ===>  {}'.format(dttm_str, func_name)
    cp(s, font_clr=clr, bg_clr=bgclr)

def debug_display_func_name(func_name, debug_show_lvl=0):
    prt_dttm_now = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    m = '{} ==> {}'
    msg = m.format(prt_dttm_now, func_name)
    print(msg)
    return

def banner_display(e, msg):
    plogit('pcp', e, '')
    plogit('pcp', e, '')
    m = '#<==|===||====|||=== ({}) - {:<20} ===|||====||===|==>#'
    msg = m.format(e, msg)
    plogit('pcp', e, msg)
    return

def clear_screen():
    if os.name == 'nt':
        os.system('cls')

def section_header(
    txt
    , l=100
    , clr=''
    , bgclr=''
    , before_ln_adv = 2
    , after_ln_adv = 0
    , show_dttm_yn = 'Y'
    , center_yn = 'N'
    ):
    if center_yn == 'Y': txt = txt.center(l)
    if before_ln_adv > 0: pa(before_ln_adv)
    dttm_str = ''
    if show_dttm_yn == 'Y':
        dttm_str = dt.now().strftime('%Y-%m-%d %H:%M:%S') + ' '
    if clr not in ('grey','red','green','yellow','blue','magenta','cyan','white'): clr = ''
    if bgclr not in ('grey','red','green','yellow','blue','magenta','cyan','white'): bgclr = ''
    if clr != '' and bgclr != '':
        cp(dttm_str + txt, font_clr=clr, bg_clr=bgclr)
    elif clr != '':
        cp(dttm_str + txt, font_clr=clr)
    else:
        print(dttm_str + txt)
    if after_ln_adv > 0: pa(after_ln_adv)
    return

def pa(r=1):
    cnt = 0
    while cnt < r:
        print('')
        cnt += 1
    return

def pb(c='*', l=235, fgclr='', bgclr=''):
    txt = c*l
    if fgclr not in ('grey','red','green','yellow','blue','magenta','cyan','white'): fgclr = ''
    if bgclr not in ('grey','red','green','yellow','blue','magenta','cyan','white'): bgclr = ''
    if fgclr != '' and bgclr != '':
        cp(txt, font_clr=fgclr, bg_clr=bgclr)
    elif fgclr != '':
        cp(txt, font_clr=fgclr)
    else:
        print(txt)
    return
