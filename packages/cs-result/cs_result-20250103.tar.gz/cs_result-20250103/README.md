Result and friends: various subclassable classes for deferred delivery of values.

*Latest release 20250103*:
New @not_cancelled decorator for methods to raise CancellationError is self.cancelled.

A `Result` is the base class for several callable subclasses
which will receive values at a later point in time,
and can also be used standalone without subclassing.

A call to a `Result` will block until the value is received or the `Result` is cancelled,
which will raise an exception in the caller.
A `Result` may be called by multiple users, before or after the value has been delivered;
if the value has been delivered the caller returns with it immediately.
A `Result`'s state may be inspected (pending, running, ready, cancelled).
Callbacks can be registered via a `Result`'s .notify method.

An incomplete `Result` can be told to call a function to compute its value;
the function return will be stored as the value unless the function raises an exception,
in which case the exception information is recorded instead.
If an exception occurred, it will be reraised for any caller of the `Result`.

Trite example:

    R = Result(name="my demo")

Thread 1:

    # this blocks until the Result is ready
    value = R()
    print(value)
    # prints 3 once Thread 2 (below) assigns to it

Thread 2:

    R.result = 3

Thread 3:

    value = R()
    # returns immediately with 3

You can also collect multiple `Result`s in completion order using the `report()` function:

    Rs = [ ... list of Results of whatever type ... ]
    ...
    for R in report(Rs):
        x = R()     # collect result, will return immediately because
                    # the Result is complete
        print(x)    # print result

## <a name="after"></a>`after(Rs, R, func, *a, **kw)`

After the completion of `Rs` call `func(*a,**kw)` and return
its result via `R`; return the `Result` object.

Parameters:
* `Rs`: an iterable of Results.
* `R`: a `Result` to collect to result of calling `func`.
  If `None`, one will be created.
* `func`, `a`, `kw`: a callable and its arguments.

## <a name="bg"></a>`bg(func, *a, **kw)`

Dispatch a `Thread` to run `func`, return a `Result` to collect its value.

Parameters:
* `_name`: optional name for the `Result`, passed to the initialiser
* `_extra`: optional extra data for the `Result`, passed to the initialiser

Other parameters are passed to `func`.

## <a name="call_in_thread"></a>`call_in_thread(func, *a, **kw)`

Run `func(*a,**kw)` in a separate `Thread` via the `@in_thread` decorator.
Return or exception is as for the original function.

## <a name="in_thread"></a>`in_thread(func)`

Decorator to evaluate `func` in a separate `Thread`.
Return or exception is as for the original function.

This exists to step out of the current `Thread's` thread
local context, such as a database transaction associated
with Django's implicit per-`Thread` database context.

## <a name="not_cancelled"></a>`not_cancelled(*da, **dkw)`

A decorator for methods to raise `CancellationError` if `self.cancelled`.

## <a name="OnDemandFunction"></a>Class `OnDemandFunction(Result)`

Wrap a callable, run it when required.

