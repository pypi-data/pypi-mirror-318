class SColors:
    """
    Static version of Colors.
    """
    # Regular colors
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    GRAY = "\033[0;37m"

    # Bold colors
    BBLACK = "\033[1;30m"
    BRED = "\033[1;31m"
    BGREEN = "\033[1;32m"
    BYELLOW = "\033[1;33m"
    BBLUE = "\033[1;34m"
    BPURPLE = "\033[1;35m"
    BCYAN = "\033[1;36m"
    BGRAY = "\033[1;37m"

    # High Intensity Colors
    HBLACK = "\033[0;90m"
    HRED = "\033[0;91m"
    HGREEN = "\033[0;92m"
    HYELLOW = "\033[0;93m"
    HBLUE = "\033[0;94m"
    HPURPLE = "\033[0;95m"
    HCYAN = "\033[0;96m"
    HGRAY = "\033[0;97m"

    # Hight Intensity and Bold Colors
    HBBLACK = "\033[1;90m"
    HBRED = "\033[1;91m"
    HBGREEN = "\033[1;92m"
    HBYELLOW = "\033[1;93m"
    HBBLUE = "\033[1;94m"
    HBPURPLE = "\033[1;95m"
    HBCYAN = "\033[1;96m"
    HBGRAY = "\033[1;97m"

    # Underline Colors
    U_BLACK = "\033[4;30m"
    U_RED = "\033[4;31m"
    U_GREEN = "\033[4;32m"
    U_YELLOW = "\033[4;33m"
    U_BLUE = "\033[4;34m"
    U_PURPLE = "\033[4;35m"
    U_CYAN = "\033[4;36m"
    U_GRAY = "\033[4;37m"

    # Bold Underline Colors
    U_BBLACK = "\033[1;4;30m"
    U_BRED = "\033[1;4;31m"
    U_BGREEN = "\033[1;4;32m"
    U_BYELLOW = "\033[1;4;33m"
    U_BBLUE = "\033[1;4;34m"
    U_BPURPLE = "\033[1;4;35m"
    U_BCYAN = "\033[1;4;36m"
    U_BGRAY = "\033[1;4;37m"

    # High Intensity Underline Colors
    U_HBLACK = "\033[4;90m"
    U_HRED = "\033[4;91m"
    U_HGREEN = "\033[4;92m"
    U_HYELLOW = "\033[4;93m"
    U_HBLUE = "\033[4;94m"
    U_HPURPLE = "\033[4;95m"
    U_HCYAN = "\033[4;96m"
    U_HGRAY = "\033[4;97m"

    # High Intensity and Bold Underline Colors
    U_HBBLACK = "\033[1;4;90m"
    U_HBRED = "\033[1;4;91m"
    U_HBGREEN = "\033[1;4;92m"
    U_HBYELLOW = "\033[1;4;93m"
    U_HBBLUE = "\033[1;4;94m"
    U_HBPURPLE = "\033[1;4;95m"
    U_HBCYAN = "\033[1;4;96m"
    U_HBGRAY = "\033[1;4;97m"

    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_PURPLE = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_GRAY = "\033[47m"

    # High intensity backgrounds
    BG_HBLACK = "\033[0;100m"
    BG_HRED = "\033[0;101m"
    BG_HGREEN = "\033[0;102m"
    BG_HYELLOW = "\033[0;103m"
    BG_HBLUE = "\033[0;104m"
    BG_HPURPLE = "\033[0;105m"
    BG_HCYAN = "\033[0;106m"
    BG_HGRAY = "\033[0;107m"

    # Text formatting
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"  # Reset all formatting


