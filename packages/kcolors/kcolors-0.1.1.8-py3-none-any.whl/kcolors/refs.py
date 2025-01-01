"""
Este modulo contiene referencias directas a las clases Colors y SColors.
    - Los colores dinámicos serían BLACK, BRED, END, etc. Los estáticos BLACK_, BRED_, END_, etc.
    - Puedes obtener las referencias inversas importando irefs.
"""
from .src.colors import Colors, SColors

if "kcolors.irefs" in __import__("sys").modules:
    raise ImportError("kcolors: Not allowed to import both 'kcolors.refs' and 'kcolors.irefs' at the same time.")


# Static Colors
# regular colors
BLACK_ = SColors.BLACK
RED_ = SColors.RED
GREEN_ = SColors.GREEN
YELLOW_ = SColors.YELLOW
BLUE_ = SColors.BLUE
PURPLE_ = SColors.PURPLE
CYAN_ = SColors.CYAN
GRAY_ = SColors.GRAY

# bold colors
BBLACK_ = SColors.BBLACK
BRED_ = SColors.BRED
BGREEN_ = SColors.BGREEN
BYELLOW_ = SColors.BYELLOW
BBLUE_ = SColors.BBLUE
BPURPLE_ = SColors.BPURPLE
BCYAN_ = SColors.BCYAN
BGRAY_ = SColors.BGRAY

# high intensity colors
HBLACK_ = SColors.HBLACK
HRED_ = SColors.HRED
HGREEN_ = SColors.HGREEN
HYELLOW_ = SColors.HYELLOW
HBLUE_ = SColors.HBLUE
HPURPLE_ = SColors.HPURPLE
HCYAN_ = SColors.HCYAN
HGRAY_ = SColors.HGRAY

# high intensity and bold colors
HBBLACK_ = SColors.HBBLACK
HBRED_ = SColors.HBRED
HBGREEN_ = SColors.HBGREEN
HBYELLOW_ = SColors.HBYELLOW
HBBLUE_ = SColors.HBBLUE
HBPURPLE_ = SColors.HBPURPLE
HBCYAN_ = SColors.HBCYAN
HBGRAY_ = SColors.HBGRAY

# background colors
BG_BLACK_ = SColors.BG_BLACK
BG_RED_ = SColors.BG_RED
BG_GREEN_ = SColors.BG_GREEN
BG_YELLOW_ = SColors.BG_YELLOW
BG_BLUE_ = SColors.BG_BLUE
BG_PURPLE_ = SColors.BG_PURPLE
BG_CYAN_ = SColors.BG_CYAN
BG_GRAY_ = SColors.BG_GRAY

# high intensity background colors
BG_HBLACK_ = SColors.BG_HBLACK
BG_HRED_ = SColors.BG_HRED
BG_HGREEN_ = SColors.BG_HGREEN
BG_HYELLOW_ = SColors.BG_HYELLOW
BG_HBLUE_ = SColors.BG_HBLUE
BG_HPURPLE_ = SColors.BG_HPURPLE
BG_HCYAN_ = SColors.BG_HCYAN
BG_HGRAY_ = SColors.BG_HGRAY

# underline colors
U_BLACK_ = SColors.U_BLACK
U_RED_ = SColors.U_RED
U_GREEN_ = SColors.U_GREEN
U_YELLOW_ = SColors.U_YELLOW
U_BLUE_ = SColors.U_BLUE
U_PURPLE_ = SColors.U_PURPLE
U_CYAN_ = SColors.U_CYAN
U_GRAY_ = SColors.U_GRAY

# bold underline colors
U_BBLACK_ = SColors.U_BBLACK
U_BRED_ = SColors.U_BRED
U_BGREEN_ = SColors.U_BGREEN
U_BYELLOW_ = SColors.U_BYELLOW
U_BBLUE_ = SColors.U_BBLUE
U_BPURPLE_ = SColors.U_BPURPLE
U_BCYAN_ = SColors.U_BCYAN
U_BGRAY_ = SColors.U_BGRAY

# high intensity underline colors
U_HBLACK_ = SColors.U_HBLACK
U_HRED_ = SColors.U_HRED
U_HGREEN_ = SColors.U_HGREEN
U_HYELLOW_ = SColors.U_HYELLOW
U_HBLUE_ = SColors.U_HBLUE
U_HPURPLE_ = SColors.U_HPURPLE
U_HCYAN_ = SColors.U_HCYAN
U_HGRAY_ = SColors.U_HGRAY

# high intensity and bold underline colors
BG_HBLACK_ = SColors.BG_HBLACK
BG_HRED_ = SColors.BG_HRED
BG_HGREEN_ = SColors.BG_HGREEN
BG_HYELLOW_ = SColors.BG_HYELLOW
BG_HBLUE_ = SColors.BG_HBLUE
BG_HPURPLE_ = SColors.BG_HPURPLE
BG_HCYAN_ = SColors.BG_HCYAN
BG_HGRAY_ = SColors.BG_HGRAY

