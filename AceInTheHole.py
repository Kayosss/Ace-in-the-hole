import tkinter as tk
RUNNING_COUNT = 0
TRUE_COUNT = 0
DECK_AMOUNT = 4
ace = 4 * DECK_AMOUNT
king = 4 * DECK_AMOUNT
queen = 4 * DECK_AMOUNT
jack = 4 * DECK_AMOUNT
ten = 4 * DECK_AMOUNT
nine = 4 * DECK_AMOUNT
eight = 4 * DECK_AMOUNT
seven = 4 * DECK_AMOUNT
six = 4 * DECK_AMOUNT
five = 4 * DECK_AMOUNT
four = 4 * DECK_AMOUNT
three = 4 * DECK_AMOUNT
two = 4 * DECK_AMOUNT

cards = 52 * DECK_AMOUNT

class GUI():
    def __init__(self, Mainwindow):
        self.Mainwindow = Mainwindow
        MainWindow.title('Ace in the hole')
        MainWindow.geometry("600x600")
        

        
        self.acePerc = tk.StringVar()
        self.acePerc.set("")
        self.kingPerc = tk.StringVar()
        self.kingPerc.set("")
        self.queenPerc = tk.StringVar()
        self.queenPerc.set("")
        self.jackPerc = tk.StringVar()
        self.jackPerc.set("")
        self.tenPerc = tk.StringVar()
        self.tenPerc.set("")
        self.ninePerc = tk.StringVar()
        self.ninePerc.set("")
        self.eightPerc = tk.StringVar()
        self.eightPerc.set("")
        self.sevenPerc = tk.StringVar()
        self.sevenPerc.set("")
        self.sixPerc = tk.StringVar()
        self.sixPerc.set("")
        self.fivePerc = tk.StringVar()
        self.fivePerc.set("")
        self.fourPerc = tk.StringVar()
        self.fourPerc.set("")
        self.threePerc = tk.StringVar()
        self.threePerc.set("")
        self.twoPerc = tk.StringVar()
        self.twoPerc.set("")
        self.highCardPerc = tk.StringVar()
        self.highCardPerc.set("High card % :" + " ")
        self.lowCardPerc = tk.StringVar()
        self.lowCardPerc.set("Low card % :" + " ")
        self.midCardPerc = tk.StringVar()
        self.midCardPerc.set("Mid card % :" + " ")

        self.Rcount = tk.StringVar()
        self.Rcount.set("Running count:" + " " + str(RUNNING_COUNT))
        self.Tcount = tk.StringVar()
        self.Tcount.set("True count:" + " " + str(TRUE_COUNT))
        ace_button = tk.Button(MainWindow, text = 'A', width=5, height=5, command= lambda: [self.update_running_count("A"), self.update_true_count(), self.card_percentage("A")])
        ace_button.grid(row=0 , column= 0, padx=(5,10), pady=20)
        king_button = tk.Button(MainWindow, text = 'K', width = 5, height = 5, command= lambda: [self.update_running_count("K"), self.update_true_count(), self.card_percentage("K")])
        king_button.grid(row =0, column= 1, padx=10)
        Queen_button = tk.Button(MainWindow, text = 'Q', width=5, height=5, command= lambda: [self.update_running_count("Q"), self.update_true_count(), self.card_percentage("Q")])
        Queen_button.grid(row =0, column= 2, padx=10)
        Jack_button = tk.Button(MainWindow, text = 'J', width=5, height=5, command= lambda: [self.update_running_count("J"),self.update_true_count(), self.card_percentage("J")])
        Jack_button.grid(row=0, column= 3, padx=10)
        Ten_button = tk.Button(MainWindow, text = '10', width=5, height=5, command= lambda: [self.update_running_count("10"), self.update_true_count(), self.card_percentage("10")])
        Ten_button.grid(row=0, column= 4, padx=10)
        Nine_button = tk.Button(MainWindow, text = '9', width=5, height=5, command= lambda: [self.update_true_count(), self.card_percentage("9")])
        Nine_button.grid(row=1, column=0, padx=(5,10))
        Eight_button = tk.Button(MainWindow, text = '8', width=5, height=5, command= lambda: [self.update_true_count(), self.card_percentage("8")])
        Eight_button.grid(row=1, column=1, padx=10)
        Seven_button = tk.Button(MainWindow, text = '7', width=5, height=5, command= lambda: [self.update_true_count(), self.card_percentage("7")])
        Seven_button.grid(row=1, column=2, padx=10, pady=20)
        Six_button = tk.Button(MainWindow, text = '6', width=5, height=5, command= lambda: [self.update_running_count("6"),self.update_true_count(), self.card_percentage("6")])
        Six_button.grid(row=2, column=0, padx=(5,10)) 
        Five_button = tk.Button(MainWindow, text = '5', width=5, height=5, command= lambda: [self.update_running_count("5"),self.update_true_count(), self.card_percentage("5")])
        Five_button.grid(row=2, column=1, padx=10)
        Four_button = tk.Button(MainWindow, text = '4', width=5, height=5, command= lambda: [self.update_running_count("4"), self.update_true_count(), self.card_percentage("4")])
        Four_button.grid(row=2, column=2, padx=10)
        Three_button = tk.Button(MainWindow, text = '3', width=5, height=5, command= lambda: [self.update_running_count("3"), self.update_true_count(), self.card_percentage("3")])
        Three_button.grid(row=2, column=3, padx=10)
        Two_button = tk.Button(MainWindow, text = '2', width=5, height=5, command= lambda: [self.update_running_count("2"), self.update_true_count(), self.card_percentage("2")])
        Two_button.grid(row=2, column=4, padx=10 , pady=20)

        True_count_label = tk.Label(MainWindow, textvariable= self.Tcount)
        True_count_label.grid(column=5, columnspan=2, row=0, padx=(100, 0))
        Running_count_label = tk.Label(MainWindow, textvariable= self.Rcount)
        Running_count_label.grid(column=5, columnspan=2, row=1, padx=(100,0))

        self.ace_percentage_label = tk.Label(MainWindow, textvariable= self.acePerc)
        self.ace_percentage_label.grid(row=0, column=0, columnspan=1, pady=(110,0), padx=(0,10))
        self.king_percentage_label = tk.Label(MainWindow, textvariable= self.kingPerc)
        self.king_percentage_label.grid(row=0, column= 1, columnspan=1, pady=(110,0), padx=(0,10))
        self.queen_percentage_label = tk.Label(MainWindow, textvariable= self.queenPerc)
        self.queen_percentage_label.grid(row=0, column= 2, columnspan=1, pady=(110,0), padx=(0,10))
        self.jack_percentage_label = tk.Label(MainWindow, textvariable= self.jackPerc)
        self.jack_percentage_label.grid(row=0, column=3, columnspan=1, pady=(110,0), padx=(0,10))
        self.ten_percentage_label = tk.Label(MainWindow, textvariable= self.tenPerc)
        self.ten_percentage_label.grid(row = 0, column = 4, columnspan=1, pady=(110,0), padx=(0,10))
        self.nine_percentage_label = tk.Label(MainWindow, textvariable= self.ninePerc)
        self.nine_percentage_label.grid(row= 1, column= 0, columnspan=1, pady=(110, 0), padx=(0,10))
        self.eight_percentage_label = tk.Label(MainWindow, textvariable= self.eightPerc)
        self.eight_percentage_label.grid(row= 1, column= 1, columnspan=1, pady=(110,0), padx=(0,10))
        self.seven_percentage_label = tk.Label(MainWindow, textvariable= self.sevenPerc)
        self.seven_percentage_label.grid(row= 1, column= 2, columnspan=1, pady=(110,0), padx=(0, 10))
        self.six_percentage_label = tk.Label(MainWindow, textvariable= self.sixPerc)
        self.six_percentage_label.grid(row= 2, column= 0, columnspan=1, pady=(110, 0), padx=(0, 10))
        self.five_percentage_label = tk.Label(MainWindow, textvariable= self.fivePerc)
        self.five_percentage_label.grid(row= 2, column=1, columnspan=1, pady=(110, 0), padx=(0 ,10))
        self.four_percentage_label = tk.Label(MainWindow, textvariable= self.fourPerc)
        self.four_percentage_label.grid(row= 2, column=2, columnspan=1, pady=(110, 0), padx=(0, 10))
        self.three_percentage_label = tk.Label(MainWindow, textvariable= self.threePerc)
        self.three_percentage_label.grid(row=2, column=3, columnspan=1, pady=(110, 0), padx=(0, 10))
        self.two_percentage_label = tk.Label(MainWindow, textvariable= self.twoPerc)
        self.two_percentage_label.grid(row=2, column= 4, columnspan=1, pady=(110, 0), padx=(0 ,10))

        self.high_percentage_label = tk.Label(MainWindow, textvariable= self.highCardPerc)
        self.high_percentage_label.grid(column=5, columnspan=2, row=2, padx=(100,0))
        self.low_percentage_label = tk.Label(MainWindow, textvariable= self.lowCardPerc)
        self.low_percentage_label.grid(column= 5, columnspan=2, row=5, padx=(100,0), pady=(40,0))
        self.mid_percentage_label = tk.Label(Mainwindow, textvariable= self.midCardPerc)
        self.mid_percentage_label.grid(column=5, columnspan=2, row=4, padx=(100,0), pady=(0,10))


        self.text = tk.StringVar()
        self.text.set("Set number of decks")
        Number_of_decks_label = tk.Label(MainWindow, textvariable= self.text)
        Number_of_decks_label.grid(column=0, columnspan=3, row=5, padx=5, pady=(20,0), sticky="W")
        

        Four_deck_button = tk.Button(MainWindow, text = '4', width=5, height=5, command= lambda: [self.set_deck_amount(4), self.card_percentage("")])
        Four_deck_button.grid(column=0, row=6, padx=5)
        Six_deck_button = tk.Button(MainWindow, text = '6', width=5, height=5, command= lambda: [self.set_deck_amount(6), self.card_percentage("")])
        Six_deck_button.grid(column=1, row=6, padx=5)
        Eight_deck_button = tk.Button(MainWindow, text = '8', width=5, height=5, command= lambda: [self.set_deck_amount(8), self.card_percentage("")])
        Eight_deck_button.grid(column=2, row=6, padx=5)

    def set_deck_amount(self,decks):
        global DECK_AMOUNT
        DECK_AMOUNT = decks
        self.text.set("Number of decks set to" + " " + str(DECK_AMOUNT))
        global cards 
        cards = 52 * DECK_AMOUNT
        global ace
        global king
        global queen
        global jack
        global ten
        global nine 
        global eight
        global seven 
        global six
        global five 
        global four 
        global three 
        global two 

        ace = 4 * DECK_AMOUNT
        king = 4 * DECK_AMOUNT
        queen = 4 * DECK_AMOUNT
        jack = 4 * DECK_AMOUNT
        ten = 4 * DECK_AMOUNT
        nine = 4 * DECK_AMOUNT
        eight = 4 * DECK_AMOUNT
        seven = 4 * DECK_AMOUNT
        six = 4 * DECK_AMOUNT
        five = 4 * DECK_AMOUNT
        four = 4 * DECK_AMOUNT
        three = 4 * DECK_AMOUNT
        two = 4 * DECK_AMOUNT

    def card_percentage(self, card):
        global ace
        global king
        global queen
        global jack
        global ten
        global nine 
        global eight
        global seven 
        global six
        global five 
        global four 
        global three 
        global two
        global cards 
        cards-=1
        if card == 'A':
            ace-= 1
        if card == 'K':
            king-= 1
        if card == 'Q':
            queen-= 1
        if card == 'J':
            jack-= 1
        if card == '10':
            ten-= 1
        if card == '9':
            nine-= 1
        if card == '8': 
            eight-= 1
        if card == '7': 
            seven-=1
        if card == '6':
            six-=1
        if card == '5':
            five-=1
        if card == '4':
            four-=1
        if card == '3':
            three-=1 
        if card == '2':
            two-=1
        if card == "":
            self.update_running_count("")
            self.update_true_count()
        
        aceP = ace/(cards)
        kingP = king/(cards)
        queenP = queen/(cards)
        jackP = jack/(cards)
        tenP = ten/(cards)
        nineP = nine/(cards)
        eightP = eight/(cards)
        sevenP = seven/(cards)
        sixP = six/(cards)
        fiveP = five/(cards)
        fourP = four/(cards)
        threeP = three/(cards)
        twoP = two/(cards)

        self.acePerc.set(str(round(aceP * 100, 4)) + "%")
        self.kingPerc.set(str(round(kingP * 100, 4)) + "%")
        self.queenPerc.set(str(round(queenP * 100, 4)) + "%")
        self.jackPerc.set(str(round(jackP * 100, 4)) + "%")
        self.tenPerc.set(str(round(tenP * 100, 4)) + "%")
        self.ninePerc.set(str(round(nineP * 100, 4)) + "%")
        self.eightPerc.set(str(round(eightP * 100, 4)) + "%")
        self.sevenPerc.set(str(round(sevenP * 100, 4)) + "%")
        self.sixPerc.set(str(round(sixP * 100, 4)) + "%")
        self.fivePerc.set(str(round(fiveP * 100, 4)) + "%")
        self.fourPerc.set(str(round(fourP * 100, 4)) + "%")
        self.threePerc.set(str(round(threeP * 100, 4)) + "%")
        self.twoPerc.set(str(round(twoP * 100, 4)) + "%")
        self.highCardPerc.set("High card % :" + " " + str(round((aceP + kingP + queenP + jackP + tenP) * 100, 4)) + "%")
        self.midCardPerc.set("Mid card % :" + " " + str(round((nineP + eightP + sevenP) * 100, 4)) + "%")
        self.lowCardPerc.set("Low card % :" + " " +str(round((sixP + fiveP + fourP + threeP + twoP) * 100, 4)) + "%")
        self.perc_colour()
    
    def perc_colour(self):

        if float(str(self.lowCardPerc.get())[13:-1]) > 40:
            self.low_percentage_label.config(fg= "light green")
        elif float(str(self.lowCardPerc.get())[13:-1]) < 30:
            self.low_percentage_label.config(fg= "red")
        else:
            self.low_percentage_label.config(fg = "orange")

        if float(str(self.midCardPerc.get())[13:-1]) > 26:
            self.mid_percentage_label.config(fg = "light green")
        elif float(str(self.midCardPerc.get())[13:-1]) < 19:
            self.mid_percentage_label.config(fg= "red")
        else:
            self.mid_percentage_label.config(fg= "orange")

        if float(str(self.highCardPerc.get())[14:-1]) > 40:
            self.high_percentage_label.config(fg= "light green")
        elif float(str(self.highCardPerc.get())[14:-1]) < 30:
            self.high_percentage_label.config(fg = "red")
        else: 
            self.high_percentage_label.config(fg = "orange")

        if float(str(self.acePerc.get())[:-1]) > 8:
            self.ace_percentage_label.config(fg= "light green")
        elif float(str(self.acePerc.get())[:-1]) < 6.2:
            self.ace_percentage_label.config(fg= "red")
        else:
            self.ace_percentage_label.config(fg= "orange")

        if float(str(self.kingPerc.get())[:-1]) > 8:
            self.king_percentage_label.config(fg= "light green")
        elif float(str(self.kingPerc.get())[:-1]) < 6.2:
            self.king_percentage_label.config(fg= "red")
        else:
            self.king_percentage_label.config(fg= "orange")
        
        if float(str(self.queenPerc.get())[:-1]) > 8:
            self.queen_percentage_label.config(fg= "light green")
        elif float(str(self.queenPerc.get())[:-1]) < 6.2:
            self.queen_percentage_label.config(fg= "red")
        else:
            self.queen_percentage_label.config(fg= "orange")
        
        if float(str(self.jackPerc.get())[:-1]) > 8:
            self.jack_percentage_label.config(fg= "light green")
        elif float(str(self.jackPerc.get())[:-1]) < 6.2:
            self.jack_percentage_label.config(fg= "red")
        else:
            self.jack_percentage_label.config(fg= "orange")

        if float(str(self.tenPerc.get())[:-1]) > 8:
            self.ten_percentage_label.config(fg= "light green")
        elif float(str(self.tenPerc.get())[:-1]) < 6.2:
            self.ten_percentage_label.config(fg= "red")
        else:
            self.ten_percentage_label.config(fg= "orange")

        if float(str(self.ninePerc.get())[:-1]) > 8:
            self.nine_percentage_label.config(fg= "light green")
        elif float(str(self.ninePerc.get())[:-1]) < 6.2:
            self.nine_percentage_label.config(fg= "red")
        else:
            self.nine_percentage_label.config(fg= "orange")
        
        if float(str(self.eightPerc.get())[:-1]) > 8:
            self.eight_percentage_label.config(fg= "light green")
        elif float(str(self.eightPerc.get())[:-1]) < 6.2:
            self.eight_percentage_label.config(fg= "red")
        else:
            self.eight_percentage_label.config(fg= "orange")
        
        if float(str(self.sevenPerc.get())[:-1]) > 8:
            self.seven_percentage_label.config(fg= "light green")
        elif float(str(self.sevenPerc.get())[:-1]) < 6.2:
            self.seven_percentage_label.config(fg= "red")
        else:
            self.seven_percentage_label.config(fg= "orange")
        
        if float(str(self.sixPerc.get())[:-1]) > 8:
            self.six_percentage_label.config(fg= "light green")
        elif float(str(self.sixPerc.get())[:-1]) < 6.2:
            self.six_percentage_label.config(fg= "red")
        else:
            self.six_percentage_label.config(fg= "orange")
        
        if float(str(self.fivePerc.get())[:-1]) > 8:
            self.five_percentage_label.config(fg= "light green")
        elif float(str(self.fivePerc.get())[:-1]) < 6.2:
            self.five_percentage_label.config(fg= "red")
        else:
            self.five_percentage_label.config(fg= "orange")
        
        if float(str(self.fourPerc.get())[:-1]) > 8:
            self.four_percentage_label.config(fg= "light green")
        elif float(str(self.fourPerc.get())[:-1]) < 6.2:
            self.four_percentage_label.config(fg= "red")
        else:
            self.four_percentage_label.config(fg= "orange")
        
        if float(str(self.threePerc.get())[:-1]) > 8:
            self.three_percentage_label.config(fg= "light green")
        elif float(str(self.threePerc.get())[:-1]) < 6.2:
            self.three_percentage_label.config(fg= "red")
        else:
            self.three_percentage_label.config(fg= "orange")
        
        if float(str(self.twoPerc.get())[:-1]) > 8:
            self.two_percentage_label.config(fg= "light green")
        elif float(str(self.twoPerc.get())[:-1]) < 6.2:
            self.two_percentage_label.config(fg= "red")
        else:
            self.two_percentage_label.config(fg= "orange")

    def update_running_count(self,card):
        global RUNNING_COUNT
        if card == '2' or card == '3' or card =='4' or card =='5' or card =='6':
            RUNNING_COUNT+=1
        elif card == '10' or card =='J' or card=='Q' or card=='K' or card=='A':
            RUNNING_COUNT = RUNNING_COUNT - 1
        elif card == "":
            RUNNING_COUNT = 0
        else:
            pass
        self.Rcount.set("Running count:" + " " + str(RUNNING_COUNT))

    def update_true_count(self):
        global TRUE_COUNT
        TRUE_COUNT = RUNNING_COUNT/DECK_AMOUNT
        self.Tcount.set("True count:" + " " + str(round(TRUE_COUNT, 4)))

if __name__ == '__main__':
    MainWindow = tk.Tk()
    gui=GUI(MainWindow)
    MainWindow.mainloop()
