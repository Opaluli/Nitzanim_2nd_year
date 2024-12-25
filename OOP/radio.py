import webbrowser
class radio:

    def __init__(self, color, manufacture_year, serial_number, company):
        self.color = color
        self.manufacture_year = manufacture_year
        self.serial_number = serial_number
        self.company = company

    def playmusic(self):
        url = "https://www.youtube.com/watch?v=Vmm_Kq1EN8k"
        webbrowser.open_new(url)

    def print_music(self):
        print("we bring the BOOM!!!")