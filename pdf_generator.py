from fpdf import FPDF
import os


class PDF(FPDF):
    font = 'Times'

    def header(self):
        """ Create header """
        self.set_font(self.font, 'B', 12)
        self.cell(0, 10, 'Sprzedawca:', ln=1, align='R')

    def footer(self):
        """ Create footer with page number """
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Strona {self.page_no()}/{{nb}}', align='C')

    def seller_data(self, file_path: str):
        """ Load seller all data """
        with open(file_path, 'r') as fh:
            txt = fh.read()
        self.set_font(self.font, '', 11)
        self.multi_cell(0, 5, txt, align="R")
        self.ln(20)

    def buyer_data(self, file_path: str):
        """ Load buyer all data """
        self.set_font(self.font, 'B', 12)
        self.cell(0, 10, 'Nabywca:')
        self.ln()
        with open(file_path, "r") as f:
            txt = f.read()
        self.set_font(self.font, '', 11)
        self.multi_cell(0, 5, txt)
        self.ln(10)

    def vat_frame(self, necessary_data: dict):
        """ Create frame with document number, date of issue and date of service """
        doc_number = necessary_data["Document Number"]
        issue_date = necessary_data["Date of issue"]
        service_date = necessary_data["Date of service"]

        self.line(10, 60, 200, 60)
        self.set_font('helvetica', '', 26)
        self.ln(3)
        self.cell(0, 10, "FAKTURA VAT", align="L")
        self.set_font('helvetica', '', 11)
        self.ln(-3)
        self.cell(0, 5, f"Numer dokumentu: {doc_number}", ln=1, align="R")
        self.set_font(self.font, '', 9)
        self.cell(0, 5, f"Data wystawienia: {issue_date}", ln=1, align="R")
        self.cell(0, 5, f"Data dostawy/wykonania uslugi: {service_date}", ln=1, align="R")
        self.ln(15)
        self.line(10, 85, 200, 85)

    def service(self, necessary_data: dict):
        """ Create section with service and costs """
        net_value = necessary_data["Net value"]
        name_of_service = necessary_data["Name of service"]

        self.line(10, 140, 200, 140)
        service_table = ["Lp.", "Nazwa towaru/uslugi", "Ilosc", "j.m.", "Cena netto", "VAT", "Wartosc netto"]
        service_value = ['1', name_of_service, '1,0000', "szt.", str(net_value), "23%", str(net_value)]
        self.set_font(self.font, 'B', 10)
        self.cell(10, 5, service_table[0])
        self.cell(90, 5, service_table[1])
        self.cell(15, 5, service_table[2])
        self.cell(15, 5, service_table[3])
        self.cell(20, 5, service_table[4])
        self.cell(15, 5, service_table[5])
        self.cell(15, 5, service_table[6])
        self.ln(5)

        self.set_font(self.font, '', 10)
        self.cell(10, 5, service_value[0])
        self.cell(89, 5, service_value[1])
        self.cell(16, 5, service_value[2])
        self.cell(16, 5, service_value[3])
        self.cell(20, 5, service_value[4])
        self.cell(17, 5, service_value[5])
        self.cell(15, 5, service_value[6])
        self.ln(5)

        self.ln(10)
        self.line(10, 150, 200, 150)

    def payments(self, necessary_data: dict):
        """ Create section with all costs """
        net_value = necessary_data["Net value"]
        gross_amount, vat = self.calculate_gross_amount(net_value)
        payment_date = necessary_data["Date of payment"]

        payments_table = ["Forma platnosci", "Termin platnosci", "Kwota do zaplaty", "VAT", "Wartosc netto",
                          "Kwota VAT", "Wartosc brutto"]
        payments_values = ["", "Przelew", str(payment_date), str(gross_amount), "W tym:", "23%", str(net_value),
                           str(vat), str(gross_amount)]
        summary_values = ["", "Suma:", str(net_value), str(vat), str(gross_amount)]

        self.set_font(self.font, 'B', 10)
        self.cell(30, 5, payments_table[0])
        self.cell(30, 5, payments_table[1])
        self.cell(45, 5, payments_table[2])
        self.cell(10, 5, payments_table[3])
        self.cell(30, 5, payments_table[4])
        self.cell(25, 5, payments_table[5])
        self.cell(25, 5, payments_table[6])

        self.line(10, 165, 97, 165)
        self.line(104, 165, 205, 165)

        self.ln(5)

        self.set_font(self.font, '', 10)
        self.cell(7, 5, payments_values[0])
        self.cell(27, 5, payments_values[1])
        self.cell(30, 5, payments_values[2])
        self.cell(29, 5, payments_values[3])
        self.cell(13, 5, payments_values[4])
        self.cell(12, 5, payments_values[5])
        self.cell(30, 5, payments_values[6])
        self.cell(25, 5, payments_values[7])
        self.cell(25, 5, payments_values[8])

        self.ln(5)

        self.set_font(self.font, 'B', 10)
        self.cell(93, 5, summary_values[0])
        self.cell(25, 5, summary_values[1])
        self.cell(30, 5, summary_values[2])
        self.cell(25, 5, summary_values[3])
        self.cell(10, 5, summary_values[4])

        self.ln(20)

    def summary(self, necessary_data: dict):
        """ Create summary section """
        net_value = necessary_data["Net value"]
        gross_amount, vat = self.calculate_gross_amount(net_value)

        self.set_font(self.font, '', 18)
        self.cell(0, 5, f"Razem do zaplaty: {gross_amount}", align="R")
        self.ln(5)
        self.set_font(self.font, '', 11)
        self.cell(0, 5, "Zaplacono: 0,00 PLN", align="L")
        self.cell(0, 5, f"Pozostaje do zaplaty: {gross_amount}", align="R")
        self.line(10, 202, 200, 202)
        self.ln(30)

    def signatures(self):
        """ Create places for signatures """
        self.line(10, 225, 83, 225)
        self.line(95, 225, 120, 225)
        self.line(131, 225, 200, 225)
        self.set_font(self.font, "", 10)
        self.cell(87, 5, "Podpis osoby uprawnionej do wystawienia faktury")
        self.cell(0, 5, "Data odbioru")
        self.cell(0, 5, "Podpis osoby upowaznionej do odbioru faktury", align="R")

    @staticmethod
    def calculate_gross_amount(net_value: int):
        """ Calculate the gross amount and vat """
        vat = net_value * 0.23
        gross_amount = round(net_value + vat, 2)
        return gross_amount, vat


def generate_page(seller_file_path: str, buyer_file_path: str, necessary_data: dict):
    """ Generate the PDF file on the desktop """
    pdf = PDF('P', 'mm')

    # get total page numbers
    pdf.alias_nb_pages()

    # Set auto page break
    pdf.set_auto_page_break(auto=True, margin=15)

    # Add Page
    pdf.add_page()

    pdf.seller_data(seller_file_path)
    pdf.vat_frame(necessary_data)
    pdf.buyer_data(buyer_file_path)
    pdf.service(necessary_data)
    pdf.payments(necessary_data)
    pdf.summary(necessary_data)
    pdf.signatures()

    desktop_path = os.path.join(os.environ["HOMEPATH"]) + "/Desktop/"
    file_name = necessary_data["Document Number"].replace("/", "-") + '.pdf'
    pdf.output(desktop_path + file_name)
