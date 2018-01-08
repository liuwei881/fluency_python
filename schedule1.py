#coding=utf-8

import warnings

import osconfeed    # 1


DB_NAME = 'schedule1_db'
CONFERENCE = 'conference.115'


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)    # 2


def load_db(db):
    raw_data = osconfeed.load() # 3
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():   # 4
        record_type = collection[:-1]   # 5
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial']) # 6
            record['serial'] = key  # 7
            db[key] = Record(**record)  # 8