class Colors:
    """
    A class for automatic color codes and text formatting for terminal output.

    Provides attributes for:
    - Regular colors and bold colors (bright versions of the regular colors)
    - Text formatting styles

    Attributes:
    - Regular colors: BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, GRAY
    - Bold (bright) colors: BBLACK, BRED, BGREEN, BYELLOW, BBLUE, BPURPLE, BCYAN, BGRAY
    - Text formatting options: BOLD, FAINT, ITALIC, UNDERLINE, BLINK, NEGATIVE, CROSSED
    - END: Resets all formatting and colors.

    Behavior:
    - If the output is not to a terminal (i.e., `sys.stdout.isatty()` is False), color codes are disabled to avoid unwanted characters in non-terminal environments.

    - If you want to avoid automatic disabling of colors when output is not to a terminal, use the `SColors` class instead.
    """

    # Regular colors
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    GRAY = "\033[0;37m"

    # Bold colors
    BBLACK = "\033[1;30m"
    BRED = "\033[1;31m"
    BGREEN = "\033[1;32m"
    BYELLOW = "\033[1;33m"
    BBLUE = "\033[1;34m"
    BPURPLE = "\033[1;35m"
    BCYAN = "\033[1;36m"
    BGRAY = "\033[1;37m"

    # High Intensity Colors
    HBLACK = "\033[0;90m"
    HRED = "\033[0;91m"
    HGREEN = "\033[0;92m"
    HYELLOW = "\033[0;93m"
    HBLUE = "\033[0;94m"
    HPURPLE = "\033[0;95m"
    HCYAN = "\033[0;96m"
    HGRAY = "\033[0;97m"

    # Hight Intensity and Bold Colors
    HBBLACK = "\033[1;90m"
    HBRED = "\033[1;91m"
    HBGREEN = "\033[1;92m"
    HBYELLOW = "\033[1;93m"
    HBBLUE = "\033[1;94m"
    HBPURPLE = "\033[1;95m"
    HBCYAN = "\033[1;96m"
    HBGRAY = "\033[1;97m"

    # Underline Colors
    U_BLACK = "\033[4;30m"
    U_RED = "\033[4;31m"
    U_GREEN = "\033[4;32m"
    U_YELLOW = "\033[4;33m"
    U_BLUE = "\033[4;34m"
    U_PURPLE = "\033[4;35m"
    U_CYAN = "\033[4;36m"
    U_GRAY = "\033[4;37m"

    # Bold Underline Colors
    U_BBLACK = "\033[1;4;30m"
    U_BRED = "\033[1;4;31m"
    U_BGREEN = "\033[1;4;32m"
    U_BYELLOW = "\033[1;4;33m"
    U_BBLUE = "\033[1;4;34m"
    U_BPURPLE = "\033[1;4;35m"
    U_BCYAN = "\033[1;4;36m"
    U_BGRAY = "\033[1;4;37m"

    # High Intensity Underline Colors
    U_HBLACK = "\033[4;90m"
    U_HRED = "\033[4;91m"
    U_HGREEN = "\033[4;92m"
    U_HYELLOW = "\033[4;93m"
    U_HBLUE = "\033[4;94m"
    U_HPURPLE = "\033[4;95m"
    U_HCYAN = "\033[4;96m"
    U_HGRAY = "\033[4;97m"

    # High Intensity and Bold Underline Colors
    U_HBBLACK = "\033[1;4;90m"
    U_HBRED = "\033[1;4;91m"
    U_HBGREEN = "\033[1;4;92m"
    U_HBYELLOW = "\033[1;4;93m"
    U_HBBLUE = "\033[1;4;94m"
    U_HBPURPLE = "\033[1;4;95m"
    U_HBCYAN = "\033[1;4;96m"
    U_HBGRAY = "\033[1;4;97m"

    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_PURPLE = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_GRAY = "\033[47m"

    # High intensity backgrounds
    BG_HBLACK = "\033[0;100m"
    BG_HRED = "\033[0;101m"
    BG_HGREEN = "\033[0;102m"
    BG_HYELLOW = "\033[0;103m"
    BG_HBLUE = "\033[0;104m"
    BG_HPURPLE = "\033[0;105m"
    BG_HCYAN = "\033[0;106m"
    BG_HGRAY = "\033[0;107m"

    # Text formatting
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"  # Reset all formatting

    # Convert color codes in "" if program output is not a terminal
    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
