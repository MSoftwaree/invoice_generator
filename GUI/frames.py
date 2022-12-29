from data_management import DataManagement
from pdf_generator import generate_page
from tkinter import filedialog
from datetime import datetime, timedelta
import customtkinter


class Frames(DataManagement):

    def __init__(self, master_window, language):
        self.master_window = master_window
        self.language = language
        self.chosen_seller_file_path = None
        self.chosen_buyer_file_path = None
        super().__init__()

    def seller_frame(self):
        """ Create seller frame """
        frame = customtkinter.CTkFrame(master=self.master_window, width=140, corner_radius=0)
        frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        frame_title = customtkinter.CTkLabel(frame, text=self.get_word("Seller"),
                                             font=customtkinter.CTkFont(size=20, weight='bold'))
        frame_title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        # Seller Name
        customtkinter.CTkLabel(frame, text=self.get_word("Company Name") + ":").grid(row=1, column=0, padx=10, pady=5,
                                                                                     sticky="e")
        self.seller_name_value = customtkinter.StringVar()
        self.seller_name = customtkinter.CTkEntry(master=frame, width=250, textvariable=self.seller_name_value)
        self.seller_name.grid(row=1, column=1, padx=20, pady=5, sticky="nsew")

        # Seller Address
        customtkinter.CTkLabel(frame, text=self.get_word("Address") + ":").grid(row=2, column=0, padx=10, pady=5,
                                                                                sticky="e")
        self.seller_address_value = customtkinter.StringVar()
        self.seller_address = customtkinter.CTkEntry(master=frame, textvariable=self.seller_address_value)
        self.seller_address.grid(row=2, column=1, padx=20, pady=5, sticky="nsew")

        # Seller Post Code
        customtkinter.CTkLabel(frame, text=self.get_word("Post Code and City") + ":").grid(row=3, column=0, padx=10,
                                                                                           pady=5, sticky="e")
        self.seller_post_code_value = customtkinter.StringVar()
        self.seller_post_code = customtkinter.CTkEntry(master=frame, textvariable=self.seller_post_code_value)
        self.seller_post_code.grid(row=3, column=1, padx=20, pady=5, sticky="nsew")

        # Seller NIP
        customtkinter.CTkLabel(frame, text=self.get_word("NIP Number") + ":").grid(row=4, column=0, padx=10, pady=5,
                                                                                   sticky="e")
        self.seller_nip_value = customtkinter.StringVar()
        self.seller_nip = customtkinter.CTkEntry(master=frame, textvariable=self.seller_nip_value)
        self.seller_nip.grid(row=4, column=1, padx=20, pady=5, sticky="nsew")

        # Seller Bank Account
        customtkinter.CTkLabel(frame, text=self.get_word("Bank Account Number") + ":").grid(row=5, column=0, padx=10,
                                                                                            pady=5, sticky="e")
        self.seller_bank_account_value = customtkinter.StringVar()
        self.seller_bank_account_number = customtkinter.CTkEntry(master=frame,
                                                                 textvariable=self.seller_bank_account_value)
        self.seller_bank_account_number.grid(row=5, column=1, padx=20, pady=5, sticky="nsew")

        load_button = customtkinter.CTkButton(master=frame, text=self.get_word("Load"), command=self._load_seller_data)
        load_button.grid(row=2, column=3, padx=20, pady=5)

        save_button = customtkinter.CTkButton(master=frame, text=self.get_word("Save"), command=self._save_seller_data)
        save_button.grid(row=4, column=3, padx=20, pady=5)

    def buyer_frame(self):
        """ Create buyer frame """
        frame = customtkinter.CTkFrame(master=self.master_window, width=140, corner_radius=0)
        frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        frame.grid_rowconfigure(6, weight=3)

        frame_title = customtkinter.CTkLabel(frame, text=self.get_word("Buyer"),
                                             font=customtkinter.CTkFont(size=20, weight='bold'))
        frame_title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        # Buyer Name
        customtkinter.CTkLabel(frame, text=self.get_word("Company Name") + ":").grid(row=1, column=0, padx=10, pady=5,
                                                                                     sticky="e")
        self.buyer_name_value = customtkinter.StringVar()
        self.buyer_name = customtkinter.CTkEntry(master=frame, width=250, textvariable=self.buyer_name_value)
        self.buyer_name.grid(row=1, column=1, columnspan=2, padx=20, pady=5, sticky="nsew")

        # Buyer Address
        customtkinter.CTkLabel(frame, text=self.get_word("Address") + ":").grid(row=2, column=0, padx=10, pady=5,
                                                                                sticky="e")
        self.buyer_address_value = customtkinter.StringVar()
        self.buyer_address = customtkinter.CTkEntry(master=frame, textvariable=self.buyer_address_value)
        self.buyer_address.grid(row=2, column=1, columnspan=2, padx=20, pady=5, sticky="nsew")

        # Buyer Post Code
        customtkinter.CTkLabel(frame, text=self.get_word("Post Code and City") + ":").grid(row=3, column=0, padx=10,
                                                                                           pady=5, sticky="e")
        self.buyer_post_code_value = customtkinter.StringVar()
        self.buyer_post_code = customtkinter.CTkEntry(master=frame, textvariable=self.buyer_post_code_value)
        self.buyer_post_code.grid(row=3, column=1, columnspan=2, padx=20, pady=5, sticky="nsew")

        # Buyer Country
        customtkinter.CTkLabel(frame, text=self.get_word("Country") + ":").grid(row=4, column=0, padx=10, pady=5,
                                                                                sticky="e")
        self.buyer_country_value = customtkinter.StringVar()
        self.buyer_country = customtkinter.CTkEntry(master=frame, textvariable=self.buyer_country_value)
        self.buyer_country.grid(row=4, column=1, columnspan=2, padx=20, pady=5, sticky="nsew")

        # Buyer NIP
        customtkinter.CTkLabel(frame, text=self.get_word("NIP Number") + ":").grid(row=5, column=0, padx=10, pady=5,
                                                                                   sticky="e")
        self.buyer_nip_value = customtkinter.StringVar()
        self.buyer_nip = customtkinter.CTkEntry(master=frame, textvariable=self.buyer_nip_value)
        self.buyer_nip.grid(row=5, column=1, columnspan=2, padx=20, pady=5, sticky="nsew")

        load_button = customtkinter.CTkButton(master=frame, text=self.get_word("Load"), command=self._load_buyer_data)
        load_button.grid(row=2, column=3, padx=20, pady=5)

        save_button = customtkinter.CTkButton(master=frame, text=self.get_word("Save"), command=self._save_buyer_data)
        save_button.grid(row=4, column=3, padx=20, pady=5)

    def data_frame(self):
        """ Crate data frame """
        frame = customtkinter.CTkFrame(master=self.master_window, width=140, corner_radius=0)
        frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        frame.grid_rowconfigure(6, weight=3)

        frame_title = customtkinter.CTkLabel(frame, text=self.get_word("Necessary data"),
                                             font=customtkinter.CTkFont(size=20, weight='bold'))
        frame_title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        # Document number
        customtkinter.CTkLabel(frame, text=self.get_word("Document Number") + ":").grid(row=1, column=0, padx=10,
                                                                                        pady=5, sticky="e")
        self.doc_number_value = customtkinter.StringVar()
        self.doc_number = customtkinter.CTkEntry(master=frame, width=250, textvariable=self.doc_number_value)
        self.doc_number.grid(row=1, column=1, padx=20, pady=5, sticky="nsew")

        # Date of issue
        customtkinter.CTkLabel(frame, text=self.get_word("Date of issue") + ":").grid(row=2, column=0, padx=10, pady=5,
                                                                                      sticky="e")
        self.issue_date_value = customtkinter.StringVar()
        self.issue_date = customtkinter.CTkEntry(master=frame, textvariable=self.issue_date_value)
        self.issue_date.grid(row=2, column=1, padx=20, pady=5, sticky="nsew")

        # Date of service
        customtkinter.CTkLabel(frame, text=self.get_word("Date of service") + ":").grid(row=3, column=0, padx=10,
                                                                                        pady=5, sticky="e")
        self.service_date_value = customtkinter.StringVar()
        self.service_date = customtkinter.CTkEntry(master=frame, textvariable=self.service_date_value)
        self.service_date.grid(row=3, column=1, padx=20, pady=5, sticky="nsew")

        # Date of payment
        customtkinter.CTkLabel(frame, text=self.get_word("Date of payment") + ":").grid(row=4, column=0, padx=10,
                                                                                        pady=5, sticky="e")
        self.payment_date_value = customtkinter.StringVar()
        self.payment_date = customtkinter.CTkEntry(master=frame, textvariable=self.payment_date_value)
        self.payment_date.grid(row=4, column=1, padx=20, pady=5, sticky="nsew")

        # Name of the service
        customtkinter.CTkLabel(frame, text=self.get_word("Name of the service") + ":").grid(row=5, column=0, padx=10,
                                                                                            pady=5, sticky="e")
        self.service_name_value = customtkinter.StringVar()
        self.service_name = customtkinter.CTkEntry(master=frame, textvariable=self.service_name_value)
        self.service_name.grid(row=5, column=1, padx=20, pady=5, sticky="nsew")

        # Net value
        customtkinter.CTkLabel(frame, text=self.get_word("Net value") + ":").grid(row=6, column=0, padx=10, pady=5,
                                                                                  sticky="e")
        self.net_service = customtkinter.CTkEntry(master=frame, placeholder_text=self.get_word("Enter the net value"),
                                                  placeholder_text_color="red")
        self.net_service.grid(row=6, column=1, padx=20, pady=5, sticky="nsew")

        load_button = customtkinter.CTkButton(master=frame, text=self.get_word("Load"),
                                              command=self._load_necessary_data)
        load_button.grid(row=3, column=3, padx=20, pady=5)

    def settings_frame(self):
        """ Create setting frame """
        frame = customtkinter.CTkFrame(master=self.master_window, width=140, corner_radius=0)
        frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        frame.grid_rowconfigure(6, weight=3)

        frame_title = customtkinter.CTkLabel(frame, text=self.get_word("Settings"),
                                             font=customtkinter.CTkFont(size=20, weight='bold'))
        frame_title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        appearance_mode_label = customtkinter.CTkLabel(frame, text=self.get_word("Appearance Mode") + ":")
        appearance_mode_label.grid(row=1, column=0)
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(master=frame, values=["Dark", "Light", "System"],
                                                                       command=self._change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=2, column=0, padx=20, pady=(10, 10))

        theme_color_label = customtkinter.CTkLabel(frame, text=self.get_word("Theme color") + ":")
        theme_color_label.grid(row=1, column=1)
        self.theme_color_optionmenu = customtkinter.CTkOptionMenu(master=frame, values=["Blue", "Dark-blue", "Green"])
        self.theme_color_optionmenu.grid(row=2, column=1, padx=20, pady=(10, 10))

        language_label = customtkinter.CTkLabel(frame, text=self.get_word("Language") + ":")
        language_label.grid(row=1, column=2)
        self.language_option_menu = customtkinter.CTkOptionMenu(master=frame, values=["English", "Polish"])
        self.language_option_menu.grid(row=2, column=2, padx=20, pady=(10, 10))

        apply_button = customtkinter.CTkButton(master=frame, text=self.get_word("Apply"), command=self._apply_settings)
        apply_button.grid(row=3, column=1, padx=20, pady=20)

    def generate_button(self):
        """ Create generate button which run generating PDF file """
        load_button = customtkinter.CTkButton(master=self.master_window, text=self.get_word("Generate"),
                                              command=self._generate_pdf, width=1200)
        load_button.place(relx=0.05, rely=0.9)

    def status_info(self):
        """ Information at the bottom of the GUI that shows you "Done!" info when everything is ok, and PDF file
         is created or shows "No data!" when some data are missed. The default value for this status label is empty."""
        self.status_label = customtkinter.CTkLabel(master=self.master_window, text="",
                                                   font=customtkinter.CTkFont(size=15))
        self.status_label.place(relx=0.49, rely=0.95)

    def signature(self):
        """ Add company name in the right bottom corner """
        msoftware_label = customtkinter.CTkLabel(master=self.master_window, text="MSoftware",
                                                 font=customtkinter.CTkFont(size=10))
        msoftware_label.place(relx=0.96, rely=0.96)

    def _generate_pdf(self):
        """ Command for generate button. It runs generating PDF file and also save the seller and buyer data in
        specific directories. """
        if self.chosen_seller_file_path is None or self.chosen_buyer_file_path is None \
                or self._check_if_empty_data(self._get_necessary_data()) is False:
            self.status_label.configure(text=self.get_word("No data!"), text_color='red')
            return

        self._save_seller_data()
        self._save_buyer_data()
        generate_page(self.chosen_seller_file_path, self.chosen_buyer_file_path, self._get_necessary_data())
        self.status_label.configure(text=self.get_word("Done!"), text_color='green')

    def _get_seller_data(self):
        """ Returning dictionary with all seller data gets from the seller frame """
        return {"Name": self.seller_name.get(), "Address": self.seller_address.get(),
                "Post Code": self.seller_post_code.get(), "NIP": self.seller_nip.get(),
                "Account": self.seller_bank_account_number.get()}

    def _get_buyer_data(self):
        """ Returning dictionary with all buyer data gets from the buyer frame """
        return {"Name": self.buyer_name.get(), "Address": self.buyer_address.get(),
                "Post Code": self.buyer_post_code.get(), "Country": self.buyer_country.get(),
                "NIP": self.buyer_nip.get()}

    def _get_necessary_data(self):
        """ Returning dictionary with all necessary data gets from the data frame """
        return {"Document Number": self.doc_number.get(), "Date of issue": self.issue_date.get(),
                "Date of service": self.service_date.get(), "Date of payment": self.payment_date.get(),
                "Name of service": self.service_name.get(), "Net value": self._get_net_service_value()}

    def _get_net_service_value(self):
        """ Verify value getting from "Net value" slot. If is empty return empty string. """
        try:
            return round(float(self.net_service.get()), 2)
        except:
            self.status_label.configure(text=self.get_word("No data!"), text_color='red')
            return ""

    def _save_seller_data(self):
        """ Save seller data to file in seller directory """
        if self._check_if_empty_data(self._get_seller_data()) is False:
            self.status_label.configure(text=self.get_word("No data!"), text_color='red')
        else:
            file_name = self._prepare_file_name(self._get_seller_data()["Name"], self.seller_file_path)
            with open(file_name, "w") as file:
                for key, value in self._get_seller_data().items():
                    if key == "NIP":
                        value = "NIP: " + value
                    elif key == "Account":
                        value = "Nr rachunku: " + value
                    file.write(value + "\n")

    def _save_buyer_data(self):
        """ Save buyer data to file in buyer directory """
        if self._check_if_empty_data(self._get_buyer_data()) is False:
            self.status_label.configure(text=self.get_word("No data!"), text_color='red')
        else:
            file_name = self._prepare_file_name(self._get_buyer_data()["Name"], self.buyer_file_path)
            with open(file_name, "w") as file:
                for key, value in self._get_buyer_data().items():
                    if key == "NIP":
                        value = "NIP: " + value
                    file.write(value + "\n")

    def _load_seller_data(self):
        """ Load seller data from file in seller directory """
        self.chosen_seller_file_path = self._askopenfile(self.seller_file_path)
        if self.chosen_seller_file_path is None:
            return
        read_data = self._load_file(self.chosen_seller_file_path)
        data_to_write = [self.seller_name_value, self.seller_address_value, self.seller_post_code_value,
                         self.seller_nip_value, self.seller_bank_account_value]

        for count, slot in enumerate(data_to_write):
            slot.set(read_data[count])

    def _load_buyer_data(self):
        """ Load buyer data from file in buyer directory """
        self.chosen_buyer_file_path = self._askopenfile(self.buyer_file_path)
        if self.chosen_buyer_file_path is None:
            return
        read_data = self._load_file(self.chosen_buyer_file_path)
        data_to_write = [self.buyer_name_value, self.buyer_address_value, self.buyer_post_code_value,
                         self.buyer_country_value, self.buyer_nip_value]

        for count, slot in enumerate(data_to_write):
            slot.set(read_data[count])

    def _load_necessary_data(self):
        """ Generate necessary data based on actual date """
        actual_month = datetime.today().month
        actual_year = datetime.today().year
        actual_date = str(datetime.today()).split(" ")[0]
        self.doc_number_value.set(f"FS/1/{actual_month}/{actual_year}")
        self.issue_date_value.set(actual_date)
        self.service_date_value.set(actual_date)
        self.payment_date_value.set(self._calculate_payment_date())
        self.service_name_value.set("Swiadczenie uslug informatycznych")   # TODO: save the last service to default file

    def _apply_settings(self):
        """ Overwrite file with default settings """
        appearance = self.appearance_mode_optionemenu.get().lower()
        theme = self.theme_color_optionmenu.get().lower()
        language = self.language_option_menu.get().lower()

        with open(self.project_path + 'defaults.txt', 'w') as f:
            f.write(f"appearance={appearance}\n"
                    f"language={language}\n"
                    f"theme={theme}")

        self.status_label.configure(text=self.get_word("Restart app to apply the settings"), text_color='yellow')

    def get_word(self, word: str):
        """ Get translated word from language file """
        try:
            return self.read_file(self.languages_file_path + self.language + ".txt")[word]
        except:
            return None

    @staticmethod
    def read_file(file_path: str):
        """ Read file with translation """
        with open(file_path, "r") as f:
            lines = [line.removesuffix('\n') for line in f.readlines()]
            translation = {}

            for line in lines:
                key, value = line.split("=")
                translation[key] = value

        return translation

    @staticmethod
    def _askopenfile(initial_dir: dict):
        """ Open window to select file on your PC """
        try:
            file = filedialog.askopenfile(initialdir=initial_dir)
            file_path = file.name
            return file_path
        except AttributeError as e:
            print(e)

    @staticmethod
    def _load_file(file_path: str):
        """ Read file with seller/buyer data """
        with open(file_path, "r") as file:
            return [line.removeprefix("NIP: ").removeprefix("Nr rachunku: ").removesuffix("\n")
                    for line in file.readlines()]

    @staticmethod
    def _check_if_empty_data(data: dict):
        """ Return False if verifying data is empty or return True if is not """
        if "" in list(data.values()):
            return False
        else:
            return True

    @staticmethod
    def _prepare_file_name(name: str, file_path: str):
        """ Prepare specific format for file name """
        new_name = name.lower()
        new_name = new_name.replace(" ", "_")
        new_name = file_path + new_name + ".txt"
        return new_name

    @staticmethod
    def _change_appearance_mode_event(new_appearance_mode: str):
        """ Change appearance mode """
        customtkinter.set_appearance_mode(new_appearance_mode)

    @staticmethod
    def _calculate_payment_date():
        """ Return calculated payment date in specific format """
        calculated_date = str(datetime.today() + timedelta(days=10))
        date = calculated_date.split(" ")[0]
        year, month, day = date.split("-")
        return f"{year}-{month}-{day}"
