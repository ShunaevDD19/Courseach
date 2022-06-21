from tkinter import *
from window import Window
from GetKeys import get_key
from Dictionaries import option_in, option_out


class Widgets(Window):
    """Класс виджетов интерфейса"""
    def __init__(self):
        super().__init__()
        self.translated = None
        self.text_to_translate = Text(self.window,

                                      width=37,
                                      height=10,
                                      bg='black',
                                      fg='white',
                                      font='Times 15'

                                      )
        self.text_to_translate.place(x=20, y=70)
        self.translated_text = Text(self.window,

                                    width=37,
                                    height=10,
                                    bg='black',
                                    fg='white',
                                    font='Times 15'

                                    )
        self.translated_text.place(x=410, y=70)

        self.clicked_in = StringVar()
        self.clicked_in.set(get_key(option_in, 'auto'))

        self.drop_in = OptionMenu(self.window, self.clicked_in, *option_in)
        self.drop_in['fg'] = 'black'
        self.drop_in['bg'] = 'violet'
        self.drop_in['width'] = 45
        self.drop_in.place(x=20, y=30)

        self.clicked_out = StringVar()
        self.clicked_out.set(get_key(option_in, 'ar'))

        self.drop_out = OptionMenu(self.window, self.clicked_out, *option_out)
        self.drop_out['fg'] = 'black'
        self.drop_out['bg'] = 'yellow'
        self.drop_out['width'] = 45
        self.drop_out.place(x=470, y=30)
