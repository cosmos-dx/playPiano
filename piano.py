

from playsound import playsound 
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("PlayPiano")
window.geometry("1280x720")
window.configure(bg = "#FFFFFF")

# setting the app logo
icon = PhotoImage(file="appLogo.png")
window.iconphoto(False, icon)

# showing played note
def showPlayedNote(note):
    canvas.create_text(
        canvas.delete("currentNote"),
        603.0,
        15.0,
        anchor="nw",
        text=str(note),
        fill="#58270B",
        font=("Roboto Bold", 60 * -1),
        tag="currentNote"
    )

# playing the note
def playNote(note):
    if len(note) == 1:
        showPlayedNote(" "+str(note))
    elif note == "LC":
        newNote = "C"
        showPlayedNote(" "+str(newNote))
    else:
        showPlayedNote(str(note))
    if note[-1] == "#":
        newNote = note[0]+"S"
        playsound("notes/"+str(newNote)+".wav")
    else:
        playsound("notes/"+str(note)+".wav")

# creating the project canvas
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# setting up the canvas
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    360.0,
    image=image_image_1
)

# button C
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: playNote("C"),
    relief="flat"
)
button_1.place(
    x=1.0,
    y=95.0,
    width=165.0,
    height=625.0
)

# button D
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: playNote("D"),
    relief="flat"
)
button_2.place(
    x=160.0,
    y=95.0,
    width=165.47296142578125,
    height=625.0
)

# button A
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: playNote("A"),
    relief="flat"
)
button_3.place(
    x=795.0,
    y=95.0,
    width=165.47296142578125,
    height=625.0
)

# button G
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: playNote("G"),
    relief="flat"
)
button_4.place(
    x=635.0,
    y=95.0,
    width=165.47296142578125,
    height=625.0
)

# button E
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: playNote("E"),
    relief="flat"
)
button_5.place(
    x=318.0,
    y=95.0,
    width=165.47296142578125,
    height=625.0
)

# button B
button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: playNote("B"),
    relief="flat"
)
button_6.place(
    x=954.0,
    y=95.0,
    width=165.472900390625,
    height=625.0
)

# button F
button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: playNote("F"),
    relief="flat"
)
button_7.place(
    x=477.0,
    y=95.0,
    width=165.469970703125,
    height=625.0
)

# button LC
button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: playNote("LC"),
    relief="flat"
)
button_8.place(
    x=1114.0,
    y=95.0,
    width=165.472900390625,
    height=625.0
)

# button C#
button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: playNote("C#"),
    relief="flat"
)
button_9.place(
    x=99.0,
    y=95.0,
    width=126.0,
    height=449.0
)

# button D#
button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: playNote("D#"),
    relief="flat"
)
button_10.place(
    x=258.0,
    y=95.0,
    width=126.0,
    height=449.0
)

# button F#
button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: playNote("F#"),
    relief="flat"
)
button_11.place(
    x=575.0,
    y=95.0,
    width=126.0,
    height=449.0
)

# button G#
button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: playNote("G#"),
    relief="flat"
)
button_12.place(
    x=733.0,
    y=95.0,
    width=126.0,
    height=449.0
)

# button A#
button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: playNote("A#"),
    relief="flat"
)
button_13.place(
    x=893.0,
    y=95.0,
    width=126.0,
    height=449.0
)

# box for showing the played note
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    641.0,
    49.5,
    image=entry_image_1
)

# app name
canvas.create_text(
    48.0,
    19.0,
    anchor="nw",
    text="PlayPiano",
    fill="#FFFFFF",
    font=("PatuaOne Regular", 50 * -1)
)

# developer details
canvas.create_text(
    1025.0,
    39.0,
    anchor="nw",
    text="",
    fill="#FFFFFF",
    font=("PatuaOne Regular", 30 * -1)
)

# making the window size fixed
window.resizable(False, False)
window.mainloop()
