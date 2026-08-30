import logging

logging.basicConfig(
    filename='app.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

    

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
