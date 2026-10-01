try:
    import module_that_does_not_exist
except ModuleNotFoundError:
    print("The requested module is not installed or does not exist.")