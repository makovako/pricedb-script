#!/usr/bin/env python3

import logging
import logging.handlers
import time
from datetime import datetime


def main2():
    current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    print(current_datetime)
    logging.basicConfig(filename=f'example{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log',
        filemode='w',
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(name)s - %(module)s : %(message)s")
    time.sleep(10)
    logging.debug("lala")
    time.sleep(10)
    logging.info("lala")

def main():
    my_logger = logging.getLogger()
    my_logger.setLevel(logging.DEBUG)

    handler = logging.handlers.SysLogHandler(address='/dev/log')
    my_logger.addHandler(handler)

    my_logger.debug("this is debug")
    my_logger.critical("this is critical")

if __name__ == '__main__':
    main2()