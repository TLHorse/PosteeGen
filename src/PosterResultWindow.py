from tkinter import *
import PosterArrangement

class PosterResultWindow:
    def __init__(self, model: PosterArrangement):
        super().__init__()
        self.model = model
        self.__root = Tk()
        self.__root.geometry('1782x1260+200+100')
        self.__root.minsize(1782, 1260)
        self.__root.maxsize(1782, 1260)
        self.__poster = Canvas(self.__root, bg='white', bd=0, cursor='cross', width=1782, height=1260)

    def __drawTitle(self, board: Canvas, mode: int, text="手抄报", font=("黑体", 100)):
        x, y = 0, 0
        finalText = text
        if mode == 1:
            x = 1782 / 2
            y = 200
        elif mode == 2 or mode == 3:
            x = 200 if mode == 2 else 1782 / 2
            y = 1260 / 2
            finalText_ls = list(finalText)
            for i in range(len(finalText_ls)):
                finalText_ls[i - 1] += '\n' if i != len(finalText_ls) else ''
            finalText = "".join(finalText_ls)
        elif mode == 4:
            x = 1782 / 2
            y = 1260 / 2
        else:
            class InvalidModeException(Exception): pass
            raise InvalidModeException(f"Invalide mode flag of {mode} with a type of {type(mode)}")
        board.create_text(x, y, text=finalText, font=font, fill="black")

    def appear(self):
        self.__root.title = f"手抄报预览 - 请截图来保存手抄报 | {self.model.posterTitle}"
        self.__poster.place(x=0, y=0, anchor=NW)
        self.__drawTitle(
            self.__poster, 
            mode=self.model.template, 
            text=self.model.posterTitle, 
            font=(self.model.posterTitleFont, self.model.posterTitleSize)
        )
        self.__root.mainloop()
