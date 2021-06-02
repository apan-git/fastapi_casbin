

#1.Dockerfile 配置
#2.构建镜像  docker build -t hahaha .  镜像名
#3.运行容器  docker run -d --name test1 -p 8090:80 hahaha    容器名   镜像名
#
#本地docker运行成功



#FROM python:3.8

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./ /app

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.douban.com/simple/

CMD ["python", "main.py"]
