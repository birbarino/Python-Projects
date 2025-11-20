import argparse
import logging

# print current time and message
# using INFO verbosity setting
logging.basicConfig(level=logging.INFO, format='%(asctime)-15s %(message)s')
logger = logging.getLogger()

def do(args):
    logger.info("This is a message.")
    logger.warning("This is a warning")
    logger.error("This is an error")

    logger.info(f"{args.argument, args.nothing}")

if __name__ == '__main__':  # if ran as a script (not imported)
    parser = argparse.ArgumentParser(
        prog="name_this_program",
        description="This is a sample using argparse",
        epilog="Yep, that's it"
    )

    # type= arg can do casting
    parser.add_argument(
        "-a", "--argument", type=str, help="This is just a test", required=False,
        default="your mom"
    )

    parser.add_argument(
        "-n", "--nothing", type=str, help="This is just a test", required=True
    )

    args = parser.parse_args()   # takes input from user and parses it

    do(args)