# text formatting
BOLD_ = SColors.BOLD
FAINT_ = SColors.FAINT
ITALIC_ = SColors.ITALIC
UNDERLINE_ = SColors.UNDERLINE
BLINK_ = SColors.BLINK
NEGATIVE_ = SColors.NEGATIVE
CROSSED_ = SColors.CROSSED
END_ = SColors.END

# Dynamic Colors
# regular colors
BLACK = Colors.BLACK
RED = Colors.RED
GREEN = Colors.GREEN
YELLOW = Colors.YELLOW
BLUE = Colors.BLUE
PURPLE = Colors.PURPLE
CYAN = Colors.CYAN
GRAY = Colors.GRAY

# bold colors
BBLACK = Colors.BBLACK
BRED = Colors.BRED
BGREEN = Colors.BGREEN
BYELLOW = Colors.BYELLOW
BBLUE = Colors.BBLUE
BPURPLE = Colors.BPURPLE
BCYAN = Colors.BCYAN
BGRAY = Colors.BGRAY

# high intensity colors
HBLACK = Colors.HBLACK
HRED = Colors.HRED
HGREEN = Colors.HGREEN
HYELLOW = Colors.HYELLOW
HBLUE = Colors.HBLUE
HPURPLE = Colors.HPURPLE
HCYAN = Colors.HCYAN
HGRAY = Colors.HGRAY

# high intensity and bold colors
HBBLACK = Colors.HBBLACK
HBRED = Colors.HBRED
HBGREEN = Colors.HBGREEN
HBYELLOW = Colors.HBYELLOW
HBBLUE = Colors.HBBLUE
HBPURPLE = Colors.HBPURPLE
HBCYAN = Colors.HBCYAN
HBGRAY = Colors.HBGRAY

# background colors
BG_BLACK = Colors.BG_BLACK
BG_RED = Colors.BG_RED
BG_GREEN = Colors.BG_GREEN
BG_YELLOW = Colors.BG_YELLOW
BG_BLUE = Colors.BG_BLUE
BG_PURPLE = Colors.BG_PURPLE
BG_CYAN = Colors.BG_CYAN
BG_GRAY = Colors.BG_GRAY

# high intensity background colors
BG_HBLACK = Colors.BG_HBLACK
BG_HRED = Colors.BG_HRED
BG_HGREEN = Colors.BG_HGREEN
BG_HYELLOW = Colors.BG_HYELLOW
BG_HBLUE = Colors.BG_HBLUE
BG_HPURPLE = Colors.BG_HPURPLE
BG_HCYAN = Colors.BG_HCYAN
BG_HGRAY = Colors.BG_HGRAY

# underline colors
U_BLACK = Colors.U_BLACK
U_RED = Colors.U_RED
U_GREEN = Colors.U_GREEN
U_YELLOW = Colors.U_YELLOW
U_BLUE = Colors.U_BLUE
U_PURPLE = Colors.U_PURPLE
U_CYAN = Colors.U_CYAN
U_GRAY = Colors.U_GRAY

# bold underline colors
U_BBLACK = Colors.U_BBLACK
U_BRED = Colors.U_BRED
U_BGREEN = Colors.U_BGREEN
U_BYELLOW = Colors.U_BYELLOW
U_BBLUE = Colors.U_BBLUE
U_BPURPLE = Colors.U_BPURPLE
U_BCYAN = Colors.U_BCYAN
U_BGRAY = Colors.U_BGRAY

# high intensity underline colors
U_HBLACK = Colors.U_HBLACK
U_HRED = Colors.U_HRED
U_HGREEN = Colors.U_HGREEN
U_HYELLOW = Colors.U_HYELLOW
U_HBLUE = Colors.U_HBLUE
U_HPURPLE = Colors.U_HPURPLE
U_HCYAN = Colors.U_HCYAN
U_HGRAY = Colors.U_HGRAY

# high intensity and bold underline colors
U_HBBLACK = Colors.U_HBBLACK
U_HBRED = Colors.U_HBRED
U_HBGREEN = Colors.U_HBGREEN
U_HBYELLOW = Colors.U_HBYELLOW
U_HBBLUE = Colors.U_HBBLUE
U_HBPURPLE = Colors.U_HBPURPLE
U_HBCYAN = Colors.U_HBCYAN
U_HBGRAY = Colors.U_HBGRAY

# text formatting
BOLD = Colors.BOLD
FAINT = Colors.FAINT
ITALIC = Colors.ITALIC
UNDERLINE = Colors.UNDERLINE
BLINK = Colors.BLINK
NEGATIVE = Colors.NEGATIVE
CROSSED = Colors.CROSSED
END = Colors.END
