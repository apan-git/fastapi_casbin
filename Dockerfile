


#FROM python:3.8

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./ /app

WORKDIR /app
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["python", "/app/main.py"]
