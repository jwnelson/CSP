# Contains text assets for networking, such as welcome messages and console art
import datetime
YEAR_OFFSET = 33
offset_timedelta = datetime.timedelta(days = YEAR_OFFSET * 365)

logo = """
    SSSSSSSSSSSSSSS RRRRRRRRRRRRRRRRR   LLLLLLLLLLL             
 SS:::::::::::::::SR::::::::::::::::R  L:::::::::L             
S:::::SSSSSS::::::SR::::::RRRRRR:::::R L:::::::::L             
S:::::S     SSSSSSSRR:::::R     R:::::RLL:::::::LL             
S:::::S              R::::R     R:::::R  L:::::L               
S:::::S              R::::R     R:::::R  L:::::L               
 S::::SSSS           R::::RRRRRR:::::R   L:::::L               
  SS::::::SSSSS      R:::::::::::::RR    L:::::L               
    SSS::::::::SS    R::::RRRRRR:::::R   L:::::L               
       SSSSSS::::S   R::::R     R:::::R  L:::::L               
            S:::::S  R::::R     R:::::R  L:::::L               
            S:::::S  R::::R     R:::::R  L:::::L         LLLLLL
SSSSSSS     S:::::SRR:::::R     R:::::RLL:::::::LLLLLLLLL:::::L
S::::::SSSSSS:::::SR::::::R     R:::::RL::::::::::::::::::::::L
S:::::::::::::::SS R::::::R     R:::::RL::::::::::::::::::::::L
 SSSSSSSSSSSSSSS   RRRRRRRR     RRRRRRRLLLLLLLLLLLLLLLLLLLLLLLL

"""

# Welcome message that gets printed when a user first connects
# TODO - Figure out how to format the timestamp so it's YYYY-MM-DD THH:MM:SS
linesep = "\n===============================================================\n"
welcome_message = linesep + logo + linesep + "STELLAR RESEARCH LABORATORIES, DEEP SPACE C2 MAINFRAME LOGIN\n" \
                 + "{}".format((datetime.datetime.now() - offset_timedelta).isoformat() ) \
                 + linesep


def test():
    print(welcome_message)
    
if __name__ == "__main__":
    test()
