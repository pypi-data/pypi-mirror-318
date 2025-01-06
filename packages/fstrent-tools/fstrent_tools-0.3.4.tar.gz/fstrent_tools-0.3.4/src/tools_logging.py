import logging
from datetime import datetime as dt
from pprint import pformat
from tools_files import dir_val

__all__ = [
    'setup_logger',
    'log_info',
    'log_warning',
    'log_error',
    'log_debug',
    'log_exception',
    'plogit'
]

def setup_logger(name, log_file, level=logging.INFO):
    """
    Sets up a logger with a file handler and a stream handler.

    Args:
        name (str): The name of the logger.
        log_file (str): The path to the log file.
        level (int, optional): The logging level. Defaults to logging.INFO.
    """
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

def log_info(logger, message):
    """
    Logs an info message.

    Args:
        logger (logging.Logger): The logger to use.
        message (str): The message to log.
    """
    logger.info(message)

def log_warning(logger, message):
    """
    Logs a warning message.

    Args:
        logger (logging.Logger): The logger to use.
        message (str): The message to log.
    """
    logger.warning(message)

def log_error(logger, message):
    """
    Logs an error message.

    Args:
        logger (logging.Logger): The logger to use.
        message (str): The message to log.
    """
    logger.error(message)

def log_debug(logger, message):
    """
    Logs a debug message.

    Args:
        logger (logging.Logger): The logger to use.
        message (str): The message to log.
    """
    logger.debug(message)

def log_exception(logger, message):
    """
    Logs an exception message.

    Args:
        logger (logging.Logger): The logger to use.
        message (str): The message to log.
    """
    logger.exception(message)

def plogit(logname, epoch, msg=None, printyn='Y', logyn='Y'):
	dttm_now = dt.now().strftime('%Y_%m_%d')
	prt_dttm_now = dt.now().strftime('%Y-%m-%d %H:%M:%S')

	logfile = 'logs/' + dttm_now + '_' + logname + '.log'

	dir_val(logfile)
	with open(logfile, 'a') as LogWriter:
		if isinstance(msg, str):
			if msg == '':
				if printyn == 'Y': print('')
				if logyn == 'Y': LogWriter.writelines('\n')
			else:
				m = '{} ({}) ==> {}'
				fmsg = m.format(prt_dttm_now, epoch, msg)
				if printyn == 'Y': print(fmsg)
				if logyn == 'Y': LogWriter.writelines(fmsg)
		else:
			if printyn == 'Y': print(pformat(msg))
			if logyn == 'Y': LogWriter.write(pformat(msg))
		LogWriter.writelines('\n')
		LogWriter.close()
	return
