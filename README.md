# Telegram Bot

This is a simple Telegram bot that replies to messages with random words from a list.

## Prerequisites

- Python 3.6 or higher
- Telethon library
- A `words.txt` file containing comma-separated words

## Description

The bot listens for new messages and if the message contains the word 'ok', it replies with a sentence composed of random words from the `words.txt` file. The number of words in the sentence is also random, ranging from 5 to 25.

## Usage

1. Replace `api_id` and `api_hash` with your own values from my.telegram.org.
2. Run the script.
3. Send a message containing 'ok' to the bot on Telegram.

## Functions

- `random_word()`: Returns a random word from the `words.txt` file.
- `sensen()`: Returns a sentence composed of a random number of words (between 5 and 25).

## Note

The bot will keep running until it is manually stopped or encounters an error. If an error occurs, it will print 'error' to the console.
