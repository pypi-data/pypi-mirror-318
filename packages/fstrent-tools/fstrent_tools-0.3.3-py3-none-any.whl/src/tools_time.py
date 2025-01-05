import datetime
import time
from datetime import datetime as dt
from tools_files import logit

__all__ = [
    'temp_timing_begin',
    'temp_timing_end',
    'temp_timer_begin',
    'temp_timer_end',
    'utc_now',
    'dttm_get',
    'now_utc_get',
    'now_utc_ts_get',
    'calc_elapsed',
    'get_now',
    'prt_dttm_get',
    'sleep_until',
    'sleep'
]

def temp_timing_begin(func_name, logname='', log_yn='Y', min_yn='N'):
    f = {}
    t0              = time.perf_counter()
    strt_dttm       = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    f['func_name']  = func_name
    f['logname']    = logname
    f['log_yn']     = log_yn
    f['min_yn']     = min_yn
    f['t0']         = t0
    f['strt_dttm']  = strt_dttm
    msg = "{:<50} begins at {}".format(func_name, strt_dttm)
    if log_yn == 'Y': logit(logname, msg)
    if min_yn == 'N': print(msg)
    return f

def temp_timing_end(f):
    t1 = time.perf_counter()
    end_dttm        = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    t0              = f['t0']
    func_name       = f['func_name']
    logname         = f['logname']
    log_yn          = f['log_yn']
    min_yn          = f['min_yn']
    f['t1']         = t1
    f['end_dttm']   = end_dttm
    secs = round(t1 - t0, 3)
    f['secs']       = secs
    m = "{:<50} completed at {}, taking {:>7.3f} seconds..."
    msg = m.format(func_name, end_dttm, secs)
    if log_yn == 'Y': logit(logname, msg)
    if min_yn != 'Y': print(msg)
    return f

def temp_timer_begin(nm):
    t = {}
    t['name']  = nm
    t0              = time.perf_counter()
    t['t0']         = t0
    strt_dttm       = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    t['strt_dttm']  = strt_dttm
    msg = "{} begins at {}".format(nm, strt_dttm)
    print(msg)
    return t

def temp_timer_end(t):

    t1 = time.perf_counter()
    t['t1']         = t1

    end_dttm        = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    t['end_dttm']   = end_dttm

    t0              = t['t0']
    nm              = t['name']

    secs = round(t1 - t0, 3)
    t['secs']       = secs

    m = "{} completed at {}, taking {} seconds..."
    msg = m.format(nm, end_dttm, secs)
    print(msg)

    return t

def utc_now():
    import datetime
    utc_now = datetime.datetime.now(datetime.UTC)
    return utc_now

def dttm_get():
    dttm_str = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    return dttm_str

def dttm_get():
    dttm_str = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    return dttm_str

def now_utc_get():
    now_utc = dt.now(datetime.timezone.utc)
    return now_utc

def now_utc_ts_get():
    now_utc_ts = dt.now(datetime.timezone.utc).timestamp()
    return now_utc_ts

def calc_elapsed(dttm_new, dttm_old, interval='seconds'):
    if interval == 'seconds':
        elapsed = (dttm_new - dttm_old).total_seconds()
    elif interval == 'minutes':
        elapsed = (dttm_new - dttm_old).total_seconds() / 60
    elif interval == 'hours':
        elapsed = (dttm_new - dttm_old).total_seconds() / (60 * 60)
    elif interval == 'days':
        elapsed = (dttm_new - dttm_old).total_seconds() / (60 * 60 * 24)
    return elapsed

def get_now():
    now = dt.now().replace(microsecond=0)

    return now

def prt_dttm_get():
    prt_dttm    = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    return prt_dttm

def sleep_until(dttm):
    cnt = 0
    now = get_now()
    while now <= dttm:
        now = get_now()
        cnt += 1
        time.sleep(1)

def sleep(sec):
    time.sleep(sec)