State diagram:
![OnDemandFunction State Diagram](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPgo8IS0tIEdlbmVyYXRlZCBieSBncmFwaHZpeiB2ZXJzaW9uIDExLjAuMCAoMjAyNDA0MjguMTUyMikKIC0tPgo8IS0tIFRpdGxlOiBPbkRlbWFuZEZ1bmN0aW9uIFN0YXRlIERpYWdyYW0gUGFnZXM6IDEgLS0+Cjxzdmcgd2lkdGg9IjM0N3B0IiBoZWlnaHQ9IjIyMXB0Igogdmlld0JveD0iMC4wMCAwLjAwIDM0Ni42OSAyMjEuMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPgo8ZyBpZD0iZ3JhcGgwIiBjbGFzcz0iZ3JhcGgiIHRyYW5zZm9ybT0ic2NhbGUoMSAxKSByb3RhdGUoMCkgdHJhbnNsYXRlKDQgMjE3KSI+Cjx0aXRsZT5PbkRlbWFuZEZ1bmN0aW9uIFN0YXRlIERpYWdyYW08L3RpdGxlPgo8cG9seWdvbiBmaWxsPSJ3aGl0ZSIgc3Ryb2tlPSJub25lIiBwb2ludHM9Ii00LDQgLTQsLTIxNyAzNDIuNjksLTIxNyAzNDIuNjksNCAtNCw0Ii8+CjwhLS0gUEVORElORyAtLT4KPGcgaWQ9Im5vZGUxIiBjbGFzcz0ibm9kZSI+Cjx0aXRsZT5QRU5ESU5HPC90aXRsZT4KPGVsbGlwc2UgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgY3g9IjE2NS42OCIgY3k9Ii0xOTUiIHJ4PSI1MS4zNSIgcnk9IjE4Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjE2NS42OCIgeT0iLTE4OS45NSIgZm9udC1mYW1pbHk9IlRpbWVzLHNlcmlmIiBmb250LXNpemU9IjE0LjAwIj5QRU5ESU5HPC90ZXh0Pgo8L2c+CjwhLS0gQ0FOQ0VMTEVEIC0tPgo8ZyBpZD0ibm9kZTIiIGNsYXNzPSJub2RlIj4KPHRpdGxlPkNBTkNFTExFRDwvdGl0bGU+CjxlbGxpcHNlIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGN4PSI2NS42OCIgY3k9Ii0xOCIgcng9IjY1LjY4IiByeT0iMTgiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNjUuNjgiIHk9Ii0xMi45NSIgZm9udC1mYW1pbHk9IlRpbWVzLHNlcmlmIiBmb250LXNpemU9IjE0LjAwIj5DQU5DRUxMRUQ8L3RleHQ+CjwvZz4KPCEtLSBQRU5ESU5HJiM0NTsmZ3Q7Q0FOQ0VMTEVEIC0tPgo8ZyBpZD0iZWRnZTEiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPlBFTkRJTkcmIzQ1OyZndDtDQU5DRUxMRUQ8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNMTMzLjk5LC0xODAuNTZDMTExLjU2LC0xNjkuMTggODMuMDcsLTE1MC41NSA2OS4xOCwtMTI0LjUgNTYuNiwtMTAwLjkgNTcuMjIsLTY5LjkxIDYwLjA5LC00Ny42MyIvPgo8cG9seWdvbiBmaWxsPSJibGFjayIgc3Ryb2tlPSJibGFjayIgcG9pbnRzPSI2My41NSwtNDguMTcgNjEuNjEsLTM3Ljc1IDU2LjYzLC00Ny4xIDYzLjU1LC00OC4xNyIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSI4Ni45MyIgeT0iLTEwMS40NSIgZm9udC1mYW1pbHk9IlRpbWVzLHNlcmlmIiBmb250LXNpemU9IjE0LjAwIj5jYW5jZWw8L3RleHQ+CjwvZz4KPCEtLSBET05FIC0tPgo8ZyBpZD0ibm9kZTMiIGNsYXNzPSJub2RlIj4KPHRpdGxlPkRPTkU8L3RpdGxlPgo8ZWxsaXBzZSBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBjeD0iMjQ5LjY4IiBjeT0iLTE4IiByeD0iMzYuNTEiIHJ5PSIxOCIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyNDkuNjgiIHk9Ii0xMi45NSIgZm9udC1mYW1pbHk9IlRpbWVzLHNlcmlmIiBmb250LXNpemU9IjE0LjAwIj5ET05FPC90ZXh0Pgo8L2c+CjwhLS0gUEVORElORyYjNDU7Jmd0O0RPTkUgLS0+CjxnIGlkPSJlZGdlMiIgY2xhc3M9ImVkZ2UiPgo8dGl0bGU+UEVORElORyYjNDU7Jmd0O0RPTkU8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNMTkyLjI2LC0xNzkuMjJDMjAwLjMyLC0xNzMuNzIgMjA4LjYzLC0xNjYuODcgMjE0LjY4LC0xNTkgMjM5Ljc2LC0xMjYuMzkgMjQ3LjA2LC03OC4wMSAyNDkuMDgsLTQ3LjUxIi8+Cjxwb2x5Z29uIGZpbGw9ImJsYWNrIiBzdHJva2U9ImJsYWNrIiBwb2ludHM9IjI1Mi41NiwtNDguMDYgMjQ5LjU2LC0zNy45IDI0NS41NywtNDcuNzIgMjUyLjU2LC00OC4wNiIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyNjcuODEiIHk9Ii0xMDEuNDUiIGZvbnQtZmFtaWx5PSJUaW1lcyxzZXJpZiIgZm9udC1zaXplPSIxNC4wMCI+Y29tcGxldGU8L3RleHQ+CjwvZz4KPCEtLSBSVU5OSU5HIC0tPgo8ZyBpZD0ibm9kZTQiIGNsYXNzPSJub2RlIj4KPHRpdGxlPlJVTk5JTkc8L3RpdGxlPgo8ZWxsaXBzZSBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBjeD0iMTY1LjY4IiBjeT0iLTEwNi41IiByeD0iNTMuNCIgcnk9IjE4Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjE2NS42OCIgeT0iLTEwMS40NSIgZm9udC1mYW1pbHk9IlRpbWVzLHNlcmlmIiBmb250LXNpemU9IjE0LjAwIj5SVU5OSU5HPC90ZXh0Pgo8L2c+CjwhLS0gUEVORElORyYjNDU7Jmd0O1JVTk5JTkcgLS0+CjxnIGlkPSJlZGdlMyIgY2xhc3M9ImVkZ2UiPgo8dGl0bGU+UEVORElORyYjNDU7Jmd0O1JVTk5JTkc8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNMTY1LjY4LC0xNzYuOTFDMTY1LjY4LC0xNjUuMjYgMTY1LjY4LC0xNDkuNTUgMTY1LjY4LC0xMzYuMDIiLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iMTY5LjE4LC0xMzYuMzYgMTY1LjY4LC0xMjYuMzYgMTYyLjE4LC0xMzYuMzYgMTY5LjE4LC0xMzYuMzYiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMTg4LjE4IiB5PSItMTQ1LjciIGZvbnQtZmFtaWx5PSJUaW1lcyxzZXJpZiIgZm9udC1zaXplPSIxNC4wMCI+ZGlzcGF0Y2g8L3RleHQ+CjwvZz4KPCEtLSBDQU5DRUxMRUQmIzQ1OyZndDtDQU5DRUxMRUQgLS0+CjxnIGlkPSJlZGdlNiIgY2xhc3M9ImVkZ2UiPgo8dGl0bGU+Q0FOQ0VMTEVEJiM0NTsmZ3Q7Q0FOQ0VMTEVEPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTEyNS4xLC0yNi4xM0MxMzkuMDYsLTI1LjQ2IDE0OS4zNiwtMjIuNzUgMTQ5LjM2LC0xOCAxNDkuMzYsLTE0LjY2IDE0NC4yNywtMTIuMzMgMTM2LjQsLTExIi8+Cjxwb2x5Z29uIGZpbGw9ImJsYWNrIiBzdHJva2U9ImJsYWNrIiBwb2ludHM9IjEzNi45MSwtNy41NCAxMjYuNjEsLTEwLjAyIDEzNi4yMSwtMTQuNSAxMzYuOTEsLTcuNTQiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMTY2LjYxIiB5PSItMTIuOTUiIGZvbnQtZmFtaWx5PSJUaW1lcyxzZXJpZiIgZm9udC1zaXplPSIxNC4wMCI+Y2FuY2VsPC90ZXh0Pgo8L2c+CjwhLS0gRE9ORSYjNDU7Jmd0O0RPTkUgLS0+CjxnIGlkPSJlZGdlNyIgY2xhc3M9ImVkZ2UiPgo8dGl0bGU+RE9ORSYjNDU7Jmd0O0RPTkU8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNMjgyLjY4LC0yNi4yOUMyOTQuNTMsLTI2LjQ3IDMwNC4xOSwtMjMuNyAzMDQuMTksLTE4IDMwNC4xOSwtMTQuMjYgMzAwLjAzLC0xMS43OCAyOTMuODIsLTEwLjU3Ii8+Cjxwb2x5Z29uIGZpbGw9ImJsYWNrIiBzdHJva2U9ImJsYWNrIiBwb2ludHM9IjI5NC40MywtNy4xMSAyODQuMTksLTkuODMgMjkzLjg5LC0xNC4wOSAyOTQuNDMsLTcuMTEiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMzIxLjQ0IiB5PSItMTIuOTUiIGZvbnQtZmFtaWx5PSJUaW1lcyxzZXJpZiIgZm9udC1zaXplPSIxNC4wMCI+Y2FuY2VsPC90ZXh0Pgo8L2c+CjwhLS0gUlVOTklORyYjNDU7Jmd0O0NBTkNFTExFRCAtLT4KPGcgaWQ9ImVkZ2U0IiBjbGFzcz0iZWRnZSI+Cjx0aXRsZT5SVU5OSU5HJiM0NTsmZ3Q7Q0FOQ0VMTEVEPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTE0Ni44NywtODkuMjNDMTMxLjc0LC03Ni4xNCAxMTAuMjcsLTU3LjU3IDkzLjIxLC00Mi44MSIvPgo8cG9seWdvbiBmaWxsPSJibGFjayIgc3Ryb2tlPSJibGFjayIgcG9pbnRzPSI5NS43NCwtNDAuMzggODUuODksLTM2LjQ4IDkxLjE3LC00NS42NyA5NS43NCwtNDAuMzgiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMTQxLjkzIiB5PSItNTcuMiIgZm9udC1mYW1pbHk9IlRpbWVzLHNlcmlmIiBmb250LXNpemU9IjE0LjAwIj5jYW5jZWw8L3RleHQ+CjwvZz4KPCEtLSBSVU5OSU5HJiM0NTsmZ3Q7RE9ORSAtLT4KPGcgaWQ9ImVkZ2U1IiBjbGFzcz0iZWRnZSI+Cjx0aXRsZT5SVU5OSU5HJiM0NTsmZ3Q7RE9ORTwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0xNzEuMDYsLTg4LjIzQzE3NS4wOCwtNzcuNDQgMTgxLjQ0LC02My43OSAxOTAuNDMsLTU0IDE5Ni44MSwtNDcuMDUgMjA0Ljg4LC00MS4wNyAyMTMsLTM2LjEiLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iMjE0LjUxLC0zOS4yNyAyMjEuNSwtMzEuMzEgMjExLjA3LC0zMy4xNyAyMTQuNTEsLTM5LjI3Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjIxNC44MSIgeT0iLTU3LjIiIGZvbnQtZmFtaWx5PSJUaW1lcyxzZXJpZiIgZm9udC1zaXplPSIxNC4wMCI+Y29tcGxldGU8L3RleHQ+CjwvZz4KPC9nPgo8L3N2Zz4K "OnDemandFunction State Diagram")


