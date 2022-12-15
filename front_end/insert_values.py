from tkinter import Tk, Frame, Label, Entry, X, Button, RAISED, CENTER

class Matrix(Tk):
    def __init__(self, n:int, m:int):
        super().__init__()
        self.n = n
        self.m = m
        self.matrix:list = []


    def get_matrix(self):
        # Construction of the grid for User's input
        for i in range(self.n):
            row = []
            for j in range(self.m):
                frame = Frame(self, relief=RAISED, borderwidth=1)
                frame.grid(row=i, column=j)
                Label(frame, text=f'Enter element at position{i+1}{j+1}').pack(fill=X)
                entry = Entry(frame)
                entry.pack(fill=X)
                row.append(entry)
            self.matrix.append(row)

        # Add a Button to submit the matrix
        Button(self, text='SUBMIT', command=lambda x='':self.submit()).grid(row=self.n+1, column=self.m//2)


    def submit(self):
        # Append User's input values into a matrix
        dummy = []
        for i in range(self.n):
            lista = []
            for j in range(self.m):
                lista.append(self.matrix[i][j].get())
            dummy.append(lista)

        # Transform values in matrix to appropriate type
        for i in range(self.n):
            for k in range(self.m):
                if dummy[i][k] == '' or dummy[i][k] == ' ':
                    dummy[i][k] = 0
                else:
                    dummy[i][k] = float(dummy[i][k])
        self.destroy()




x = Matrix(2,3)
x.get_matrix()
x.mainloop()
