from setuptools import setup, find_packages

setup(
    name="jh_scrapyd",
    version="0.2.5",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "jh_scrapyd=jh_scrapyd.__main__:main",  # 定义命令行入口
        ],
    },
    package_data={
        'jh_scrapyd': ['default_scrapyd.conf', 'VERSION', 'jh/*', 'jh/queue/*', 'jh/utils/*'],
    },
    license='MIT',
    description='Preemptive scraping cluster',
    long_description=open('jh_scrapyd/README.md').read(),
    long_description_content_type='text/markdown',
    author='Mr Ye',
    author_email='mrye5869@gmail.com',
    url='https://github.com/mrye5869/jh_scrapyd'
)