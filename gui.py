from tkinter import *

class Gui:
    def __init__(self, window):
        self.window = window

        # Main Frame
        self.main_frame = Frame(self.window)

        self.main_title_label = Label(self.main_frame, text="Collection Tracker", font=("Helvetica", 15))
        self.main_collections_listbox = Listbox(self.main_frame, selectmode=SINGLE)

        self.main_title_label.pack()
        self.main_collections_listbox.pack(pady=15)

        self.main_button_frame = Frame(self.main_frame)
        self.main_add_collection_button = Button(self.main_button_frame, text='Add New')
        self.main_view_button = Button(self.main_button_frame, text='View')
        self.main_delete_button = Button(self.main_button_frame, text='Delete')

        self.main_add_collection_button.pack(side='left')
        self.main_view_button.pack(side='left', padx=10)
        self.main_delete_button.pack(side='right')
        self.main_button_frame.pack()

        self.main_error_label = Label(self.main_frame, fg='red')

        self.main_error_label.pack(pady=10)
        self.main_frame.pack()

        # Add Collection Frame
        self.add_collection_frame = Frame(self.window)

        self.add_collection_title_label = Label(self.add_collection_frame, text="Add Collection", font=("Helvetica", 15))

        self.add_collection_title_label.pack()

        self.add_collection_name_frame = Frame(self.add_collection_frame)
        self.add_collection_name_label = Label(self.add_collection_name_frame, text="Name")
        self.add_collection_name_entry = Entry(self.add_collection_name_frame)

        self.add_collection_name_label.pack(side='left')
        self.add_collection_name_entry.pack(side='right', padx=10)
        self.add_collection_name_frame.pack(pady=15)

        self.add_collection_button_frame = Frame(self.add_collection_frame)
        self.add_collection_save_button = Button(self.add_collection_button_frame, text='Save')
        self.add_collection_back_button = Button(self.add_collection_button_frame, text='Back')

        self.add_collection_save_button.pack(side='left')
        self.add_collection_back_button.pack(side='right', padx=10)
        self.add_collection_button_frame.pack()

        self.add_collection_error_label = Label(self.add_collection_frame, fg='red')

        self.add_collection_error_label.pack(pady=10)

        # Collection Frame
        self.collection_frame = Frame(self.window)

        self.collection_title_label = Label(self.collection_frame, font=("Helvetica", 15))
        self.collection_item_listbox = Listbox(self.collection_frame, selectmode=NONE)

        self.collection_title_label.pack()
        self.collection_item_listbox.pack(pady=15)

        self.collection_button_frame = Frame(self.collection_frame)
        self.collection_add_item_button = Button(self.collection_button_frame, text='Add New')
        self.collection_back_button = Button(self.collection_button_frame, text='Back')

        self.collection_add_item_button.pack(side='left')
        self.collection_back_button.pack(side='right', padx=10)
        self.collection_button_frame.pack()

        # Add Item Frame
        self.add_item_frame = Frame(self.window)
        self.add_item_title_label = Label(self.add_item_frame, text="Add Item", font=("Helvetica", 15))

        self.add_item_title_label.pack()

        self.add_item_name_frame = Frame(self.add_item_frame)
        self.add_item_name_label = Label(self.add_item_name_frame, text="Name")
        self.add_item_name_entry = Entry(self.add_item_name_frame)

        self.add_item_name_label.pack(side='left')
        self.add_item_name_entry.pack(side='right', padx=10)
        self.add_item_name_frame.pack(pady=15)

        self.add_item_button_frame = Frame(self.add_item_frame)
        self.add_item_save_button = Button(self.add_item_button_frame, text='Save')
        self.add_item_back_button = Button(self.add_item_button_frame, text='Back')

        self.add_item_save_button.pack(side='left')
        self.add_item_back_button.pack(side='right', padx=10)
        self.add_item_button_frame.pack()

        self.add_item_error_label = Label(self.add_item_frame, fg='red')

        self.add_item_error_label.pack(pady=10)


