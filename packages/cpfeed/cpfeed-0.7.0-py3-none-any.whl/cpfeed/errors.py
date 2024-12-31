class InvalidCoinError(Exception):
    pass

class InvalidCurrencyError(Exception):
    pass


ERROR_MESSAGES = {
    400: 'Bad Request: 400',
    429: 'Too Many Requests: 429',
    503: 'Service Unavailable: 503',
    500: 'Internal Server Error: 500',
    403: 'Forbidden: 403',
    1020: 'Access Denied: 1020'
}
