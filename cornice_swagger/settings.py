"""
When particular docstring are long and complex, there appears a need to
put it into <description> of the path, and fill <summary> block
only with begining of this long docstring.
To do so, we must set threshold, above which we will treat docstring as long.
That threshold is set by the LONG_DOCSTRING_LENGTH variable below.
"""
LONG_DOCSTRING_LENGTH = 50
