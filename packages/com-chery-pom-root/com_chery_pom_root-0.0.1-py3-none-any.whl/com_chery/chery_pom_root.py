"""
todo:
    tcp 链接池
    grpc
    done!!!! env from dotenv ?
    done!!!! other connection
    pip requirements validate in com_chery
    代码生成
    旧版服务注册和发现（不推荐）
"""
import os
import logging

# logging.basicConfig(level=logging.INFO)

__version__ = '0.0.1'


class ProjectConst(object):
    chery_user = 'chery_user'
    chery_school = 'chery_school'
    chery_user_model_service = 'chery_user_model_service'

    project_name_all = [
        chery_user,
        chery_school,
        chery_user_model_service,
    ]


_map_project_http_url = {
    ProjectConst.chery_user: 'http://127.0.0.1:3001',
    ProjectConst.chery_school: 'http://127.0.0.1:3002',
}

_map_project_db_session = {
    # 'chery_user': xxx,
}


class CheryPomError(Exception):
    pass


# import dotenv
# dotenv.load_dotenv(dotenv_path=os.path.join(sys.path[0], '.env'), verbose=True)
self_project_name = os.environ.get('PROJECT_NAME', None)

logging.info(f"chery_pom_root.version={__version__}, PROJECT_NAME={self_project_name}")

# if not self_project_name:
#     raise CheryPomRootError(f'环境变量缺失 PROJECT_NAME, sys.path[0]={sys.path[0]}')


if self_project_name:
    _map_project_http_url.pop(self_project_name, None)


def get_base_url(project_name: str):
    project_name = project_name.strip()
    if bool(self_project_name) and project_name == self_project_name:
        raise CheryPomError(f'暂不支持调用自己, project_name={project_name}')

    r = _map_project_http_url.get(project_name)
    if r is None:
        raise CheryPomError(f'http_url 没有找到, project_name={project_name}')
    else:
        return r


def set_db_session(project_name, db_session):
    assert project_name in ProjectConst.project_name_all
    _map_project_db_session[project_name] = db_session
    return True


def get_db_session(project_name):
    return _map_project_db_session.get(project_name)
