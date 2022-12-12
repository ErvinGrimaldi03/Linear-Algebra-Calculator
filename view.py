import tkinter
from tkinter import Tk
from front_end.insert_values import get_matrix


class View(Tk):

    def __init__(self, h:int=1080, w:int=720, bg_c:str='white', txt_c:str=str, titolo:str='Linear Algebra Calculator'):
        self.h = h
        self.w = w
        self.bg_c = bg_c
        self.txt_c = txt_c
        super().__init__()
        self.geometry(f'{h}x{w}')
        self.title(titolo)




    def select_operation(self):
        self.selection_operation = tkinter.StringVar()
        self.selection_operation.set('SELECT OPERATION')
        self.select_m = tkinter.IntVar()
        self.select_n = tkinter.IntVar()
        operations = ['Matrix Inverse', 'Matrix Transpose', 'Matrix Cross Product', 'Dot Product', 'Unit Vector', 'Echelon Form', 'SVD']
        operations_menu = tkinter.OptionMenu(
            self,
            self.selection_operation,
            *operations
        )
        operations_menu.pack()
        tkinter.Label(self, text='Dimension of matrix (NxM): ').pack()
        n_size = tkinter.Entry(self, textvariable=self.select_n, width=6).pack()
        intemediate = tkinter.Label(self, text='X').pack()
        m_size = tkinter.Entry(self, textvariable=self.select_m, width=6).pack()
        requests = self.select_n, self.select_m, self.selection_operation
        invio = tkinter.Button(self, text='CONFIRM', command=lambda x='' : self.retrive_selection()).pack()


    def retrive_selection(self):
        get_matrix(self.select_n.get(), self.select_m.get())




def run():
    view = View()
    view.select_operation()
    view.mainloop()


if __name__ == '__main__':
    run()
