# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_simple_block']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.0.0,<3.0.0', 'nonebot2>=2.2.0,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-simple-block',
    'version': '1.0.1',
    'description': '屏蔽某个群聊或只相应某个群聊，方便开发者进行插件测试',
    'long_description': '<div align="center">\n  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n  <img src="https://github.com/WStudioGroup/hifumi-plugins/blob/main/remove.photos-removed-background.png" width="200">\n  <br>\n  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>\n</div>\n\n<div align="center">\n\n# nonebot-plugin-simple-block\n\n_✨ 屏蔽某个群聊或只相应某个群聊，方便开发者进行插件测试 ✨_\n\n\n<a href="./LICENSE">\n    <img src="https://img.shields.io/github/license/captain-wangrun-cn/nonebot-plugin-simple-block.svg" alt="license">\n</a>\n<a href="https://pypi.python.org/pypi/nonebot-plugin-simple-block">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-simple-block.svg" alt="pypi">\n</a>\n<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">\n\n</div>\n\n## 📖 介绍\n\n屏蔽某个群聊或只相应某个群聊，方便开发者进行插件测试\n\n## 💿 安装\n\n<details open>\n<summary>使用 nb-cli 安装</summary>\n在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装\n\n    nb plugin install nonebot-plugin-simple-block\n\n</details>\n\n<details>\n<summary>使用包管理器安装</summary>\n在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令\n\n<details>\n<summary>pip</summary>\n\n    pip install nonebot-plugin-simple-block\n\n</details>\n\n\n打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入\n\n    plugins = ["nonebot_plugin_simple_block"]\n\n</details>\n\n## ⚙️ 配置\n\n在 nonebot2 项目的`.env`文件中添加下表中的必填配置\n\n| 配置项          | 类型   | 必填 | 默认值 | 说明                  |\n|:------------:|:----:|:---:|:---:|:-------------------:|\n| group_blacklist | list | 否  | [ ]  | 黑名单，添加在黑名单内的群将不会响应 |\n| group_whitelist | list | 否  | [ ]  | 白名单，只会响应白名单内的群    |\n\n>[!IMPORTANT]\n>当黑名单和白名单同时配置时，将会优先使用黑名单\n\n## 📃 更新日志\n### 1.0.1（2025.01.01）\n- 📃修复了一些问题\n### 1.0.0（2024.12.20）\n- 🧋发布插件\n',
    'author': 'WR',
    'author_email': 'wangrun114514@foxmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/captain-wangrun-cn/nonebot-plugin-simple-block',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
