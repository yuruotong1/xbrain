## 打包

打包成 whl 文件：

```
py -m pip install --upgrade build
py -m build
```

在 `C:\Users\用户名`下的 `.pypirc`文件配置基本信息：

```
[distutils]
index-servers = pypi
[pypi]
#测试环境
repository = https://upload.pypi.org/legacy/
username = __token__
password = token
```

上传到官方：

`py -m twine upload dist/*`
