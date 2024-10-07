==============
Pytest CrateDB
==============

.. image:: https://github.com/crate/pytest-cratedb/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/crate/pytest-cratedb/actions/workflows/tests.yml
    :alt: Build status

.. image:: https://codecov.io/gh/crate/pytest-cratedb/branch/master/graph/badge.svg
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
package `pytest-crate`_.


.. _CrateDB: https://cratedb.com
.. _pytest: https://docs.pytest.org
.. _pytest-crate: https://pypi.org/project/pytest-crate/
.. _pytest-cratedb: https://pypi.org/project/pytest-cratedb/
