#coding=utf-8


import requests
import collecitons

import tqdm


def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = requests.get(url)
    if resp.status_code != 200:     # 1
        resp.raise_for_status()
    return resp.content


def download_one(cc, base_url, verbose=False):
    try:
        image = get_flag(base_url, cc)
    except requests.exceptions.HTTPError as exc:    # 2
        res = exc.response
        if res.status_code == 404:
            status = HTTPStatus.not_found   # 3 (见示例A-10)
            msg = 'not found'
        else:   # 4
            raise
    else:
        save_flag(image, cc.lower() + '.gif')
        status = HTTPStatus.ok
        msg = 'OK'
    if verbose:     # 5
        print(cc, msg)
    return Result(status, cc)   # 6


def download_many(cc_list, base_url, verbose, max_req):
    counter = collecitons.Counter()     # 1
    cc_iter = sorted(cc_list)   # 2
    if not verbose:
        cc_iter = tqdm.tqdm(cc_iter)    # 3
    for cc in cc_iter:  # 4
        try:
            res = download_one(cc, base_url, verbose)   # 5
        except requests.exceptions.HTTPError as exc:    # 6
            error_msg = 'HTTP error {res.status_code} - {res.reason}'
            error_msg = error_msg.format(res=exc.response)
        except requests.exceptions.ConnectionError as exc:  # 7
            error_msg = 'Connection error'
        else:   # 8
            error_msg = ''
            status = res.status
        if error_msg:
            status = HTTPStatus.error   # 9
        counter[status] += 1    # 10
        if verbose and error_msg:   # 11
            print('** Error for {}: {}'.format(cc, error_msg))
    return counter  # 12