FROM continuumio/miniconda3:latest

USER root

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN conda install -y -c conda-forge pip

COPY ./requirements /requirements
# All imports needed for autodoc.
RUN pip install  -r /requirements/requirements.txt

WORKDIR /app
ENV PYTHONPATH /app/:${PYTHONPATH}

#CMD make livehtml
