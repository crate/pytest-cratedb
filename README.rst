==============
Pytest CrateDB
==============

.. image:: https://github.com/crate/pytest-cratedb/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/crate/pytest-cratedb/actions/workflows/tests.yml
    :alt: Build status

.. image:: https://codecov.io/gh/crate/pytest-cratedb/graph/badge.svg?token=OGZKWMMGMN
    :target: https://app.codecov.io/gh/crate/pytest-cratedb
    :alt: Coverage

.. image:: https://img.shields.io/pypi/v/pytest-cratedb.svg
    :target: https://pypi.org/project/pytest-cratedb/
    :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/pytest-cratedb.svg
    :target: https://pypi.org/project/pytest-cratedb/
    :alt: Python Version

.. image:: https://static.pepy.tech/badge/pytest-cratedb/month
    :target: https://pepy.tech/project/pytest-cratedb
    :alt: PyPI Downloads

.. image:: https://img.shields.io/pypi/status/pytest-cratedb.svg
    :target: https://pypi.org/project/pytest-cratedb/
    :alt: Status

.. image:: https://img.shields.io/pypi/l/pytest-cratedb.svg
    :target: https://pypi.org/project/pytest-cratedb/
    :alt: License

|

``pytest-cratedb`` is a plugin for pytest_ for writing integration tests that
interact with CrateDB_.

The CrateDB version can be specified using the ``--crate-version`` option when
running ``pytest``. By default, the latest stable version of CrateDB is used.

Usage
=====
``pytest-cratedb`` provides a pytest ``crate`` session fixture which downloads,
starts and stops a CrateDB node.

.. code-block:: python

   >>> def test_database_access(crate):
   ...     # perform database access
   ...     ...

Examples
========
See `tests/test_layer.py <https://github.com/crate/pytest-cratedb/blob/main/tests/test_layer.py>`_
for further examples.

Migration Notes
===============
This package, `pytest-cratedb`_ is a drop-in replacement for its predecessor
package `pytest-crate`_. It is recommended to uninstall pytest-crate
before installing pytest-cratedb in your Python environment.

Documentation and Help
======================
- `CrateDB Python Client documentation`_
- `CrateDB reference documentation`_
- `CrateDB cr8 utilities`_
- Other `support channels`_

Contributions
=============
The Pytest CrateDB Plugin is an open source project, and is `managed on
GitHub`_. We appreciate contributions of any kind.


.. _crate-python: https://pypi.org/project/crate/
.. _CrateDB: https://github.com/crate/crate
.. _CrateDB Python Client documentation: https://cratedb.com/docs/python/
.. _CrateDB cr8 utilities: https://github.com/mfussenegger/cr8/
.. _CrateDB reference documentation: https://cratedb.com/docs/reference/
.. _DB API 2.0: https://peps.python.org/pep-0249/
.. _managed on GitHub: https://github.com/crate/pytest-cratedb
.. _PyPI: https://pypi.org/
.. _pytest: https://docs.pytest.org
.. _pytest-crate: https://pypi.org/project/pytest-crate/
.. _pytest-cratedb: https://pypi.org/project/pytest-cratedb/
.. _support channels: https://cratedb.com/support/
