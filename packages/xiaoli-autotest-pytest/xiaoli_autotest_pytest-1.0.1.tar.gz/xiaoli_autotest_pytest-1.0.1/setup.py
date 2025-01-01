from setuptools import setup, find_packages

setup(
    # 包的名称
    name='xiaoli-autotest-pytest',

    # 版本号，遵循 PEP 440
    version='1.0.1',

    # 项目主页
    url='https://gitee.com/roger813/xiaoli-autotest-pytest.git',

    # 作者
    author='Li wenhuan',

    # 作者邮箱
    author_email='roger813@163.com',

    # 许可证类型
    license='MIT',

    # 项目的简短描述
    description='Simple autotest framework, using python and pytest as the basis for data comparison, interface testing, UI testing and so on',

    # 长描述，可以从README文件中读取
    long_description=open('README.md', encoding='utf-8').read(),

    # 长描述的类型，例如text/plain或text/markdown
    long_description_content_type='text/markdown',

    # 包的分类
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],

    # 包的关键字
    keywords='example project',

    # 包的包
    packages=find_packages(),

    # 需要的依赖
    install_requires=[
        'allure-pytest',
        'openpyxl',
        'pandas',
        'playwright',
        'psycopg2',
        'pyodbc',
        'pytest-assume',
        'pytest-xdist',
        'requests',
        'xlwings',
    ],

    # 额外的依赖
    extras_require={
        'dev': [],
    },

    # 包含的数据文件
    include_package_data=True,

    # 其他参数
    zip_safe=False,
)