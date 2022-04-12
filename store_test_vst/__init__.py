try:
    from vstutils.environment import prepare_environment, cmd_execution  # noqa: F401
except ImportError:  # nocv
    def prepare_environment(*args, **kwargs):  # type: ignore
        pass

__version__ = '1.0.0'

settings = {
    "VST_PROJECT": 'store_test_vst',
    "VST_ROOT_URLCONF": 'vstutils.urls',
    "VST_WSGI": 'vstutils.wsgi',
    "VST_PROJECT_GUI_NAME": "STORE_TEST_VST",
    "DJANGO_SETTINGS_MODULE": 'store_test_vst.settings',
}

prepare_environment(**settings)
