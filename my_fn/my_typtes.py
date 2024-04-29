# For many years, Python has supported type hints
# NB type hints DO NOT AFFECT code execution
# remember - type hints do not exist at run-time
# the purpose of a type hint is two-fold:
#  - code hinting is improved (if linting and code completion tools are extant)
#  - development-time coding is more rigorous

class MyClass():
    '''type hints can help with docstring - IDE may help auto-generate'''
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        return []

