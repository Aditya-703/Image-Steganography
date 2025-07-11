from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk,Image
from stegano import exifHeader as stg
from tkinter import messagebox


Screen = Tk()
Screen.title("Image Steganography")
Screen.geometry("500x500+300+300")
Screen.config(bg="pink")




def Decode():
    Screen.destroy()
    DecScreen = Tk()
    DecScreen.title("Decode")
    DecScreen.geometry("500x500+300+300")
    DecScreen.config(bg="pink")

    def OpenFile():
        global FileOpen
        FileOpen = StringVar()
        FileOpen = askopenfilename(initialdir="/Desktop",
                                   title="Select the File",
                                   filetypes=(("only jpeg files", "*jpg"),
                                              ("all type of files", "*.*")))

    def Decoder():
        Message = stg.reveal(FileOpen)
        label3 = Label(text=Message)
        label3.place(relx=0.3, rely=0.3)

    SelectButton = Button(text="Select the file", command=OpenFile)
    SelectButton.place(relx=0.1, rely=0.4)
    EncodeButton = Button(text="Decode", command=Decoder)
    EncodeButton.place(relx=0.4, rely=0.5)


def Encode():
    Screen.destroy()
    EncScreen = Tk()
    EncScreen.title("Encode")
    EncScreen.geometry("500x500+300+300")
    EncScreen.config(bg="yellow")
    label = Label(text="Confidential Message")
    label.place(relx=0.1, rely=0.2)
    entry = Entry()
    entry.place(relx=0.5, rely=0.2)
    label1 = Label(text="Name of the File")
    label1.place(relx=0.1, rely=0.3)
    SaveEntry = Entry()
    SaveEntry.place(relx=0.5, rely=0.3)

    def OpenFile():
        global FileOpen
        FileOpen = StringVar()
        FileOpen = askopenfilename(initialdir="/Desktop", title="SelectFile",
                                   filetypes=(("jpeg files", "*jpg"),
                                              ("all files", "*.*")))

        label2 = Label(text=FileOpen)
        label2.place(relx=0.3, rely=0.3)

    def Encoder():
        Response = messagebox.askyesno("PopUp",
                                       "Do you want to encode the image")
        if Response == 1:
            stg.hide(FileOpen, SaveEntry.get() + ".jpg", entry.get())
            messagebox.showinfo("Pop Up", "Successfully Encoded the image")
        else:
            messagebox.showwarning("Pop Up", "Unsuccessful,please try again")

    SelectButton = Button(text="Select the file", command=OpenFile)
    SelectButton.place(relx=0.1, rely=0.4)
    EncodeButton = Button(text="Encode", command=Encoder)
    EncodeButton.place(relx=0.4, rely=0.5)


# creating buttons
EncodeButton = Button(text="Encode", command=Encode)
EncodeButton.place(relx=0.3, rely=0.4)

DecodeButton = Button(text="Decode", command=Decode)
DecodeButton.place(relx=0.6, rely=0.4)

mainloop()
