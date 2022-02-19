
from app.Ui.console import Console
from app.Ui.gui import GameGui

if __name__ == '__main__':
    console = Console()
    gui = GameGui()

    ui = input("choose between console ui and gui [console/gui]: ")
    if ui == 'console':
        console.start()
    elif ui == 'gui':
        gui.start()
    else:
        print("ops.. wrong command!")
