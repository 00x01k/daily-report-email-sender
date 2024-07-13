import smtplib
import os
import logging
import yaml
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
from datetime import datetime

# Загрузка переменных окружения из файла .env
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_path="config.yaml"):
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def load_html_template(template_path):
    try:
        with open(template_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"HTML template file not found: {template_path}")
        return None

def send_email(config):
    try:
        # Настройка параметров сообщения
        msg = MIMEMultipart()
        msg['From'] = config['email']['from_email']
        msg['To'] = ", ".join(config['email']['to_email'])
        msg['Subject'] = f"{config['email']['subject']} - {datetime.now().strftime('%Y-%m-%d')}"

        # Загрузка HTML шаблона
        html_body = load_html_template(config['email']['body'])
        if html_body is None:
            return

        # Тело письма
        msg.attach(MIMEText(html_body, 'html'))

        # Прикрепление файла
        attachment_path = config['email'].get('attachment_path')
        if attachment_path and os.path.isfile(attachment_path):
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
                msg.attach(part)
        else:
            logging.warning(f"Attachment file not found or not specified: {attachment_path}")

        # Подключение к SMTP серверу и отправка письма
        smtp_config = config['smtp']
        if smtp_config['use_ssl']:
            server = smtplib.SMTP_SSL(smtp_config['server'], smtp_config['port'])
        else:
            server = smtplib.SMTP(smtp_config['server'], smtp_config['port'])
            server.starttls()
        
        if smtp_config['login']:
            server.login(smtp_config['username'], smtp_config['password'])

        server.sendmail(config['email']['from_email'], config['email']['to_email'], msg.as_string())
        server.quit()
        logging.info(f"Email sent to {', '.join(config['email']['to_email'])}")

    except FileNotFoundError as fnf_error:
        logging.error(f"Attachment file not found: {fnf_error}")
    except smtplib.SMTPException as smtp_error:
        logging.error(f"SMTP error occurred: {smtp_error}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

if __name__ == "__main__":
    config_path = "config.yaml"
    config = load_config(config_path)
    if not config:
        logging.error("Failed to load configuration file.")
    elif not all(key in config['smtp'] for key in ('server', 'port', 'username', 'password')):
        logging.error("SMTP configuration is incomplete.")
    elif not all(key in config['email'] for key in ('from_email', 'to_email', 'subject', 'body')):
        logging.error("Email configuration is incomplete.")
    else:
        send_email(config)
