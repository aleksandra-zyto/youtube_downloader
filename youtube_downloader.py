# UI PART #
from tkinter import *
from tkinter import ttk
from pytube import YouTube

root = Tk()
root.title("YouTube Downloader")

# WINDOW GEOMETRY #
window_width = 600
window_height =350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2-window_width/2)
centre_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{centre_y}')
root.resizable(False, True)
root.minsize(600,350)
root.attributes("-topmost", 1)

# WINDOW ELEMENTS AND YOUTUBE BIT #

link = StringVar()

url_input = ttk.Frame(root)
url_input.pack(padx=10, pady=10, fill='x')
url_label = ttk.Label(url_input, text="Insert a link to the video:")
url_label.pack(ipadx=10, ipady=10,fill="x")

url_entry = ttk.Entry(url_input, width = 70, textvariable=link)
url_entry.pack(fill='x')
url_entry.focus()

def submit_link():
    """Triggered when 'submit link' button clicked.
    interacts with submitted url to fetch available resolutions """
    button['state'] = DISABLED # button disabled so the user can only click it once
    available_res = []
    url = link.get()
    yt_url = YouTube(str(url))
    video_audio = yt_url.streams.filter(progressive=True) #progressive=True ensures that audio and video are in one file
    for stream in video_audio:
        available_res.append(stream.resolution)

    selected_quality = StringVar()

    radio_buttons = ttk.Frame(root)
    radio_buttons.pack(padx=10, pady=10, fill='x')
    res_label = ttk.Label(radio_buttons, text= "Available resolutions: ")
    res_label.pack(padx=10, pady=10, fill="x")

    for quality in available_res: #creates radio buttons for available resolutions
        r = ttk.Radiobutton(
            radio_buttons,
            text=quality,
            value=quality,
            variable=selected_quality
        )
        r.pack(fill='x', padx=5, pady=5)

    def download():
        """Triggered when download button clicked. Downloads video in selected quality"""
        download_button["state"]= DISABLED
        chosen_res = selected_quality.get()
        video = video_audio.filter(resolution=chosen_res).first()
        video.download()


    download_button = Button(
        radio_buttons,
        text= "Download",
        command=download,
    )
    download_button.pack()

    def download_more():
        """Resets the fields for a new download. Recovers buttons and wipes the radio buttons frame"""
        url_entry.delete(0, END)
        radio_buttons.destroy()
        available_res.clear()
        button['state'] = NORMAL
        download_button["state"] = NORMAL


    again_button = Button(radio_buttons, text= "Download more",command = download_more)
    close_button = Button(radio_buttons, text="Close",command= root.destroy) #window closed
    again_button.pack( padx=2, fill="x",side="left", expand=True, )
    close_button.pack( padx=2, fill="x", side="left", expand=True)

button = Button(
    root,
    text="Submit link",
    command=submit_link
)

button.pack()

root.mainloop()
