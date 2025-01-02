"""
如果看到这里说明 pip install 已成功。
本 pkg 的另一些代码在 chery_pom_tool 下，需要一起使用。
com_chery 代码是主体逻辑。
chery_pom_tool 代码是各种打包发布，或更新本地 import 的工具类
"""
from .chery_pom_root import (
    __version__,
    CheryPomError,
    ProjectConst,
)

version = __version__