## <a name="OnDemandResult"></a>Class `OnDemandResult(Result)`

Wrap a callable, run it when required.

State diagram:
![OnDemandResult State Diagram](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPgo8IS0tIEdlbmVyYXRlZCBieSBncmFwaHZpeiB2ZXJzaW9uIDExLjAuMCAoMjAyNDA0MjguMTUyMikKIC0tPgo8IS0tIFRpdGxlOiBPbkRlbWFuZFJlc3VsdCBTdGF0ZSBEaWFncmFtIFBhZ2VzOiAxIC0tPgo8c3ZnIHdpZHRoPSIzNDdwdCIgaGVpZ2h0PSIyMjFwdCIKIHZpZXdCb3g9IjAuMDAgMC4wMCAzNDYuNjkgMjIxLjAwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KPGcgaWQ9ImdyYXBoMCIgY2xhc3M9ImdyYXBoIiB0cmFuc2Zvcm09InNjYWxlKDEgMSkgcm90YXRlKDApIHRyYW5zbGF0ZSg0IDIxNykiPgo8dGl0bGU+T25EZW1hbmRSZXN1bHQgU3RhdGUgRGlhZ3JhbTwvdGl0bGU+Cjxwb2x5Z29uIGZpbGw9IndoaXRlIiBzdHJva2U9Im5vbmUiIHBvaW50cz0iLTQsNCAtNCwtMjE3IDM0Mi42OSwtMjE3IDM0Mi42OSw0IC00LDQiLz4KPCEtLSBQRU5ESU5HIC0tPgo8ZyBpZD0ibm9kZTEiIGNsYXNzPSJub2RlIj4KPHRpdGxlPlBFTkRJTkc8L3RpdGxlPgo8ZWxsaXBzZSBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBjeD0iMTY1LjY4IiBjeT0iLTE5NSIgcng9IjUxLjM1IiByeT0iMTgiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMTY1LjY4IiB5PSItMTg5Ljk1IiBmb250LWZhbWlseT0iVGltZXMsc2VyaWYiIGZvbnQtc2l6ZT0iMTQuMDAiPlBFTkRJTkc8L3RleHQ+CjwvZz4KPCEtLSBDQU5DRUxMRUQgLS0+CjxnIGlkPSJub2RlMiIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+Q0FOQ0VMTEVEPC90aXRsZT4KPGVsbGlwc2UgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgY3g9IjY1LjY4IiBjeT0iLTE4IiByeD0iNjUuNjgiIHJ5PSIxOCIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSI2NS42OCIgeT0iLTEyLjk1IiBmb250LWZhbWlseT0iVGltZXMsc2VyaWYiIGZvbnQtc2l6ZT0iMTQuMDAiPkNBTkNFTExFRDwvdGV4dD4KPC9nPgo8IS0tIFBFTkRJTkcmIzQ1OyZndDtDQU5DRUxMRUQgLS0+CjxnIGlkPSJlZGdlMSIgY2xhc3M9ImVkZ2UiPgo8dGl0bGU+UEVORElORyYjNDU7Jmd0O0NBTkNFTExFRDwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0xMzMuOTksLTE4MC41NkMxMTEuNTYsLTE2OS4xOCA4My4wNywtMTUwLjU1IDY5LjE4LC0xMjQuNSA1Ni42LC0xMDAuOSA1Ny4yMiwtNjkuOTEgNjAuMDksLTQ3LjYzIi8+Cjxwb2x5Z29uIGZpbGw9ImJsYWNrIiBzdHJva2U9ImJsYWNrIiBwb2ludHM9IjYzLjU1LC00OC4xNyA2MS42MSwtMzcuNzUgNTYuNjMsLTQ3LjEgNjMuNTUsLTQ4LjE3Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9Ijg2LjkzIiB5PSItMTAxLjQ1IiBmb250LWZhbWlseT0iVGltZXMsc2VyaWYiIGZvbnQtc2l6ZT0iMTQuMDAiPmNhbmNlbDwvdGV4dD4KPC9nPgo8IS0tIERPTkUgLS0+CjxnIGlkPSJub2RlMyIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+RE9ORTwvdGl0bGU+CjxlbGxpcHNlIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGN4PSIyNDkuNjgiIGN5PSItMTgiIHJ4PSIzNi41MSIgcnk9IjE4Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjI0OS42OCIgeT0iLTEyLjk1IiBmb250LWZhbWlseT0iVGltZXMsc2VyaWYiIGZvbnQtc2l6ZT0iMTQuMDAiPkRPTkU8L3RleHQ+CjwvZz4KPCEtLSBQRU5ESU5HJiM0NTsmZ3Q7RE9ORSAtLT4KPGcgaWQ9ImVkZ2UyIiBjbGFzcz0iZWRnZSI+Cjx0aXRsZT5QRU5ESU5HJiM0NTsmZ3Q7RE9ORTwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0xOTIuMjYsLTE3OS4yMkMyMDAuMzIsLTE3My43MiAyMDguNjMsLTE2Ni44NyAyMTQuNjgsLTE1OSAyMzkuNzYsLTEyNi4zOSAyNDcuMDYsLTc4LjAxIDI0OS4wOCwtNDcuNTEiLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iMjUyLjU2LC00OC4wNiAyNDkuNTYsLTM3LjkgMjQ1LjU3LC00Ny43MiAyNTIuNTYsLTQ4LjA2Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjI2Ny44MSIgeT0iLTEwMS40NSIgZm9udC1mYW1pbHk9IlRpbWVzLHNlcmlmIiBmb250LXNpemU9IjE0LjAwIj5jb21wbGV0ZTwvdGV4dD4KPC9nPgo8IS0tIFJVTk5JTkcgLS0+CjxnIGlkPSJub2RlNCIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+UlVOTklORzwvdGl0bGU+CjxlbGxpcHNlIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGN4PSIxNjUuNjgiIGN5PSItMTA2LjUiIHJ4PSI1My40IiByeT0iMTgiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMTY1LjY4IiB5PSItMTAxLjQ1IiBmb250LWZhbWlseT0iVGltZXMsc2VyaWYiIGZvbnQtc2l6ZT0iMTQuMDAiPlJVTk5JTkc8L3RleHQ+CjwvZz4KPCEtLSBQRU5ESU5HJiM0NTsmZ3Q7UlVOTklORyAtLT4KPGcgaWQ9ImVkZ2UzIiBjbGFzcz0iZWRnZSI+Cjx0aXRsZT5QRU5ESU5HJiM0NTsmZ3Q7UlVOTklORzwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0xNjUuNjgsLTE3Ni45MUMxNjUuNjgsLTE2NS4yNiAxNjUuNjgsLTE0OS41NSAxNjUuNjgsLTEzNi4wMiIvPgo8cG9seWdvbiBmaWxsPSJibGFjayIgc3Ryb2tlPSJibGFjayIgcG9pbnRzPSIxNjkuMTgsLTEzNi4zNiAxNjUuNjgsLTEyNi4zNiAxNjIuMTgsLTEzNi4zNiAxNjkuMTgsLTEzNi4zNiIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIxODguMTgiIHk9Ii0xNDUuNyIgZm9udC1mYW1pbHk9IlRpbWVzLHNlcmlmIiBmb250LXNpemU9IjE0LjAwIj5kaXNwYXRjaDwvdGV4dD4KPC9nPgo8IS0tIENBTkNFTExFRCYjNDU7Jmd0O0NBTkNFTExFRCAtLT4KPGcgaWQ9ImVkZ2U2IiBjbGFzcz0iZWRnZSI+Cjx0aXRsZT5DQU5DRUxMRUQmIzQ1OyZndDtDQU5DRUxMRUQ8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNMTI1LjEsLTI2LjEzQzEzOS4wNiwtMjUuNDYgMTQ5LjM2LC0yMi43NSAxNDkuMzYsLTE4IDE0OS4zNiwtMTQuNjYgMTQ0LjI3LC0xMi4zMyAxMzYuNCwtMTEiLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iMTM2LjkxLC03LjU0IDEyNi42MSwtMTAuMDIgMTM2LjIxLC0xNC41IDEzNi45MSwtNy41NCIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIxNjYuNjEiIHk9Ii0xMi45NSIgZm9udC1mYW1pbHk9IlRpbWVzLHNlcmlmIiBmb250LXNpemU9IjE0LjAwIj5jYW5jZWw8L3RleHQ+CjwvZz4KPCEtLSBET05FJiM0NTsmZ3Q7RE9ORSAtLT4KPGcgaWQ9ImVkZ2U3IiBjbGFzcz0iZWRnZSI+Cjx0aXRsZT5ET05FJiM0NTsmZ3Q7RE9ORTwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0yODIuNjgsLTI2LjI5QzI5NC41MywtMjYuNDcgMzA0LjE5LC0yMy43IDMwNC4xOSwtMTggMzA0LjE5LC0xNC4yNiAzMDAuMDMsLTExLjc4IDI5My44MiwtMTAuNTciLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iMjk0LjQzLC03LjExIDI4NC4xOSwtOS44MyAyOTMuODksLTE0LjA5IDI5NC40MywtNy4xMSIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIzMjEuNDQiIHk9Ii0xMi45NSIgZm9udC1mYW1pbHk9IlRpbWVzLHNlcmlmIiBmb250LXNpemU9IjE0LjAwIj5jYW5jZWw8L3RleHQ+CjwvZz4KPCEtLSBSVU5OSU5HJiM0NTsmZ3Q7Q0FOQ0VMTEVEIC0tPgo8ZyBpZD0iZWRnZTQiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPlJVTk5JTkcmIzQ1OyZndDtDQU5DRUxMRUQ8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNMTQ2Ljg3LC04OS4yM0MxMzEuNzQsLTc2LjE0IDExMC4yNywtNTcuNTcgOTMuMjEsLTQyLjgxIi8+Cjxwb2x5Z29uIGZpbGw9ImJsYWNrIiBzdHJva2U9ImJsYWNrIiBwb2ludHM9Ijk1Ljc0LC00MC4zOCA4NS44OSwtMzYuNDggOTEuMTcsLTQ1LjY3IDk1Ljc0LC00MC4zOCIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIxNDEuOTMiIHk9Ii01Ny4yIiBmb250LWZhbWlseT0iVGltZXMsc2VyaWYiIGZvbnQtc2l6ZT0iMTQuMDAiPmNhbmNlbDwvdGV4dD4KPC9nPgo8IS0tIFJVTk5JTkcmIzQ1OyZndDtET05FIC0tPgo8ZyBpZD0iZWRnZTUiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPlJVTk5JTkcmIzQ1OyZndDtET05FPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTE3MS4wNiwtODguMjNDMTc1LjA4LC03Ny40NCAxODEuNDQsLTYzLjc5IDE5MC40MywtNTQgMTk2LjgxLC00Ny4wNSAyMDQuODgsLTQxLjA3IDIxMywtMzYuMSIvPgo8cG9seWdvbiBmaWxsPSJibGFjayIgc3Ryb2tlPSJibGFjayIgcG9pbnRzPSIyMTQuNTEsLTM5LjI3IDIyMS41LC0zMS4zMSAyMTEuMDcsLTMzLjE3IDIxNC41MSwtMzkuMjciLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjE0LjgxIiB5PSItNTcuMiIgZm9udC1mYW1pbHk9IlRpbWVzLHNlcmlmIiBmb250LXNpemU9IjE0LjAwIj5jb21wbGV0ZTwvdGV4dD4KPC9nPgo8L2c+Cjwvc3ZnPgo= "OnDemandResult State Diagram")


