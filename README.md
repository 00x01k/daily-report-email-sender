# daily-report-email-sender
Daily Report Email Sender
Этот проект предназначен для автоматической отправки ежедневных отчетов по электронной почте с использованием Python.

Оглавление
Описание
Требования
Установка
Настройка
Использование
Планировщик задач
Unix (cron)
Windows (Task Scheduler)
Структура проекта
Вклад
Лицензия
Описание
Этот скрипт позволяет автоматически отправлять ежедневные отчеты по электронной почте. Он поддерживает отправку писем с вложениями и позволяет настраивать HTML-шаблон для тела письма. Скрипт легко настраивается через конфигурационный файл и поддерживает работу с несколькими получателями.

Требования
Python 3.x
Установленные библиотеки (см. requirements.txt)
Установка
Клонируйте репозиторий:

sh
Копировать код
git clone https://github.com/yourusername/daily-report-email-sender.git
cd daily-report-email-sender
Создайте и активируйте виртуальное окружение (необязательно, но рекомендуется):

sh
Копировать код
python -m venv venv
source venv/bin/activate  # для Windows используйте `venv\Scripts\activate`
Установите зависимости:

sh
Копировать код
pip install -r requirements.txt
Создайте файл .env в корневом каталоге и добавьте переменные окружения:

plaintext
Копировать код
EMAIL_PASSWORD=your_password
Настройте config.yaml согласно вашим требованиям.

НастройкаDaily Report Email Sender
Этот проект предназначен для автоматической отправки ежедневных отчетов по электронной почте с использованием Python.

Оглавление
Описание
Требования
Установка
Настройка
Использование
Планировщик задач
Unix (cron)
Windows (Task Scheduler)
Структура проекта
Вклад
Лицензия
Описание
Этот скрипт позволяет автоматически отправлять ежедневные отчеты по электронной почте. Он поддерживает отправку писем с вложениями и позволяет настраивать HTML-шаблон для тела письма. Скрипт легко настраивается через конфигурационный файл и поддерживает работу с несколькими получателями.

Требования
Python 3.x
Установленные библиотеки (см. requirements.txt)
Установка
Клонируйте репозиторий:

sh
Копировать код
git clone https://github.com/yourusername/daily-report-email-sender.git
cd daily-report-email-sender
Создайте и активируйте виртуальное окружение (необязательно, но рекомендуется):

sh
Копировать код
python -m venv venv
source venv/bin/activate  # для Windows используйте `venv\Scripts\activate`
Установите зависимости:

sh
Копировать код
pip install -r requirements.txt
Создайте файл .env в корневом каталоге и добавьте переменные окружения:

plaintext
Копировать код
EMAIL_PASSWORD=your_password
Настройте config.yaml согласно вашим требованиям.

Настройка
Конфигурационный файл
Файл config.yaml содержит настройки для отправки писем и подключения к SMTP-серверу. Пример файла:

yaml
Копировать код
email:
  to_email:
    - "recipient1@example.com"
    - "recipient2@example.com"
  from_email: "your_email@example.com"
  subject: "Ежедневный отчет"
  body: "templates/email_body.html"
  attachment_path: "path_to_report.pdf"
smtp:
  server: "smtp.gmail.com"
  port: 465
  use_ssl: true
  login: true
  username: "your_email@example.com"
  password: "your_password"
Шаблон HTML
Файл templates/email_body.html содержит HTML-шаблон для тела письма. Пример файла:

html
Копировать код
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Body</title>
</head>
<body>
    <p>Здравствуйте,</p>
    <p>Прилагаю ежедневный отчет.</p>
    <p>С уважением,<br>Ваше имя</p>
</body>
</html>
Использование
Для отправки ежедневного отчета запустите скрипт:

sh
Копировать код
python email_sender.py
Планировщик задач
Unix (cron)
Откройте crontab для редактирования:

