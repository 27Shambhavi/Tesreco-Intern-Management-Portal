import logging


logging.basicConfig(

    filename="tesreco.log",

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)

logger = logging.getLogger(__name__)


def login_event(username):

    logger.info(f"Login Event : {username} logged in")


def report_generated(report):

    logger.info(f"{report} Generated Successfully")


def error_log(error):

    logger.error(error)


if __name__ == "__main__":

    login_event("Vaibhav")

    report_generated("Attendance Report")

    error_log("Invalid Email")