## <a name="report"></a>`report(LFs)`

Generator which yields completed `Result`s.

This is a generator that yields `Result`s as they complete,
useful for waiting for a sequence of `Result`s
that may complete in an arbitrary order.

## <a name="Result"></a>Class `Result(cs.fsm.FSM)`

Base class for asynchronous collection of a result.
This is used to make `Result`, `OnDemandFunction`s, `LateFunction`s
and other objects with asynchronous termination.

In addition to the methods below, for each state value such
as `self.PENDING` there is a corresponding attribute `is_pending`
testing whether the `Result` is in that state.

State diagram:
![Result State Diagram](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPgo8IS0tIEdlbmVyYXRlZCBieSBncmFwaHZpeiB2ZXJzaW9uIDExLjAuMCAoMjAyNDA0MjguMTUyMikKIC0tPgo8IS0tIFRpdGxlOiBSZXN1bHQgU3RhdGUgRGlhZ3JhbSBQYWdlczogMSAtLT4KPHN2ZyB3aWR0aD0iMzQ3cHQiIGhlaWdodD0iMjIxcHQiCiB2aWV3Qm94PSIwLjAwIDAuMDAgMzQ2LjY5IDIyMS4wMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CjxnIGlkPSJncmFwaDAiIGNsYXNzPSJncmFwaCIgdHJhbnNmb3JtPSJzY2FsZSgxIDEpIHJvdGF0ZSgwKSB0cmFuc2xhdGUoNCAyMTcpIj4KPHRpdGxlPlJlc3VsdCBTdGF0ZSBEaWFncmFtPC90aXRsZT4KPHBvbHlnb24gZmlsbD0id2hpdGUiIHN0cm9rZT0ibm9uZSIgcG9pbnRzPSItNCw0IC00LC0yMTcgMzQyLjY5LC0yMTcgMzQyLjY5LDQgLTQsNCIvPgo8IS0tIFBFTkRJTkcgLS0+CjxnIGlkPSJub2RlMSIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+UEVORElORzwvdGl0bGU+CjxlbGxpcHNlIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGN4PSIxNjUuNjgiIGN5PSItMTk1IiByeD0iNTEuMzUiIHJ5PSIxOCIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIxNjUuNjgiIHk9Ii0xODkuOTUiIGZvbnQtZmFtaWx5PSJUaW1lcyxzZXJpZiIgZm9udC1zaXplPSIxNC4wMCI+UEVORElORzwvdGV4dD4KPC9nPgo8IS0tIENBTkNFTExFRCAtLT4KPGcgaWQ9Im5vZGUyIiBjbGFzcz0ibm9kZSI+Cjx0aXRsZT5DQU5DRUxMRUQ8L3RpdGxlPgo8ZWxsaXBzZSBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBjeD0iNjUuNjgiIGN5PSItMTgiIHJ4PSI2NS42OCIgcnk9IjE4Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjY1LjY4IiB5PSItMTIuOTUiIGZvbnQtZmFtaWx5PSJUaW1lcyxzZXJpZiIgZm9udC1zaXplPSIxNC4wMCI+Q0FOQ0VMTEVEPC90ZXh0Pgo8L2c+CjwhLS0gUEVORElORyYjNDU7Jmd0O0NBTkNFTExFRCAtLT4KPGcgaWQ9ImVkZ2UxIiBjbGFzcz0iZWRnZSI+Cjx0aXRsZT5QRU5ESU5HJiM0NTsmZ3Q7Q0FOQ0VMTEVEPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTEzMy45OSwtMTgwLjU2QzExMS41NiwtMTY5LjE4IDgzLjA3LC0xNTAuNTUgNjkuMTgsLTEyNC41IDU2LjYsLTEwMC45IDU3LjIyLC02OS45MSA2MC4wOSwtNDcuNjMiLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iNjMuNTUsLTQ4LjE3IDYxLjYxLC0zNy43NSA1Ni42MywtNDcuMSA2My41NSwtNDguMTciLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iODYuOTMiIHk9Ii0xMDEuNDUiIGZvbnQtZmFtaWx5PSJUaW1lcyxzZXJpZiIgZm9udC1zaXplPSIxNC4wMCI+Y2FuY2VsPC90ZXh0Pgo8L2c+CjwhLS0gRE9ORSAtLT4KPGcgaWQ9Im5vZGUzIiBjbGFzcz0ibm9kZSI+Cjx0aXRsZT5ET05FPC90aXRsZT4KPGVsbGlwc2UgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgY3g9IjI0OS42OCIgY3k9Ii0xOCIgcng9IjM2LjUxIiByeT0iMTgiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjQ5LjY4IiB5PSItMTIuOTUiIGZvbnQtZmFtaWx5PSJUaW1lcyxzZXJpZiIgZm9udC1zaXplPSIxNC4wMCI+RE9ORTwvdGV4dD4KPC9nPgo8IS0tIFBFTkRJTkcmIzQ1OyZndDtET05FIC0tPgo8ZyBpZD0iZWRnZTIiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPlBFTkRJTkcmIzQ1OyZndDtET05FPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTE5Mi4yNiwtMTc5LjIyQzIwMC4zMiwtMTczLjcyIDIwOC42MywtMTY2Ljg3IDIxNC42OCwtMTU5IDIzOS43NiwtMTI2LjM5IDI0Ny4wNiwtNzguMDEgMjQ5LjA4LC00Ny41MSIvPgo8cG9seWdvbiBmaWxsPSJibGFjayIgc3Ryb2tlPSJibGFjayIgcG9pbnRzPSIyNTIuNTYsLTQ4LjA2IDI0OS41NiwtMzcuOSAyNDUuNTcsLTQ3LjcyIDI1Mi41NiwtNDguMDYiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMjY3LjgxIiB5PSItMTAxLjQ1IiBmb250LWZhbWlseT0iVGltZXMsc2VyaWYiIGZvbnQtc2l6ZT0iMTQuMDAiPmNvbXBsZXRlPC90ZXh0Pgo8L2c+CjwhLS0gUlVOTklORyAtLT4KPGcgaWQ9Im5vZGU0IiBjbGFzcz0ibm9kZSI+Cjx0aXRsZT5SVU5OSU5HPC90aXRsZT4KPGVsbGlwc2UgZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgY3g9IjE2NS42OCIgY3k9Ii0xMDYuNSIgcng9IjUzLjQiIHJ5PSIxOCIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIxNjUuNjgiIHk9Ii0xMDEuNDUiIGZvbnQtZmFtaWx5PSJUaW1lcyxzZXJpZiIgZm9udC1zaXplPSIxNC4wMCI+UlVOTklORzwvdGV4dD4KPC9nPgo8IS0tIFBFTkRJTkcmIzQ1OyZndDtSVU5OSU5HIC0tPgo8ZyBpZD0iZWRnZTMiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPlBFTkRJTkcmIzQ1OyZndDtSVU5OSU5HPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTE2NS42OCwtMTc2LjkxQzE2NS42OCwtMTY1LjI2IDE2NS42OCwtMTQ5LjU1IDE2NS42OCwtMTM2LjAyIi8+Cjxwb2x5Z29uIGZpbGw9ImJsYWNrIiBzdHJva2U9ImJsYWNrIiBwb2ludHM9IjE2OS4xOCwtMTM2LjM2IDE2NS42OCwtMTI2LjM2IDE2Mi4xOCwtMTM2LjM2IDE2OS4xOCwtMTM2LjM2Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjE4OC4xOCIgeT0iLTE0NS43IiBmb250LWZhbWlseT0iVGltZXMsc2VyaWYiIGZvbnQtc2l6ZT0iMTQuMDAiPmRpc3BhdGNoPC90ZXh0Pgo8L2c+CjwhLS0gQ0FOQ0VMTEVEJiM0NTsmZ3Q7Q0FOQ0VMTEVEIC0tPgo8ZyBpZD0iZWRnZTYiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPkNBTkNFTExFRCYjNDU7Jmd0O0NBTkNFTExFRDwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0xMjUuMSwtMjYuMTNDMTM5LjA2LC0yNS40NiAxNDkuMzYsLTIyLjc1IDE0OS4zNiwtMTggMTQ5LjM2LC0xNC42NiAxNDQuMjcsLTEyLjMzIDEzNi40LC0xMSIvPgo8cG9seWdvbiBmaWxsPSJibGFjayIgc3Ryb2tlPSJibGFjayIgcG9pbnRzPSIxMzYuOTEsLTcuNTQgMTI2LjYxLC0xMC4wMiAxMzYuMjEsLTE0LjUgMTM2LjkxLC03LjU0Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjE2Ni42MSIgeT0iLTEyLjk1IiBmb250LWZhbWlseT0iVGltZXMsc2VyaWYiIGZvbnQtc2l6ZT0iMTQuMDAiPmNhbmNlbDwvdGV4dD4KPC9nPgo8IS0tIERPTkUmIzQ1OyZndDtET05FIC0tPgo8ZyBpZD0iZWRnZTciIGNsYXNzPSJlZGdlIj4KPHRpdGxlPkRPTkUmIzQ1OyZndDtET05FPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTI4Mi42OCwtMjYuMjlDMjk0LjUzLC0yNi40NyAzMDQuMTksLTIzLjcgMzA0LjE5LC0xOCAzMDQuMTksLTE0LjI2IDMwMC4wMywtMTEuNzggMjkzLjgyLC0xMC41NyIvPgo8cG9seWdvbiBmaWxsPSJibGFjayIgc3Ryb2tlPSJibGFjayIgcG9pbnRzPSIyOTQuNDMsLTcuMTEgMjg0LjE5LC05LjgzIDI5My44OSwtMTQuMDkgMjk0LjQzLC03LjExIi8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjMyMS40NCIgeT0iLTEyLjk1IiBmb250LWZhbWlseT0iVGltZXMsc2VyaWYiIGZvbnQtc2l6ZT0iMTQuMDAiPmNhbmNlbDwvdGV4dD4KPC9nPgo8IS0tIFJVTk5JTkcmIzQ1OyZndDtDQU5DRUxMRUQgLS0+CjxnIGlkPSJlZGdlNCIgY2xhc3M9ImVkZ2UiPgo8dGl0bGU+UlVOTklORyYjNDU7Jmd0O0NBTkNFTExFRDwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0xNDYuODcsLTg5LjIzQzEzMS43NCwtNzYuMTQgMTEwLjI3LC01Ny41NyA5My4yMSwtNDIuODEiLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iOTUuNzQsLTQwLjM4IDg1Ljg5LC0zNi40OCA5MS4xNywtNDUuNjcgOTUuNzQsLTQwLjM4Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjE0MS45MyIgeT0iLTU3LjIiIGZvbnQtZmFtaWx5PSJUaW1lcyxzZXJpZiIgZm9udC1zaXplPSIxNC4wMCI+Y2FuY2VsPC90ZXh0Pgo8L2c+CjwhLS0gUlVOTklORyYjNDU7Jmd0O0RPTkUgLS0+CjxnIGlkPSJlZGdlNSIgY2xhc3M9ImVkZ2UiPgo8dGl0bGU+UlVOTklORyYjNDU7Jmd0O0RPTkU8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNMTcxLjA2LC04OC4yM0MxNzUuMDgsLTc3LjQ0IDE4MS40NCwtNjMuNzkgMTkwLjQzLC01NCAxOTYuODEsLTQ3LjA1IDIwNC44OCwtNDEuMDcgMjEzLC0zNi4xIi8+Cjxwb2x5Z29uIGZpbGw9ImJsYWNrIiBzdHJva2U9ImJsYWNrIiBwb2ludHM9IjIxNC41MSwtMzkuMjcgMjIxLjUsLTMxLjMxIDIxMS4wNywtMzMuMTcgMjE0LjUxLC0zOS4yNyIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIyMTQuODEiIHk9Ii01Ny4yIiBmb250LWZhbWlseT0iVGltZXMsc2VyaWYiIGZvbnQtc2l6ZT0iMTQuMDAiPmNvbXBsZXRlPC90ZXh0Pgo8L2c+CjwvZz4KPC9zdmc+Cg== "Result State Diagram")


