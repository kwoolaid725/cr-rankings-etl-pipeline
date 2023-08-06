FROM ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.6.3-python3.11}
ENV PYTHONPATH=$PYTHONPATH:${AIRFLOW_USER_HOME}


USER airflow
RUN pip install --upgrade pip
RUN pip install "setuptools<58"
#RUN pip3 install \
#    psycopg2==2.7.5



COPY requirements.txt requirements.txt
WORKDIR /opt/airflow
RUN pip install -r requirements.txt
#RUN pip install selenium && \
#    pip install bs4 && \
#    pip install lxml && \
#    pip install selenium-stealth
