from .user import Account
from .pom import PROJECT_PKG_NAME as _project_pkg_name

import com_chery


db_session = com_chery.chery_pom_root.get_db_session(_project_pkg_name)


def get_all_accounts():
    accounts = db_session.query(Account).filter().limit(3).all()
    return accounts

