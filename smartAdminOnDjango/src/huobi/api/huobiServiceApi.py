#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-20 15:40:03
# @Author  : KlausQiu
# @QQ      : 375235513
# @github  : https://github.com/KlausQIU

from huobi.Utils import *

'''
Market data API
'''


# ��ȡKLine
def get_kline(symbol, period, size=150):
    """
    :param symbol
    :param period: ��ѡֵ��{1min, 5min, 15min, 30min, 60min, 1day, 1mon, 1week, 1year }
    :param size: ��ѡֵ�� [1,2000]
    :return:
    """
    params = {'symbol': symbol,
              'period': period,
              'size': size}

    url = MARKET_URL + '/market/history/kline'
    return http_get_request(url, params)


# ��ȡmarketdepth
def get_depth(symbol, type):
    """
    :param symbol
    :param type: ��ѡֵ��{ percent10, step0, step1, step2, step3, step4, step5 }
    :return:
    """
    params = {'symbol': symbol,
              'type': type}
    
    url = MARKET_URL + '/market/depth'
    return http_get_request(url, params)


# ��ȡtradedetail
def get_trade(symbol):
    """
    :param symbol
    :return:
    """
    params = {'symbol': symbol}

    url = MARKET_URL + '/market/trade'
    return http_get_request(url, params)


# ��ȡmerge ticker
def get_ticker(symbol):
    """
    :param symbol: 
    :return:
    """
    params = {'symbol': symbol}

    url = MARKET_URL + '/market/detail/merged'
    return http_get_request(url, params)


# ��ȡ Market Detail 24Сʱ�ɽ�������
def get_detail(symbol):
    """
    :param symbol
    :return:
    """
    params = {'symbol': symbol}

    url = MARKET_URL + '/market/detail'
    return http_get_request(url, params)

# ��ȡ  ֧�ֵĽ��׶�
def get_symbols(long_polling=None):
    """
    """
    params = {}
    if long_polling:
        params['long-polling'] = long_polling
    path = '/v1/common/symbols'
    return api_key_get(params, path)

'''
Trade/Account API
'''


def get_accounts():
    """
    :return: 
    """
    path = "/v1/account/accounts"
    params = {}
    return api_key_get(params, path)

ACCOUNT_ID = 0
# ��ȡ��ǰ�˻��ʲ�
def get_balance(acct_id=None):
    """
    :param acct_id
    :return:
    """
    global ACCOUNT_ID
    
    if not acct_id:
        accounts = get_accounts()
        acct_id = accounts['data'][0]['id'];

    url = "/v1/account/accounts/{0}/balance".format(acct_id)
    params = {"account-id": acct_id}
    return api_key_get(params, url)


# �µ�

# ������ִ�ж���
def send_order(amount, source, symbol, _type, price=0):
    """
    :param amount: 
    :param source: ���ʹ�ý���ʲ����ף������µ��ӿ�,�������source����д'margin-api'
    :param symbol: 
    :param _type: ��ѡֵ {buy-market���м���, sell-market���м���, buy-limit���޼���, sell-limit���޼���}
    :param price: 
    :return: 
    """
    try:
        accounts = get_accounts()
        acct_id = accounts['data'][0]['id']
    except BaseException as e:
        print ('get acct_id error.%s' % e)
        acct_id = ACCOUNT_ID

    params = {"account-id": acct_id,
              "amount": amount,
              "symbol": symbol,
              "type": _type,
              "source": source}
    if price:
        params["price"] = price

    url = '/v1/order/orders/place'
    return api_key_post(params, url)


# ��������
def cancel_order(order_id):
    """
    
    :param order_id: 
    :return: 
    """
    params = {}
    url = "/v1/order/orders/{0}/submitcancel".format(order_id)
    return api_key_post(params, url)


# ��ѯĳ������
def order_info(order_id):
    """
    
    :param order_id: 
    :return: 
    """
    params = {}
    url = "/v1/order/orders/{0}".format(order_id)
    return api_key_get(params, url)


# ��ѯĳ�������ĳɽ���ϸ
def order_matchresults(order_id):
    """
    
    :param order_id: 
    :return: 
    """
    params = {}
    url = "/v1/order/orders/{0}/matchresults".format(order_id)
    return api_key_get(params, url)


# ��ѯ��ǰί�С���ʷί��
def orders_list(symbol, states, types=None, start_date=None, end_date=None, _from=None, direct=None, size=None):
    """
    
    :param symbol: 
    :param states: ��ѡֵ {pre-submitted ׼���ύ, submitted ���ύ, partial-filled ���ֳɽ�, partial-canceled ���ֳɽ�����, filled ��ȫ�ɽ�, canceled �ѳ���}
    :param types: ��ѡֵ {buy-market���м���, sell-market���м���, buy-limit���޼���, sell-limit���޼���}
    :param start_date: 
    :param end_date: 
    :param _from: 
    :param direct: ��ѡֵ{prev ��ǰ��next ���}
    :param size: 
    :return: 
    """
    params = {'symbol': symbol,
              'states': states}

    if types:
        params['types'] = types
    if start_date:
        params['start-date'] = start_date
    if end_date:
        params['end-date'] = end_date
    if _from:
        params['from'] = _from
    if direct:
        params['direct'] = direct
    if size:
        params['size'] = size
    url = '/v1/order/orders'
    return api_key_get(params, url)


