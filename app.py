import tkinter as tk
import tkcalendar as tkc
import datetime

class MainApplication(tk.Frame):
    WIDTH = 526
    HEIGHT = 297


    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        window = tk.Frame(self, width=self.WIDTH, height=self.HEIGHT)
        window.pack(fill="both", expand=True)

        form = tk.Frame(window, borderwidth=2, relief="groove")
        form.place(relx=.05, rely=.05, relwidth=.9, relheight=.9)

        from_frame = FormRow(form, "From:")
        from_frame.pack(side=tk.TOP, fill="both")
        to_frame = FormRow(form, "To:")
        to_frame.pack(side=tk.TOP, fill="both")

        date_frame = tk.Frame(form, height=200)
        date_frame.pack(side=tk.TOP, fill="x")
        date_label = tk.Label(date_frame, text="Date:")
        date_label.place(rely=.5, anchor="w")
        date_calendar = tkc.Calendar(date_frame, foreground="black", selectforeground="red", selectbackground="red")
        date_calendar.place(rely=.5, relx=.9, anchor="e")

        form_button = tk.Button(form, text="SEARCH", command=lambda: self.testmethod(date_calendar.selection_get()))
        form_button.pack(side=tk.BOTTOM)

    def testmethod(self, var):
        self.parent.update()
        print("a", self.winfo_geometry())


class FormRow(tk.Frame):
    HEIGHT = 20
    def __init__(self, parent, label_text):
        tk.Frame.__init__(self, parent, height=20)
        self.parent = parent
        self.label_text = label_text
        self.label = tk.Label(self, text=label_text)
        self.label.place(anchor="w", relheight=1, relx=.02, rely=.5)
        self.entry = tk.Entry(self)
        self.entry.place(anchor="e", relwidth=.7, relheight=1, relx=.98, rely=.5)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
