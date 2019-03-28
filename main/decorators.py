import logging, functools, sys, traceback, os

# Decorator class for collection of utility decorators
class Decorators:
    # use basic formatter
    logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s', level=logging.DEBUG)
    # instantiate logger
    _logger = logging.getLogger('app_logger')
    _root_path = os.path.dirname(sys.modules['__main__'].__file__)
    
    # decorator for safe handling of exceptions and logging out error    
    @staticmethod
    def catch_and_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return_output = func(*args, **kwargs)
            except Exception as e:
                # extract relevant data and log out error and origin
                exc_type, exc_obj, exc_tb = sys.exc_info()
                file_path = traceback.extract_tb(exc_tb)[-1][0].replace(Decorators._root_path, '')
                line_number = traceback.extract_tb(exc_tb)[-1][1]
                Decorators._logger.error("%s:%s | %s" % (file_path, line_number, str(e)) )
                raise(e)
            return return_output
        return wrapper
    