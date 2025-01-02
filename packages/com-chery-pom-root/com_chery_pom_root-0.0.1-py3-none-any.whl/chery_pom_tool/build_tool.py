"""
私有pypi上传
"""


def build_and_upload(
        project_pkg_name,
        pypi_pkg_name,
        chery_pom_root_required_version,
        project_pkg_version,
        include_files,
):
    import os
    import shutil
    import uuid
    import subprocess
    import sys
    import datetime

    def create_temp_build_dir():
        # 在系统目录下（~/）创建 .chery_pom 文件夹，再创建临时文件夹作为打包的临时目录，临时文件夹名字是 uuid4 + time now
        home_dir = os.path.expanduser("~")
        chery_pom_dir = os.path.join(home_dir, ".chery_pom")
        if not os.path.exists(chery_pom_dir):
            os.makedirs(chery_pom_dir, exist_ok=True)

        # 创建以 uuid4 命名的文件夹
        build_folder_uuid = str(uuid.uuid4())
        time_strftime = 'tmp_%Y%m%d_%H%M%S_'
        build_folder_uuid = datetime.datetime.now().strftime(time_strftime) + build_folder_uuid
        build_folder_path = os.path.join(chery_pom_dir, build_folder_uuid)
        os.makedirs(build_folder_path)

        return build_folder_path

    def generate_setup_content():
        s = f'''
from setuptools import setup, find_packages

setup(
    name='{pypi_pkg_name}',
    version='{project_pkg_version}',
    packages=[
        'com_chery',
        'com_chery.{project_pkg_name}',
    ],
    include_package_data=True,
    install_requires=[
        'requests',
        'python-dotenv',
    ],
    description='temp package, will be deleted later 2024-12-24',
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    # author='Your Name',
    # author_email='your.email@example.com',
    # url='https://example.com/com_example_root',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
        '''.strip()
        return s

    def check_and_copy_file(temp_build_dir: str):
        abs_filepath = sys.argv[0]
        if not abs_filepath.endswith('pom.py'):
            raise Exception('打包上传程序必须在 pom.py 中执行')

        current_dir = os.path.dirname(abs_filepath)
        # print('current_dir', current_dir)

        # 3. 判断 current_dir 下是否有 xx.py 文件
        if len(include_files) == 0:
            raise Exception(f'{include_files} 必须包含想要打包的 .py 文件（ __init__ 会自动添加）')

        include_files.extend(['pom.py', '__init__.py'])
        include_file_target_dir = os.path.join(temp_build_dir, 'com_chery', project_pkg_name)
        if not os.path.exists(include_file_target_dir):
            os.makedirs(include_file_target_dir, exist_ok=True)

        for i in include_files:
            file_py_path = os.path.join(current_dir, i)
            if not os.path.exists(file_py_path):
                if i == '__init__.py':
                    continue
                else:
                    raise Exception(f"{file_py_path} 在 include_files 中，但是文件夹下没有找到")
            # ----------------
            shutil.copy(file_py_path, os.path.join(include_file_target_dir, i))

        # -----------------------------
        # 文件夹中写入 setup.py 文件
        setup_py_path = os.path.join(temp_build_dir, "setup.py")
        with open(setup_py_path, "w") as setup_file:
            setup_content = generate_setup_content()
            setup_file.write(setup_content)

        python_exec = sys.executable
        cmd_res1 = subprocess.run([python_exec, "setup.py", "sdist", "bdist_wheel"], cwd=temp_build_dir)
        # cmd_res = subprocess.run([python_exec, "-m", "build"], cwd=temp_build_dir)
        if cmd_res1.returncode != 0:
            raise Exception(f'打包失败, {cmd_res1.stdout}, {cmd_res1.stderr}')

        cmd_res2 = subprocess.run([python_exec, "-m", "twine", "upload", "dist/*"], cwd=temp_build_dir)
        if cmd_res2.returncode != 0:
            raise Exception(f'上传失败, {cmd_res2.stdout}, {cmd_res2.stderr}')

    temp_build_dir = None
    try:
        temp_build_dir = create_temp_build_dir()
        check_and_copy_file(temp_build_dir)
    finally:
        if temp_build_dir is None:
            pass
        else:
            shutil.rmtree(temp_build_dir)
            pass
