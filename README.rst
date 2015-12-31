This is a pygments style based on the popular Monokai color scheme. This version is suitable for light backgrounds, whereas the original scheme is designed for dark backgrounds.


Installation
============

Conda
-----
::

   $ conda install -c mlgill pygments-style-monokailight

PyPI and pip
------------
::

   $ pip install pygments-style-monokailight


Source
------
::

   $ git clone git://github.com/mlgill/pygments-style-monokailight
   $ cd pygments-style-monokailight
   $ python setup.py install


Usage Sample
------------
::

   >>> from pygments.formatters import HtmlFormatter
   >>> HtmlFormatter(style='monokailight').style
   <class 'pygments_style_monokailight.MonokaiLightStyle'>


Export the style as CSS
-----------------------
::

   pygmentize -S monokailight -f html > monokailight.css

