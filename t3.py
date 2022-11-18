import csv
import datetime
import time
from functools import wraps


def universal_cache(time_in_minutes, cache_to_file=False):
    def write_to_logs(data):
        now = datetime.datetime.now()
        with open('cache_log.txt', 'a+') as log_file:
            csv_writer = csv.writer(log_file)
            csv_writer.writerow([now] + list(data.values()))

    def get_now():
        return time.time()

    def wrapper(func):

        cache = {}

        @wraps(func)
        def inner(*args, **kwargs):

            if str(args) in cache:
                if int(get_now()) - int(cache[str(args)][1]) / 60 >= time_in_minutes:
                    del cache[str(args)]
                else:
                    return cache[str(args)][0]

            cache.update({str(args): [func(*args, **kwargs), get_now()]})

            if cache_to_file:
                write_to_logs(
                    {
                        'function_name': func.__name__,
                        'args': args,
                        'kwargs': kwargs
                    }
                )

            return cache[str(args)][0]

        return inner

    return wrapper


@universal_cache(3, cache_to_file=True)
def calc_price(route, comf_class, additions, *args, **kwargs):
    """ asdasdasd """
    print('Some handling of very important data with super hard functions')


calc_price(1, 2, 3, 4, 5, 6, 7, 8)
calc_price(1, 2, 3, 4, 5, 6, 7, 8)
calc_price(1, 2, 3, 4, 5, 6, 7, 8)
calc_price(1, 2, 3, 4, 5, 6, 7, 8)
calc_price(1, 2, 3, 4, 5, 6, 7, 8)
calc_price(1, 2, 3, 4, 5, 6, 7, 8)
