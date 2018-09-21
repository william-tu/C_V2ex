# C_V2ex

### 简介

本项目是一款文章浏览型应用，旨在提供优质的文章导航。 目前爬取的文章有知乎豆瓣果壳的文章，数据来源于爬虫 [N-spider](https://github.com/william-tu/N-Spider)

本项目亦可自己发布优秀文章，对优秀文章进行收藏

更多功能正在开发中

### 后端技术栈
* Python
* Flask
* Mysql
* Redis
* Celery

### 技术介绍
- 使用Redis对高请求的接口数据进行存储与备份

- 使用Celery和Redis异步处理任务，提高并发与稳定性

- 设计Restful Api,解决跨域问题，降低前后端耦合

- 使用Nginx+supervisor+gunicorn+virtualenv进行部署

- 灵活使用第三发库和服务（邮件服务，七牛云等）

### 前端技术栈
* Vue
* Vuex
* axios
* element-ui
* vue-route
* 等


