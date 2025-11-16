============================
Changelog for pytest-cratedb
============================

Unreleased
==========
- Maintenance: Fixed type hint for ``CrateLayer::dsn(self) -> Optional[str]``

2024/10/08 v0.4.0
=================
- Modernized package
- Renamed package to ``pytest-cratedb``
- Published maintenance release

2019/05/28 v0.3.0
=================

- Replace ``print`` statements with ``logging.debug`` statements so that
  retrieving the fixture does not produce output that is captured in doctests.
  This may break existing usages of the fixture in doctests in case the output
  of the ``getfixture`` method was matched.

2019/04/05 v0.2.0
=================

- Allow additional CrateDB settings in the ``crate_layer`` factory fixture
  which are applied on node start.

- Expose addresses of started CrateDB nodes

2019/04/05 v0.1.0
=================

- Initial pytest plugin
