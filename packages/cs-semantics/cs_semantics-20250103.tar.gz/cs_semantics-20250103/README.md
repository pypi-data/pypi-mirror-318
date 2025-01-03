Some basic functions and exceptions for various semantics shared by modules.

*Latest release 20250103*:
Initial PyPI release: ClosedError and @not_closed.

## <a name="ClosedError"></a>Class `ClosedError(builtins.Exception)`

Exception for operations which are invalid when something is closed.

## <a name="not_closed"></a>`not_closed(*da, **dkw)`

A decorator to wrap methods of objects with a `.closed` property
which should raise when `self.closed`.
This raised `ClosedError` if the object is closed.

Excample:

    @not_closed
    def doit(self):
        ... proceed know we were not closed ...

# Release Log



*Release 20250103*:
Initial PyPI release: ClosedError and @not_closed.