*`Result.__init__(self, name=None, *, lock=None, result=None, state=None, extra=None)`*:
Base initialiser for `Result` objects and subclasses.

Parameter:
* `name`: optional parameter naming this object.
* `lock`: optional locking object, defaults to a new `threading.Lock`.
* `result`: if not `None`, prefill the `.result` property.
* `extra`: an optional mapping of extra information to
  associate with the `Result`, useful to provide context
  when collecting the result; the `Result` has a public
  attribute `.extra` which is an `AttrableMapping` to hold
  this information.

*`Result.__call__(self, *a, **kw)`*:
Call the `Result`: wait for it to be ready and then return or raise.

You can optionally supply a callable and arguments,
in which case `callable(*args,**kwargs)` will be called
via `Result.call` and the results applied to this `Result`.

Basic example:

    R = Result()
    ... hand R to something which will fulfil it later ...
    x = R() # wait for fulfilment - value lands in x

Direct call:

    R = Result()
    ... pass R to something which wants the result ...
    # call func(1,2,z=3), save result in R
    # ready for collection by whatever received R
    R(func,1,2,z=3)

*`Result.bg(self, func, *a, **kw)`*:
Submit a function to compute the result in a separate `Thread`,
returning the `Thread`.

Keyword arguments for `cs.threads.bg` may be supplied by
prefixing their names with an underscore, for example:

    T = R.bg(mainloop, _pre_enter_objects=(S, fs))

