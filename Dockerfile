FROM python
COPY flask_server.py . 
COPY index.html .
COPY requirements.txt .

RUN command pip install --root-user-action=ignore -r requirements.txt

CMD python flask_server.py