# ��ѯ��ǰ�ɽ�����ʷ�ɽ�
def orders_matchresults(symbol, types=None, start_date=None, end_date=None, _from=None, direct=None, size=None):
    """
    
    :param symbol: 
    :param types: ��ѡֵ {buy-market���м���, sell-market���м���, buy-limit���޼���, sell-limit���޼���}
    :param start_date: 
    :param end_date: 
    :param _from: 
    :param direct: ��ѡֵ{prev ��ǰ��next ���}
    :param size: 
    :return: 
    """
    params = {'symbol': symbol}

    if types:
        params['types'] = types
    if start_date:
        params['start-date'] = start_date
    if end_date:
        params['end-date'] = end_date
    if _from:
        params['from'] = _from
    if direct:
        params['direct'] = direct
    if size:
        params['size'] = size
    url = '/v1/order/matchresults'
    return api_key_get(params, url)



# �������������
def withdraw(address, amount, currency, fee=0, addr_tag=""):
    """
    :param address_id: 
    :param amount: 
    :param currency:btc, ltc, bcc, eth, etc ...(���Pro֧�ֵı���)
    :param fee: 
    :param addr-tag:
    :return: {
              "status": "ok",
              "data": 700
            }
    """
    params = {'address': address,
              'amount': amount,
              "currency": currency,
              "fee": fee,
              "addr-tag": addr_tag}
    url = '/v1/dw/withdraw/api/create'

    return api_key_post(params, url)

# ����ȡ�����������
def cancel_withdraw(address_id):
    """
    :param address_id: 
    :return: {
              "status": "ok",
              "data": 700
            }
    """
    params = {}
    url = '/v1/dw/withdraw-virtual/{0}/cancel'.format(address_id)

    return api_key_post(params, url)


'''
���API
'''

# ������ִ�н������


def send_margin_order(amount, source, symbol, _type, price=0):
    """
    :param amount: 
    :param source: 'margin-api'
    :param symbol: 
    :param _type: ��ѡֵ {buy-market���м���, sell-market���м���, buy-limit���޼���, sell-limit���޼���}
    :param price: 
    :return: 
    """
    try:
        accounts = get_accounts()
        acct_id = accounts['data'][0]['id']
    except BaseException as e:
        print ('get acct_id error.%s' % e)
        acct_id = ACCOUNT_ID

    params = {"account-id": acct_id,
              "amount": amount,
              "symbol": symbol,
              "type": _type,
              "source": 'margin-api'}
    if price:
        params["price"] = price

    url = '/v1/order/orders/place'
    return api_key_post(params, url)

# �ֻ��˻�����������˻�


def exchange_to_margin(symbol, currency, amount):
    """
    :param amount: 
    :param currency: 
    :param symbol: 
    :return: 
    """
    params = {"symbol": symbol,
              "currency": currency,
              "amount": amount}

    url = "/v1/dw/transfer-in/margin"
    return api_key_post(params, url)

# ����˻��������ֻ��˻�


def margin_to_exchange(symbol, currency, amount):
    """
    :param amount: 
    :param currency: 
    :param symbol: 
    :return: 
    """
    params = {"symbol": symbol,
              "currency": currency,
              "amount": amount}

    url = "/v1/dw/transfer-out/margin"
    return api_key_post(params, url)

# ������
def get_margin(symbol, currency, amount):
    """
    :param amount: 
    :param currency: 
    :param symbol: 
    :return: 
    """
    params = {"symbol": symbol,
              "currency": currency,
              "amount": amount}
    url = "/v1/margin/orders"
    return api_key_post(params, url)

# �黹���
def repay_margin(order_id, amount):
    """
    :param order_id: 
    :param amount: 
    :return: 
    """
    params = {"order-id": order_id,
              "amount": amount}
    url = "/v1/margin/orders/{0}/repay".format(order_id)
    return api_key_post(params, url)

# �������
def loan_orders(symbol, currency, start_date="", end_date="", start="", direct="", size=""):
    """
    :param symbol: 
    :param currency: 
    :param direct: prev ��ǰ��next ���
    :return: 
    """
    params = {"symbol": symbol,
              "currency": currency}
    if start_date:
        params["start-date"] = start_date
    if end_date:
        params["end-date"] = end_date
    if start:
        params["from"] = start
    if direct and direct in ["prev", "next"]:
        params["direct"] = direct
    if size:
        params["size"] = size
    url = "/v1/margin/loan-orders"
    return api_key_get(params, url)


# ����˻�����,֧�ֲ�ѯ��������
def margin_balance(symbol):
    """
    :param symbol: 
    :return: 
    """
    params = {}
    url = "/v1/margin/accounts/balance"
    if symbol:
        params['symbol'] = symbol
    
    return api_key_get(params, url)

    
  
        