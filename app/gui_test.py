from Tkinter import *
import threading


def chooser():
    top = Tk()
    total = []

    #Title
    top.title("Science Data Catalog Picker")

    # LABEL
    Label(top, text="Science Data Catalog Keywords").grid(row=0, column=1)

    def get_em(kw):
        print(kw)
        total.append(kw)

    def mk_radio(kw, var):
        cb = Radiobutton(top, variable=var, text=kw, value="test", command=lambda: get_em(kw))
        return cb

    count = 1
    count_col2 = 1
    with open('keywords.txt', 'r') as f:
        rl = f.readlines()
        for l in rl:
            if count < 13:
                unq_var = count
                new_box = mk_radio(l, unq_var)
                count += 1
                new_box.grid(row=count, column=1, sticky='w')

            else:
                unq_var = count_col2 + 20
                new_box = mk_radio(l, unq_var)
                count_col2 += 1
                new_box.grid(row=count_col2, column=2, sticky='w')

    cleaned = []
    def clean_kws():
        for i in total:
            if i.endswith('\n'):
                add_to = i.replace('\n','')
                cleaned.append(add_to)

    def loading():
        hm = Tk()
        Label(hm, text="Loading files please wait ")

    # BUTTON
    def callback():
        clean_kws()
        print("Downloading files: " + str(cleaned))
        top.destroy()

    Label(top, text="Maximum file size").grid(row=14, column=1)

    variable = StringVar(top)
    variable.set("5mb")

    def file_s():
        print("File limit: " + str(variable.get()))

    # RECORD ID option
    Label(top, text="Record ID: ").grid(row=16, column=1)
    record_id = StringVar()
    Entry(top, textvariable=record_id).grid(row=16, column=2)

    # Download Criteria
    OptionMenu(top, variable, "5mb","10mb","50mb","1gb").grid(row=15, column=1)


    button = Button(top,text="Download files",command=callback)
    button.grid(row=17, column=1)

    #print(record_id.get())
    file_s()
    top.mainloop()


    # Return tuple with KWS / ID / SIZE LIMIT
    info = (cleaned, record_id.get(), variable.get())

    return info
    #return cleaned





