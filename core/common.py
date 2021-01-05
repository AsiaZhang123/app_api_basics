import uuid
import json
import urllib.parse

from flask import request

def get_trace_id():
    try:
        if request.trace_id is None:
            return uuid.uuid1()
        else:
            return request.trace_id
    except Exception:
        return str(uuid.uuid1())


def is_none(arg):
    return not arg or str(arg) in ['null','none','false']


def get_version():
    try:
        return request.version
    except AttributeError:
        pass
    return request.args.get('version')


def get_ip_address():
    try:
        if request.headers.get('x-forwarded-for') is not None:
            ip_address = str(request.headers.get('x-forwarded-for'))
            if "," in ip_address:
                return ip_address.split(",")[0]
            return ip_address
    except:
        pass
    return '127.0.0.1'


# 获取get请求时，传的参数params并解url
def get_request_params():
    try:
        request_params = json.loads(urllib.parse.unquote_plus(request.args.get('params')))
        params = get_common_params(request_params)
    except Exception:
        params = None
    return params


# 获取post请求时，传的参数params并解json
def post_request_params():
    try:
        request_params = json.loads(request.data)
        params = get_common_params(request_params)
    except Exception:
        params = None

    return params


# 获取form_data中的参数并转换为字典格式
def form_data_to_dict():
    return {key: dict(request.form)[key][0] for key in dict(request.form)}


# 获取公共参数并加到params中
def get_common_params(params):
    try:
        if request.args.get('platform') is not None:
            params['platform'] = request.args.get('platform')
    except Exception:
        pass
    return params