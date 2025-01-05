import datetime
import nest_asyncio

from telegram import Bot
from telegram.error import TelegramError

import asyncio
import telegram
import textwrap
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mail_to(title: str, text: str, mail_addr='hj3415@hanmail.net') -> bool:
    # 메일을 보내는 함수
    login_id_pass = ('hj3415@gmail.com', 'orlhfaqihcdytvsw')
    # 로그인 인자의 두번째 앱비밀번호는 구글계정 관리에서 설정함.
    smtp = ('smtp.gmail.com', 587)

    msg = MIMEMultipart()
    msg['From'] = login_id_pass[0]
    msg['Subject'] = title
    msg['To'] = mail_addr
    msg.attach(MIMEText(datetime.datetime.today().strftime('%I:%M%p') + '\n' + textwrap.dedent(text)))

    smtp = smtplib.SMTP(smtp[0], smtp[1])
    smtp.ehlo()
    try:
        smtp.starttls()
        smtp.login(login_id_pass[0], login_id_pass[1])
        smtp.sendmail(login_id_pass[0], mail_addr, msg.as_string())
        print(f'Sent mail to {mail_addr} successfully.')
        return True
    except:
        print(f'Unknown error occurred during sending mail to {mail_addr}.')
        return False
    finally:
        smtp.close()


CHAT_ID = '924939307'
BOT_DICT = {
    # botname : token
    'manager': '1445235613:AAHR5fFT0-9lEoyMmTxXx8VfsafoRnOiZzo',
    'dart': '1442133926:AAEiknxYWfHsxQgmyVRBOlWTT_vpO3Zc96c',
    'eval': '1409424097:AAFln-N_Wjfy32uDap4TKB1BjeUr1DvQJBQ',
    'cybos': '1757566630:AAFntsPJZQ8zWH0DaRe92waFELTzsFzyqmo',
    'servers': '5601845727:AAEKD-HK4R2XyvwmOeqU-3E0_iRw9AtNxxo',
}

nest_asyncio.apply()


async def send_messge(bot: Bot, chat_id: str, text: str):
    try:
        await bot.send_message(chat_id=chat_id, text=text)
        print(f"Message sent to {bot}: {text}")
    except TelegramError as e:
        print(f"Failed to send message: {e}")


def telegram_to(botname: str, text: str):
    """

    :param botname: manager, dart, eval, cybos, servers
    :param text: 전송할 문자열
    """
    # reference from https://pypi.org/project/python-telegram-bot/#learning-by-example
    if botname in BOT_DICT.keys():
        token = BOT_DICT[botname]
        bot = telegram.Bot(token=token)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(send_messge(bot, CHAT_ID, textwrap.dedent(text)))
    else:
        raise Exception(f'Invalid bot name : {botname} / {BOT_DICT.keys()}')