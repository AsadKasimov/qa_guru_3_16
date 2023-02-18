
# Пример организации автотестирования для образовательной платформы look.online

## :open_book: Содержание:
- [Описание проекта](#heavy_check_mark-описание)
- [Кратко](#heavy_check_mark-кратко)
- [Технологии и инструменты](#gear-технологии-и-инструменты)
- Что проверяем:
  - [UI](#heavy_check_mark-реализованные-ui-проверки)
  - [API](#heavy_check_mark-реализованные-api-проверки)
- Запуск тестов:
  - [Jenkins](#-запуск-тестов-из-jenkins)
- Отчеты:
  - [Allure](#bar_chart-отчеты-о-прохождении-тестов-доступны-в-allure)
  - [Telegram](#-telegram)
  - [Email](#email-email)
- [Allure TestOps](#briefcase-проект-интегрирован-с-allure-testops)
- [Видео прогона теста](#movie_camera-пример-видео-тестового-прогона)


## :heavy_check_mark: Описание
В проекте представлены примеры UI и API автоматизации тестирования на Python. 
<p>При написании тестов применялись инструменты объектно-ориентированной парадигмы, а также использовался шаблон 
проектирования PageObjects.
<p>Выделены тест-кейсы. Реализована параметризация тестов.
<p>Подключена система отчетности Allure Reports с вложениями (логи, скриншоты, видео, etc). 
В UI-тестах отображено два типа передачи шагов теста в отчет:
 
- Лямбда-степы через with allure.step
- Декораторы @step с автоматическим подтягиванием allure.title из названия функций и их параметров

<p>Также по факту прохождения теста отправляется уведомление с результатами в Telegram и на электронную почту.
<p>Браузер в UI-тестах запускается удаленно в Selenoid.
<p>Реализована интеграция с Allure TestOps.

## :heavy_check_mark: Кратко
- [x] `Page Object` с шагами `Fluent of Invocations`
- [x] `Application Manager`
- [x] Параметризованный запуск тестов
- [x] `Request/response` спецификация для API тестов
- [x] Self-documenting code
- [x] Запуск тестов, используя `Jenkins` и `Selenoid`
- [x] `Allure Reports` с вложениями (логи, скриншоты, видео)
- [x] Логирование requests/responses в `Allure Reports`
- [x] Интеграция с `Allure TestOps`
- [x] Отправка результатов тестирования по `email` и в `Telegram`

## :gear: Технологии и инструменты:

<p  align="center">
  <code><img width="5%" title="Python" src="https://github.com/GithubRedMouth/kasimov/blob/main/images/icons/Python-logo-notext.svg"></code>
  <code><img width="5%" title="PyCharm" src="https://github.com/GithubRedMouth/kasimov/blob/main/images/icons/pycharm.svg"></code>
  <code><img width="6%" title="PyCharm" src="https://github.com/GithubRedMouth/kasimov/blob/main/images/icons/pytest.png"></code>
  <code><img width="6%" title="PyCharm" src="https://github.com/GithubRedMouth/kasimov/blob/main/images/icons/selene.png"></code>
  <code><img width="5%" title="Allure Report" src="https://github.com/GithubRedMouth/kasimov/blob/main/images/icons/allure-Report-logo.svg"></code>
  <code><img width="5%" title="Allure TestOps" src="https://github.com/GithubRedMouth/kasimov/blob/main/images/icons/allure-ee-logo.svg"></code>
  <code><img width="5%" title="Github" src="https://github.com/GithubRedMouth/kasimov/blob/main/images/icons/git-logo.svg"></code>
  <code><img width="5%" title="Jenkins" src="https://github.com/GithubRedMouth/kasimov/blob/main/images/icons/jenkins-logo.svg"></code>
  <code><img width="5%" title="Jira" src="https://github.com/GithubRedMouth/kasimov/blob/main/images/icons/jira-logo.svg"></code>
  <code><img width="5%" title="Selenoid" src="https://github.com/GithubRedMouth/kasimov/blob/main/images/icons/selenoid-logo.svg"></code>
  <code><img width="5%" title="Telegram" src="https://github.com/GithubRedMouth/kasimov/blob/main/images/icons/Telegram.svg"></code>

</p>

## :heavy_check_mark: Реализованные UI-проверки

> - авторизация зарегистрированным пользователем;
> - добавление курса в 'Wishlist';
> - поступление на курс:
>   - авторизованным пользователем;
>   - неавторизованным пользователем;
> - поиск:
>   - бесплатного курса с сертификатом;
>   - несуществующего курса;
> - открытие поп-ап окна 'News' из меню.

## :heavy_check_mark: Реализованные API-проверки

> - OAuth 2.0 авторизация:
>   - зарегистрированным пользователем;
>   - зарегистрированным пользователем с невалидным паролем;
>   - несуществующим пользователем;
> - получение курс-листа по номеру;
> - получение информации профиля:
>   - существующего пользователя;
>   - несуществующего пользователя;
> - изменение имени зарегистрированным пользователем.

## <img width="4%" title="Jenkins" src=""> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/003_python-edbeg1337-unit16/)


## :bar_chart: Отчеты о прохождении тестов доступны в Allure


### <code><img width="5%" title="Allure Report" src="./images/icons/allure-Report-logo.svg"></code>

#### Примеры отображения тестов



### <code><img width="5%" title="Telegram" src="./images/icons/Telegram.svg"></code> Telegram

Настроена отправка отчета в Telegram

<img src="media/screenshots/telegram.jpg" alt="Telegram"/>


## :briefcase: Проект интегрирован с Allure TestOps 

#### Автоматически собраны тест-кейсы

<code><img width="5%" title="Allure TestOps" src="./images/icons/allure-ee-logo.svg"></code>

#### Представлены дашборды аналитики

<img src="media/screenshots/allure_testops2.jpg" alt="Allure TestOps"/>

## :movie_camera: Пример видео тестового прогона

В отчетах Allure для каждого UI-теста прикреплен не только скриншот, но и видео прохождения теста

<p align="center">
  <img title="Video" src="media/video/video_test_search_free_course_with_certificate.gif">
</p>