This dispatches a `Thread` to run `self.run_func(func,*a,**kw)`
and as such the `Result` must be in "pending" state,
and transitions to "running".

*`Result.cancel(self, msg: Optional[str] = None)`*:
Cancel this `Result`.

*`Result.cancelled`*:
OBSOLETE cancelled

Test whether this `Result` has been cancelled.
       Obsolete: use `.is_cancelled`.

*`Result.empty(self)`*:
Analogue to `Queue.empty()`.

*`Result.exc_info`*:
The exception information from a completed `Result`.
This is not available before completion.
Accessing this on a cancelled `Result` raises `CancellationError`.

*`Result.get(self, default=None)`*:
Wait for readiness; return the result if `self.exc_info` is `None`,
otherwise `default`.

*`Result.join(self)`*:
Calling the `.join()` method waits for the function to run to
completion and returns a tuple of `(result,exc_info)`.

On completion the sequence `(result,None)` is returned.
If an exception occurred computing the result the sequence
`(None,exc_info)` is returned
where `exc_info` is a tuple of `(exc_type,exc_value,exc_traceback)`.
If the function was cancelled the sequence `(None,None)`
is returned.

*`Result.notify(self, notifier: Callable[[ForwardRef('Result')], NoneType])`*:
After the `Result` completes, call `notifier(self)`.

