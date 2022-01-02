from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox,filedialog
import subprocess

class Vs_code:
    def __init__(self,root):
        self.root=root
        self.root.title('VS Code Editor')
        self.root.geometry('1350x700+0+0')
        self.path_name=''
        self.color_theme=StringVar()
        self.color_theme.set('Light Default')
        self.font_size=18

        ############## Menu Icons ################
        # file icons
        fileImg1=Image.open('images/folder.png')
        fileImg1=fileImg1.resize((20,20),Image.ANTIALIAS)
        self.new_file_icons=ImageTk.PhotoImage(fileImg1)

        fileImg2=Image.open('images/file.png')
        fileImg2=fileImg2.resize((20,20),Image.ANTIALIAS)
        self.open_file_icon=ImageTk.PhotoImage(fileImg2)

        fileImg3=Image.open('images/save.png')
        fileImg3=fileImg3.resize((20,20),Image.ANTIALIAS)
        self.save_icon=ImageTk.PhotoImage(fileImg3)

        fileImg4=Image.open('images/save as.png')
        fileImg4=fileImg4.resize((20,20),Image.ANTIALIAS)
        self.save_as_icon=ImageTk.PhotoImage(fileImg4)

        fileImg5=Image.open('images/exit.png')
        fileImg5=fileImg5.resize((20,20),Image.ANTIALIAS)
        self.exit_icon=ImageTk.PhotoImage(fileImg5)

        # theme icons
        fileImg6=Image.open('images/white.png')
        fileImg6=fileImg6.resize((20,20),Image.ANTIALIAS)
        self.default_bg=ImageTk.PhotoImage(fileImg6)

        fileImg7=Image.open('images/light default.png')
        fileImg7=fileImg7.resize((20,20),Image.ANTIALIAS)
        self.light_plus_bg=ImageTk.PhotoImage(fileImg7)

        fileImg8=Image.open('images/black.jfif')
        fileImg8=fileImg8.resize((20,20),Image.ANTIALIAS)
        self.dark_bg=ImageTk.PhotoImage(fileImg8)

        fileImg9=Image.open('images/pink.png')
        fileImg9=fileImg9.resize((20,20),Image.ANTIALIAS)
        self.pink_bg=ImageTk.PhotoImage(fileImg9)

        fileImg10=Image.open('images/monokai.png')
        fileImg10=fileImg10.resize((20,20),Image.ANTIALIAS)
        self.monokai_bg=ImageTk.PhotoImage(fileImg10)

        fileImg11=Image.open('images/blue.jpg')
        fileImg11=fileImg11.resize((20,20),Image.ANTIALIAS)
        self.blue_bg=ImageTk.PhotoImage(fileImg11)

        # img3=Image.open('images')



        ############## Menus ################
        myMenu=Menu(self.root)
        fileMenu=Menu(myMenu,tearoff=False)
        fileMenu.add_command(label='New File ',image=self.new_file_icons,compound=LEFT,accelerator='Ctl+N',command=self.new_file)
        fileMenu.add_command(label='Open File ',compound=LEFT,image=self.open_file_icon,accelerator='Ctl+O',command=self.open_file)
        fileMenu.add_command(label='Save ',compound=LEFT,image=self.save_icon,accelerator='Ctl+S',command=self.save_file)
        fileMenu.add_command(label='Save As ',compound=LEFT,image=self.save_as_icon,accelerator='Ctl+Alt+S',command=self.save_as_file)
        fileMenu.add_command(label='Exit',compound=LEFT,image=self.exit_icon,accelerator='Ctl+Q',command=self.exit_func)

        color_theme=Menu(myMenu,tearoff=False)
        color_theme.add_radiobutton(label='Light Default ',value='Light Default',image=self.default_bg,variable=self.color_theme,compound=LEFT,command=self.color_change)
        color_theme.add_radiobutton(label='Light Plus ',value='Light Plus',image=self.light_plus_bg,variable=self.color_theme,compound=LEFT,command=self.color_change)
        color_theme.add_radiobutton(label='Dark ',value='Dark',image=self.dark_bg,variable=self.color_theme,compound=LEFT,command=self.color_change)
        color_theme.add_radiobutton(label='Red ',value='Red',image=self.pink_bg,variable=self.color_theme,compound=LEFT,command=self.color_change)
        color_theme.add_radiobutton(label='Monokai ',value='Monokai',image=self.monokai_bg,variable=self.color_theme,compound=LEFT,command=self.color_change)
        color_theme.add_radiobutton(label='Night Blue',value='Night Blue',image=self.blue_bg,variable=self.color_theme,compound=LEFT,command=self.color_change)


        myMenu.add_cascade(label='File',menu=fileMenu)
        myMenu.add_cascade(label='Color Theme',menu=color_theme)
        myMenu.add_command(label='Clear',command=self.clear_all)
        myMenu.add_command(label='Run',command=self.run)

        self.root.config(menu=myMenu)


        ############## Editor Frame ################
        editorFrame=Frame(self.root,bg='white')
        editorFrame.place(x=0,y=0,relwidth=1,height=500)
        scrollY=Scrollbar(editorFrame,orient=VERTICAL)
        scrollY.pack(side=RIGHT,fill=Y)
        self.txt_editor=Text(editorFrame,bg='white',font=('times new roman',self.font_size),yscrollcommand=scrollY.set)
        self.txt_editor.pack(fill=BOTH,expand=1)
        scrollY.config(command=self.txt_editor.yview)


        ############## Output Frame ################
        self.font_size = 18
        outputFrame = Frame(self.root, bg='white')
        outputFrame.place(x=0, y=500, relwidth=1, height=200)
        scrollY = Scrollbar(outputFrame, orient=VERTICAL)
        scrollY.pack(side=RIGHT, fill=Y)
        self.txt_output = Text(outputFrame, bg='white', font=('times new roman', 18),
                               yscrollcommand=scrollY.set)
        self.txt_output.pack(fill=BOTH, expand=1)
        scrollY.config(command=self.txt_output.yview)

        ############## All Shortcuts ################
        self.root.bind('<Control-plus>',self.font_size_increment)
        self.root.bind('<Control-minus>',self.font_size_decrement)
        self.root.bind('<Control-o>',self.open_file)
        self.root.bind('<Control-n>',self.new_file)
        self.root.bind('<Control-s>',self.save_file)
        self.root.bind('<Control-Alt-s>',self.save_as_file)
        self.root.bind('<Control-q>',self.exit_func)

    ############## All Functions ################
    def font_size_increment(self,event=None):
        self.font_size+=1
        self.txt_editor.config( font=('times new roman', self.font_size))

    def font_size_decrement(self,event=None):
        self.font_size -= 1
        self.txt_editor.config(font=('times new roman', self.font_size))

    def run(self,event=None):
        if self.path_name=='':
            messagebox.showerror('Error','Please save the file to execute the code!',parent=self.root)

        else:
            command=f'python {self.path_name}'
            run_file=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            output=run_file.communicate()
            error=run_file.communicate()
            self.txt_output.delete('1.0',END)
            self.txt_output.insert('1.0',output)
            self.txt_output.insert('1.0',error)

    def clear_all(self):
        self.txt_editor.delete('1.0',END)
        self.txt_output.delete('1.0',END)

    def color_change(self):
        if self.color_theme.get()=='Light Default':
            self.txt_editor.config(bg='#ffffff',fg='#000000')
            self.txt_output.config(bg='#ffffff',fg='#000000')

        if self.color_theme.get()=='Light Plus':
            self.txt_editor.config(bg='#e0e0e0',fg='##474747')
            self.txt_output.config(bg='#e0e0e0',fg='##474747')

        if self.color_theme.get()=='Dark':
            self.txt_editor.config(bg='#2d2d2d',fg='#c4c4c4')
            self.txt_output.config(bg='#2d2d2d',fg='#c4c4c4')

        if self.color_theme.get()=='Red':
            self.txt_editor.config(bg='#ffe8e8',fg='#2d2d2d')
            self.txt_output.config(bg='#ffe8e8',fg='#2d2d2d')

        if self.color_theme.get()=='Monokai':
            self.txt_editor.config(bg='#d3b774',fg='#474747')
            self.txt_output.config(bg='#d3b774',fg='#474747')

        if self.color_theme.get()=='Night Blue':
            self.txt_editor.config(bg='#6b9dc2',fg='#ededed')
            self.txt_output.config(bg='#6b9dc2',fg='#ededed')

    def exit_func(self,event=None):
        self.root.destroy()

    def new_file(self,event=None):
        self.path_name=''
        self.txt_editor.delete('1.0',END)
        self.txt_output.delete('1.0',END)

    def save_file(self,event=None):
        if self.path_name=='':
            self.save_as_file()
        else:
            fp=open(self.path_name,'w')
            fp.write(self.txt_editor.get('1.0',END))
            fp.close()

    def open_file(self,event=None):
        path=filedialog.askopenfile(filetypes=[('Python Files','*.py')],defaultextension=('.py'))
        if path!='':
            self.path_name=path
            fp=open(self.path_name,'r')
            data=fp.read()
            self.txt_editor.delete('1.0',END)
            self.txt_editor.insert('1.0',data)
            fp.close()

    def save_as_file(self,event=None):
        path=filedialog.asksaveasfile(filetypes=[('Python Files','*.py')],defaultextension=('.py'))
        if path!='':
            self.path_name=path
            fp=open(self.path_name,'w')
            fp.write(self.txt_editor.get('1.0',END))
            fp.close()


root=Tk()
obj=Vs_code(root)
root.mainloop()
