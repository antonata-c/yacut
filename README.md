# Укорачиватель ссылок YaCut

**Ссылка на [документацию](https://github.com/antonata-c/yacut/blob/master/openapi.yml)**


### Используемые технологии:
- ***Python 3.10***
- ***Flask***
- ***SQLAlchemy***

## Подготовка
##### Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/antonata-c/yacut.git
```

```
cd yacut
```

##### Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
* Если у вас Linux/macOS
  ```
  source venv/bin/activate
  ```
* Если у вас windows
  ```
  source venv/Scripts/activate
  ```

##### Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

##### Создайте файл .env, содержащий переменные окружения, пример представлен в файле `.env.example`

## Развертывание и запуск
##### Проинициализируйте базу данных, примените миграции:
```
flask db init
```
```
flask db migrate
```
##### Запустите проект
```
flask run
```
#### Проект готов к использованию!
***
### Автор работы:
**[Антон Земцов](https://github.com/antonata-c)**
