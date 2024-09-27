FROM python:3.11

WORKDIR /code

COPY /src/stdash/home.py /code

RUN pip install --no-cache-dir --upgrade git+https://github.com/sooj1n/stdash.git@0.4/dockerizing

CMD ["streamlit", "run", "home.py", "--server.port=8501", "--server.address=0.0.0.0"]
