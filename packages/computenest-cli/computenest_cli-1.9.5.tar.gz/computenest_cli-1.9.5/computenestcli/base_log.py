import functools
import logging
import logging.config
import threading
import time
import yaml
import sys

if sys.version_info >= (3, 9):
    from importlib import resources
else:
    import importlib_resources as resources

from computenestcli.exception.cli_common_exception import CliCommonException
from computenestcli.common.logging_constant import PROCESS_LOGGER, DEFAULT_PROGRESS, DEVELOPER_INFO_LOG_HANDLER_NAME, \
    LOGGING_CLOSURE_NAME
from computenestcli.common.logging_type import LoggingType

logging_initialized = False
global_config = None


class UTCFormatter(logging.Formatter):
    converter = time.gmtime


class InfoWarningFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO or record.levelno == logging.WARNING


def load_process_config():
    global global_config
    if global_config is None:
        logger_path = resources.files(__package__).joinpath(PROCESS_LOGGER)
        with logger_path.open() as f:
            global_config = yaml.safe_load(f.read())
    return global_config


def setup_logging(config_file='log.conf'):
    """Set up logging configuration from a configuration file."""
    global logging_initialized
    if not logging_initialized:
        # 获取配置文件的路径
        with resources.path(__package__, config_file) as config_path:
            logging.config.fileConfig(config_path)
            # 设置所有格式化器的转换器为 time.gmtime（UTC时间）
            for logger_name in logging.root.manager.loggerDict:
                logger = logging.getLogger(logger_name)
                for handler in logger.handlers:
                    formatter = handler.formatter
                    if isinstance(formatter, logging.Formatter):
                        formatter.converter = time.gmtime

            # 处理 root logger 的处理器
            for handler in logging.root.handlers:
                formatter = handler.formatter
                if isinstance(formatter, logging.Formatter):
                    formatter.converter = time.gmtime
        logging_initialized = True


def get_logger(name):
    """Get a logger with the specified name."""
    return logging.getLogger(name)


def get_developer_logger():
    setup_logging()
    developer_logger = get_logger(LoggingType.DEVELOPER.value)
    for handler in developer_logger.handlers:
        if handler.get_name() == DEVELOPER_INFO_LOG_HANDLER_NAME:
            handler.addFilter(InfoWarningFilter())
    return developer_logger


def get_user_logger():
    setup_logging()
    return get_logger(LoggingType.USER.value)


def get_user_logger(service_name=None):
    """
    获取用户 Logger，并根据 service_name 设置日志格式。
    如果 service_name 不为空，则采用包含 service_name 的格式。
    否则，采用默认格式。
    """
    setup_logging()
    user_logger = get_logger(LoggingType.USER.value)

    # 定义有 service_name 和无 service_name 的格式
    fmt_with_service = '[%(asctime)s][%(levelname)s][%(service_name)s] %(message)s'
    fmt_without_service = '[%(asctime)s][%(levelname)s]%(message)s'
    datefmt = '%Y-%m-%dT%H:%M:%SZ'

    # 创建一个自定义格式化器，根据是否有 service_name 来选择格式
    class CustomFormatter(UTCFormatter):
        """自定义格式化器，根据是否提供 service_name 使用不同的日志格式."""

        def __init__(self, fmt_with_service, fmt_without_service, datefmt=None):
            super().__init__(fmt_with_service, datefmt)
            self.fmt_with_service = fmt_with_service
            self.fmt_without_service = fmt_without_service

        def format(self, record):
            if getattr(record, 'service_name', ''):
                self._style._fmt = self.fmt_with_service
            else:
                self._style._fmt = self.fmt_without_service
            return super().format(record)

    # 实例化 CustomFormatter
    formatter = CustomFormatter(fmt_with_service, fmt_without_service, datefmt)

    # 为 user_logger 的所有处理器设置 CustomFormatter
    for handler in user_logger.handlers:
        handler.setFormatter(formatter)

    # 定义过滤器，根据 service_name 的存在与否设置 record.service_name
    if service_name:
        def add_service_name(record):
            record.service_name = service_name
            return True

        user_logger.addFilter(add_service_name)
    else:
        def add_empty_service_name(record):
            record.service_name = ''
            return True

        user_logger.addFilter(add_empty_service_name)

    return user_logger


