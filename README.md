# Realtime chat Bot


## Description
Real Time Chat project is built on Django and Django Channels.

This project is an extension very important for realtime-chat 
(https://github.com/saduqz/realtime-chat).

This is supposed to be setup *after* setup the realtime-chat project.

This just need to be running into some port, eg `localhost:8001` and put this information into
the file `database_info.py` in the realtime-chat project.

Note: realtime-chat project means this: https://github.com/saduqz/realtime-chat

## Technical setup (It take about 5 minutes)

#### Development environment

1. Remember, This is for development environment. For production or any deployment setup,
this use environment variables.

1. Clone the project and go to the directory using the terminal/console

1. Install requirements with `pip install -r requirements.txt`

1. You need to create a file allocated into `realtime_chat/database_info.py` 
(At the same level that `settings.py`)

1. This file should contains the Database info and realtime chat bot URL (Second project
url/port execution)

    - Second project URL: https://github.com/saduqz/realtime-chat-bot
    

    ENGINE = "django.db.backends.postgresql"
    NAME = "realtime_chat"
    HOST = "localhost"
    PORT = "5432"
    USER = "myuser"
    PASSWORD = "mypassword"
    REALTIME_CHAT_BOT_URL = "localhost:8001"
    