If the `Result` has already completed this will happen immediately.
If you'd rather `self` got put on some queue `Q`, supply `Q.put`.

*`Result.pending`*:
OBSOLETE pending

Whether the `Result` is pending.
       Obsolete: use `.is_pending`.

*`Result.post_notify(self, post_func) -> 'Result'`*:
Return a secondary `Result` which processes the result of `self`.

After the `self` completes, call `post_func(retval)` where
`retval` is the result of `self`, and use that to complete
the secondary `Result`.

*Important note*: because the completion lock object is
released after the internal `FSM.fsm_event` call, the
callback used to implement `.post_notify` is fired before
the lock object is released. As such, it would deadlock as
it waits for completion of `self` by using that lock.
Therefore the callback dispatches a separate `Thread` to
wait for `self` and then run `post_func`.

Example:

    # submit packet to data stream
    R = submit_packet()
    # arrange that when the response is received, decode the response
    R2 = R.post_notify(lambda response: decode(response))
    # collect decoded response
    decoded = R2()

If the `Result` has already completed this will happen immediately.

*`Result.put(self, value)`*:
Store the value. `Queue`-like idiom.

*`Result.raise_(self, exc=None)`*:
Convenience wrapper for `self.exc_info` to store an exception result `exc`.
If `exc` is omitted or `None`, uses `sys.exc_info()`.