sh
Копировать код
crontab -e
Добавьте следующую строку, чтобы скрипт выполнялся ежедневно в 9 утра:

sh
Копировать код
0 9 * * * /usr/bin/python3 /path/to/email_sender.py
Windows (Task Scheduler)
Откройте "Планировщик задач" и выберите "Создать задачу".
Установите триггер на ежедневное выполнение.
В разделе "Действия" укажите "Запустить программу" и введите путь к Python интерпретатору, а также путь к вашему скрипту.
Структура проекта
plaintext
Копировать код
daily-report-email-sender/
│
├── .env.example            # Пример файла переменных окружения
├── .gitignore              # Файл исключений Git
├── config.yaml             # Конфигурационный файл
├── email_sender.py         # Основной скрипт для отправки писем
├── templates/
│   └── email_body.html     # HTML-шаблон тела письма
├── README.md               # Документация проекта
└── requirements.txt        # Список зависимостей
Вклад
PR приветствуются! Для крупных изменений, пожалуйста, сначала откройте issue, чтобы обсудить, что вы хотели бы изменить. Убедитесь, что все тесты прошли успешно перед отправкой PR.

Лицензия
Этот проект лицензирован под лицензией MIT. Подробнее см. файл LICENSE.

Теперь у вас есть расширенный README.md, который включает в себя всю необходимую информацию для настройки и использования проекта, а также инструкции по вкладу и лицензии.
Конфигурационный файл
Файл config.yaml содержит настройки для отправки писем и подключения к SMTP-серверу. Пример файла:

yaml
Копировать код
email:
  to_email:
    - "recipient1@example.com"
    - "recipient2@example.com"
  from_email: "your_email@example.com"
  subject: "Ежедневный отчет"
  body: "templates/email_body.html"
  attachment_path: "path_to_report.pdf"
smtp:
  server: "smtp.gmail.com"
  port: 465
  use_ssl: true
  login: true
  username: "your_email@example.com"
  password: "your_password"
Шаблон HTML
Файл templates/email_body.html содержит HTML-шаблон для тела письма. Пример файла:

html
Копировать код
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Body</title>
</head>
<body>
    <p>Здравствуйте,</p>
    <p>Прилагаю ежедневный отчет.</p>
    <p>С уважением,<br>Ваше имя</p>
</body>
</html>
Использование
Для отправки ежедневного отчета запустите скрипт:

sh
Копировать код
python email_sender.py
Планировщик задач
Unix (cron)
Откройте crontab для редактирования:

sh
Копировать код
crontab -e
Добавьте следующую строку, чтобы скрипт выполнялся ежедневно в 9 утра:

sh
Копировать код
0 9 * * * /usr/bin/python3 /path/to/email_sender.py
Windows (Task Scheduler)
Откройте "Планировщик задач" и выберите "Создать задачу".
Установите триггер на ежедневное выполнение.
В разделе "Действия" укажите "Запустить программу" и введите путь к Python интерпретатору, а также путь к вашему скрипту.
Структура проекта
plaintext
Копировать код
daily-report-email-sender/
│
├── .env.example            # Пример файла переменных окружения
├── .gitignore              # Файл исключений Git
├── config.yaml             # Конфигурационный файл
├── email_sender.py         # Основной скрипт для отправки писем
├── templates/
│   └── email_body.html     # HTML-шаблон тела письма
├── README.md               # Документация проекта
└── requirements.txt        # Список зависимостей
Вклад
PR приветствуются! Для крупных изменений, пожалуйста, сначала откройте issue, чтобы обсудить, что вы хотели бы изменить. Убедитесь, что все тесты прошли успешно перед отправкой PR.

Лицензия
Этот проект лицензирован под лицензией MIT. Подробнее см. файл LICENSE.

Теперь у вас есть расширенный README.md, который включает в себя всю необходимую информацию для настройки и использования проекта, а также инструкции по вкладу и лицензии.
