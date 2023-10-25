from tkinter import*


# **Exercício 1: Janela Simples**

# Crie uma janela simples com o Tkinter que exiba o texto "Olá, Tkinter!" 
#no centro da janela.


janela =  Tk()
janela.geometry('600x600+720+300')
lb  =  Label(janela, text='Olá, Tkinter!')
lb.place(x=250, y=250)
janela['bg'] = 'blue' 


janela.mainloop()
print('JANela')



# **Exercício 2: Janela Simples**

# Crie uma janela simples com o Tkinter que exiba o texto seu 
# nome no centro 
#da janela



from tkinter import *

janela = Tk()
janela.title('Janela')
janela.geometry('400x200+750+450')
lb  = Label(janela, text = 'Nome', )
lb.place(x = 180, y=90)

janela.mainloop()
