import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
from utils import *

def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    print 'content type: %s' % content_type

    if content_type == 'photo':
        bot.download_file(msg['photo'][-1]['file_id'], './file.png')

        text = extractText('./file.png')
        text = processText(text)
        characters = extractCharactersNew(text)
        output = recogniseText(characters)
        integrable_function = convert_ocr_to_string(output)
        integral = integrate_from_string(integrable_function)
        print 'Output string: %s' % output
        print 'Integrable function: %s' % integrable_function
        print 'Integral: %s' % integral
        bot.sendMessage(chat_id, str(integral))

    elif content_type == 'text':
        command = msg['text']
        print 'Got command: %s' % command

        if command == '/roll':
            bot.sendMessage(chat_id, random.randint(1,6))
        elif command == '/time':
            bot.sendMessage(chat_id, str(datetime.datetime.now()))

TOKEN = '599987596:AAHM0aPTvq1BzzjmLv0licH7n5NWvpmRE3I'
bot = telepot.Bot(TOKEN)

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
