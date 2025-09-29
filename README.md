# Лабораторная работа #1


## Continuous Integration & Continuous Delivery


Реализовано CRUD приложение над сущностью Person

API:

* `GET /persons/{personId}` – информация о человеке;
* `GET /persons` – информация по всем людям;
* `POST /persons` – создание новой записи о человеке;
* `PATCH /persons/{personId}` – обновление существующей записи о человеке;
* `DELETE /persons/{personId}` – удаление записи о человеке.

[Описание API](person-service.yaml) в формате OpenAPI.

* Для сборки использовался Github Actions.
* Запросы / ответы должны в формате JSON
* Если запись по id не найдена, то возвращает HTTP статус 404 Not Found.
* При создании новой записи о человека (метод POST /person) возвращается HTTP статус 201 Created с пустым телом и
  Header `Location: /api/v1/persons/{personId}`, где `personId` – id созданной записи.
* Приложение содержит unit-тесты на реализованные операции.
* Приложение завернуто в Docker.
* Деплой на Render реализован средствами GitHub Actions, для деплоя использовался Docker.
