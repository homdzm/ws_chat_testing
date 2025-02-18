#!/bin/bash

IMAGE_NAME="image_widget_chat_testing"

echo "Собираем Docker-образ..."
docker build -t $IMAGE_NAME .

echo "Запускаем контейнер и выполняем тесты..."
docker run --rm \
  -v $(pwd)/allure-results:/app/allure-results \
  -v $(pwd)/allure-report:/app/allure-report \
  $IMAGE_NAME

echo "Allure отчет находится в $(pwd)/allure-report"
sleep 10