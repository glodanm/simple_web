FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /simple_web

COPY start.sh requirements.txt /simple_web/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

RUN chmod +x start.sh

CMD ["sh", "start.sh"]
