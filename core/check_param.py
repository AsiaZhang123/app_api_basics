
class CheckParam(object):
    def __init__(self):
        self.check_rules = dict()

    def register_check_param(self, check_param=None, url_prefix=''):
        if not isinstance(check_param, SubCheckParam):
            raise RuntimeError('check_param is not a SubCheckParam object. '
                               'type: %s' % type(check_param))

        check_rules = check_param.get_check_rules()

        for check_rule in check_rules:
            url = check_rule.url
            version = check_rule.version
            methods = check_rule.methods
            f = check_rule.f

            self.check_rules[str({'url':url_prefix + url,
                                  'version':sorted(version),
                                  'methods': sorted(methods)})] = f
    def get_check_rules(self):
        return self.check_rules


class SubCheckParam(object):
    def __init__(self,default_methods):
        self.check_rules = list()
        self.default_methods = default_methods

    def check(self, url=None, version=None, methods=None):
        methods = methods if methods is not None else self.default_methods

        def decorator(f):
            if not url:
                raise ValueError('A non-empty url is required.')
            if not methods:
                raise ValueError('A non-empty method is required.')

            self.__add_check_rule(url, version, methods, f)

            return f
        return decorator

    def __add_check_rule(self, url, version, methods, f):
        if version and isinstance(version, list):
            version = sorted(version)
        else:
            version = []

        self.check_rules.append(CheckRule(url=url, version=version, methods=methods, f=f))

    def get_check_rules(self):
        return self.check_rules


class CheckRule(object):
    def __init__(self,url, version, methods, f):
        self.url = url
        self.version = version
        self.methods = methods
        self.f = f


def build_check_rule(url=None, version=None, methods=None):
    if not url:
        raise ValueError('A non-empty url is required.')
    if not methods:
        raise ValueError('A non-empty method is required.')

    if version and isinstance(version, list):
        version = sorted(version)
    else:
        version = []

    return str({'url': url,'version': version,'methods': sorted(methods)})