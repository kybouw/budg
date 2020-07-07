FROM python:3-alpine

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY defaultplan.ini /root/.config/budg/defaultplan.ini

CMD [ "python", "budg.py", "123.45" ]