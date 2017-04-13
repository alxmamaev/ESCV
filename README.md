# Электронная система учета посетителей
![Header](https://github.com/alxmamaev/image-storage/blob/master/escv/header.png)
<br>
**Электронная система учета посетителей** - это совокупность программно аппаратных средств, главной задачей которых является - учет посещений какой либо организации или заведения в электронном виде.

## Как это работает
  Работа ЭСУП заключается в электронном учете посещений каких либо пользователей. Это можеть быть необходимо, например, для учета посещения
столовой в школе, учета рабочего времени сотрудников, или же учет посещения различных занятий в учебных учреждениях.

![Работа системы](https://github.com/alxmamaev/image-storage/blob/master/escv/img_1.jpg)

 Работа системы выглядит следующим образом:
* Пользователь подносит карту к устройству
* Устройство считывает данные с карты и отправляет их на сервер
* Сервер обрабатывает полученные данные и записывает их в базу данных
* Полученные даные можно просмотреть через веб-интерфейс, а так же сохранить в виде документа.

## Устройства
### ЭСУП-wifi
* Данная версия устройства базируется на чипе *ESP8266*, под управлением node-mcu.
* В качестве "меток" используются *rfid карты/брелоки*.
* Данные передаются по средствам *wifi*, по протоколу *http* на сервер.
* Для работы *wifi*, используется встроенный в *ESP8266* wifi модуль

### ЭСУП-ethernet
* Данная версия устройства базируется на чипе *atmega-128*.
* В качестве "меток" используются *rfid карты/брелоки*.
* Данные передаются по средствам *ethernet*, по протоколу *http*.
* Для работы *ethernet*, используется *enc28j60*.


## Установка системы
### Сервер
Для работы серверной части системы необходимо иметь:

* Компьютер под управлением Linux или Windows
* bash
* Python3 с установленным pip3

Все операции ниже выполняются через терминал Bash.

После того как вы произвели установку python3, необходимо установить все зависимости проекта из файла *requirements.txt*


`pip3 install -r requirements.txt`


Создайте файл с настройками *.env*.
```
export DATABASE_URL="путь_до_базы_данных/название.db"
```
Запустите файл *setup.py*, `python3 setup.py`.
После этого будет создана база данных, которую вы можете заполнить с помощью DBbrowser.



После данных операций можно запустить сервер с помощью команды: `python3 run.py`.


Таким образом сервер станет доступен в локальной сети сервера.

### Устройство
#### ЭСУП-wifi
Подключите устройство к компьютеру с помощью usb-кабеля, далее с помощью serial-монитора введите название и пароль wifi сети, а так же адрес сервера.
Устройство запомнит эти настройки и в дальнейшем данная операция понадобится только при смене wifi сети или адреса сервера.


Подключите устройство к сети с помощью micro-usb кабеля. После того как устройство перестанет мигать светодиодом, оно будет готово к работе.

#### ЭСУП-ethernet
Настройка данной модели аналогична настройки предыдущей, отличие заключается в ненадобоности введения настроек wifi.

Подключите устройство к сети с помощью micro-usb, а так же Ethernet кабель к локальной сети сервера. После того как устройство перестанет мигать светодиодом, оно будет готово к работе.


## Политика распространения
Исходный код, а так же другие исходники в виде печатных плат распространяется бесплатно под лицензией GPLv3.


Если вы хотите получить готовый образец устройства, или настроенную серверную часть системы, свяжитесь с нами по контактам ниже.

## Контакты
**Мамаев Александр** главный разработчик, основатель проекта- alxmamaev@ya.ru

**Адрей Жевлаков** Веб разработчик, дизайнер проекта - azbango5@gmail.com
