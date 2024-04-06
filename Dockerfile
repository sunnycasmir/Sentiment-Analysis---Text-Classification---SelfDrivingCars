FROM python:3.8.18
COPY . /sent_app
WORKDIR /sent_app
RUN pip install -r requirements.txt
CMD streamlit run sent_app.py