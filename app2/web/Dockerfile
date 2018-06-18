FROM python
LABEL maintainer="abanbn@almbrand.dk"

EXPOSE 8000
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]