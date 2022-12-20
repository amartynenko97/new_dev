### *Generate 2500 thousand historical records in excel using functions and load the insert query into the database*
___

#### *Installing nessesary software*

*У меня ОС Linux Debian 11, в которую я собираюсь устновить `MySQL-8` и подключатся к ней с моего хоста с виндой. Тип сети VirtualBox - `NAT`*

+ *Обновить системные пакеты до последней версии*

```sh
$ sudo apt update
$ sudo apt upgrade
```

+ *Установить утилиту `wget`*

```sh
$ apt install wget
```

+ *Загрузите пакет `mySQL` последней версии с помощью следующей команды*

```sh
$ wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb
```

+ *Установить пакет `mySQL`. В выпадающем меню выбрать -ОК*

```sh
$ wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb
$ sudo apt update
$ sudo apt install mysql-server
```  

+ *Проверить статус базы данных*

```sh
$ sudo service mysql status
``` 

+ *Можно в нее зайти локально*
  
```sh
$ sudo mysql -u root -p
``` 

![](./data/photo1.png)

+ *Установить `MySQL Workbench` на `Windows`. С его помощью можно создавать и редактировать таблицы и другие объекты, управлять доступом пользователей и полноценно администрировать БД. По ссылке https://dev.mysql.com/downloads/workbench/*


+ *Для удаленного доступа откроем порт 3306 на виртуальной машине Debian*

```sh
$ sudo ufw allow 3306
$ sudo ufw enable
$ sudo ufw status verbose
``` 
![](./data/photo5.png)

+ *Настроить проброс портов для `ssh` и `mysql` на VirtualBox для того чтобы мы смогли подключиться к базе при режиме сети NAT*

![](./data/photo2.png)

+ *Настройка сеанса выглядит так:*

![](./data/photo3.png)

*У меня получилось установить сеанс. Хотя Экземпляр `MySQL` настроен только на прослушивание локальных подключений. Это настройка `MySQL` по умолчанию, но она не будет работать для удаленной настройки базы данных, поскольку `MySQL` должна иметь возможность прослушивать внешний IP-адрес, по которому можно получить доступ к серверу. По этой инструкции - https://ruslanmv.com/blog/How-to-create-your-MySQL-Server-in-Virtual-Box. В этом конфиге:*

```sh
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
``` 

![](./data/photo4.png)

___
#### *Наполняем базу с помощью ранее сформированных квери их excel*


+ *Дальше нужно создать базу данных `schema` можно это делать с помощью `Workbench` а можно вбить запрос в консоль. И не забыть указать какакой будет стандарт кодирования символов для базы, чтобы она распознавала кирилицу и все-такое. Ниже будет 2 варианта:*

![](./data/photo8.png)

![](./data/photo7.png)

+ *Потом выбрав базу данных в `Workbench` проклацать и заполнить колонки с соответсвующими форматами которые были указаны в задании. Обратить внимание какая колонка будет иметь `primary key`, это ключик который дает возможность идентифицировать каждую строку в таблице, и значения его должны быть однозначны и уникальны. Для этого я и создал отдельный столбец `id_pk`*

![](./data/photo13.png)

*`Workbench` сам сгенерирует запрос к базе данных остается только его запустить*


*Я же потом когда у меня не получалось вставить некотрые значения в базу  подкоректировал формат `DATATIME` добавив `(3)` потому что база данных видит только такой формат даты `YYYY-MM-DD HH:MI:SS`, а нам необходимы были милисекунды.
`VARCHAR` это формат для текста
`ENUM` это формат для нескольких значений*

```sql
CREATE TABLE `test`.`new_table` (
  `id_pk` INT NOT NULL,
  `ID` VARCHAR(10) NOT NULL,
  `ProviderID` ENUM('FCXM', 'SQM') NOT NULL,
  `Direction` ENUM('sell', 'buy') NOT NULL,
  `Instrument` VARCHAR(6) NOT NULL,
  `CreationDate` DATETIME(3) NOT NULL,
  `ChangeDate` DATETIME(3) NOT NULL,
  `Status` ENUM('new', 'in progress', 'reject', 'part fill', 'done', 'fill') NOT NULL,
  `InitialPrice` DOUBLE NOT NULL,
  `FillPrice` DOUBLE NOT NULL,
  `InitialVolume` DOUBLE NOT NULL,
  `FillVolume` DOUBLE NOT NULL,
  `Tags` VARCHAR(45) NOT NULL,
  `Description` VARCHAR(45) NOT NULL,
  `ExtraData` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id_pk`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;
```
+ *Проверим как отображаются колонки при `utf8` `utf_unicode_ci` которые мы создали*

![](./data/photo14.png)


+ *Теперь наполняем нашу таблицу строками которые я подготовил в ексель. Важно то что `mysql` не понимает что такое разделитель запятая, нужно вставлять с точкой. И дату в `DATATIME` пришлось перевернуть именно в `excel` но можно было использовать функцию `STR_TO_DATE` для колонки для отображения даты в какой хочешь полседовательности.*



```sql
INSERT INTO `test`.`new_table` (`id_pk`,`ID`, `ProviderID`, `Direction`, `Instrument`, `CreationDate`, `ChangeDate`, `Status`, `InitialPrice`, `FillPrice`, `InitialVolume`, `FillVolume`, `Tags`, `Description`, `ExtraData`) VALUES('1','104C4DA18', 'SQM', 'buy', 'GBPUSD', '2022.11.22 12:24:31.949', '2022.11.22 12:26:09.259', 'reject', '1.1950', '0', '9379.361', '0', 'Sociedad Quimica', 'Ордер на сумму 9379,4 создан', 'Ордер на покупку был открыт, его состояние сейчас - reject');
```

![](./data/photo15.png)

  
![](./data/photo16.png)
