1.0.1
-----

Unreleased

-   Fix old-style class issue in Python 2. :pr:`1`
-   Account for a ".x" suffix on the project version. "1.1.x" will
    be seen as "1.1" for hiding old log entries. :pr:`5`
-   Fix error when log entries are at the very top of a page before any
    other content. :issue:`3`
-   Config is now prefixed with ``log_cabinet_`` instead of
    ``changelog_``. The old names are deprecated. :pr:`7`


1.0.0
-----

Released 2017-05-05

-   Initial release
