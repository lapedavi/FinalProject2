import os.path

from gui import *

class Logic(Gui):
    DATA_FOLDER = 'data/'

    def __init__(self, window) -> None:
        super().__init__(window)

        if not os.path.exists(self.DATA_FOLDER):
            os.makedirs(self.DATA_FOLDER)

        collections = os.listdir(Logic.DATA_FOLDER)

        for collection in collections:
            clean_collection = collection.split('.')[0]
            self.main_collections_listbox.insert(END, clean_collection)

        self.main_add_collection_button.config(command=self.select_add_collection)
        self.collection_add_item_button.config(command=self.select_add_item)

        self.add_collection_back_button.config(command=self.select_add_collection_back)
        self.collection_back_button.config(command=self.select_collection_back)
        self.add_item_back_button.config(command=self.select_add_item_back)
        self.main_view_button.config(command=self.select_view_collection)
        self.main_delete_button.config(command=self.select_delete_collection)

        self.add_collection_save_button.config(command=self.save_collection)
        self.add_item_save_button.config(command=self.save_item)

    def select_add_collection(self) -> None:
        """Close the main menu and open the add collection form"""
        self.main_frame.pack_forget()
        self.add_collection_frame.pack()

    def select_add_item(self) -> None:
        """Close the collection view and open the add item form"""
        self.collection_frame.pack_forget()
        self.add_item_frame.pack()

    def select_add_collection_back(self) -> None:
        """Close the add collection form and open the main menu"""
        self.add_collection_frame.pack_forget()
        self.main_frame.pack()

    def select_collection_back(self) -> None:
        """Close the collection view and open the main menu"""
        self.collection_item_listbox.delete(0, END)
        self.collection_frame.pack_forget()
        self.main_frame.pack()

    def select_add_item_back(self) -> None:
        """Close the add item form and open the collection view"""
        self.add_item_frame.pack_forget()
        self.collection_frame.pack()

    def select_view_collection(self) -> None:
        """Close the main menu and open the selected collection"""
        index = self.main_collections_listbox.curselection()

        if len(index) == 0:
            self.main_error_label.config(text="No collection selected")
            return

        item = self.main_collections_listbox.get(index[0])

        collection_file = open(f'{Logic.DATA_FOLDER}{item}.csv', 'r')
        for line in collection_file:
            self.collection_item_listbox.insert(END, line)

        self.main_error_label.config(text='')
        self.main_frame.pack_forget()
        self.collection_title_label.config(text=item)
        self.collection_frame.pack()

    def select_delete_collection(self) -> None:
        index = self.main_collections_listbox.curselection()

        if len(index) == 0:
            self.main_error_label.config(text="No collection selected")
            return

        item = self.main_collections_listbox.get(index[0])

        self.main_collections_listbox.delete(index[0])
        os.remove(f"{Logic.DATA_FOLDER}{item}.csv")
        self.main_error_label.config(text='')


    def save_collection(self) -> None:
        """Create new collection based on inputs from the collection form"""
        collection_name = self.add_collection_name_entry.get().strip()

        if collection_name == '':
            self.add_collection_error_label.config(text='Collection must have a name')
            return

        self.add_collection_name_entry.delete(0, END)
        if os.path.exists(f'{Logic.DATA_FOLDER}{collection_name}.csv'):
            self.add_collection_error_label.config(text="Collection already exists")
            return

        collection_file = open(f'{Logic.DATA_FOLDER}{collection_name}.csv', 'w')
        collection_file.close()

        self.main_collections_listbox.insert(END, collection_name)

        self.add_collection_frame.pack_forget()
        self.main_frame.pack()
        self.add_collection_error_label.config(text="")

    def save_item(self) -> None:
        """Create new item in collection based on inputs from the item form"""
        item_name = self.add_item_name_entry.get().strip()

        if item_name == '':
            self.add_item_error_label.config(text='Item must have a name')
            return

        self.add_item_name_entry.delete(0, END)
        collection_file = open(f'{Logic.DATA_FOLDER}{self.collection_title_label.cget('text')}.csv', 'a')
        collection_file.write(f'{item_name}\n')
        collection_file.close()

        self.collection_item_listbox.insert(END, item_name)

        self.add_item_frame.pack_forget()
        self.collection_frame.pack()
        self.add_item_error_label.config(text='')