Examples:

    # complete the result using the current exception state
    R.raise_()

    # complete the result with an exception type
    R.raise_(RuntimeError)

    # complete the result with an exception
    R.raise_(ValueError("bad value!"))

*`Result.ready`*:
True if the `Result` state is `DONE` or `CANCELLED`..

*`Result.result`*:
The result.
This property is not available before completion.
Accessing this on a cancelled `Result` raises `CancellationError`.

*`Result.run_func(self, func, *a, **kw)`*:
Fulfil the `Result` by running `func(*a,**kw)`.

*`Result.run_func_in_thread(self, func, *a, **kw)`*:
Fulfil the `Result` by running `func(*a,**kw)`
in a separate `Thread`.

This exists to step out of the current `Thread's` thread
local context, such as a database transaction associated
with Django's implicit per-`Thread` database context.

*`Result.state`*:
OBSOLETE state

The `FSM` state (obsolete).
       Obsolete: use `.fsm_state`.

## <a name="ResultSet"></a>Class `ResultSet(builtins.set)`

A `set` subclass containing `Result`s,
on which one may iterate as `Result`s complete.

*`ResultSet.__iter__(self)`*:
Iterating on a `ResultSet` yields `Result`s as they complete.

*`ResultSet.wait(self)`*:
Convenience function to wait for all the `Result`s.

# Release Log



*Release 20250103*:
New @not_cancelled decorator for methods to raise CancellationError is self.cancelled.

*Release 20241119*:
OnDemandResult.__call__: bodge: use the private lock name instead of the obsolete lock name.

*Release 20240630*:
* Move CancellationError from cs.result to cs.fsm.
* report: avoid iterating over the live set.
* Result: drop the PREPARE state, allow 'cancel' no-op event in CANCELLED and DONE states.
* Result.result,exc_info getters: raise CancellationError if the Result is cancelled.
* Result._complete: fire the 'complete' event after the ._result and ._exc_info attributes are set but still before the self._get_lock.release().
* Result: preserve message passed to .cancel(), _complete raises RuntimeError if already complete.

*Release 20240412*:
Result.bg: plumb _foo arguments to cs.threads.bg as foo.

*Release 20240316*:
Fixed release upload artifacts.

*Release 20240305*:
Result.__str__: handle early use where __dict__ lacks various entries.

*Release 20231221*:
Doc update.

*Release 20231129*:
Result.__del__: issue a warning about no collection instead of raising an exception.

*Release 20230331*:
Result.join: access self._result instead of the property.

*Release 20230212*:
* Result._complete: release self._get_lock before firing the event, as the event is what fires the notifiers.
* Result.notify: when we make a direct notifier call, call the notifier outside the lock and remember to set self.collected=True.
* Result: new post_notify() method to queue a function of the Result.result, returning a Result for the completion of the post function.

*Release 20221207*:
CancellationError: accept keyword arguments, apply as attributes.

*Release 20221118*:
* CancellationError: rename msg to message.
* Result.run_func_in_thread: new method to run an arbitrary function in a separate Thread and return it via the Result.
* New @in_thread decorator to cause a function to run in a separate Thread using Result.run_in_thread.
* New call_in_thread to run an arbitrary function in a distinct Thread.
* @in_thread: expose the original function as the decorated function's .direct attribute.

*Release 20220918*:
OnDemandResult: modern "pending" check.

*Release 20220805*:
Result now subclasses cs.fsm.FSM.

*Release 20220311*:
* Result: class local Seq instance.
* Result.call: thread safe runtime check of self.state==pending.
* New Task and @task decorator, prototype for rerunnable blocking chaining tasks scheme - very alpha.

*Release 20210420*:
Update dependencies, add docstring.

*Release 20210407*:
New ResultSet(set) class, with context manager and wait methods, and whose __iter__ iterates completed Results.

*Release 20210123*:
bg: accept optional _extra parameter for use by the Result.

*Release 20201102*:
Result: now .extra attribute for associated data and a new optional "extra" parameter in the initialiser.

*Release 20200521*:
* OnDemandResult: bugfixes and improvements.
* Result.bg: accept optional _name parameter to specify the Result.name.

*Release 20191007*:
* Simplify ResultState definition.
* Result.bg: use cs.threads.bg to dispatch the Thread.

*Release 20190522*:
* Result.__call__ now accepts an optional callable and args.
* Result.call: set the Result state to "running" before dispatching the function.
* Rename OnDemandFunction to OnDemandResult, keep old name around for compatibility.
* Result._complete: also permitted if state==cancelled.

*Release 20190309*:
Small bugfix.

*Release 20181231*:
* Result.call: report baser exceptions than BaseException.
* Drop _PendingFunction abstract class.

*Release 20181109.1*:
DISTINFO update.

*Release 20181109*:
* Derive CancellationError from Exception instead of RuntimeError, fix initialiser.
* Rename AsynchState to ResultState and make it an Enum.
* Make Results hashable and comparable for equality for use as mapping keys: equality is identity.
* New Result.collected attribute, set true if .result or .exc_info are accessed, logs an error if Result.__del__ is called when false, may be set true externally if a Result is not required.
* Drop `final` parameter; never used and supplanted by Result.notify.
* Result.join: return the .result and .exc_info properties in order to mark the Result as collected.
* Result: set .collected to True when a notifier has been called successfully.
* Bugfix Result.cancel: apply the new cancelled state.

*Release 20171231*:
* Bugfix Result.call to catch BaseException instead of Exception.
* New convenience function bg(func) to dispatch `func` in a separate Thread and return a Result to collect its value.

*Release 20171030.1*:
Fix module requirements specification.

*Release 20171030*:
New Result.bg(func, *a, **kw) method to dispatch function in separate Thread to compute the Result value.

*Release 20170903*:
rename cs.asynchron to cs.result
