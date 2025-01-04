v6.5.0
======

Features
--------

- Add type annotations for Traversable.open. (#317)
- Require Python 3.9 or later.


v6.4.5
======

Bugfixes
--------

- Omit sentinel values from a namespace path. (#311)


v6.4.4
======

No significant changes.


v6.4.3
======

Bugfixes
--------

- When inferring the caller in ``files()`` correctly detect one's own module even when the resources package source is not present. (python/cpython#123085)


v6.4.2
======

Bugfixes
--------

- Merged fix for UTF-16 BOM handling in functional tests. (#312)


v6.4.1
======

Bugfixes
--------

- When constructing ZipReader, only append the name if the indicated module is a package. (python/cpython#121735)


v6.4.0
======

Features
--------

- The functions
  ``is_resource()``,
  ``open_binary()``,
  ``open_text()``,
  ``path()``,
  ``read_binary()``, and
  ``read_text()`` are un-deprecated, and support
  subdirectories via multiple positional arguments.
  The ``contents()`` function also allows subdirectories,
  but remains deprecated. (#303)
- Deferred select imports in for a speedup (python/cpython#109829).


v6.3.2
======

Bugfixes
--------

- Restored expectation that local standard readers are preferred over degenerate readers. (#298)


v6.3.1
======

Bugfixes
--------

- Restored expectation that stdlib readers are suppressed on Python 3.10. (#257)


v6.3.0
======

Features
--------

- Add ``Anchor`` to ``importlib.resources`` (in order for the code to comply with the documentation)


v6.2.0
======

Features
--------

- Future compatibility adapters now ensure that standard library readers are replaced without overriding non-standard readers. (#295)


v6.1.3
======

No significant changes.


v6.1.2
======

Bugfixes
--------

- Fixed NotADirectoryError when calling files on a subdirectory of a namespace package. (#293)


v6.1.1
======

Bugfixes
--------

- Added missed stream argument in simple.ResourceHandle. Ref python/cpython#111775.


v6.1.0
======

Features
--------

- MultiplexedPath now expects Traversable paths. String arguments to MultiplexedPath are now deprecated.


Bugfixes
--------

- Enabled support for resources in namespace packages in zip files. (#287)


v6.0.1
======

Bugfixes
--------

- Restored Apache license. (#285)


v6.0.0
======

Deprecations and Removals
-------------------------

- Removed legacy functions deprecated in 5.3. (#80)


v5.13.0
=======

Features
--------

- Require Python 3.8 or later.


v5.12.0
=======

* #257: ``importlib_resources`` (backport) now gives
  precedence to built-in readers (file system, zip,
  namespace packages), providing forward-compatibility
  of behaviors like ``MultiplexedPath``.

v5.11.1
=======

v5.10.4
=======

* #280: Fixed one more ``EncodingWarning`` in test suite.

v5.11.0
=======

* #265: ``MultiplexedPath`` now honors multiple subdirectories
  in ``iterdir`` and ``joinpath``.

v5.10.3
=======

* Packaging refresh, including fixing EncodingWarnings
  and some tests cleanup.

v5.10.2
=======

* #274: Prefer ``write_bytes`` to context manager as
  proposed in gh-100586.

v5.10.1
=======

* #274: Fixed ``ResourceWarning`` in ``_common``.

v5.10.0
=======

* #203: Lifted restriction on modules passed to ``files``.
  Now modules need not be a package and if a non-package
  module is passed, resources will be resolved adjacent to
  those modules, even for modules not found in any package.
  For example, ``files(import_module('mod.py'))`` will
  resolve resources found at the root. The parameter to
  files was renamed from 'package' to 'anchor', with a
  compatibility shim for those passing by keyword.

* #259: ``files`` no longer requires the anchor to be
  specified and can infer the anchor from the caller's scope
  (defaults to the caller's module).

v5.9.0
======

* #228: ``as_file`` now also supports a ``Traversable``
  representing a directory and (when needed) renders the
  full tree to a temporary directory.

v5.8.1
======

* #253: In ``MultiplexedPath``, restore expectation that
  a compound path with a non-existent directory does not
  raise an exception.

v5.8.0
======

* #250: Now ``Traversable.joinpath`` provides a concrete
  implementation, replacing the implementation in ``.simple``
  and converging with the behavior in ``MultiplexedPath``.

v5.7.1
======

* #249: In ``simple.ResourceContainer.joinpath``, honor
  names split by ``posixpath.sep``.

v5.7.0
======

* #248: ``abc.Traversable.joinpath`` now allows for multiple
  arguments and specifies that ``posixpath.sep`` is allowed
  in any argument to accept multiple arguments, matching the
  behavior found in ``zipfile.Path`` and ``pathlib.Path``.

  ``simple.ResourceContainer`` now honors this behavior.

v5.6.0
======

* #244: Add type declarations in ABCs.

v5.5.0
======

* Require Python 3.7 or later.
* #243: Fix error when no ``__pycache__`` directories exist
  when testing ``update-zips``.

v5.4.0
======

* #80: Test suite now relies entirely on the traversable
  API.

v5.3.0
======

* #80: Now raise a ``DeprecationWarning`` for all legacy
  functions. Instead, users should rely on the ``files()``
  API introduced in importlib_resources 1.3. See
  `Migrating from Legacy <https://importlib-resources.readthedocs.io/en/latest/using.html#migrating-from-legacy>`_
  for guidance on avoiding the deprecated functions.

v5.2.3
======

* Updated readme to reflect current behavior and show
  which versions correspond to which behavior in CPython.

v5.0.7
======

* bpo-45419: Correct ``DegenerateFiles.Path`` ``.name``
  and ``.open()`` interfaces to match ``Traversable``.

v5.2.2
======

* #234: Fix refleak in ``as_file`` caught by CPython tests.

v5.2.1
======

* bpo-38291: Avoid DeprecationWarning on ``typing.io``.

v5.2.0
======

* #80 via #221: Legacy API (``path``, ``contents``, ...)
  is now supported entirely by the ``.files()`` API with
  a compatibility shim supplied for resource loaders without
  that functionality.

v5.0.6
======

* bpo-38693: Prefer f-strings to ``.format`` calls.

v5.1.4
======

* #225: Require
  `zipp 3.1.0 <https://zipp.readthedocs.io/en/latest/history.html#v3-1-0>`_
  or later on Python prior to 3.10 to incorporate those fixes.

v5.0.5
======

* #216: Make MultiplexedPath.name a property per the
  spec.

v5.1.3
======

* Refresh packaging and improve tests.
* #216: Make MultiplexedPath.name a property per the
  spec.

v5.1.2
======

* Re-release with changes from 5.0.4.

v5.0.4
======

* Fixed non-hermetic test in test_reader, revealed by
  GH-24670.

v5.1.1
======

* Re-release with changes from 5.0.3.

v5.0.3
======

* Simplified DegenerateFiles.Path.

v5.0.2
======

* #214: Added ``_adapters`` module to ensure that degenerate
  ``files`` behavior can be made available for legacy loaders
  whose resource readers don't implement it. Fixes issue where
  backport compatibility module was masking this fallback
  behavior only to discover the defect when applying changes to
  CPython.

v5.1.0
======

* Added ``simple`` module implementing adapters from
  a low-level resource reader interface to a
  ``TraversableResources`` interface. Closes #90.

v5.0.1
======

* Remove pyinstaller hook for hidden 'trees' module.

v5.0.0
======

* Removed ``importlib_resources.trees``, deprecated since 1.3.0.

v4.1.1
======

* Fixed badges in README.

v4.1.0
======

* #209: Adopt
  `jaraco/skeleton <https://github.com/jaraco/skeleton>`_.

* Cleaned up some straggling Python 2 compatibility code.

* Refreshed test zip files without .pyc and .pyo files.

v4.0.0
======

* #108: Drop support for Python 2.7. Now requires Python 3.6+.

v3.3.1
======

* Minor cleanup.

v3.3.0
======

* #107: Drop support for Python 3.5. Now requires Python 2.7 or 3.6+.

v3.2.1
======

* #200: Minor fixes and improved tests for namespace package support.

v3.2.0
======

* #68: Resources in PEP 420 Namespace packages are now supported.

v3.1.1
======

* bpo-41490: ``contents`` is now also more aggressive about
  consuming any iterator from the ``Reader``.

v3.1.0
======

* #110 and bpo-41490: ``path`` method is more aggressive about
  releasing handles to zipfile objects early, enabling use-cases
  like ``certifi`` to leave the context open but delete the underlying
  zip file.

v3.0.0
======

* Package no longer exposes ``importlib_resources.__version__``.
  Users that wish to inspect the version of ``importlib_resources``
  should instead invoke ``.version('importlib_resources')`` from
  ``importlib-metadata`` (
  `stdlib <https://docs.python.org/3/library/importlib.metadata.html>`_
  or `backport <https://pypi.org/project/importlib-metadata>`_)
  directly. This change eliminates the dependency on
  ``importlib_metadata``. Closes #100.
* Package now always includes its data. Closes #93.
* Declare hidden imports for PyInstaller. Closes #101.

v2.0.1
======

* Select pathlib and contextlib imports based on Python version
  and avoid pulling in deprecated
  [pathlib](https://pypi.org/project/pathlib). Closes #97.

v2.0.0
======

* Loaders are no longer expected to implement the
  ``abc.TraversableResources`` interface, but are instead
  expected to return ``TraversableResources`` from their
  ``get_resource_reader`` method.

v1.5.0
======

* Traversable is now a Protocol instead of an Abstract Base
  Class (Python 2.7 and Python 3.8+).

* Traversable objects now require a ``.name`` property.

v1.4.0
======

* #79: Temporary files created will now reflect the filename of
  their origin.

v1.3.1
======

* For improved compatibility, ``importlib_resources.trees`` is
  now imported implicitly. Closes #88.

v1.3.0
======

* Add extensibility support for non-standard loaders to supply
  ``Traversable`` resources. Introduces a new abstract base
  class ``abc.TraversableResources`` that supersedes (but
  implements for compatibility) ``abc.ResourceReader``. Any
  loader that implements (implicitly or explicitly) the
  ``TraversableResources.files`` method will be capable of
  supplying resources with subdirectory support. Closes #77.
* Preferred way to access ``as_file`` is now from top-level module.
  ``importlib_resources.trees.as_file`` is deprecated and discouraged.
  Closes #86.
* Moved ``Traversable`` abc to ``abc`` module. Closes #87.

v1.2.0
======

* Traversable now requires an ``open`` method. Closes #81.
* Fixed error on ``Python 3.5.{0,3}``. Closes #83.
* Updated packaging to resolve version from package metadata.
  Closes #82.

v1.1.0
======

* Add support for retrieving resources from subdirectories of packages
  through the new ``files()`` function, which returns a ``Traversable``
  object with ``joinpath`` and ``read_*`` interfaces matching those
  of ``pathlib.Path`` objects. This new function supersedes all of the
  previous functionality as it provides a more general-purpose access
  to a package's resources.

  With this function, subdirectories are supported (Closes #58).

  The
  documentation has been updated to reflect that this function is now
  the preferred interface for loading package resources. It does not,
  however, support resources from arbitrary loaders. It currently only
  supports resources from file system path and zipfile packages (a
  consequence of the ResourceReader interface only operating on
  Python packages).

1.0.2
=====

* Fix ``setup_requires`` and ``install_requires`` metadata in ``setup.cfg``.
  Given by Anthony Sottile.

1.0.1
=====

* Update Trove classifiers.  Closes #63

1.0
===

* Backport fix for test isolation from Python 3.8/3.7.  Closes #61

0.8
===

* Strip ``importlib_resources.__version__``.  Closes #56
* Fix a metadata problem with older setuptools.  Closes #57
* Add an ``__all__`` to ``importlib_resources``.  Closes #59

0.7
===

* Fix ``setup.cfg`` metadata bug.  Closes #55

0.6
===

* Move everything from ``pyproject.toml`` to ``setup.cfg``, with the added
  benefit of fixing the PyPI metadata.  Closes #54
* Turn off mypy's ``strict_optional`` setting for now.

0.5
===

* Resynchronize with Python 3.7; changes the return type of ``contents()`` to
  be an ``Iterable``.  Closes #52

0.4
===

* Correctly find resources in subpackages inside a zip file.  Closes #51

0.3
===

* The API, implementation, and documentation is synchronized with the Python
  3.7 standard library.  Closes #47
* When run under Python 3.7 this API shadows the stdlib versions.  Closes #50

0.2
===

* **Backward incompatible change**.  Split the ``open()`` and ``read()`` calls
  into separate binary and text versions, i.e. ``open_binary()``,
  ``open_text()``, ``read_binary()``, and ``read_text()``.  Closes #41
* Fix a bug where unrelated resources could be returned from ``contents()``.
  Closes #44
* Correctly prevent namespace packages from containing resources.  Closes #20

0.1
===

* Initial release.


..
   Local Variables:
   mode: change-log-mode
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 78
   coding: utf-8
   End:
