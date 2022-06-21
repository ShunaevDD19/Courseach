from tkinter import *
from widgets import Widgets
from deep_translator import GoogleTranslator
from gtts import gTTS
from os import getcwd
from os import startfile
from Dictionaries import option_in, option_out


class WidgetsWithBinds(Widgets):
    """Класс кнопок и их реализация."""
    def __init__(self):
        super().__init__()

        self.submit = Button(self.window,

                             width=15,
                             height=1,
                             bg='white',
                             fg='black',
                             font='Times 13',
                             text='submit',
                             command=self.button_bind

                             )
        self.submit.place(relx=0.5, y=325, anchor=CENTER)

        self.voice_out = Button(self.window,

                                width=5,
                                height=1,
                                bg='yellow',
                                fg='black',
                                font='Times 14',
                                text='🔊',
                                command=self.bind_voice_out

                                )
        self.voice_out.place(x=485, y=309)

        self.switch = Button(self.window,

                             width=10,
                             height=1,
                             bg='white',
                             fg='black',
                             font='Times 13',
                             text='⇆',
                             command=self.switch

                             )
        self.switch.place(x=352, y=30)

        self.voice_in = Button(self.window,

                               width=5,
                               height=1,
                               bg='violet',
                               fg='black',
                               font='Times 14',
                               text='🔊',
                               command=self.bind_voice_in

                               )
        self.voice_in.place(x=260, y=309)

    def switch(self):
        """Функция, которая меняет местами выбранные языки и текста местами."""

        temp_switch_1 = self.clicked_out.get()
        temp_switch_2 = self.clicked_in.get()

        self.clicked_in.set(temp_switch_1)
        self.clicked_out.set(temp_switch_2)

        temp_switch_1, temp_switch_2 = temp_switch_2, temp_switch_1

        temp_word_1 = self.text_to_translate.get('1.0', END).replace('\n', "")
        temp_word_2 = self.translated_text.get('1.0', END).replace('\n', "")

        self.text_to_translate.delete('1.0', END)
        self.translated_text.delete('1.0', END)

        self.text_to_translate.insert('1.0', temp_word_2)
        self.translated_text.insert('1.0', temp_word_1)

    def button_bind(self):
        """Функция, которая переводит текст в соответствии с выбраными пользователем языками."""
        self.text_to_translate.get('1.0', END)
        self.translated = GoogleTranslator(

            source=self.clicked_in.get(),
            target=self.clicked_out.get()).translate(self.text_to_translate.get('1.0', END))

        self.translated_text.delete('1.0', END)
        self.translated_text.insert('1.0', self.translated)

    def bind_voice_in(self):
        """Функция, которая преобразует введённый пользователем текст в mp3 файл, после чего при помощи OS запускает."""
        try:

            text = self.text_to_translate.get('1.0', END).replace('\n', "")
            language = option_in.get(self.clicked_in.get())

            tts = gTTS(text=text, lang=language)
            tts.save("voice.mp3")

            startfile(f'{getcwd()}' + r'\voice.mp3')

        except Exception:
            pass

    def bind_voice_out(self):
        """Функция, которая преобразует переведённый текст в mp3 файл, после чего при помощи OS запускает его."""
        try:

            text = self.translated_text.get('1.0', END).replace('\n', "")
            language = option_out.get(self.clicked_out.get())

            tts = gTTS(text=text, lang=language)
            tts.save("voice_out.mp3")

            startfile(f'{getcwd()}' + r'\voice_out.mp3')

        except Exception:
            pass
