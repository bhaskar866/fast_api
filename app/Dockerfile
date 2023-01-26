FROM python:3

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY . /fast_api

WORKDIR /fast_api

ENV PYTHONPATH="${PYTHONPATH}:/fast_api/app"


# CMD python -m uvicorn app.main:app --reload

CMD ["/bin/bash","./server.sh"]