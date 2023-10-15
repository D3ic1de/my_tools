## 非常简单的一个子域名扫描工具

使用前需先在`/ProxyPool`中运行`docker-compose up`来启动代理池

`ProxyPool`的原地址是 https://github.com/Python3WebSpider/ProxyPool

### agent.py

这是一个测试代理池是否能用的脚本

### scan.py

这是用来子域名爆破的脚本

### subdomain.txt

这是自己收集的一些子域名，师傅们可以自己添加些东西

#### 使用方法

`python ./scan.py`

然后会让你输入需要爆破的父域名

就差不多是这样

![text.png](https://bu.dusays.com/2023/10/16/652c1495074b1.png)

### 之后可能会做

多线程扫描，加快一下爆破的速度

可能会改用别的语言写