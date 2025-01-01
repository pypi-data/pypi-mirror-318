import sys

from loguru import logger

fmt = "{time:DD.MM.YY HH:mm:ss} <b>| {level: <8}{level.icon} |</b> {file}:{line: <3} | {function: ^10} | {message}"

logger.remove()
logger.add(sys.stdout,
           format=f"<w>{fmt}</w>",
           colorize=True,
           filter=lambda record: record['level'].name == 'TRACE',
           level="TRACE")
logger.add(sys.stdout,
           format=f"<w>{fmt}</w>",
           colorize=True,
           filter=lambda record: record['level'].name == 'DEBUG',
           level="DEBUG")
logger.add(sys.stdout,
           format=f"<c>{fmt}</c>",
           colorize=True,
           filter=lambda record: record['level'].name == 'INFO',
           level="INFO")
logger.add(sys.stdout,
           format=f"<g>{fmt}</g>",
           colorize=True,
           filter=lambda record: record['level'].name == 'SUCCESS',
           level="SUCCESS")
logger.add(sys.stdout,
           format=f"<y>{fmt}</y>",
           colorize=True,
           filter=lambda record: record['level'].name == 'WARNING',
           level="WARNING")
logger.add(sys.stdout,
           format=f"<r>{fmt}</r>",
           colorize=True,
           filter=lambda record: record['level'].name == 'ERROR',
           level="ERROR")
logger.add(sys.stdout,
           format=f"<r>{fmt}</r>",
           colorize=True,
           filter=lambda record: record['level'].name == 'CRITICAL',
           level="CRITICAL")

logger.add("logs/trace.log",
           format=fmt,
           colorize=False,
           filter=lambda record: record['level'].name == 'TRACE',
           level="TRACE",
           encoding="utf-8")
logger.add("logs/debug.log",
           format=fmt,
           colorize=False,
           filter=lambda record: record['level'].name == 'DEBUG',
           level="DEBUG",
           encoding="utf-8")
logger.add("logs/info.log",
           format=fmt,
           colorize=False,
           filter=lambda record: record['level'].name == 'INFO',
           level="INFO",
           encoding="utf-8")
logger.add("logs/success.log",
           format=fmt,
           colorize=False,
           filter=lambda record: record['level'].name == 'SUCCESS',
           level="TRACE",
           encoding="utf-8")
logger.add("logs/warning.log",
           format=fmt,
           colorize=False,
           filter=lambda record: record['level'].name == 'WARNING',
           level="DEBUG",
           encoding="utf-8")
logger.add("logs/error.log",
           format=fmt,
           colorize=False,
           filter=lambda record: record['level'].name == 'ERROR',
           level="INFO",
           encoding="utf-8")
logger.add("logs/critical.log",
           format=fmt,
           colorize=False,
           filter=lambda record: record['level'].name == 'CRITICAL',
           level="INFO",
           encoding="utf-8")

logger.add("logs/main.log",
           format=fmt,
           colorize=False,
           filter=lambda record: record['level'].name == 'TRACE',
           level="TRACE",
           encoding="utf-8")
logger.add("logs/main.log",
           format=fmt,
           colorize=False,
           filter=lambda record: record['level'].name == 'DEBUG',
           level="DEBUG",
           encoding="utf-8")
logger.add("logs/main.log",
           format=fmt,
           colorize=False,
           filter=lambda record: record['level'].name == 'INFO',
           level="INFO",
           encoding="utf-8")
logger.add("logs/main.log",
           format=fmt,
           colorize=False,
           filter=lambda record: record['level'].name == 'SUCCESS',
           level="TRACE",
           encoding="utf-8")
logger.add("logs/main.log",
           format=fmt,
           colorize=False,
           filter=lambda record: record['level'].name == 'WARNING',
           level="DEBUG",
           encoding="utf-8")
logger.add("logs/main.log",
           format=fmt,
           colorize=False,
           filter=lambda record: record['level'].name == 'ERROR',
           level="INFO",
           encoding="utf-8")
logger.add("logs/main.log",
           format=fmt,
           colorize=False,
           filter=lambda record: record['level'].name == 'CRITICAL',
           level="INFO",
           encoding="utf-8")

s = logger
