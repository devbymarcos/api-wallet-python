FROM python:3.10


WORKDIR /app
COPY pyproject.toml .
RUN pip install poetry
RUN poetry install --no-root
COPY . .
EXPOSE 5000
CMD [ "poetry","run","python","app.py" ]