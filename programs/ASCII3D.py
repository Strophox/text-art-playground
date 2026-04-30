# 2026-04-30 13:14
""" Initialise """
glyphs = { # contains the main glyphs, codified as follows:
#####
#S     TTT
#S    /LL/\ 
#S   /LL/VH\ 
#S  /LL/V/\H\ 
#S /LL/VH\B\H\ 
#S/FF/V/\H\E\H\ 
#S\EE\/BB\H\/V/
#S     \EE\HV/
#S     /LL/V/
#S    /FF/V/
#S    \EE\/
#####
# S: Space modifier
# T: Top bar
# D: Down bar
# H: Horizontal stroke
#V:Vertical stroke
# B: Bottom shading
# L: Left shading
# E: Bottom edge
# F: Left edge
# whereas one should not forget to put spaces after backslashes, or else...
' ':"""





""",
'!':"""S       TTT
S      /LL/\ 
S     /LL/V/
S    /LL/V/
S   /FF/V/
S  T\EE\/
S /FF/\ 
S \EE\/""",
'"':"""S       TTT
S      /LL/\ 
S     /FF/V/T
S     \EE\/L/\ 
S       /FF/V/
S       \EE\/""",
'#':"""S    TTTTT
S   /FF/\/\ 
S  T\EB\HV/T
S /FF/\/VH\/\ 
S \EE\HV/\HV/
S /FF/VH\/VH\ 
S \EE\/\HV/\/ 
S   /FF/VH\D
S   \EE\/\/
S       DD""",
'$':"""S     TTT
S    /LL/\TT
S   /LL/VH\/\ 
S  /FF/V/\HV/
S T\EB\H\/VH\ 
S/FF/\E\HV/\H\ 
S\BB\H\/VH\E\/
S \EE\HV/\H\ 
S /FF/VH\/V/
S \EE\/\HV/
S    \EE\/""",
'%':"""S      TTT
S     /FF/\ 
S     \EE\/T
S   TTTT/LL/\ 
S  /LL/\/\/V/
S /FF/V/\/\/
S \EE\/TDDD
S   /FF/\ 
S   \EE\/""",
"'":"""S       TTT
S      /LL/\ 
S     /FF/V/
S     \EE\/""",
'(':"""S     TTTTT
S    /LL/\/\ 
S   /LL/V/\/
S  /LL/V/DD
S /FF/V/
S \EE\/
S /FF/\ 
S \EE\/""",
')':"""S      TTT
S     /FF/\ 
S     \EE\/
S     /LL/\ 
S    /LL/V/
S TT/LL/V/
S/FF/\/V/
S\EE\/\/
S    DD""",
'*':"""S      TTT
S     /FF/\ 
S    T\EE\/T
S   /FF/\/\/\ 
S   \EE\/\/\/
S     /FF/\D
S     \EE\/""",
'+':"""S   TTTTTTT
S  /FF/\LL/\ 
S  \BB\H\/V/
S   \EE\HV/
S   /LL/VH\ 
S  /FF/V/\H\ 
S  \EE\/EE\/
S""",
',':"""S
S
S
S
S
S   TTT
S  /LL/\ 
S /FF/V/
S \EE\/""",
'-':"""S
S   TTT
S  /FF/\ 
S  \BB\H\ 
S   \BB\H\ 
S    \BB\H\ 
S     \BB\H\ 
S      \EE\/
S""",
'.':"""S
S
S
S
S
S
S   TTT
S  /FF/\ 
S  \EE\/""",
'/':"""S
S
S        TTT
S   TTTT/LL/\ 
S  /LL/\/\/V/
S /FF/V/\/\/
S \EE\/DDDD
S""",
'0':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/V/BB\H\ 
S/FF/V/ \EE\H\ 
S\BB\H\ /LL/V/
S \BB\H\LL/V/
S  \BB\H\/V/
S   \BB\HV/
S    \EE\/""",
'1':"""S      TTT
S     /FF/\ 
S     \EE\H\ 
S     /LL/V/
S  TT/LL/V/
S /FF/\/V/
S \BB\HV/
S  \BB\H\ 
S   \EE\/""",
'2':"""S     TTT
S    /FF/\ 
S   T\EB\H\ 
S  /LL/\B\H\ 
S /LL/VH\B\H\ 
S/FF/V/\H\E\H\ 
S\BB\H\B\H\/V/
S \BB\H\B\HV/
S  \BB\H\E\/
S   \BB\H\ 
S    \EE\/""",
'3':"""S     TTT
S    /FF/\ 
S   T\EB\H\ 
S  /FF/\B\H\ 
S T\EB\H\B\H\ 
S/FF/\B\H\E\H\ 
S\BB\H\B\H\/V/
S \BB\H\E\HV/
S  \BB\H\/V/
S   \BB\HV/
S    \EE\/""",
'4':"""S     TTT
S    /LL/\ 
S   /LL/V/
S  /FF/V/
S  \BB\H\ TTT
S   \BB\H\LL/\ 
S    \BB\H\/V/
S     \EE\HV/
S     /LL/V/
S    /FF/V/
S    \EE\/""",
'5':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /FF/V/\H\ 
S T\EB\H\B\H\ 
S/FF/\B\H\B\H\ 
S\BB\H\B\H\E\/
S \BB\H\E\H\ 
S  \BB\H\/V/
S   \BB\HV/
S    \EE\/""",
'6':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/VH\B\H\ 
S/FF/V/\H\B\H\ 
S\BB\H\B\H\E\/
S \BB\H\E\H\ 
S  \BB\H\/V/
S   \BB\HV/
S    \EE\/""",
'7':"""S     TTT
S    /FF/\ 
S    \BB\H\ 
S     \BB\H\ 
S     T\EB\H\ 
S    /FF/\E\H\ 
S    \BB\H\/V/
S     \EE\HV/
S     /LL/V/
S    /FF/V/
S    \EE\/""",
'8':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/VH\B\H\ 
S/FF/V/\H\E\H\ 
S\BB\H\B\H\/V/
S \BB\H\E\HV/
S  \BB\H\/V/
S   \BB\HV/
S    \EE\/""",
'9':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /FF/V/\H\ 
S T\EB\H\B\H\ 
S/FF/\B\H\E\H\ 
S\BB\H\B\H\/V/
S \BB\H\E\HV/
S  \BB\H\/V/
S   \BB\HV/
S    \EE\/""",
':':"""S
S
S      TTT
S     /FF/\ 
S    T\EE\/
S   /FF/\ 
S   \EE\/""",
';':"""S
S      TTT
S     /FF/\ 
S    T\EE\/
S   /LL/\ 
S  /FF/V/
S  \EE\/""",
'<':"""S     
S    TTTTT
S   /FF/\/\ 
S   \EE\/\H\ 
S   /FF/\E\/
S   \BB\H\ 
S    \EE\/""",
'=':"""S     TTT
S    /FF/\ 
S   T\EB\H\ 
S  /FF/\E\H\ 
S  \BB\H\ \/
S   \BB\H\ 
S    \EE\/""",
'>':"""S
S     TTT
S    /FF/\ 
S   T\EB\H\ 
S  /FF/\E\/
S  \BB\H\/\ 
S   \EE\/\/
S       DD""",
'?':"""S     TTT
S    /FF/\ 
S    \BB\H\ 
S     \BB\H\ 
S     T\EB\H\ 
S    /LL/\B\H\ 
S   /FF/VH\/V/
S  T\EE\/\HV/
S /FF/\\\EE\/
S \EE\/""",
'@':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/V/L/VH\ 
S/FF/V/F/VVHH\ 
S\BB\H\B\HHVV/
S \BB\H\B\HV/
S  \BB\H\E\/
S   \BB\H\ 
S    \EE\/""",
'A':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/VH\B\H\ 
S/FF/V/\H\E\H\ 
S\EE\/BB\H\/V/
S     \EE\HV/
S     /LL/V/
S    /FF/V/
S    \EE\/""",
'B':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/VH\B\H\ 
S/FF/V/\H\E\H|
S\BB\H\B\H\/V/
S \BB\H\E\HV/
S  \BB\H\/V|
S   \EE\HV/
S       ~~""",
'C':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/V/BB\H\ 
S/FF/V/ \BB\H\ 
S\BB\H\  \EE\/
S \BB\H\ 
S  \BB\H\ 
S   \BB\H\ 
S    \EE\/""",
'D':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/V/BB\H\ 
S/FF/V/ \EE\H|
S\BB\H\ /LL/V/
S \BB\H\LL/V/
S  \BB\H\/V/
S   \EE\HV/
S       ~~""",
'E':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/VH\B\H\ 
S/FF/V/\H\B\H\ 
S\BB\H\B\H\E\/
S \BB\H\B\H\ 
S  \BB\H\E\/
S   \BB\H\ 
S    \EE\/""",
'F':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/VH\B\H\ 
S/FF/V/\H\B\H\ 
S\EE\/BB\H\E\/
S     \BB\H\ 
S      \EE\/""",
'G':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/V/BB\H\ 
S/FF/V/ \BB\H\ 
S\BB\H\  \EE\/
S \BB\H\DD/\ 
S  \BB\H\/V/
S   \BB\HV/
S    \EE\/""",
'H':"""S     TTT
S    /LL/\ 
S   /LL/V/
S  /LL/V/
S /LL/VH\ TTT
S/FF/V/\H\LL/\ 
S\EE\/BB\H\/V/
S     \EE\HV/
S     /LL/V/
S    /FF/V/
S    \EE\/""",
'I':"""S      TTT
S     /FF/\ 
S     \EE\H\ 
S     /LL/VH\ 
S  TT/LL/V/\/
S /FF/\/V/DD
S \BB\HV/
S  \BB\H\ 
S   \EE\/""",
'J':"""S  TTT
S /LL/\   TTT
S/FF/V/  /LL/\ 
S\BB\H\ /LL/V/
S \BB\H\LL/V/
S  \BB\H\/V/
S   \BB\HV/
S    \EE\/""",
'K':"""S     ___
S    /LL/\ 
S   /LL/V/
S  /LL/V/TTT
S /LL/VH\LL/\ 
S/FF/V/\H\/V/
S\EE\/BB\HV/
S     \EE\H\ 
S     /LL/V/
S    /FF/V/
S    \EE\/""",
'L':"""S     TTT
S    /LL/\ 
S   /LL/V/
S  /LL/V/
S /LL/V/
S/FF/V/
S\BB\H\ 
S \BB\H\ 
S  \BB\H\ 
S   \BB\H\ 
S    \EE\/""",
'M':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/V/L/VH\ 
S/FF/V/L/V/\H\ 
S\EE\/L/V/L/V/
S  /FF/V/L/V/
S  \EE\/L/V/
S    /FF/V/
S    \EE\/""",
'N':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/V/BB\H\ 
S/FF/V/ \EE\H\ 
S\EE\/  /LL/V/
S      /LL/V/
S     /LL/V/
S    /FF/V/
S    \EE\/""",
'O':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/V/BB\H\ 
S/FF/V/ \EE\H\ 
S\BB\H\ /LL/V/
S \BB\H\LL/V/
S  \BB\H\/V/
S   \BB\HV/
S    \EE\/""",
'P':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/VH\B\H\ 
S/FF/V/\H\E\H\ 
S\EE\/BB\H\/V/
S     \BB\HV/
S      \EE\/""",
'Q':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/V/BB\H\ 
S/FF/V/T\EE\H\ 
S\BB\H\/\LL/V/
S \BB\HV/L/V/
S /FF/VH\/V/
S \EE\/\HV/
S    \EE\/""",
'R':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /LL/V/\H\ 
S /LL/VH\B\H\ 
S/FF/V/\H\E\H\ 
S\EE\/EE\H\/V/
S    /LL/VHV/
S   /FF/V/\/
S   \EE\/DD""",
'S':"""S     TTT
S    /LL/\ 
S   /LL/VH\ 
S  /FF/V/\H\ 
S T\EB\H\B\H\ 
S/FF/\B\H\B\H\ 
S\BB\H\B\H\E\/
S \BB\H\E\H\ 
S  \BB\H\/V/
S   \BB\HV/
S    \EE\/""",
'T':"""S     TTT     
S    /FF/\ 
S    \BB\H\ 
S     \EE\H\ 
S     /LL/VH\ 
S    /LL/V/\H\ 
S   /LL/V/EE\/
S  /FF/V/
S  \EE\/""",
'U':"""S     TTT
S    /LL/\ 
S   /LL/V/
S  /LL/V/
S /LL/V/  TTT
S/FF/V/  /LL/\ 
S\BB\H\ /LL/V/
S \BB\H\LL/V/
S  \BB\H\/V/
S   \BB\HV/
S    \EE\/""",
'V':"""S     TTT
S    /LL/\ 
S   /LL/V/
S  /LL/V/
S /LL/V/  TTT
S/FF/V/  /LL/\ 
S\BB\H\ /LL/V/
S \BB\H\FF/V/
S  \EE\____/""",
'W':"""S     TTT
S    /LL/\ 
S   /LL/V/
S  /LL/V/
S /LL/V/T TTT
S/FF/V/L/\LL/\ 
S\BB\H\/V/L/V/
S \BB\HV/L/V/
S  \BB\H\/V/
S   \BB\HV/
S    \EE\/""",
'X':"""S      TTT
S   TT/LL/\ 
S  /LL/\/V/
S /LL/VHV/TTT
S/FF/V/\H\LL/\ 
S\EE\/EE\H\/V/
S    /LL/VHV/
S   /FF/V/\/
S   \EE\/DD""",
'Y':"""S     TTT
S    /LL/\ 
S   /LL/V/
S  /FF/V/
S T\EB\H\ TTT
S/FF/\B\H\LL/\ 
S\BB\H\B\H\/V/
S \BB\H\E\HV/
S  \BB\H\/V/
S   \BB\HV/
S    \EE\/""",
'Z':"""S     TTT
S    /FF/\ 
S   T\EB\H\ 
S  /LL/\B\H\ 
S /LL/VH\B\H\ 
S/FF/V/\H\E\H\ 
S\BB\H\B\H\/V/
S \BB\H\B\HV/
S  \BB\H\E\/
S   \BB\H\ 
S    \EE\/""",
'[':"""S      TTT
S     /LL/\ 
S    /LL/VH\ 
S   /LL/V/\/
S  /LL/V/DD
S /LL/V/
S/FF/V/
S\BB\H\ 
S \EE\/
""",
'\\':"""S   TTT
S  /LL/\ 
S /FF/V/
S \EE\/
S /FF/\ 
S \EE\/
S /LL/\ 
S/FF/V/
S\EE\/""",
']':"""S      TTT
S     /FF/\ 
S     \EE\H\ 
S     /LL/V/
S    /LL/V/
S TT/LL/V/
S/FF/\/V/
S\BB\HV/
S \EE\/""",
'^':"""S
S TTTTTTT
S/FF/\/\/\ 
S\BB\HVHV/
S \EE\/\H\ 
S   /FF/V/
S   \BB\H\ 
S    \EE\/
S
S
""",
'_':"""S
S
S
S
S TTT
S/FF/\ 
S\BB\H\ 
S \BB\H\ 
S  \BB\H\ 
S   \BB\H\ 
S    \EE\/""",
'`':"""S
S     TTT
S    /LL/\ 
S   /FF/V/
S   \EE\H\ 
S   /FF/V/
S   \EE\/
S      
S
S
""",
'{':"""S      TTT
S   TT/LL/\ 
S  /LL/\/VH\ 
S /FF/VHV/\/
S \EE\HV/DD
S /LL/V/
S/FF/V/
S\BB\H\ 
S \EE\/""",
'|':"""S       TTT
S      /LL/\ 
S     /LL/V/
S    /LL/V/
S   /LL/V/
S  /LL/V/
S /FF/V/
S \EE\/""",
'}':"""S      TTT
S     /FF/\ 
S     \EE\H\ 
S     /LL/V/
S    /LL/V/
S TT/LL/VH\ 
S/FF/\/VHV/
S\BB\HV/\/
S \EE\/DD""",
'~':"""S
S
S   TTT
S  /FF/\ 
S  \EE\/TTT
S  /FF/\/\/\ 
S  \EE\/\/\/
S      /FF/\ 
S      \EE\/
S
""",
}
style = {
'S':"    ",
'T':"_",
'D':"~",
'H':"#",
'V':"#",
'B':" ",
'L':" ",
'E':"_",
'F':"_",
}

""" Functions """
def print_ascii3d(text, glyphs, style):
  for letter in text:
    letter = glyphs[letter]
    for infill in style:
      letter = letter.replace(infill, style[infill])
    print(letter)

def settings(glyphs, style):
  print("Press enter to exit settings.")
  while True:
    print(glyphs['A'])
    print(3*f"{style['S']}     | |\n"+f"{style['S']}     V V\n")
    print_ascii3d('A', glyphs, style)
    command = input(f"Please type a certain letter ({', '.join([infill for infill in style])}) to modify its infill appearance: ").upper()
    if not command: return
    if command in style: style[command] = input(f"Please enter desired character(s) to fill region {command}: ")

""" Main """
print(f"Press enter to quit program. Type 'settings' to modify glyph appearance.\nAvailable glyphs: {''.join([glyph for glyph in glyphs])}")
while True:
  text = input("\nInsert text to convert: ")
  if not text: break
  elif text.lower() == 'settings': settings(glyphs, style)
  else:
    try: print_ascii3d(text, glyphs, style)
    except: print(f"OOPs! Looks like your text contains letters that cannot be converted.\n(Available glyphs: {''.join([glyph for glyph in glyphs])})")
