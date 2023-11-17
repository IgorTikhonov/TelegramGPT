# ChatGPT Telegram Bot

![python-version](https://img.shields.io/badge/python-3.9+-blue.svg)
[![python-telegram-bot-version](https://img.shields.io/badge/PythonTelegramBot-20.3+-critical.svg)](https://github.com/python-telegram-bot/python-telegram-bot/releases/tag/v20.3)
![db](https://img.shields.io/badge/db-MySQL8-ff69b4.svg)
[![openai-version](https://img.shields.io/badge/openai-0.27.6-orange.svg)](https://openai.com/)
[![license](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

## 🥰️️️️️️Before everything

The solution is based on https://github.com/V-know/ChatGPT-Telegram-Bot v1.0.3.

written by [V-know](https://github.com/V-know).

Thank you, V-know, very much for your contribution to the development of convenient modern intelligent solutions available to the average Python user.

## 📄General info

A Telegram bot with a smooth AI experience.

## ⚡Feature

[✓] Support only native OpenAI. For Azure OpenAI use: https://github.com/V-know/ChatGPT-Telegram-Bot

[✓] Real-time (streaming) response to AI, with faster and smoother experience.

[✓] 15 preset bot identities that can be quickly switched.

[✓] Support for custom bot identities to meet personalized needs.

[✓] Support to clear the contents of the chat with a single click, and restart the conversation at any time.

[✓]Native Telegram bot button support, making it easy and intuitive to implement required functions.

[✓] User level division, with different levels enjoying different single session token numbers, context numbers, and session frequencies.

[✓] Support English and Chinese on UI

[✓] More...

## Release 1.1.0 from 17.11.2023 notes

[✓] Russian language supported.

[✓] The database creation script has been fixed, a “lang” column has been added to record the bot language selected by the user. The default language is English.

[✓] Fixed incorrectly changing the bot's role to "cancel" when user clicking the cancel button in the Сustom roles menu.

[✓] Information text templates for the selected language have been moved to templates.py.

[✓] Start message text templates have been moved to templates.py.

[✓] Updated configuration file, removed support for Azure OpenAI.

[✓] Added date and time logging for pooling event.


## 🤖Quick Experience

Telegram Bot: [VassermannBot](https://t.me/VassermannBot)

## 🛠️Deployment

### Install Dependencies

```shell
pip install -r requirements.txt
```

### Configure Database

#### Install Database

You can quickly create a local MySQL database using:

```shell
docker-compose up -d -f db/docker-compose.yaml
```

#### Initialize Database

```shell
mysql -uusername -p -e "source db/database.sql"
```

### Add Configuration

All the required configurations are in `config.yaml`, please refer to `config.yaml.example` for file format and content.

| Parameter           | Optional | Description                                                                                                                                                                                                                                                 |
|---------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BOT`.`TOKEN`       | No       | Create a bot from [@botFather](https://t.me/BotFather) and get the Token.                                                                                                                                                                                   |
| `DEVELOPER_CHAT_ID` | No       | Telegram account ID that receives messages when the bot encounters an error. You can use [@get_id_bot](https://t.me/get_id_bot) to get your ID.                                                                                                             |
| `MYSQL`             | No       | Parameters related to MySQL connection.                                                                                                                                                                                                                     |
| `TIME_SPAN`         | No       | The time window size used to calculate the ratelimit, in minutes.                                                                                                                                                                                           |
| `RATE_LIMIT`        | No       | `key` is the user level, and `value` is the maximum number of chats that can be made within the TIME_SPAN time period.                                                                                                                                      |
| `CONTEXT_COUNT`     | No       | `key` is the user level, and `value` is the number of contexts included in each chat.                                                                                                                                                                       |
| `MAX_TOKEN`         | No       | `key` is the user level, and `value` is the maximum number of tokens returned by the AI per chat.                                                                                                                                                                         |


## 🚀Start

```shell
python main.py | tee >> debug.log
```
