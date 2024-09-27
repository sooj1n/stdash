FROM python:3.11

WORKDIR /code

COPY /src/stdash/home.py /code
COPY /src/stdash/img /code/img
COPY /src/stdash/pages /code/pages

RUN pip install --no-cache-dir --upgrade git+https://github.com/sooj1n/stdash.git@0.4/dockerizing

CMD ["streamlit", "run", "home.py", "--server.port=8000", "--server.address=0.0.0.0"]
