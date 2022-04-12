STORE_TEST_VST
==============


GUI
---

* Run: `python -m store_test_vst web`
* Stop: `python -m store_test_vst web stop=/tmp/store_test_vst_web.pid`

Before first run, you should run:

* `python -m store_test_vst migrate`
* `python -m store_test_vst createsuperuser`


Tests
-----

Just run `tox` in project directory.
Read more: `https://tox.readthedocs.io/en/latest/`_.


Build
-----

* Run ``tox -e build``
