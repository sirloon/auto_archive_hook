import datetime
from dateutil import parser as dtparser
from biothings import config
logger = config.logger

def auto_archive(build_config_name, days=5):
    """
    Archive any builds which build date is older than today's date
    by "days" day.
    """
    logger.info("Auto-archive builds older than %s days" % days)
    builds = lsmerge(build_config_name)
    today = datetime.datetime.now()
    at_least_one = False
    for bid in builds:
        build = bm.build_info(bid)
        bdate = dtparser.parse(build["_meta"]["build_date"])
        deltadate = today - bdate
        if deltadate.days > days:
            logger.info("Archiving build %s (older than %s)" % (bid,deltadate))
            archive(bid)
            at_least_one = True
    if not at_least_one:
        logger.info("Nothing to archive")

schedule("0 12 * * *",auto_archive,"covid19")     
