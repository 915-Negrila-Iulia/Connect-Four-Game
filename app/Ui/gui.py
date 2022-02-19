
from functools import partial
from tkinter import *
from app.Game.game import ConnectFour
from PIL import ImageTk, Image

class GameGui:
    def __init__(self):
        self._game = ConnectFour()
        self._init_window()
        self._init_images()
        self._list_buttons = []

    def _init_window(self):
        """
        Settings for the game board
        :return: -
        """
        self._window = Tk()
        self._window.title("Connect4")
        self._window.geometry("770x770+10+20")

    def _init_images(self):
        """
        Sets the images needed for the game board
        :return: -
        """
        self._arrow_image = self.resize_image("arrow.png", 110, 110)
        self._empty_move_image = self.resize_image("empty_move.jpg", 110, 110)
        self._yellow_move_image = self.resize_image("yellow_move.png", 110, 110)
        self._red_move_image = self.resize_image("red_move.png", 110, 110)


    def display_board(self):
        """
        Constructs the game board and the buttons used to perform actions
        :return: -
        """
        for i in range(7):
            self._window.columnconfigure(i, weight=1, minsize=75)
            self._window.rowconfigure(i, weight=1, minsize=50)
            for j in range(7):
                frame = Frame(
                    master=self._window,
                    relief=RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j)
                if i == 0:
                    button=Button(master=frame, image=self._arrow_image)
                    self._list_buttons.append(button)
                    button.pack()
                if i != 0:
                    self.labels(frame,i,j)

    def labels(self,frame, i, j):
        """
        Based on the game board and its elements ('x','o','')
        places corresponding labels for each box
        Also function disables buttons if the game is over (if human or computer wins)
        :param frame: game board
        :param i: row of frame
        :param j: column of frame
        :return: -
        """
        if self._game.board.check_win() == 'x':
            label = Label(master=frame, text="HUMAN WINS")
            label.pack()
            self.disable_buttons()
        elif self._game.board.check_win() == 'o':
            label = Label(master=frame, text="COMPUTER WINS")
            label.pack()
            self.disable_buttons()
        if self._game.board.get_board[i - 1][j] == '':
            move = self._empty_move_image
        elif self._game.board.get_board[i - 1][j] == 'x':
            move = self._red_move_image
        elif self._game.board.get_board[i - 1][j] == 'o':
            move = self._yellow_move_image
        label = Label(master=frame, image=move)
        label.pack()
        for j in range(0,7):
            if '' not in self._game.board.get_column(j):
                self._list_buttons[j]['state']='disabled'

    def disable_buttons(self):
        """
        Disables all the buttons on the game board
        :return: -
        """
        for i in range(len(self._list_buttons)):
            self._list_buttons[i]['state'] = 'disabled'

    def function(self,i):
        """
        Performs the user move according to the chosen column and also performs the computer move
        Performing a move means updating the board game by replacing empty boxes with images
        :param i: column given by the user
        :return: -
        """
        self._game.human_move(i)
        for i in range(7):
            self._window.columnconfigure(i, weight=1, minsize=75)
            self._window.rowconfigure(i, weight=1, minsize=50)
            for j in range(7):
                frame = Frame(
                    master=self._window,
                    relief=RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j)
                if i != 0:
                    self.labels(frame,i,j)
        self._game.computer_move()
        for i in range(7):
            self._window.columnconfigure(i, weight=1, minsize=75)
            self._window.rowconfigure(i, weight=1, minsize=50)
            for j in range(7):
                frame = Frame(
                    master=self._window,
                    relief=RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j)
                if i != 0:
                    self.labels(frame,i,j)

    def resize_image(self,path,width,height):
        """
        Changes the initial size of a given image
        :param path: path of the given image
        :param width: new width of the given image
        :param height: new height of the given image
        :return: resized image
        """
        image = Image.open(path)
        resize_image = image.resize((width, height))
        result = ImageTk.PhotoImage(resize_image)
        return result

    def start(self):
        self.display_board()

        for i in range(len(self._list_buttons)):
            self._list_buttons[i]['command'] = partial(self.function, i)

        self._window.mainloop()
