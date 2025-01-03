Here's a README.md for the "Session Converter" package based on the provided code:

---

# Session Converter

The **Session Converter** package provides a straightforward way to convert sessions between Pyrogram and Telethon, two popular Telegram API wrappers. This package supports converting both session files and string sessions between the two libraries.

## Features

- Convert **Pyrogram session files** to Telethon sessions.
- Convert **Pyrogram string sessions** to Telethon sessions.
- Convert **Telethon string sessions** to Pyrogram sessions.
- Convert **Telethon session files** to Pyrogram sessions.
- Handles both **API ID** and **DC ID**.

## Installation

```bash
pip install telegram-session-converter
```

## Usage

### Converting from Pyrogram Session File to Telethon Session

```python
from session_converter import SessionManager

# Convert to Telethon session
session_manager = SessionManager.from_pyrogram_session_file("path/to/pyrogram_session_file.session")

session_manager.telethon_file("path/to/telethon_session_file.session")
```

### Converting from Pyrogram String Session to Telethon Session

```python
from session_converter import SessionManager

# Provide the Pyrogram session string
pyrogram_session_string = "<your_pyrogram_session_string>"

# Convert to Telethon session
session_manager = SessionManager.from_pyrogram_string_session(pyrogram_session_string)

session_manager.telethon_file("path/to/telethon_session_file.session")
```

### Converting from Telethon Session File to Pyrogram Session

```python
from session_converter import SessionManager

# Provide the path to the Telethon session file
telethon_session_file = "path/to/telethon_session_file.session"

# Convert to Pyrogram session
session_manager = SessionManager.from_telethon_file(telethon_session_file)

# Access the converted session details
print(session_manager.session)
```

### Converting from Telethon String Session to Pyrogram Session

```python
from session_converter import SessionManager

# Provide the Telethon session string
telethon_session_string = "<your_telethon_session_string>"

# Convert to Pyrogram session
session_manager = SessionManager.from_telethon_string_session(telethon_session_string)

# Access the converted session details
print(session_manager.session)
```

### Ready-to-use converter code

```python
import uuid
from telethon import TelegramClient
from telethon.sessions import StringSession
from session_converter import SessionManager
import asyncio
import os
from pyrogram import Client

API_ID = 0
API_HASH = ''


class SessionConverter:

    @staticmethod
    async def convert_to_pyrogram(session_file_path: str, save_path: str = "."):
        try:
            session = SessionManager.from_telethon_file(session_file_path)

            session.pyrogram_file(
                f"{save_path}/{str(uuid.uuid4())[:8]}_pyrogram.session",
                api_id=API_ID,
            )
        except Exception as e:
            raise e

    @staticmethod
    async def convert_to_telethon(session_file_path: str, save_path: str = "."):

        try:
            session = SessionManager.from_pyrogram_session_file(session_file_path)

            session.telethon_file(
                f"{save_path}/{str(uuid.uuid4())[:8]}_telethon.session"
            )

        except Exception as e:
            raise e



async def check_telethon_connection(session_file_path: str):

    client = TelegramClient(session_file_path, API_ID, API_HASH)
    await client.start()

    print(await client.get_me())

    await client.disconnect()


async def check_pyrogram_connection(session_file_path: str, workdir: str):
    client = Client(
        session_file_path.strip(".session"), API_ID, API_HASH, workdir=workdir
    )
    await client.start()

    print(await client.get_me())

    await client.stop()


async def main():
    try:
        await SessionConverter.convert_to_telethon(
            "./pyrogram_sessions/<pyrogram_file>.session", "./telethon_sessions"
        )
        print("Successfully converted from PYROGRAM to TELETHON")

        await SessionConverter.convert_to_pyrogram(
            "./telethon_sessions/<telethon file>.session", "./pyrogram_sessions"
        )
        print("Successfully converted from TELETHON to PYROGRAM")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(main())

```


## Classes

### `SessionManager`

The main class for managing session conversions. Provides methods to convert between Pyrogram and Telethon sessions.

#### Methods:
- `from_pyrogram_session_file(file: str)`: Converts a Pyrogram session file to a Telethon session.
- `from_pyrogram_string_session(session_string: str)`: Converts a Pyrogram session string to a Telethon session.
- `from_telethon_string_session(session_string: str, do_login: bool = False)`: Converts a Telethon session string to a Pyrogram session.
- `from_telethon_file(file: str, do_login: bool = False)`: Converts a Telethon session file to a Pyrogram session.
- `pyrogram_file(file: str, **kwargs)`: Exports the session to a Pyrogram session file.
- `telethon_file(file: str)`: Exports the session to a Telethon session file.
- `pyrogram_string_session(version: int = 3, api_id: int = 0)`: Exports the session as a Pyrogram string.
- `telethon_string_session()`: Exports the session as a Telethon string.

### `TDSession`

A data model class for representing Telegram session details, including `dc_id`, `api_id`, `auth_key`, and other properties.

## Requirements

- Python 3.6+
- Pyrogram
- Telethon
- Pydantic

## License

This package is licensed under the MIT License.

---

Let me know if you'd like any changes or additions to this README!