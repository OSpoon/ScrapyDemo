问题描述

当前环境win10，python_3.6.1，64位。
在windows下，在dos中运行pip install Scrapy报错：

building 'twisted.test.raiser' extension
error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
解决方案

http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted 下载twisted对应版本的whl文件（如我的Twisted‑17.5.0‑cp36‑cp36m‑win_amd64.whl），cp后面是python版本，amd64代表64位，运行命令：

pip install C:\Users\CR\Downloads\Twisted-17.5.0-cp36-cp36m-win_amd64.whl
其中install后面为下载的whl文件的完整路径名
安装完成后，再次运行：

pip install Scrapy
即可成功。

scrapy startproject tutorial

tutorial/
    scrapy.cfg            # 部署配置文件

    tutorial/             # Python模块,代码写在这个目录下
        __init__.py

        items.py          # 项目项定义文件

        pipelines.py      # 项目管道文件

        settings.py       # 项目设置文件

        spiders/          # 我们的爬虫/蜘蛛 目录
            __init__.py


如何运行我们爬虫

进入项目根目录，也就是上面的tutorial目录
cd tutorial
执行爬虫：
scrapy crawl quotes


Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\zhanxiaolin-n22\PycharmProjects\ScrapyDemo>scrapy startproject tutorial
'scrapy' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

C:\Users\zhanxiaolin-n22\PycharmProjects\ScrapyDemo>scrapy startproject tutorial
'scrapy' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

C:\Users\zhanxiaolin-n22\PycharmProjects\ScrapyDemo>scrapy startproject tutorial
'scrapy' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

C:\Users\zhanxiaolin-n22\PycharmProjects\ScrapyDemo>Scrapy
'Scrapy' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

C:\Users\zhanxiaolin-n22\PycharmProjects\ScrapyDemo>Scrapy
'Scrapy' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

C:\Users\zhanxiaolin-n22\PycharmProjects\ScrapyDemo>Scrapy
'Scrapy' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

C:\Users\zhanxiaolin-n22\PycharmProjects\ScrapyDemo>scrapy startproject tutorial
New Scrapy project 'tutorial', using template directory 'c:\\users\\zhanxiaolin-n22\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\scrapy\\templates\\project', created in:
    C:\Users\zhanxiaolin-n22\PycharmProjects\ScrapyDemo\tutorial

You can start your first spider with:
    cd tutorial
    scrapy genspider example example.com

C:\Users\zhanxiaolin-n22\PycharmProjects\ScrapyDemo>cd tutorial

C:\Users\zhanxiaolin-n22\PycharmProjects\ScrapyDemo\tutorial>scrapy crawl quotes
2017-11-15 16:17:15 [scrapy.utils.log] INFO: Scrapy 1.4.0 started (bot: tutorial)
2017-11-15 16:17:15 [scrapy.utils.log] INFO: Overridden settings: {'BOT_NAME': 'tutorial', 'NEWSPIDER_MODULE': 'tutorial.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['tutorial.spiders']}
2017-11-15 16:17:15 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.logstats.LogStats']

Unhandled error in Deferred:
2017-11-15 16:17:15 [twisted] CRITICAL: Unhandled error in Deferred:

2017-11-15 16:17:15 [twisted] CRITICAL:
Traceback (most recent call last):
  File "c:\users\zhanxiaolin-n22\appdata\local\programs\python\python36\lib\site-packages\twisted\internet\defer.py", line 1386, in _inlineCallbacks
    result = g.send(result)
  File "c:\users\zhanxiaolin-n22\appdata\local\programs\python\python36\lib\site-packages\scrapy\crawler.py", line 77, in crawl
    self.engine = self._create_engine()
  File "c:\users\zhanxiaolin-n22\appdata\local\programs\python\python36\lib\site-packages\scrapy\crawler.py", line 102, in _create_engine
    return ExecutionEngine(self, lambda _: self.stop())
  File "c:\users\zhanxiaolin-n22\appdata\local\programs\python\python36\lib\site-packages\scrapy\core\engine.py", line 69, in __init__
    self.downloader = downloader_cls(crawler)
  File "c:\users\zhanxiaolin-n22\appdata\local\programs\python\python36\lib\site-packages\scrapy\core\downloader\__init__.py", line 88, in __init__
    self.middleware = DownloaderMiddlewareManager.from_crawler(crawler)
  File "c:\users\zhanxiaolin-n22\appdata\local\programs\python\python36\lib\site-packages\scrapy\middleware.py", line 58, in from_crawler
    return cls.from_settings(crawler.settings, crawler)
  File "c:\users\zhanxiaolin-n22\appdata\local\programs\python\python36\lib\site-packages\scrapy\middleware.py", line 34, in from_settings
    mwcls = load_object(clspath)
  File "c:\users\zhanxiaolin-n22\appdata\local\programs\python\python36\lib\site-packages\scrapy\utils\misc.py", line 44, in load_object
    mod = import_module(module)
  File "c:\users\zhanxiaolin-n22\appdata\local\programs\python\python36\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "c:\users\zhanxiaolin-n22\appdata\local\programs\python\python36\lib\site-packages\scrapy\downloadermiddlewares\retry.py", line 20, in <module>
    from twisted.web.client import ResponseFailed
  File "c:\users\zhanxiaolin-n22\appdata\local\programs\python\python36\lib\site-packages\twisted\web\client.py", line 42, in <module>
    from twisted.internet.endpoints import HostnameEndpoint, wrapClientTLS
  File "c:\users\zhanxiaolin-n22\appdata\local\programs\python\python36\lib\site-packages\twisted\internet\endpoints.py", line 41, in <module>
    from twisted.internet.stdio import StandardIO, PipeAddress
  File "c:\users\zhanxiaolin-n22\appdata\local\programs\python\python36\lib\site-packages\twisted\internet\stdio.py", line 30, in <module>
    from twisted.internet import _win32stdio
  File "c:\users\zhanxiaolin-n22\appdata\local\programs\python\python36\lib\site-packages\twisted\internet\_win32stdio.py", line 9, in <module>
    import win32api
ModuleNotFoundError: No module named 'win32api'

C:\Users\zhanxiaolin-n22\PycharmProjects\ScrapyDemo\tutorial>

    安装win32compat

1. 基本命令

1. scrapy startproject 项目名称
   - 在当前目录中创建中创建一个项目文件（类似于Django）

2. scrapy genspider [-t template] <name> <domain>
   - 创建爬虫应用
   如：
      scrapy gensipider -t basic oldboy oldboy.com
      scrapy gensipider -t xmlfeed autohome autohome.com.cn
   PS:
      查看所有命令：scrapy gensipider -l
      查看模板命令：scrapy gensipider -d 模板名称

3. scrapy list
   - 展示爬虫应用列表

4. scrapy crawl 爬虫应用名称
   - 运行单独爬虫应用


文件说明：

scrapy.cfg  项目的主配置信息。（真正爬虫相关的配置信息在settings.py文件中）
items.py    设置数据存储模板，用于结构化数据，如：Django的Model
pipelines    数据处理行为，如：一般结构化的数据持久化
settings.py 配置文件，如：递归的层数、并发数，延迟下载等
spiders      爬虫目录，如：创建文件，编写爬虫规则