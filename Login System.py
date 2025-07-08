import tkinter as tk
#
def Login():
        UserName = entry_username.get()
        PassWord = entry_password.get()
        if(UserName=="i._.sumit._.nagar" and PassWord=="1234"):
            label_login.config(text="Login Successful! ✅",fg="green",font=('arial',20,"bold"))
        else:
         label_login.config(text="Username and password not match! ❌",fg="red",font=('arial',20,"bold"))
    
# Funcation Show\Hide        
def toggle_password():
    if entry_password.cget('show') == "":
        entry_password.config(show="*")
        btn_toggle.config(text="show")
    else:
        entry_password.config(show="")
        btn_toggle.config(text="hide")
# Main Window 
window = tk.Tk()
window.title("LOGIN SYSTEM")
window.configure(bg="#f0f0f0")
window.geometry("530x600")

# UserName
label_username=tk.Label(window,text=" UserName ",font=('arial',18,"bold"),width=25)
label_username.pack(pady=5,padx=5)
entry_username =tk.Entry(window,font=('Gadugi',14))
entry_username.pack(pady=5,padx=5)

# Password
label_password=tk.Label(window,text=" PassWord",font=('arial',18,"bold"),width=25)
label_password.pack(pady=5,padx=5)
entry_password =tk.Entry(window,font=('Gadugi',14),show="*")
entry_password.pack(pady=5,padx=5)
# Login button
butoon_login =tk.Button(window,text="Login",command=Login,width=20,bg='skyblue',fg='white',font=('arial',14))
butoon_login.pack(pady=5,padx=5)
# Toggle password
btn_toggle =tk.Button(window,text="show",command=toggle_password,width=20,font=('arial',14))
btn_toggle.pack(pady=5,padx=5)
# Message label
label_login = tk.Label(window, text="", anchor='center', justify='center')

label_login.pack()
# Start GUI
window.mainloop()
