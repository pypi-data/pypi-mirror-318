import requests

from com_chery import chery_pom_root
from .pom import PROJECT_PKG_NAME as _project_pkg_name


# todo
import typing
# if typing.TYPE_CHECKING:
#     from .user_blueprint import get_user_profile
#     get_user_profile = get_user_profile
#     exit(-1)

_base_url = chery_pom_root.get_base_url(_project_pkg_name)


def get_user_profile():
    res = requests.get(_base_url + '/api/user/profile')
    return res.json()
