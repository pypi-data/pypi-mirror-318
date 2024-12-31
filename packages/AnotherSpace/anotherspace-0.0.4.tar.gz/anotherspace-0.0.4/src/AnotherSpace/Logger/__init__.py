import sys

from loguru import logger

fmt_info = "<g>{time:DD.MM.YY HH:mm:ss} <b>| {level: <8}{level.icon} |</b> {file}:{line: <3} | {function: ^10} | {message}</g>"
fmt_trace = "<w>{time:DD.MM.YY HH:mm:ss} <b>| {level: <8}{level.icon} |</b> {file}:{line: <3} | {function: ^10} | {message}</w>"

logger.remove()
logger.add(sys.stdout,
           format=fmt_trace,
           colorize=True,
           filter=lambda record: record['level'].name == 'TRACE',
           level="TRACE")
logger.add(sys.stdout,
           format=fmt_trace,
           colorize=True,
           filter=lambda record: record['level'].name == 'DEBUG',
           level="DEBUG")
logger.add(sys.stdout,
           format=fmt_info,
           colorize=True,
           filter=lambda record: record['level'].name == 'INFO',
           level="INFO")

logger.add("logs/trace.log",
           format=fmt_trace,
           colorize=False,
           filter=lambda record: record['level'].name == 'TRACE',
           level="TRACE",
           encoding="utf-8")
logger.add("logs/debug.log",
           format=fmt_trace,
           colorize=False,
           filter=lambda record: record['level'].name == 'DEBUG',
           level="DEBUG",
           encoding="utf-8")
logger.add("logs/info.log",
           format=fmt_info,
           colorize=False,
           filter=lambda record: record['level'].name == 'INFO',
           level="INFO",
           encoding="utf-8")

logger.add("logs/main.log",
           format=fmt_trace,
           colorize=False,
           filter=lambda record: record['level'].name == 'TRACE',
           level="TRACE",
           encoding="utf-8")
logger.add("logs/main.log",
           format=fmt_trace,
           colorize=False,
           filter=lambda record: record['level'].name == 'DEBUG',
           level="DEBUG",
           encoding="utf-8")
logger.add("logs/main.log",
           format=fmt_info,
           colorize=False,
           filter=lambda record: record['level'].name == 'INFO',
           level="INFO",
           encoding="utf-8")

s = logger
