from tkinter import *
from pytube import YouTube
from tkinter import ttk
from tkinter import filedialog, messagebox

# from tqdm import tqdm

window = Tk()

window.geometry('600x450')

window.resizable(0, 0)

window.title('Djimbalinux Downloader')

Label(window, text="Télécharger vidéo Youtube", font=("arial", 20, "bold")).pack()


def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)


folderPath = StringVar()

Label(window, text="Chemin du dossier").place(x=240, y=120)
folderPath_entered = Entry(window, textvariable=folderPath, width=70).place(x=15, y=150)
ttk.Button(window, text="choisir le dossier", command=getFolderPath).place(x=240, y=180)

link = StringVar()

Label(window, text="Coler le lien ici ⬇️ ", font='arial 20 bold').place(x=200, y=60)

link_entered = Entry(window, width=70, textvariable=link).place(x=15, y=90)

Label(window, text="le téléchargement peut prendre quelques minutes, veillez patienter lors de ce dernier...").place(
    x=10, y=350)


def ExitApp():
    window.destroy()


def downloader(extension="mp4"):
    try:
        url = YouTube(str(link.get()))
        video = url.streams.filter(progressive=True, file_extension=extension).order_by('resolution').desc().first()
        video.download()
        video.download(folderPath.get())

        # Displaying the message
        messagebox.showinfo("téléchargement terminé !", "vidéo sauvegardée dans\n" + folderPath.get())
    except Exception as e:
        messagebox.showinfo("échec !", "verifié votre lien youtube")


Button(window, text="Télécharger", font='arial 15 bold', bg='orange', padx=5, command=downloader).place(x=235, y=230)

Button(window, text="Cliquez ici pour quitter", font='arial 13 bold', bg='red', padx=5,
       command=ExitApp).place(x=190, y=280)

window.mainloop()
