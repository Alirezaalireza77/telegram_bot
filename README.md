# Telegram File Downloader Bot

This is a Telegram bot built using the `aiogram` library that allows users to download files by sending a URL. The bot fetches the file from the given URL and sends it back to the user as a downloadable document.

## Features

- Responds to the `/start` command to initiate the bot and prompt the user for a file download link.
- Downloads files from URLs provided by the user.
- Sends the downloaded file to the user and deletes the local copy after it is sent.

## Requirements

- Python 3.8+
- Libraries: 
  - `aiogram` (for building the Telegram bot)
  - `requests` (for handling HTTP requests)

## Installation

1. Clone this repository or download the code.
   
2. Install the required Python libraries:

    ```bash
        pip install aiogram requests
    ```

3. Create a `.env` file to store your Telegram bot API token.

    ```env
        BOT_TOKEN=your_bot_token_here
    ```

4. Replace the placeholder token in the script with your bot token or load it from the `.env` file.

## Usage

1. Start the bot:

    ```bash
        python bot.py
    ```

2. Interact with the bot by sending the `/start` command in Telegram.

3. Send a valid URL of a file you wish to download. The bot will download and send it back to you as a Telegram document.

## Example

1. Send `/start` to the bot.
2. The bot will ask for a link: `Enter your link please...`.
3. Send a valid file URL, e.g., `https://example.com/file.pdf`.
4. The bot will respond with: `Your file is downloading...`.
5. The file will be sent to you once the download is complete.

## Notes

- Make sure the URL you send points to a direct download link for a file.
- The bot deletes the file after sending it to the user to free up space.

## Contributing

Feel free to fork this project and submit pull requests.

## License

This project is licensed under the MIT License.
