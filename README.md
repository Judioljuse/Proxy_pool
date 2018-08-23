# IP代理池

本项目所采集的IP资源都来自互联网，愿景是为企业级爬虫项目提供一个**高可用低延迟的高匿IP代理池**。

# 项目亮点
- 代理抓取提取精准
- 代理校验严格合理
- 架构灵活，便于扩展

# 快速开始

注意，代码请在[release](https://github.com/Judioljuse/Proxy_pool/)列表中下载

## 单机部署

### 服务端
- 安装Redis。 有问题可以阅读[这篇文章](http://www.runoob.com/redis/redis-install.html)的相关部分。
- 根据Redis的实际配置修改项目配置文件[config.py](config.py)中的`REDIS_HOST`、`REDIS_PASSWORD`等参数。
- 安装[flask](http://flask.pocoo.org/)

  > pip install flask
- 启动整个项目，包括网页和爬虫
  > python run.py 

- 只启动网页调试，
  > python api.py




