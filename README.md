# SmartStudy. Как правильно развернуть и ничего не сломать

## 1. Клонируем git-repo

```bash
git clone https://github.com/Sashayerty/SmartStudy.git
```

## 2. Переходим в него

```bash
cd path/to/your/repo # лучше всего вводить относительный путь
```

## 3. Создаем виртуальное окружение

```bash
python3 -m venv venv
```

## 4. Активируем venv

```bash
# Windows
venv/Scripts/activate

# Unix/MacOs
source venv/bin/activate
```

## 5. Загружаем зависимости

```bash
pip3 install -r ./requirements/prod.txt
```

## 6. Запуск приложения

```bash
python3 main.py
```
