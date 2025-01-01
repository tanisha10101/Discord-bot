# Discord Bot 

---

## Introduction

This project is a simple yet functional Discord bot built using the `discord.py` library. The bot connects to a Discord server, listens to messages in real-time, and responds to specific commands. It serves as a basic example of how to set up a bot, handle events, and interact with users.

---

## Features

- **Greeting Command**: Responds with a friendly "Hi" message when a user types `$hello`.
- **Ping-Pong Interaction**: Responds with "pong" when a user types `ping`.
- **Event Handling**: The bot utilizes event-driven programming to respond to server events such as logging in and receiving messages.

---

## Prerequisites
Python 3.8 or later
The discord.py library installed (pip install discord.py)

---

## Setup Instructions
1. Clone the repository or copy the code.
2. Install the required library using pip:
```bash
pip install discord.py
```
3. Replace YOUR_BOT_TOKEN in the code with your bot's token obtained from the Discord Developer Portal.
4. Run the script:
```bash
python bot.py
```

---

## Usage

- Add the bot to your server using its OAuth2 URL.
- Type `$hello` in any channel where the bot is active, and it will respond with "Hi."
- Type `ping` in the channel, and the bot will reply with "pong."

---

## Notes

- Ensure the bot has the necessary permissions to read and send messages in the server.
- Avoid sharing your bot token publicly to prevent unauthorized access.

---

## Future Enhancements

- Add more commands and functionalities like moderation tools or fun interactions.
- Implement error handling for better reliability.
- Expand the bot's capabilities using Discord's advanced features like slash commands and embeds.
