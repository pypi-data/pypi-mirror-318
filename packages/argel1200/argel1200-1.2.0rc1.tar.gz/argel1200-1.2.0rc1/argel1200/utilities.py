import errno
import click
import dumper
import logging
import os
import re
import sys
import platform
import traceback

#
# Dumper utilities
#

def get_variable_name(stack_back=-2):
    """
    Called by dumps()

    Pulls the variable names from the function that called this function

    This function traces back through the call stack, so we have to subtract -1
    for every intermediate function, including this function.

    Subtract -1 for every intermediate step in the call stack.
    So we have: -1 for this function -1 for whoever called it = -2, which is the default.

    If there are more functions in the middle then subtract -1 for each of them. For example:
    -1 for this function -1 for dumps(), and -1 for whoever called dumps = -3.

    :param stack_back: How far back we need to go in the stack (see above description)
    :return: Returns the variable name(s)
    """
    stack = traceback.extract_stack()
    caller_name = stack[-2].name
    caller_len = len(caller_name)
    line = stack[stack_back].line
    # Example line: print('fu', 'bar/', argel1200.utilities.dumps(header), '/foobar')
    my_line = re.sub(r'(\s|\u180B|\u200B|\u200C|\u200D|\u2060|\uFEFF)+', '', line)  # Remove all whitespace
    caller_start = my_line.find(caller_name + '(')  # Find where the caller string is (e.g. where "dumps(" starts)
    caller_end = caller_start + caller_len  # And where it ends (the index of the '(' in "dumps("  )
    my_line_substr = my_line[caller_end:]  # Get a substr of everything past the caller (e.g. "dumps").

    # Now let's find all the variable names passed in
    vars_passed_in = []
    parens = 0
    str_start = None
    for idx, char in enumerate(my_line_substr):
        if char == '(':
            parens += 1
            str_start = idx + 1
        elif char == ',' or char == ')':
            vars_passed_in.append(my_line_substr[str_start:idx])
            str_start = idx + 1
            if char == ')':
                parens -= 1
                if parens == 0:
                    break
    return vars_passed_in


def dumps(*items):
    """
    Front end to dumper.dumps that does some helpful things like
    finding the variable names and adding them to the output string
    """
    dumper.max_depth = 10
    item_names = get_variable_name(-3)
    ret_str = ""
    for idx, item in enumerate(items):
        if idx > 0:
            ret_str += f"\n"
        item_name = item_names[idx]
        ret_str += f"'{item_name}' = "
        ret_str += dumper.dumps(item)  # string version of dump
    return ret_str


#
# Class utilities
#

def import_class_from_string(path, parent_class_name=''):
    """
    Takes a string name of a class and returns an actual instance of that class.
    Useful when you need to (or it's just more elegant to) dynamically determine the class.

    :param path: The full class path.  (For example:  package.module.class)
    :param parent_class_name: Name of the parent class (For example: BaseClass)
    :return: The class, the parent class, or None
    """
    from importlib import import_module
    module_path, _, class_name = path.rpartition('.')
    mod = import_module(module_path)
    try:
        klass = getattr(mod, class_name)
    except:
        if parent_class_name:
            try:
                klass = getattr(mod, parent_class_name)
            except:
                return None
        else:
            return None
    return klass

#
# Logging utilities
#

def add_logging_level(level_name, level_num, method_name=None):
    """
    Dynamically adds a new logging level to the Python logging module.

    :param level_name: Name of the logging level (e.g. 'TRACE', 'MEMDUMP').
    :param level_num: Numeric value of the logging level (e.g. logging.DEBUG - 1 for TRACE).
    :param method_name: The method name to be added to the logging module (e.g. 'trace').
                        If not provided, both lowercase and uppercase versions of level_name
                        will be created.
    """
    # Determine method names based on whether method_name is provided
    if not method_name:  # If no method_name provided, generate lowercase and uppercase names by default
        method_names = [level_name.lower(), level_name.upper()]
    else:
        # Only use the explicitly provided method_name
        method_names = [method_name]

    # Check for conflicts for all method names in the list
    for name in method_names:
        if hasattr(logging, name):
            raise ValueError(f"Logging level or method {name} already exists")
    if hasattr(logging, level_name):
        raise ValueError(f"Logging level {level_name} already exists")

    # Add the level to the logging module
    logging.addLevelName(level_num, level_name)
    setattr(logging, level_name, level_num)  # Add the constant in UPPERCASE

    # Define the custom logging methods
    def log_for_level(self, message, *args, **kwargs):
        if self.isEnabledFor(level_num):
            self._log(level_num, message, args, **kwargs)

    def log_to_root(message, *args, **kwargs):
        logging.log(level_num, message, *args, **kwargs)

    # Add each method name in the list to the logger and root logger
    for name in method_names:
        setattr(logging.getLoggerClass(), name, log_for_level)
        setattr(logging, name, log_to_root)


