"""
Este módulo contiene referencias directas a las clases Colors y SColors.
    - Los colores dinámicos serían BLACK_, BRED_, END_, etc. Los estáticos BLACK, BRED, END, etc.
    - Puedes obtener las referencias inversas importando refs.
"""
from .src.colors import Colors, SColors

if "kcolors.refs" in __import__("sys").modules:
    raise ImportError("kcolors: Not allowed to import both 'kcolors.refs' and 'kcolors.irefs' at the same time.")

# Static Colors
# regular colors
BLACK = SColors.BLACK
RED = SColors.RED
GREEN = SColors.GREEN
YELLOW = SColors.YELLOW
BLUE = SColors.BLUE
PURPLE = SColors.PURPLE
CYAN = SColors.CYAN
GRAY = SColors.GRAY

# bold colors
BBLACK = SColors.BBLACK
BRED = SColors.BRED
BGREEN = SColors.BGREEN
BYELLOW = SColors.BYELLOW
BBLUE = SColors.BBLUE
BPURPLE = SColors.BPURPLE
BCYAN = SColors.BCYAN
BGRAY = SColors.BGRAY

# high intensity colors
HBLACK = SColors.HBLACK
HRED = SColors.HRED
HGREEN = SColors.HGREEN
HYELLOW = SColors.HYELLOW
HBLUE = SColors.HBLUE
HPURPLE = SColors.HPURPLE
HCYAN = SColors.HCYAN
HGRAY = SColors.HGRAY

# high intensity and bold colors
HBBLACK = SColors.HBBLACK
HBRED = SColors.HBRED
HBGREEN = SColors.HBGREEN
HBYELLOW = SColors.HBYELLOW
HBBLUE = SColors.HBBLUE
HBPURPLE = SColors.HBPURPLE
HBCYAN = SColors.HBCYAN
HBGRAY = SColors.HBGRAY

# background colors
BG_BLACK = SColors.BG_BLACK
BG_RED = SColors.BG_RED
BG_GREEN = SColors.BG_GREEN
BG_YELLOW = SColors.BG_YELLOW
BG_BLUE = SColors.BG_BLUE
BG_PURPLE = SColors.BG_PURPLE
BG_CYAN = SColors.BG_CYAN
BG_GRAY = SColors.BG_GRAY

# high intensity background colors
BG_HBLACK = SColors.BG_HBLACK
BG_HRED = SColors.BG_HRED
BG_HGREEN = SColors.BG_HGREEN
BG_HYELLOW = SColors.BG_HYELLOW
BG_HBLUE = SColors.BG_HBLUE
BG_HPURPLE = SColors.BG_HPURPLE
BG_HCYAN = SColors.BG_HCYAN
BG_HGRAY = SColors.BG_HGRAY

# underline colors
U_BLACK = SColors.U_BLACK
U_RED = SColors.U_RED
U_GREEN = SColors.U_GREEN
U_YELLOW = SColors.U_YELLOW
U_BLUE = SColors.U_BLUE
U_PURPLE = SColors.U_PURPLE
U_CYAN = SColors.U_CYAN
U_GRAY = SColors.U_GRAY

# bold underline colors
U_BBLACK = SColors.U_BBLACK
U_BRED = SColors.U_BRED
U_BGREEN = SColors.U_BGREEN
U_BYELLOW = SColors.U_BYELLOW
U_BBLUE = SColors.U_BBLUE
U_BPURPLE = SColors.U_BPURPLE
U_BCYAN = SColors.U_BCYAN
U_BGRAY = SColors.U_BGRAY

# high intensity underline colors
U_HBLACK = SColors.U_HBLACK
U_HRED = SColors.U_HRED
U_HGREEN = SColors.U_HGREEN
U_HYELLOW = SColors.U_HYELLOW
U_HBLUE = SColors.U_HBLUE
U_HPURPLE = SColors.U_HPURPLE
U_HCYAN = SColors.U_HCYAN
U_HGRAY = SColors.U_HGRAY

# high intensity and bold underline colors
U_HBBLACK = SColors.U_HBBLACK
U_HBRED = SColors.U_HBRED
U_HBGREEN = SColors.U_HBGREEN
U_HBYELLOW = SColors.U_HBYELLOW
U_HBBLUE = SColors.U_HBBLUE
U_HBPURPLE = SColors.U_HBPURPLE
U_HBCYAN = SColors.U_HBCYAN
U_HBGRAY = SColors.U_HBGRAY

# text formatting
BOLD = SColors.BOLD
FAINT = SColors.FAINT
ITALIC = SColors.ITALIC
UNDERLINE = SColors.UNDERLINE
BLINK = SColors.BLINK
NEGATIVE = SColors.NEGATIVE
CROSSED = SColors.CROSSED
END = SColors.END

