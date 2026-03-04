FROM docker.io/library/python:3.13.12-alpine3.23
COPY dist/ .
COPY lib/ .
RUN pip install frcm-0.1.0-py3-none-any.whl
RUN pip install ttf_indicator-0.1.0-py3-none-any.whl
CMD ["ttf-service"]