def logging_init(return_logger=False):
    """
    Initializes the logging module with custom levels and a default configuration.

    TRACE is for more detail beyond DEBUG
    MEMDUMP for even more detail than TRACE.
    """
    add_logging_level('TRACE', logging.DEBUG - 1)
    add_logging_level('MEMDUMP', logging.DEBUG - 9)
    logging.basicConfig(level=logging.MEMDUMP, format='%(asctime)s - %(levelname)s - %(message)s')

    log_levels = {
        'memdump': logging.MEMDUMP,
        'trace': logging.TRACE,
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL,
        }

    if return_logger is True:
        logger = logging.getLogger()
        return [logger, log_levels]
    else:
        return log_levels



def log_or_print(msg, logger=None, level='debug'):
    """
    Logs the message via the supplied logger or prints to console if no logger is provided.
    If the provided logging level is invalid, logs a warning and defaults to 'critical'.

    :param msg: The message to log or print.
    :param logger: Logger instance, optional.
    :param level: Logging level as a string (e.g., 'debug', 'info', 'error').
                  Defaults to 'debug'.
    """
    if logger:
        # Check if the provided logging level is valid
        if hasattr(logger, level):
            log_method = getattr(logger, level)
            log_method(msg)
        else:
            # Log a message indicating the issue and fall back to critical
            logger.error(f"Invalid logging level '{level}' passed to log_or_print. Falling back to 'critical'.")
            logger.critical(msg)
    else:
        print(msg)


#
# File utilities
#

def open_file(filename, mode='r', newline='', encoding='utf-8', logger=None):
    """
    Opens a file, with some error handling and enhanced functionality for permission checking.
    :param encoding: Encoding used by the file
    :param filename: The name of the file to pass to open()
    :param mode: The read/write mode to pass to open()
    :param newline: The newline to pass to open()
    :param logger: Optional instance of the logging module
    :return: The file handle (or it exits if there is an error)
    """

    # Step 1: Check permissions
    try:
        access_mode = os.R_OK if 'r' in mode else os.W_OK
        if not os.access(filename, access_mode):
            raise PermissionError(f"ERROR: Insufficient permissions to access {filename} in mode {mode}.")
    except PermissionError as err:
        log_or_print(f"ERROR: {err}", logger=logger, level='critical')
        sys.exit(1)
    except Exception as err:
        log_or_print(
            f"ERROR: Unexpected error occurred while checking permissions for {filename}: {repr(err)}",
            logger=logger,
            level='critical'
            )
        sys.exit(1)

    # Step 2: Try to open the file
    try:
        if mode == 'rb' or mode == 'wb':  # Binary mode
            file_handle = open(filename, mode)
        else:
            file_handle = open(filename, mode, newline=newline, encoding=encoding)
    except FileNotFoundError:
        log_or_print(f"ERROR: File {filename} not found. Aborting.", logger=logger, level='critical')
        sys.exit(1)
    except PermissionError:
        if platform.system() == 'Windows':  # Windows-specific locking warning
            log_or_print(
                f"ERROR: File {filename} might be open in another application or locked on Windows.",
                logger=logger,
                level='critical'
                )
        else:
            log_or_print(f"ERROR: Permission error accessing {filename}.", logger=logger, level='critical')
        sys.exit(1)
    except OSError as err:
        error_details = errno.errorcode.get(err.errno, "Unknown error")
        log_or_print(
            f"ERROR: Cannot open file {filename}; mode: {mode}; (OSError.errno: {err.errno}; message: {error_details}); Exception: {repr(err)}",
            logger=logger,
            level='critical'
            )
        sys.exit(os.EX_OSFILE)
    except Exception as err:
        log_or_print(f"ERROR: Unexpected error occurred while opening {filename}: {repr(err)}", logger=logger,
                     level='critical')
        sys.exit(1)

    # Return the open file handle
    return file_handle



# Click (command-line/cli) utilities

def process_cli_using_click(my_cli):
    """
    Because we are *not* using click's standalone mode, we need to do our own error handling.
    This function takes care of that.

    :param my_cli:  The function you defined via click to process the command line arguments
    """
    click_invoke_rc = None

    try:
        click_invoke_rc = my_cli(standalone_mode=False)
    except click.exceptions.NoSuchOption as err:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(f"Invalid option detected:")
        print(f"Type: {exc_type}; Value: {exc_value}; Traceback: {exc_traceback}")
        print(f"Try running the program with -h or --help.")
        exit(3)
    except click.exceptions.UsageError as err:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(f"A usage error occurred:")
        print(f"Type: {exc_type}; Value: {exc_value}; Traceback: {exc_traceback}")
        print(f"Try running the program with -h or --help.")
        exit(5)
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(f"An unexpected command line processing error occurred:")
        print(f"Type: {exc_type}; Value: {exc_value}; Traceback: {exc_traceback}")
        print(f"Try running the program with -h or --help.")
        exit(10)

    if click_invoke_rc == 0:  # Catch if -h, --help, --version, or something unknown was specified
        exit(1)
