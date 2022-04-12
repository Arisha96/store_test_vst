from vstutils.settings import *  # noqa: F403
import os


INSTALLED_APPS += [  # noqa: F405
    'store_test_vst',
]

DEBUG = True

API[VST_API_VERSION][r'items'] = dict(
    model='store_test_vst.models.Item',
    view='store_test_vst.views.ItemViewSet'
)

# Adds link to the task view to the GUI menu
PROJECT_GUI_MENU.insert(0, {
    'name': 'Item',
    'span_class': 'fa fa-list-alt',
    'url': '/items'
})

CORS_ORIGIN_WHITELIST = (
    'http://localhost:5000',
    'http://127.0.0.1:5000',
)
CORS_ORIGIN_ALLOW_ALL = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'client/static/media')
