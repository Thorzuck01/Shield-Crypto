from cryptography.fernet import Fernet 
import tkinter as tk 
from tkinter import messagebox
from tkinter import filedialog 
import os 
from PIL import Image, ImageTk
#Code: Thorzuck01 
class Encrypt_file: 

  def __init__(self,root):
    ############# TELA ##############
    self.root = root 
    self.root.title("Shield Crypto")
    self.root.resizable(False,False)
    self.root.config(bg="black")
    self.root.geometry("950x630")
    self.key = None 
    self.name_label = tk.Label(text="Shield Crypto",font="roboto 30 bold ",fg="white",bg="black")
    self.name_label.place(x=360,y=8)
    ######################################

    ################## IMAGEM ######################
    self.im = os.path.abspath('.\oni-bg.png')
      
    self.image = Image.open(self.im)
    imagetk = ImageTk.PhotoImage(self.image)
    label_imagem = tk.Label(root, image=imagetk,background="black")
    label_imagem.imagem_tk = imagetk 
    label_imagem.place(x=390,y=60)
    #####################################

    ################## BUTTONS ######################
    self.button_encrypt = tk.Button(text="Encrypt Folder",font="arial 20 bold",fg="black",command=self.encrypt_folder)
    self.button_encrypt.place(x=160,y=300) 

    self.button_decrypt = tk.Button(text="Decrypt Folder",font="arial 20 bold",bg="white",command=self.decrypt_folder)
    self.button_decrypt.place(x=560,y=300)

    self.button_clear = tk.Button(text="Clear Folder",font="arial 22 bold",bg="white",command=self.clear_folder)
    self.button_clear.place(x=170,y=460)

    self.button_exit = tk.Button(text="Crédito",font="arial 23 bold",bg="white",command=self.creditos)
    self.button_exit.place(x=600,y=460)
   #####################################
  

  def generete_key(self):

    key = Fernet.generate_key()
       
    key_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'encryption_key.key')
    with open(key_file_path, 'wb') as key_file:
      key_file.write(key)

    return key
    
    
  def clear_folder(self):

    folder_path = filedialog.askdirectory()
    
    if folder_path:

      for root,dir,file in os.walk(folder_path):

        for files in file:

          full_path = os.path.abspath(os.path.join(root,files))

          os.remove(full_path)

      messagebox.showinfo("Clear Folder","Sua pasta foi limpa com sucesso")
  

  def creditos(self):
    
    messagebox.showinfo("Criador","Criador: Thorzuck01")

  def encrypt_file(self,key,input_file):
      
    with open(input_file,"rb") as bin_file:

      content = bin_file.read()
    
    encrypt = Fernet(key).encrypt(content)
    with open(input_file,"wb") as bin_file:
      bin_file.write(encrypt)
  

  def decrypt_file(self,key,input_file): 

    with open(input_file,"rb") as bin_file:
      content = bin_file.read()

    decrypt = Fernet(key).decrypt(content)

    with open(input_file,"wb") as bin_file:

      bin_file.write(decrypt)
  

  def encrypt_folder(self):

    folder_path = filedialog.askdirectory()

    if folder_path:

      key =  self.generete_key()

      for root, dirs, files in os.walk(folder_path):
        for file in files:
          input_filename = os.path.join(root, file)
        
          self.encrypt_file(key, input_filename)
         
      
      messagebox.showinfo("Criptografia Completa","Sua pasta foi criptografada com sucesso!")

  def decrypt_folder(self):
    
    folder_path = filedialog.askdirectory()

    if folder_path:
      key_path = os.path.join(os.path.expanduser('~'),"Desktop","key.key")
    
      if not os.path.exists(key_path):
        messagebox.showerror("Error","Chave não encontrada, Não foi possivel decriptografar pasta") 
        return
    
    with open(key_path,"rb") as key_file:

      key = key_file.read()
    

    for root,dir,file in os.walk(folder_path):

      for files in file:

        input_file = os.path.abspath(os.path.join(root,files))

        self.decrypt_file(key,input_file)

    messagebox.showinfo("Descriptografado","Sua pasta foi Descriptografada com sucesso")
  

      
if __name__ =="__main__":

  app = tk.Tk()
  folder_encryptor = Encrypt_file(app)
  app.mainloop()
 
