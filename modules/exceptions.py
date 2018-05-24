class AzException(Exception):
    pass


class EmptyDatasetException(AzException):
    pass


class AbsentUserConfigException(AzException):
    pass


class NotDefinedConfigValue(AzException):
    pass


class ValidationException(AzException):
    pass

class NoArgsException(AzException):
    pass
