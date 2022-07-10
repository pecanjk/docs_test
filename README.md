# mkdocs test

## Requirements
``` bash
pip install -r requirements.txt
```

## How To
[refer this](https://zhuanlan.zhihu.com/p/383582472)
``` bash
mkdir docs
cd docs
mkdocs new . #- Create a new project.
mkdocs build #build and generate static html folder 'site'. put site/ into .gitignore
mkdocs serve #visit local site
```

需要修改一下配置文件mkdocs.yml把site_name改成自己项目的名称，然后执行：
``` bash
mkdocs gh-deploy --clean
```
这个命令会在github项目上创建一个gh-pages分支，并将当前目录中的site/目录下的内容推送到远程的gh-pages分支。 然后就可以在你访问你的文档了地址https://{username}.github.io/{projectname}

后面文档编写就放到docs目录下编写即可，每次更新文档后上传，进入docs目录，然后执行一行命令即可：
```
mkdocs gh-deploy --clean
```


### Project Layout
```
mkdocs.yml    # The configuration file.
docs/
    index.md  # The documentation homepage.
    ...       # Other markdown pages, images and other files.
```


### Reference
[Python技术文档最佳实践](https://zhuanlan.zhihu.com/p/333742823)