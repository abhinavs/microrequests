microrequests
=============

This module makes consuming microservices in Python more efficient.
Python’s requests module is fantastic and highly configurable,
microrequests builds a wrapper over requests module and enables
connection pooling as part of initialisation. This ensures that you use
the same connection instead of creating one with every new request,
while still working with requests’ clean APIs and mechanism.

This is first version of microrequests and we intend to add more
customisation for to consume microservices easily and efficiently.

Installation
------------

The easiest way to install microrequests is using pip

.. code:: sh

   $ pip install microrequests


Usage
-----

To use, simply do:

.. code:: python

   import microrequests

   mr = microrequests.init()
   res = mr.get("http://httpbin.org") # mr is requests' session object and you can use it in similar manner
   print(res.text)

you can also customize max_retries, pool_connections and pool_maxsize -
they are by default set to 1, 100 and 50 respectively pool_connections
is the number of urllib3 connection pools to cache and poolmaxsize\* is
the maximum number of connections to save in the pool

.. code:: python

   import microrequests

   mr = microrequests.init(max_retries=2, pool_connections=10, pool_size=5)
   res = mr.get("http://httpbin.org")
   print(res.text)

Tests
-----

To run tests:

.. code:: sh

   $ tox

TODO
----

-  Write more tests

Contributing
------------

Bug reports and pull requests are welcome on GitHub at
https://github.com/abhinavs/microrequests. This project is intended to
be a safe, welcoming space for collaboration, and contributors are
expected to adhere to the `code of conduct`_.

Code of Conduct
---------------

Everyone interacting in the microrequests project’s codebases, issue
trackers, chat rooms and mailing lists is expected to follow the `code
of conduct`_.

Copyright
---------

Copyright (c) 2020 Abhinav Saxena. See `MIT License`_ for further
details.

.. _code of conduct: https://github.com/abhinavs/microrequests/blob/master/CODE_OF_CONDUCT.md
.. _MIT License: LICENSE.txt

