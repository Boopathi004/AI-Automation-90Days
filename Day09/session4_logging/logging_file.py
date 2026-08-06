import logging

logging.basicConfig(

    filename="app.log",

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)

logging.info("Application Started")

logging.warning("Low Memory")

logging.error("Database Connection Failed")

logging.critical("Critical Error Occurred")

print("Logs Written Successfully")