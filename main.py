from telethon import TelegramClient
import random , time

Reply_Word = "" # Reply word that bot will reply your msg by this word

# Random Word From Words in Words.txt For Bypass Telegram AntiSpammer 

def random_word():
    file = open('words.txt', 'r')
    file_contents = file.read()
    r = random.randint(1, 7200) #use the last words count instead of 7200
    word = file_contents.split(",")[r]
    return word

def sensen():
    r1 = random.randint(5,25) # How Many Words You Want To Be Sentens
    sentenses = ""
    while (r1 > 1):
        word = random_word()
        sentenses = sentenses + " " + word
        r1 = r1 - 1
    return sentens


# Remember to use your own values from my.telegram.org!
while(True):
    try :
        api_id =  # Your Api ID here From my.telegram.org!
        api_hash = '' # Your hash here From my.telegram.org!
        from telethon import TelegramClient, events

        client = TelegramClient('anon', api_id, api_hash)

        @client.on(events.NewMessage)
        async def my_event_handler(event):
            if 'ok' in event.raw_text:
                while(True):
                    random_time = random.randint(1, 3)
                    time.sleep(random_time)
                    sentens = sensen()
                    await event.reply(sentens)
        client.start()
        client.run_until_disconnected()
    except:
        print("error")