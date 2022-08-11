import logging
from loader import DEBUG

filename: str = "bot.log" if DEBUG else ""
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    filename=filename
                    )
