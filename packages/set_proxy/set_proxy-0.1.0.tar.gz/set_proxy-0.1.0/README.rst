set_proxy
=========

一个简单的 Python 工具，用于设置和管理系统代理。

功能特点
--------

- 快速设置系统代理
- 支持 HTTP 和 HTTPS 代理
- 跨平台支持（Windows、macOS、Linux）

安装
----

.. code-block:: bash

    pip install set-proxy

使用方法
--------

.. code-block:: python

    from set_proxy import set_proxy

    # 设置代理
    set_proxy("http://127.0.0.1:7890")

    # 清除代理
    set_proxy(None)

    # 检查 Google 连接状态
    from set_proxy import check_google

    # 默认检查 https://www.google.com
    check_google()

    # 或者指定自定义 URL
    check_google("https://www.google.com/search")

贡献
----

欢迎提交 Issue 和 Pull Request！

发布流程
--------

本项目使用 GitHub Actions 自动发布到 PyPI。发布新版本的步骤如下：

1. 更新版本号（在 pyproject.toml 中手动修改版本号）：

   .. code-block:: toml

       [project]
       name = "set-proxy"
       version = "0.1.0"  # 修改这里的版本号
       # ...

2. 提交更改：

   .. code-block:: bash

       git add pyproject.toml
       git commit -m "bump: 版本更新到 0.1.0"

3. 创建标签：

   .. code-block:: bash

       git tag v0.1.0  # 使用对应的版本号

4. 推送更改和标签：

   .. code-block:: bash

       git push
       git push --tags

推送标签后，GitHub Actions 将自动构建并发布包到 PyPI。

许可证
------

MIT License