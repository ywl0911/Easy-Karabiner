# -*- coding: utf-8 -*-

class NeedOverrideError(NotImplementedError):
    def __init__(self):
        errmsg = 'You need override this method'
        super(NotImplementedError, self).__init__(self, errmsg)

class ConfigError(Exception):
    pass

class UnsupportDefType(ConfigError):
    pass

class UndefinedFilterException(ConfigError):
    pass