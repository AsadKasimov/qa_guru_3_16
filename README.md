# Проект по тестированию главной страницы сайта "look.online"
> <a target="_blank" href="https://rosatom-career.ru/">Ссылка на портал</a>

тут скрин сайта
![This is an image](/design/images/rosatom-career.ru.jpeg)

#### Список проверок, реализованных в автотестах
- [x] Наличие требуемых заголовков в верхнем меню страницы
- [x] Наличие заданных пунктов подменю для меню "Молодым специалистам"
- [x] Наличие блока подписки на социальные сети в подвале сайта
- [x] Наличие имиджевого текста на первой странице
- [x] Выполнение поиска заданной вакансии. Проверка, что открылась соответствующая страница и содержимое строки поиска соответствует заданному
#### Список проверок ручного тестирования
- [x] Визуальная характеристика главной страницы сайта, соответствие единому корпоративному стилю
- [x] Адаптивность вёрстки
- [x] Соответствие вёрстки сайта общепринятым стандартам

## Проект реализован с использованием
Java Gradle IntelliJ IDEA Selenide Selenoid JUnit5 Jenkins Allure Report Allure TestOps Telegram Jira

<p  align="center">
  <code><img width="5%" title="Python" src="./images/icons/Python-logo-notext.svg"></code>
  <code><img width="5%" title="PyCharm" src="./images/icons/pycharm.svg"></code>
  <code><img width="6%" title="PyCharm" src="./images/icons/pytest.png"></code>
  <code><img width="6%" title="PyCharm" src="./images/icons/selene.png"></code>
  <code><img width="5%" title="Allure Report" src="./images/icons/allure-Report-logo.svg"></code>
  <code><img width="5%" title="Allure TestOps" src="./images/icons/allure-ee-logo.svg"></code>
  <code><img width="5%" title="Github" src="./images/icons/git-logo.svg"></code>
  <code><img width="5%" title="Jenkins" src="./images/icons/jenkins-logo.svg"></code>
  <code><img width="5%" title="Jira" src="./images/icons/jira-logo.svg"></code>
  <code><img width="5%" title="Selenoid" src="./images/icons/selenoid-logo.svg"></code>
  <code><img width="5%" title="Telegram" src="./images/icons/Telegram.svg"></code>

</p>

### Для запуска автотестов в Jenkins
#### 1. Открыть <a target="_blank" href="[https://jenkins.autotests.cloud/job/09-ElenaSeversk-unit13/](https://jenkins.autotests.cloud/job/003_python-edbeg1337-unit16/)">проект</a>

![This is an image](.images/icons/jenkins1.png)

#### 2. Выбрать пункт **Собрать сейчас**
#### 3. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](.images/icons/jenkins1.png)


# Полная статистика по прохождению тестпланов, отчёты и приложения к ним хранятся в Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/804">Сссылка на проект в AllureTestOps</a> (запрос доступа admin@qa.guru)

### Кейсы тест-плана выполнения ручного тестирования
![This is an image](/design/images/manual.png)
### Кейсы тест-плана выполнения автотестирования
![This is an image](/design/images/auto.png)
### Общий список всех кейсов, имеющихся в системе (без разделения по тест-планам и виду выполнения тестирования)
![This is an image](/design/images/testcases.png)
### Пример dashboard с общими результатами тестирования
![This is an image](/design/images/dashboard_all.png)
### В том числе сводная статистика запусков
![This is an image](/design/images/dashboard_all2.png)

### Пример отчёта выполнения одного из автотестов
![This is an image](/design/images/onecasereport.png)
#### *После окончания выполнения автотестов по каждому из них в отчёте доступны скриншоты и исходный код страницы, лог консоли браузера и видеозапись выполнения теста.*

### Пример видеозаписи прохождения теста
![This is an image](/design/images/Video.gif)


## По результатам ручного тестирования выявлены дефекты, зафиксированные в соответствующих задачах AllureTestOps
### Тест план выполнения ручного тестирования
![This is an image](/design/images/testplan2.png)
### Сводные результаты ручного тестирования
![This is an image](/design/images/failedresult.png)
### Пример описания дефекта в Allure TestOps
![This is an image](/design/images/testops2.png)
### Список выявленных дефектов, открытых как задачи в Allure TestOps
![This is an image](design/images/defects.png)

# Результаты выполнения тестов и информация о выявленных дефектах интегрированы с Atlassian Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-286">Ссылка на задачу в Jira</a> (запрос доступа admin@qa.guru)

Задачи на выявленные дефекты оформлены как подзадачи к данной. Связаны с соответствующими дефектами в Allure TestOps

![This is an image](/design/images/jira_n.png)

# Настроено автоматическое оповещение о результатах сборки Jenkins в Telegram-бот
![This is an image](/design/images/bot.png)


:heart: <a target="_blank" href="https://qa.guru">qa.guru</a><br/>
:blue_heart: <a target="_blank" href="https://t.me/qa_automation">t.me/qa_automation</a>
