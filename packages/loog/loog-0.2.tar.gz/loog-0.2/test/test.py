from test_function import test_function

from loog import (
    LogLevel,
    log,
    log_off,
    log_on,
    log_to_file,
    set_display_level,
    set_loglevel_color,
)


def main():
    log("DEBUG test", LogLevel.DEBUG)
    log("INFO test", LogLevel.INFO)
    log("WARNING test", LogLevel.WARNING)
    log("ERROR test", LogLevel.ERROR)
    log("CRITICAL test", LogLevel.CRITICAL)

    log_off()

    sub_module()

    test_function(1)


def sub_module():
    log("DEBUG test", LogLevel.DEBUG)
    log("INFO test", LogLevel.INFO)
    log("WARNING test", LogLevel.WARNING)
    log("ERROR test", LogLevel.ERROR)
    log("CRITICAL test", LogLevel.CRITICAL)

    sub_module2()


def sub_module2():
    log_on()

    log("DEBUG test", LogLevel.DEBUG)
    log("INFO test", LogLevel.INFO)
    log("WARNING test", LogLevel.WARNING)
    log("ERROR test", LogLevel.ERROR)
    log("CRITICAL test", LogLevel.CRITICAL)

    # log_off()


if __name__ == "__main__":
    set_display_level(LogLevel.DEBUG)
    # log_to_file("log_test.log")
    # set_loglevel_color(LogLevel.ERROR, "#000000")
    main()
