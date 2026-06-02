from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

root = Tk()
root.title("Advanced Music Player")
root.geometry("700x500")
root.config(bg="#1e1e1e")

songs = []
current_song = 0
paused = False

# ---------------- Functions ---------------- #

def load_music():
    global songs

    folder = filedialog.askdirectory()

    if folder:
        songs = []

        playlist.delete(0, END)

        for file in os.listdir(folder):
            if file.endswith(".mp3"):
                songs.append(os.path.join(folder, file))
                playlist.insert(END, file)

        status_label.config(text=f"{len(songs)} Songs Loaded")

def play_music():
    global current_song

    if not songs:
        return

    selected = playlist.curselection()

    if selected:
        current_song = selected[0]

    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()

    song_name.set(os.path.basename(songs[current_song]))
    status_label.config(text="Playing")

def stop_music():
    pygame.mixer.music.stop()
    status_label.config(text="Stopped")

def pause_music():
    global paused

    if not paused:
        pygame.mixer.music.pause()
        paused = True
        status_label.config(text="Paused")
    else:
        pygame.mixer.music.unpause()
        paused = False
        status_label.config(text="Playing")

def next_song():
    global current_song

    if not songs:
        return

    current_song += 1

    if current_song >= len(songs):
        current_song = 0

    playlist.selection_clear(0, END)
    playlist.selection_set(current_song)
    playlist.activate(current_song)

    play_music()

def previous_song():
    global current_song

    if not songs:
        return

    current_song -= 1

    if current_song < 0:
        current_song = len(songs) - 1

    playlist.selection_clear(0, END)
    playlist.selection_set(current_song)
    playlist.activate(current_song)

    play_music()

def change_volume(value):
    pygame.mixer.music.set_volume(float(value) / 100)

# ---------------- UI ---------------- #

title = Label(
    root,
    text="🎵 Advanced Music Player",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=10)

song_name = StringVar()
song_name.set("No Song Selected")

current_song_label = Label(
    root,
    textvariable=song_name,
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="cyan"
)
current_song_label.pack(pady=5)

playlist_frame = Frame(root)
playlist_frame.pack(pady=10)

scrollbar = Scrollbar(playlist_frame)

playlist = Listbox(
    playlist_frame,
    width=60,
    height=12,
    bg="black",
    fg="white",
    selectbackground="cyan"
)

scrollbar.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT)

playlist.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=playlist.yview)

Button(
    root,
    text="Load Songs",
    font=("Arial", 12),
    bg="orange",
    command=load_music
).pack(pady=10)

controls = Frame(root, bg="#1e1e1e")
controls.pack(pady=10)

Button(
    controls,
    text="⏮ Previous",
    width=12,
    command=previous_song
).grid(row=0, column=0, padx=5)

Button(
    controls,
    text="▶ Play",
    width=12,
    command=play_music
).grid(row=0, column=1, padx=5)

Button(
    controls,
    text="⏸ Pause",
    width=12,
    command=pause_music
).grid(row=0, column=2, padx=5)

Button(
    controls,
    text="⏹ Stop",
    width=12,
    command=stop_music
).grid(row=0, column=3, padx=5)

Button(
    controls,
    text="⏭ Next",
    width=12,
    command=next_song
).grid(row=0, column=4, padx=5)

# Progress Bar
progress = ttk.Progressbar(
    root,
    orient=HORIZONTAL,
    length=500,
    mode='indeterminate'
)
progress.pack(pady=15)
progress.start(20)

# Volume Control
volume_frame = Frame(root, bg="#1e1e1e")
volume_frame.pack()

Label(
    volume_frame,
    text="🔊 Volume",
    bg="#1e1e1e",
    fg="white"
).pack()

volume_slider = Scale(
    volume_frame,
    from_=0,
    to=100,
    orient=HORIZONTAL,
    command=change_volume,
    length=250
)
volume_slider.set(70)
volume_slider.pack()

pygame.mixer.music.set_volume(0.7)

status_label = Label(
    root,
    text="Ready",
    bg="#1e1e1e",
    fg="lightgreen",
    font=("Arial", 11)
)
status_label.pack(pady=10)

root.mainloop()
