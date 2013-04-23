#! /usr/bin/env python
# -*- coding: gbk -*-
def initlog():
    import logging
    logger = logging.getLogger()
    hdlr = logging.FileHandler('copytjb.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.NOTSET)
    return logger
if __name__ == '__main__':
    list = ['1','2','3']
    x = initlog()
    for file in list: 
        x.debug(file)


    