# Dynamic Colors
# regular colors
BLACK_ = Colors.BLACK
RED_ = Colors.RED
GREEN_ = Colors.GREEN
YELLOW_ = Colors.YELLOW
BLUE_ = Colors.BLUE
PURPLE_ = Colors.PURPLE
CYAN_ = Colors.CYAN
GRAY_ = Colors.GRAY

# bold colors
BBLACK_ = Colors.BBLACK
BRED_ = Colors.BRED
BGREEN_ = Colors.BGREEN
BYELLOW_ = Colors.BYELLOW
BBLUE_ = Colors.BBLUE
BPURPLE_ = Colors.BPURPLE
BCYAN_ = Colors.BCYAN
BGRAY_ = Colors.BGRAY

# high intensity colors
HBLACK_ = Colors.HBLACK
HRED_ = Colors.HRED
HGREEN_ = Colors.HGREEN
HYELLOW_ = Colors.HYELLOW
HBLUE_ = Colors.HBLUE
HPURPLE_ = Colors.HPURPLE
HCYAN_ = Colors.HCYAN
HGRAY_ = Colors.HGRAY

# high intensity and bold colors
HBBLACK_ = Colors.HBBLACK
HBRED_ = Colors.HBRED
HBGREEN_ = Colors.HBGREEN
HBYELLOW_ = Colors.HBYELLOW
HBBLUE_ = Colors.HBBLUE
HBPURPLE_ = Colors.HBPURPLE
HBCYAN_ = Colors.HBCYAN
HBGRAY_ = Colors.HBGRAY

# background colors
BG_BLACK_ = Colors.BG_BLACK
BG_RED_ = Colors.BG_RED
BG_GREEN_ = Colors.BG_GREEN
BG_YELLOW_ = Colors.BG_YELLOW
BG_BLUE_ = Colors.BG_BLUE
BG_PURPLE_ = Colors.BG_PURPLE
BG_CYAN_ = Colors.BG_CYAN
BG_GRAY_ = Colors.BG_GRAY

# high intensity background colors
BG_HBLACK_ = Colors.BG_HBLACK
BG_HRED_ = Colors.BG_HRED
BG_HGREEN_ = Colors.BG_HGREEN
BG_HYELLOW_ = Colors.BG_HYELLOW
BG_HBLUE_ = Colors.BG_HBLUE
BG_HPURPLE_ = Colors.BG_HPURPLE
BG_HCYAN_ = Colors.BG_HCYAN
BG_HGRAY_ = Colors.BG_HGRAY

# underline colors
U_BLACK_ = Colors.U_BLACK
U_RED_ = Colors.U_RED
U_GREEN_ = Colors.U_GREEN
U_YELLOW_ = Colors.U_YELLOW
U_BLUE_ = Colors.U_BLUE
U_PURPLE_ = Colors.U_PURPLE
U_CYAN_ = Colors.U_CYAN
U_GRAY_ = Colors.U_GRAY

# bold underline colors
U_BBLACK_ = Colors.U_BBLACK
U_BRED_ = Colors.U_BRED
U_BGREEN_ = Colors.U_BGREEN
U_BYELLOW_ = Colors.U_BYELLOW
U_BBLUE_ = Colors.U_BBLUE
U_BPURPLE_ = Colors.U_BPURPLE
U_BCYAN_ = Colors.U_BCYAN
U_BGRAY_ = Colors.U_BGRAY

# high intensity underline colors
U_HBLACK_ = Colors.U_HBLACK
U_HRED_ = Colors.U_HRED
U_HGREEN_ = Colors.U_HGREEN
U_HYELLOW_ = Colors.U_HYELLOW
U_HBLUE_ = Colors.U_HBLUE
U_HPURPLE_ = Colors.U_HPURPLE
U_HCYAN_ = Colors.U_HCYAN
U_HGRAY_ = Colors.U_HGRAY

# high intensity and bold underline colors
BG_HBLACK_ = Colors.BG_HBLACK
BG_HRED_ = Colors.BG_HRED
BG_HGREEN_ = Colors.BG_HGREEN
BG_HYELLOW_ = Colors.BG_HYELLOW
BG_HBLUE_ = Colors.BG_HBLUE
BG_HPURPLE_ = Colors.BG_HPURPLE
BG_HCYAN_ = Colors.BG_HCYAN
BG_HGRAY_ = Colors.BG_HGRAY

# text formatting
BOLD_ = Colors.BOLD
FAINT_ = Colors.FAINT
ITALIC_ = Colors.ITALIC
UNDERLINE_ = Colors.UNDERLINE
BLINK_ = Colors.BLINK
NEGATIVE_ = Colors.NEGATIVE
CROSSED_ = Colors.CROSSED
END_ = Colors.END