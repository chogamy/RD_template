FROM python:3.10.13

WORKDIR /this_repo

COPY ./this_repo/ .

# RUN apt update etc...

RUN pip install --no-cache-dir -r /this_repo/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "port(int)"]