def __get_inner_logger():
    setup_logging()
    return get_logger(LoggingType.INNER.value)


"""
Decorator to log the execution of a process.

:param service_name: Represents the execution of a CLI command, e.g., `import`.
:param process_name: A major step in the execution, e.g., `BuildArtifacts`.
:param task_name: A minor step/component of the process, e.g., AcrImageBuild.
:param periodic_logging: A boolean flag indicating if periodic logs should be printed 
                         for long-running tasks.
:param dynamic_logging: A boolean flag indicating if dynamic logging should be enabled.
                        If True, passes a logging closure to the decorated function.

用于记录进程执行的装饰器。
:param service_name: 表示CLI命令的执行，例如 import。
:param process_name: 执行过程中的主要步骤，例如 BuildArtifacts。
:param task_name: 进程中的次要步骤或组件，例如 AcrImageBuild。
:param periodic_logging: 一个布尔标志，指示是否应为长时间运行的任务打印周期性日志。
:param dynamic_logging: 一个布尔标志，指示是否应启用动态日志记录。
如果为 True，则将日志记录闭包传递给装饰的函数。
"""


def log_monitor(service_name, process_name, task_name=None, periodic_logging=False, dynamic_logging=False,
                periodic_logging_interval=30):
    def get_step_info(service_name, step_name):
        config = load_process_config()
        process_steps = config.get(service_name, {})
        if not process_steps:
            raise ValueError(f"Service {service_name} not found.")

        step_order = process_steps.get(step_name)
        if step_order is None:
            return DEFAULT_PROGRESS

        total_steps = max(process_steps.values())  # 获取最大的步骤数作为总步数
        return f"{step_order}/{total_steps}"

    progress = get_step_info(service_name, process_name)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = __get_inner_logger()
            extra = {'service_name': service_name, 'progress': progress}

            def log_message(message, error=False):
                if error:
                    logger.error(message, extra=extra)
                else:
                    logger.info(message, extra=extra)

            # 可供调用的闭包，用于被装饰的对象动态传入日志
            def dynamic_logging_message(message):
                logger.info(message, extra=extra)

            if dynamic_logging:
                kwargs[LOGGING_CLOSURE_NAME] = dynamic_logging_message

            stop_thread = None
            logging_thread = None

            def periodic_logging_task():
                if stop_thread:
                    while not stop_thread.is_set():
                        # 使用 wait 代替 sleep，使其可以被提前中断
                        if stop_thread.wait(periodic_logging_interval):
                            break
                        if task_name:
                            logger.info(f"{task_name} is processing...", extra=extra)
                        else:
                            logger.info(f"{process_name} is processing...", extra=extra)

            try:

                if periodic_logging:
                    stop_thread = threading.Event()
                    logging_thread = threading.Thread(target=periodic_logging_task)
                    logging_thread.start()
                else:
                    stop_thread = None
                    logging_thread = None

                # 日志开始
                if task_name:
                    log_message(f"{process_name}-{task_name} Start!")
                else:
                    log_message(f"{process_name} Start!")
                logger.info("Processing...", extra=extra)
                result = func(*args, **kwargs)

                if logging_thread is not None:
                    stop_thread.set()
                    logging_thread.join()

                # 日志成功
                if task_name:
                    log_message(f"{process_name}-{task_name} Success!")
                else:
                    log_message(f"{process_name} Success!")

                return result
            except Exception as e:
                if logging_thread is not None:
                    stop_thread.set()
                    logging_thread.join()
                if task_name:
                    log_message(f"Error occurred in {process_name}-{task_name}\n"
                                f"{process_name}-{task_name} Failed!", error=True)
                else:
                    log_message(f"Error occurred in {process_name}\n"
                                f"{process_name} Failed!", error=True)

                raise CliCommonException(f"[{service_name}] CLI has stopped running due to an error in {process_name}",
                                         original_exception=e) from e

        return wrapper

    return decorator
