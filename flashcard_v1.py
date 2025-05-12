import tkinter as tk
from tkinter import messagebox
import random

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        # Define theme colors before any widget uses them
        self.bg_color     = '#1f3b4d'  # Dark blue background
        self.fg_color     = '#ffffff'  # White text
        self.accent_color = '#3a7ca5'  # Accent button color

        # Configure root window
        self.master.title('Top 100 German Flashcards')
        self.master.geometry('450x350')
        self.master.configure(bg=self.bg_color)

        self.words = [
    ('der', 'the (masculine)'), ('die', 'the (feminine/plural)'), ('und', 'and'),
    ('in', 'in'), ('von', 'from, of'), ('zu', 'to, at'), ('das', 'the (neuter)'),
    ('mit', 'with'), ('sich', 'oneself'), ('auf', 'on'), ('für', 'for'), ('ist', 'is'),
    ('nicht', 'not'), ('ein', 'a, an'), ('als', 'as, than, when'), ('auch', 'also, too'),
    ('es', 'it'), ('an', 'at, on'), ('werden', 'to become, will'), ('aus', 'out, from'),
    ('er', 'he'), ('hat', 'has'), ('dass', 'that'), ('sie', 'she, they'), ('nach', 'after, to'),
    ('bei', 'at, by'), ('um', 'around, at (time)'), ('noch', 'still, yet'), ('wie', 'how, like (as)'),
    ('über', 'over, about'), ('so', 'so, thus'), ('nur', 'only'), ('oder', 'or'), ('aber', 'but'),
    ('vor', 'before, in front of'), ('bis', 'until, up to'), ('mehr', 'more'), ('durch', 'through, by'),
    ('man', 'one (impersonal)'), ('Prozent', 'percent'), ('kann', 'can'), ('gegen', 'against'),
    ('schon', 'already'), ('wenn', 'if, when'), ('sein', 'his'), ('Mark', 'currency'), ('ihr', 'her, their'),
    ('dann', 'then'), ('unter', 'under, among'), ('wir', 'we'), ('soll', 'should, ought to'), ('ich', 'I'),
    ('Jahr', 'year'), ('zwei', 'two'), ('diese', 'this, these'), ('wieder', 'again'), ('Uhr', 'clock, time'),
    ('will', 'wants'), ('zwischen', 'between'), ('immer', 'always'), ('Millionen', 'millions'), ('was', 'what'),
    ('sagte', 'said'), ('gibt', 'there is/are'), ('alle', 'all'), ('seit', 'since'), ('muss', 'must, have to'),
    ('doch', 'however, still'), ('jetzt', 'now'), ('drei', 'three'), ('neue', 'new'), ('damit', 'so that'),
    ('bereits', 'already'), ('da', 'there, because'), ('ab', 'from, starting at'), ('ohne', 'without'),
    ('sondern', 'but rather'), ('selbst', 'self, even'), ('ersten', 'first'), ('nun', 'now, well then'),
    ('etwa', 'approximately'), ('heute', 'today'), ('weil', 'because'), ('ihm', 'him'), ('Menschen', 'people'),
    ('Deutschland', 'Germany'), ('anderen', 'other(s)'), ('rund', 'approximately, around'), ('ihn', 'him'),
    ('Ende', 'end'), ('jedoch', 'however'), ('Zeit', 'time'), ('uns', 'us'), ('Stadt', 'city, town'),
    ('geht', 'goes'), ('sehr', 'very'), ('hier', 'here'), ('ganz', 'whole, entirely'), ('Berlin', 'Berlin')
]

        self.known_words = set()
        self.current_word = None
        self.show_translation = False

        # Label for word display
        self.word_label = tk.Label(
            master,
            text='Click Start to begin',
            font=('Helvetica', 24, 'bold'),
            bg=self.bg_color,
            fg=self.fg_color,
            wraplength=400,
            justify='center'
        )
        self.word_label.pack(pady=30)

        # Button frame
        self.button_frame = tk.Frame(master, bg=self.bg_color)
        self.button_frame.pack(pady=20)

        # "I Know This" button
        self.known_button = tk.Button(
            self.button_frame,
            text='I Know This',
            command=self.mark_known,
            bg=self.accent_color,
            fg=self.fg_color,
            font=('Helvetica', 12),
            activebackground='#559bc1',
            relief='flat',
            width=12,
            pady=8
        )
        self.known_button.grid(row=0, column=0, padx=10)

        # "Next" button
        self.next_button = tk.Button(
            self.button_frame,
            text='Next',
            command=self.show_next_word,
            bg=self.accent_color,
            fg=self.fg_color,
            font=('Helvetica', 12),
            activebackground='#559bc1',
            relief='flat',
            width=12,
            pady=8
        )
        self.next_button.grid(row=0, column=1, padx=10)

        # Key binding for space bar to toggle translation
        self.master.bind('<space>', self.toggle_translation)

        self.show_next_word()

    def show_next_word(self):
        remaining = [w for w in self.words if w[0] not in self.known_words]
        if not remaining:
            self.word_label.config(text='All words completed!')
            return
        self.current_word = random.choice(remaining)
        self.show_translation = False
        self.update_display()

    def toggle_translation(self, event=None):
        if not self.current_word:
            return
        self.show_translation = not self.show_translation
        self.update_display()

    def update_display(self):
        if self.show_translation:
            text = f"{self.current_word[0]} – {self.current_word[1]}"
        else:
            text = self.current_word[0]
        self.word_label.config(text=text)

    def mark_known(self):
        if self.current_word:
            self.known_words.add(self.current_word[0])
        self.show_next_word()

if __name__ == '__main__':
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
