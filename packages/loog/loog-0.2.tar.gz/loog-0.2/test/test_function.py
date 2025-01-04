from loog import LogLevel, log


def test_function(x):
    log("DEBUG test", LogLevel.DEBUG)
    log("INFO test", LogLevel.INFO)
    log("WARNING test", LogLevel.WARNING)
    log("ERROR test", LogLevel.ERROR)
    log("CRITICAL test", LogLevel.CRITICAL)

    for i in range(10):
        log(f"INFO test {i}", LogLevel.INFO)


if __name__ == "__main__":
    test_function()
