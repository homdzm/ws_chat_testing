FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN apt update && \
    apt install -y curl unzip && \
    rm -rf /var/lib/apt/lists/*

ADD https://github.com/allure-framework/allure2/releases/download/2.23.0/allure-2.23.0.zip /tmp/allure.zip

RUN unzip /tmp/allure.zip -d /opt && \
    mv /opt/allure-2.23.0 /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/local/bin/allure && \
    rm /tmp/allure.zip

RUN mkdir -p /app/allure-results /app/allure-report && chmod -R 777 /app

ENTRYPOINT ["sh", "-c", "echo 'Запуск тестов...'; pytest -v -s --alluredir=/app/allure-results && allure generate /app/allure-results -o /app/allure-report --clean; echo 'Тесты завершены и отчет сгенерирован.'"]
