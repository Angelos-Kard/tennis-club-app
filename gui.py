import tkinter as tk
import tkinter.messagebox as tkm
import tkinter.tix as tx
import datetime
import _frameDestroyers as fd
import _sqlQueries as q
import _checkEntryBox as checking

#import pymysql
#import sqlite3


class GraphEnv():
    '''Creating the UI'''

    def __init__(self, root):
        '''Creating the main window'''

        self.large_font="Arial 20"
        self.medium_font="Courrier 17"
        self.small_font="Courrier 15"
        root.title("Tennis Club App - Ομάδα 39")
        root.wm_geometry("1000x900-500+100")
        root.resizable(True,True)
        (self.conn, self.cursor) = q.create_sqlite_connection(self)
        self.initial_screen()


    def quit_window(self):
        '''Message Box for exiting the app'''

        response=tkm.askyesno("Έξοδος","Σίγουρα θέλεις να τερματίσεις το πρόγραμμα;")
        if response==True:
            self.cursor.close()
            self.conn.close()
            root.destroy()


    def initial_screen(self):
        '''You choose whether to login or to register'''

        self.ftitlos=tk.Frame(root) #Το Frame του τιτλου
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΚαλωσήλθατε στο Tennis Club App")
        self.titlos.pack(side="bottom",expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_login = tk.Frame(root)
        self.f_login.pack()
        self.login_button = tk.Button(self.f_login, text="Σύνδεση", font=self.medium_font, width=20, command=self.login_event)
        self.login_button.pack()

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_login_staff = tk.Frame(root)
        self.f_login_staff.pack()
        self.login_staff_button = tk.Button(self.f_login_staff, text="Σύνδεση ως Προσωπικό", font=self.medium_font, width=20, command=self.login_staff_event)
        self.login_staff_button.pack()

        self.f_blank2 = tk.Frame(root)
        self.f_blank2.pack()
        self.blanklabel2=tk.Label(self.f_blank2,text="\n")
        self.blanklabel2.pack()

        self.f_login_as_admin = tk.Frame(root)
        self.f_login_as_admin.pack()
        self.login_admin_button = tk.Button(self.f_login_as_admin, text="Σύνδεση ως Διαχειριστής", font=self.medium_font, width=20, command=self.login_admin_event)
        self.login_admin_button.pack()

        self.f_blank3 = tk.Frame(root)
        self.f_blank3.pack()
        self.blanklabel3=tk.Label(self.f_blank3,text="\n")
        self.blanklabel3.pack()

        self.f_register = tk.Frame(root)
        self.f_register.pack()
        self.register_button = tk.Button(self.f_register, text="Εγγραφή", font=self.medium_font, width=20, command=self.register_event)
        self.register_button.pack()        

        self.f_blank4 = tk.Frame(root)
        self.f_blank4.pack()
        self.blanklabel4=tk.Label(self.f_blank4,text="\n")
        self.blanklabel4.pack()

        self.f_exit = tk.Frame(root)
        self.f_exit.pack()
        self.exit_button = tk.Button(self.f_exit, text="Έξοδος", font=self.medium_font, width=20, command=self.quit_window)
        self.exit_button.pack()


    #Login Page ---------------------------------------------------------------------------------------------------------------------
    def login_event(self):
        '''Creating Login Screen'''

        fd.initial_screen_destroyer(self)
        #self.username_str = tk.StringVar()

        self.titlos.config(text='\nΣύνδεση')

        self.f_username = tk.Frame(root)
        self.f_username.pack()
        self.username_label = tk.Label(self.f_username, font=self.medium_font, text="Όνομα Χρήστη: ")
        self.username_label.pack(side='left')
        self.username_box = tk.Entry(self.f_username, font=self.medium_font, width=20)
        self.username_box.pack(side='left')

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_password = tk.Frame(root)
        self.f_password.pack()
        self.password_label = tk.Label(self.f_password, font=self.medium_font, text="Κωδικός: ")
        self.password_label.pack(side='left')
        self.password_box = tk.Entry(self.f_password, font=self.medium_font, width=20, show="*")
        self.password_box.pack(side='left')

        self.f_blank2 = tk.Frame(root)
        self.f_blank2.pack()
        self.blanklabel2=tk.Label(self.f_blank2,text="\n")
        self.blanklabel2.pack()

        self.f_login = tk.Frame(root)
        self.f_login.pack()
        self.back_button = tk.Button(self.f_login, text="Πίσω", font=self.medium_font, width=20, command=self.return_initial_login)
        self.back_button.pack(side="left")
        self.login_button = tk.Button(self.f_login, text="Σύνδεση", font=self.medium_font, width=20, command=self.login_check)
        self.login_button.pack(side="left")
        

    def login_check(self):
        flag = checking.login(self.username_box.get(), self.password_box.get())
        if flag == True:
            (flag, memberid) = q.login_checker(self, self.cursor, self.username_box.get(), self.password_box.get())
            if flag==True: 
                #tkm.showinfo(title="Σύνδεση", message="Η σύνδεση ήταν επιτυχής")
                self.logged_in(memberid)
            else: 
                tkm.showerror(title="Σύνδεση", message="Η σύνδεση δεν ήταν επιτυχής")


    # -------------------------------------------------------------------------------------------------------------------------------------------------------

    #Login Page For Staff ---------------------------------------------------------------------------------------------------------------------
    def login_staff_event(self):
        '''Creating Login Screen For Staff'''

        fd.initial_screen_destroyer(self)

        self.titlos.config(text='\nΣύνδεση Ως Προσωπικό')

        self.f_username = tk.Frame(root)
        self.f_username.pack()
        self.username_label = tk.Label(self.f_username, font=self.medium_font, text="Όνομα Χρήστη: ")
        self.username_label.pack(side='left')
        self.username_box = tk.Entry(self.f_username, font=self.medium_font, width=20)
        self.username_box.pack(side='left')

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_password = tk.Frame(root)
        self.f_password.pack()
        self.password_label = tk.Label(self.f_password, font=self.medium_font, text="Κωδικός: ")
        self.password_label.pack(side='left')
        self.password_box = tk.Entry(self.f_password, font=self.medium_font, width=20, show="*")
        self.password_box.pack(side='left')

        self.f_blank2 = tk.Frame(root)
        self.f_blank2.pack()
        self.blanklabel2=tk.Label(self.f_blank2,text="\n")
        self.blanklabel2.pack()

        self.f_login = tk.Frame(root)
        self.f_login.pack()
        self.back_button = tk.Button(self.f_login, text="Πίσω", font=self.medium_font, width=20, command=self.return_initial_login)
        self.back_button.pack(side="left")
        self.login_button = tk.Button(self.f_login, text="Σύνδεση", font=self.medium_font, width=20, command=self.login_staff_check)
        self.login_button.pack(side="left")
 
    
    def login_staff_check(self):
        flag = checking.login(self.username_box.get(), self.password_box.get())
        if flag == True:
            (flag, employeeid, job) = q.login_staff_checker(self.cursor, self.username_box.get(), self.password_box.get())
            if flag==True: 
                #tkm.showinfo(title="Σύνδεση", message="Η σύνδεση ήταν επιτυχής")
                self.logged_in_staff(employeeid, job)
            else: 
                tkm.showerror(title="Σύνδεση", message="Η σύνδεση δεν ήταν επιτυχής")

    # -------------------------------------------------------------------------------------------------------------------------------------------------------

    #Login Page For Admin -----------------------------------------------------------------------------------------------------------------------------------
    def login_admin_event(self):
        '''Creating Login Screen For Admin'''

        fd.initial_screen_destroyer(self)

        self.titlos.config(text='\nΣύνδεση Ως Διαχειριστής')

        self.f_username = tk.Frame(root)
        self.f_username.pack()
        self.username_label = tk.Label(self.f_username, font=self.medium_font, text="Όνομα Χρήστη: ")
        self.username_label.pack(side='left')
        self.username_box = tk.Entry(self.f_username, font=self.medium_font, width=20)
        self.username_box.pack(side='left')

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_password = tk.Frame(root)
        self.f_password.pack()
        self.password_label = tk.Label(self.f_password, font=self.medium_font, text="Κωδικός: ")
        self.password_label.pack(side='left')
        self.password_box = tk.Entry(self.f_password, font=self.medium_font, width=20, show="*")
        self.password_box.pack(side='left')

        self.f_blank2 = tk.Frame(root)
        self.f_blank2.pack()
        self.blanklabel2=tk.Label(self.f_blank2,text="\n")
        self.blanklabel2.pack()

        self.f_login = tk.Frame(root)
        self.f_login.pack()
        self.back_button = tk.Button(self.f_login, text="Πίσω", font=self.medium_font, width=20, command=self.return_initial_login)
        self.back_button.pack(side="left")
        self.login_button = tk.Button(self.f_login, text="Σύνδεση", font=self.medium_font, width=20, command=self.login_admin_check)
        self.login_button.pack(side="left")
 
    
    def login_admin_check(self):
        flag = checking.login(self.username_box.get(), self.password_box.get())
        if flag == True:
            (flag, employeeid, job) = q.login_staff_checker(self.cursor, self.username_box.get(), self.password_box.get())
            employeeid += employeeid
            if flag==True: 
                if job == "Διαχειριστής":
                    self.logged_in_admin()
                else:
                    tkm.showerror(title="Σύνδεση", message="Δεν έχετε διακιώματα διαχειριστή")
            else: 
                tkm.showerror(title="Σύνδεση", message="Η σύνδεση δεν ήταν επιτυχής")



    def return_initial_login(self):
        fd.login_destroyer(self)
        self.initial_screen()

    # -------------------------------------------------------------------------------------------------------------------------------------------------------

    #Register Page ------------------------------------------------------------------------------------------------------------------------------------------
    def register_event(self):
        '''Creating Login Screen For Admin'''

        fd.initial_screen_destroyer(self)

        self.titlos.config(text='\nΕγγραφή')


        self.f_name = tk.Frame(root)
        self.f_name.pack()
        self.name_label = tk.Label(self.f_name, font=self.medium_font, text="Όνομα: ")
        self.name_label.pack(side='left')
        self.name_box = tk.Entry(self.f_name, font=self.medium_font, width=20)
        self.name_box.pack(side='left')
        
        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()
        
        self.f_surname = tk.Frame(root)
        self.f_surname.pack()
        self.surname_label = tk.Label(self.f_surname, font=self.medium_font, text="Επώνυμο: ")
        self.surname_label.pack(side='left')
        self.surname_box = tk.Entry(self.f_surname, font=self.medium_font, width=20)
        self.surname_box.pack(side='right')

        self.f_blank2 = tk.Frame(root)
        self.f_blank2.pack()
        self.blanklabel2=tk.Label(self.f_blank2,text="\n")
        self.blanklabel2.pack()

        self.f_sex = tk.Frame(root)
        self.f_sex.pack()
        self.sex_label = tk.Label(self.f_sex, font=self.medium_font, text="Φύλο: ")
        self.sex_label.pack(side="left")
        self.sex = tk.StringVar(root)
        self.sex.set("Άνδρας")
        self.sex_box = tk.OptionMenu(self.f_sex, self.sex, "Άνδρας", "Γυναίκα")
        self.sex_box.pack(side="left")

        self.f_blank2_5 = tk.Frame(root)
        self.f_blank2_5.pack()
        self.blanklabel2_5=tk.Label(self.f_blank2_5,text="\n")
        self.blanklabel2_5.pack()

        self.f_ssn = tk.Frame(root)
        self.f_ssn.pack()
        self.ssn_label = tk.Label(self.f_ssn, font=self.medium_font, text="Αριθμός Ταυτότητας: ")
        self.ssn_label.pack(side='left')
        self.ssn_box = tk.Entry(self.f_ssn, font=self.medium_font, width=20)
        self.ssn_box.pack(side='left')

        self.f_blank3 = tk.Frame(root)
        self.f_blank3.pack()
        self.blanklabel3=tk.Label(self.f_blank3,text="\n")
        self.blanklabel3.pack()

        self.f_address = tk.Frame(root)
        self.f_address.pack()
        self.address_label = tk.Label(self.f_address, font=self.medium_font, text="Διεύθυνση: ")
        self.address_label.pack(side='left')
        self.address_box = tk.Entry(self.f_address, font=self.medium_font, width=20)
        self.address_box.pack(side='left')

        self.f_blank4 = tk.Frame(root)
        self.f_blank4.pack()
        self.blanklabel4=tk.Label(self.f_blank4,text="\n")
        self.blanklabel4.pack()

        self.f_telephone = tk.Frame(root)
        self.f_telephone.pack()
        self.telephone_label = tk.Label(self.f_telephone, font=self.medium_font, text="Τηλέφωνο: ")
        self.telephone_label.pack(side='left')
        self.telephone_box = tk.Entry(self.f_telephone, font=self.medium_font, width=20)
        self.telephone_box.pack(side='left')

        self.f_blank5 = tk.Frame(root)
        self.f_blank5.pack()
        self.blanklabel5=tk.Label(self.f_blank5,text="\n")
        self.blanklabel5.pack()

        self.f_email = tk.Frame(root)
        self.f_email.pack()
        self.email_label = tk.Label(self.f_email, font=self.medium_font, text="Email: ")
        self.email_label.pack(side='left')
        self.email_box = tk.Entry(self.f_email, font=self.medium_font, width=20)
        self.email_box.pack(side='left')        

        self.f_blank6 = tk.Frame(root)
        self.f_blank6.pack()
        self.blanklabel6=tk.Label(self.f_blank6,text="\n")
        self.blanklabel6.pack()

        self.f_subscription = tk.Frame(root)
        self.f_subscription.pack()
        self.subscription_label = tk.Label(self.f_subscription, font=self.medium_font, text="Συνδρομή: ")
        self.subscription_label.pack(side="left")

        self.choice = tk.StringVar(root)
        OPTIONS = ["1. Gold (35€/μήνα)", "2. Silver (25€/μήνα)", "3. Standard (18€/μήνα)"]
        self.choice.set(OPTIONS[0])
        
        self.subscription_box = tk.OptionMenu(self.f_subscription, self.choice, *OPTIONS)
        self.subscription_box.pack(side="left")

        self.f_blank6_5 = tk.Frame(root)
        self.f_blank6_5.pack()
        self.blanklabel6_5=tk.Label(self.f_blank6_5,text="\n")
        self.blanklabel6_5.pack()

        self.f_username = tk.Frame(root)
        self.f_username.pack()
        self.username_label = tk.Label(self.f_username, font=self.medium_font, text="Όνομα Χρήστη: ")
        self.username_label.pack(side='left')
        self.username_box = tk.Entry(self.f_username, font=self.medium_font, width=20)
        self.username_box.pack(side='left')

        self.f_blank7 = tk.Frame(root)
        self.f_blank7.pack()
        self.blanklabel7=tk.Label(self.f_blank7,text="\n")
        self.blanklabel7.pack()

        self.f_password = tk.Frame(root)
        self.f_password.pack()
        self.password_label = tk.Label(self.f_password, font=self.medium_font, text="Κωδικός: ")
        self.password_label.pack(side='left')
        self.password_box = tk.Entry(self.f_password, font=self.medium_font, width=20, show="*")
        self.password_box.pack(side='left')

        self.f_blank8 = tk.Frame(root)
        self.f_blank8.pack()
        self.blanklabel8=tk.Label(self.f_blank8,text="\n")
        self.blanklabel8.pack()

        self.f_register = tk.Frame(root)
        self.f_register.pack()
        self.back_button = tk.Button(self.f_register, text="Πίσω", font=self.medium_font, width=20, command=self.return_initial_register)
        self.back_button.pack(side="left")
        self.register_button = tk.Button(self.f_register, text="Εγγραφή", font=self.medium_font, width=20, command=self.register_check)
        self.register_button.pack(side="left")


    def register_check(self):
        flag = checking.register(self.name_box.get(), self.surname_box.get(), self.ssn_box.get(), self.address_box.get(), self.email_box.get(), self.telephone_box.get(), self.username_box.get(), self.password_box.get())
        if flag == True:
            flag = q.register_checker(self, self.cursor, self.name_box.get(), self.surname_box.get(), self.sex.get(), self.ssn_box.get(), self.address_box.get(), self.email_box.get(), self.telephone_box.get(), self.choice.get(), self.username_box.get(), self.password_box.get())
            if flag == 0:
                tkm.showinfo(title="Εγγραφή", message="Η εγγραφή ήταν επιτυχής")
                self.return_initial_register()
            elif flag == 1:
                tkm.showerror(title="Εγγραφή", message="Το 'Όνομα Χρήστη' χρησιμοποιείται ήδη.\nΠαρακαλούμε εισάγεται διαφορετικό όνομα χρήστη.")
            elif flag == 2:
                tkm.showerror(title="Εγγραφή", message="Είστε ήδη εγγεγραμμένοι.")
            else:
                tkm.showerror(title="Εγγραφή", message="Η εγγραφή δεν ήταν επιτυχής.\nΠαρακαλούμε προσπαθήστε αργότερα")


    def return_initial_register(self):
        fd.register_destroyer(self)
        self.initial_screen()

    # -------------------------------------------------------------------------------------------------------------------------------------------------------

    #When you are logged in (as member) ------------------------------------------------------------------------------------------------------------------------------------------

    def logged_in(self, memberid):
        self.memberid = memberid
        self.page_status = 0
        fd.login_destroyer(self)
        self.create_menu_member()
        self.profile.entryconfig("Προβολή Προφίλ", state="disabled")
        self.view_profile_page()


    def create_menu_member(self):
        self.menu = tk.Menu(root)
        self.profile = tk.Menu(self.menu, tearoff=0)
        self.matches = tk.Menu(self.menu, tearoff=0)
        self.exit = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Προφίλ",menu=self.profile)
        self.menu.add_command(label="Πρόγραμμα", command=lambda: self.page_transition(2)) #status 2
        self.menu.add_cascade(label="Αγώνες", menu=self.matches)
        self.menu.add_cascade(label="Έξοδος", menu=self.exit)
        self.profile.add_command(label="Προβολή Προφίλ", command= lambda: self.page_transition(0)) #status 0
        self.profile.add_command(label="Επεξεργασία Προφίλ", command=lambda: self.page_transition(1)) #status 1
        self.matches.add_command(label="Επερχόμενοι Αγώνες", command= lambda: self.page_transition(3)) #status 3
        self.matches.add_command(label="Αρχείο Αγώνων", command= lambda: self.page_transition(5)) #status 5
        self.matches.add_command(label="Μη Καταχωρημένοι Αγώνες", command=lambda: self.page_transition(4)) #status 4
        self.exit.add_command(label="Αποσύνδεση", command=lambda: self.page_transition(-1)) #status -1
        self.exit.add_separator()
        self.exit.add_command(label="Κλείσιμο Προγράμματος", command=self.quit_window)

        root.config(menu=self.menu)


    def page_transition(self, next_status):
        if self.page_status == 0:
            self.profile.entryconfig("Προβολή Προφίλ", state="normal")
            fd.view_profile_destroyer(self)

        if self.page_status == 1:
            self.profile.entryconfig("Επεξεργασία Προφίλ", state="normal")
            fd.edit_profile_destroyer(self)

        if self.page_status == 2:
            self.menu.entryconfig("Πρόγραμμα", state="normal")
            fd.program_destroyer(self)

        if self.page_status == 3:
            self.matches.entryconfig("Επερχόμενοι Αγώνες", state="normal")
            fd.upcoming_matches_destroyer(self)

        if self.page_status == 4:
            self.matches.entryconfig("Μη Καταχωρημένοι Αγώνες", state="normal")
            fd.submit_matches_destroyer(self)

        if self.page_status == 5:
            self.matches.entryconfig("Αρχείο Αγώνων", state="normal")
            fd.log_matches_destroyer(self)
        
        if next_status == -1:
            response=tkm.askyesno("Έξοδος","Σίγουρα θέλεις να αποσυνδεθείς;")
            if response == True:
                self.page_status == 0
                emptyMenu = tk.Menu(root)
                root.config(menu=emptyMenu)
                self.initial_screen()
            else:
                next_status = self.page_status

        self.page_status = next_status

        if self.page_status == 0:
            self.profile.entryconfig("Προβολή Προφίλ", state="disabled")
            self.view_profile_page()

        if self.page_status == 1:
            self.profile.entryconfig("Επεξεργασία Προφίλ", state="disabled")
            self.edit_profile_page()

        if self.page_status == 2:
            self.menu.entryconfig("Πρόγραμμα", state="disabled")
            self.view_program_page()

        if self.page_status == 3:
            self.matches.entryconfig("Επερχόμενοι Αγώνες", state="disabled")
            self.upcoming_matches_page()

        if self.page_status == 4:
            self.matches.entryconfig("Μη Καταχωρημένοι Αγώνες", state="disabled")
            self.submit_matches_page()

        if self.page_status == 5:
            self.matches.entryconfig("Αρχείο Αγώνων", state="disabled")
            self.log_matches_page()


    def view_profile_page(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΠροφίλ")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        result = q.fetch_profile_info(self, self.cursor, self.memberid)
        sub = q.subscription_details(self, self.cursor, result[7])

        if type(result) is bool or type(sub) is bool: 
            pass
        else:
            if result[2] == 'M': sex="Άνδρας"
            else: sex="Γυναίκα"

            self.f_member = tk.Frame(root)
            self.f_member.pack()
            self.member_label = tk.Label(self.f_member, font=self.medium_font, text="Member ID: #"+str(self.memberid))
            self.member_label.pack(side='left')

            self.f_blank0_5 = tk.Frame(root)
            self.f_blank0_5.pack()
            self.blanklabel0_5=tk.Label(self.f_blank0_5,text="\n")
            self.blanklabel0_5.pack()


            self.f_name = tk.Frame(root)
            self.f_name.pack()
            self.name_label = tk.Label(self.f_name, font=self.medium_font, text="Όνομα: "+result[0])
            self.name_label.pack(side='left')

            self.f_blank1 = tk.Frame(root)
            self.f_blank1.pack()
            self.blanklabel1=tk.Label(self.f_blank1,text="\n")
            self.blanklabel1.pack()
            
            self.f_surname = tk.Frame(root)
            self.f_surname.pack()
            self.surname_label = tk.Label(self.f_surname, font=self.medium_font, text="Επώνυμο: "+result[1])
            self.surname_label.pack(side='left')

            self.f_blank2 = tk.Frame(root)
            self.f_blank2.pack()
            self.blanklabel2=tk.Label(self.f_blank2,text="\n")
            self.blanklabel2.pack()

            self.f_sex = tk.Frame(root)
            self.f_sex.pack()
            self.sex_label = tk.Label(self.f_sex, font=self.medium_font, text="Φύλο: "+sex)
            self.sex_label.pack(side="left")


            self.f_blank2_5 = tk.Frame(root)
            self.f_blank2_5.pack()
            self.blanklabel2_5=tk.Label(self.f_blank2_5,text="\n")
            self.blanklabel2_5.pack()

            self.f_ssn = tk.Frame(root)
            self.f_ssn.pack()
            self.ssn_label = tk.Label(self.f_ssn, font=self.medium_font, text="Αριθμός Ταυτότητας: "+result[3])
            self.ssn_label.pack(side='left')

            self.f_blank3 = tk.Frame(root)
            self.f_blank3.pack()
            self.blanklabel3=tk.Label(self.f_blank3,text="\n")
            self.blanklabel3.pack()

            self.f_address = tk.Frame(root)
            self.f_address.pack()
            self.address_label = tk.Label(self.f_address, font=self.medium_font, text="Διεύθυνση: "+result[4])
            self.address_label.pack(side='left')

            self.f_blank4 = tk.Frame(root)
            self.f_blank4.pack()
            self.blanklabel4=tk.Label(self.f_blank4,text="\n")
            self.blanklabel4.pack()

            self.f_telephone = tk.Frame(root)
            self.f_telephone.pack()
            self.telephone_label = tk.Label(self.f_telephone, font=self.medium_font, text="Τηλέφωνο: "+result[6])
            self.telephone_label.pack(side='left')

            self.f_blank5 = tk.Frame(root)
            self.f_blank5.pack()
            self.blanklabel5=tk.Label(self.f_blank5,text="\n")
            self.blanklabel5.pack()

            self.f_email = tk.Frame(root)
            self.f_email.pack()
            self.email_label = tk.Label(self.f_email, font=self.medium_font, text="Email: "+result[5])
            self.email_label.pack(side='left')       

            self.f_blank6 = tk.Frame(root)
            self.f_blank6.pack()
            self.blanklabel6=tk.Label(self.f_blank6,text="\n")
            self.blanklabel6.pack()

            self.f_subscription = tk.Frame(root)
            self.f_subscription.pack()
            self.subscription_label = tk.Label(self.f_subscription, font=self.medium_font, text="Συνδρομή: "+str(sub["id"])+". "+sub["onoma"]+" ("+str(sub["timh/m"])+"€/μήνα)")
            self.subscription_label.pack(side="left")
            
            self.f_subscription2 = tk.Frame(root)
            self.f_subscription2.pack()
            self.subscription_label_2 = tk.Label(self.f_subscription2, font=self.medium_font, text="Παροχές: "+sub["paroxes"])
            self.subscription_label_2.pack()

            self.f_blank6_5 = tk.Frame(root)
            self.f_blank6_5.pack()
            self.blanklabel6_5=tk.Label(self.f_blank6_5,text="\n")
            self.blanklabel6_5.pack()

            self.f_date = tk.Frame(root)
            self.f_date.pack()
            self.date_label = tk.Label(self.f_date, font=self.medium_font, text="Ημερομηνία πρώτης εγγραφής: "+result[8])
            self.date_label.pack(side='left')


    def edit_profile_page(self):

        (username, password) = q.user_info(self, self.cursor, self.memberid)

        usernameVar = tk.StringVar()
        usernameVar.set(username)

        passwordVar = tk.StringVar()
        passwordVar.set(password)

        self.ftitlos=tk.Frame(root) 
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΕπεξεργασία Προφίλ")
        self.titlos.pack(side="bottom",expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_username = tk.Frame(root)
        self.f_username.pack()
        self.username_label = tk.Label(self.f_username, font=self.medium_font, text="Όνομα Χρήστη: ")
        self.username_label.pack(side='left')
        self.username_box = tk.Entry(self.f_username, font=self.large_font, width=20, textvariable=usernameVar)
        self.username_box.pack(side='left')

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_password = tk.Frame(root)
        self.f_password.pack()
        self.password_label = tk.Label(self.f_password, font=self.medium_font, text="Κωδικός: ")
        self.password_label.pack(side='left')
        self.password_box = tk.Entry(self.f_password, font=self.large_font, width=20, textvariable=passwordVar)
        self.password_box.pack(side='left')

        self.f_blank2 = tk.Frame(root)
        self.f_blank2.pack()
        self.blanklabel2=tk.Label(self.f_blank2,text="\n")
        self.blanklabel2.pack()

        self.f_save_edit = tk.Frame(root)
        self.f_save_edit.pack()
        self.back_button = tk.Button(self.f_save_edit, text="Ακύρωση", font=self.large_font, width=20, command=lambda: self.page_transition(0))
        self.back_button.pack(side="left")
        self.save_button = tk.Button(self.f_save_edit, text="Αποθήκευση", font=self.large_font, width=20, command=lambda: self.save_profile_edit(username, password, usernameVar.get(), passwordVar.get(), self.memberid))
        self.save_button.pack(side="left")


    def save_profile_edit(self, username_old, password_old, username_new, password_new, memberid):
        flag = checking.edit_profile(username_new, username_old)
        if flag == True:
            if username_new == username_old and password_new==password_old:
                tkm.showerror(title="Αποθήκευση Αλλαγών", message="Δεν πραγματοποιήθηκαν αλλαγές για να αποθηκευτούν")
            else:
                flag = q.edit_profile(self, self.cursor, username_new, password_new, memberid)
                if flag == 1:
                    tkm.showerror(title="Αποθήκευση Αλλαγών", message="Το 'Όνομα Χρήστη' χρησιμοποιείται ήδη.")
                elif flag == -1:
                    tkm.showerror(title="Αποθήκευση Αλλαγών", message="Υπήρξε πρόβλημα κατά την αποθήκευση των δεδομένων.\nΠροσπαθήστε αργότερα.")
                elif flag == 0:
                    tkm.showinfo(title="Αποθήκευση Αλλαγών", message="Οι αλλαγές αποθηκεύτηκαν επιτυχώς.")
                    self.page_transition(0)


    def view_program_page(self):

        row = q.my_program(self.cursor, self.memberid)

        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΠρόγραμμα")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

       
        if type(row) is int:
            if row == 1:
                self.info = tk.Label(self.f_table, text="Δεν συμμετέχετε σε κάποιο πρόγραμμα", font=self.medium_font)
                self.info.pack()
            elif row == -1:
                pass
        else:

            self.titlos_day = tk.Label(self.f_table, width=10, text="Δευτέρα", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_day.grid(row=0, column=1, sticky="nsew")

            self.titlos_day = tk.Label(self.f_table, width=10, text="Τρίτη", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_day.grid(row=0, column=2, sticky="nsew")

            self.titlos_day = tk.Label(self.f_table, width=10, text="Τετάρτη", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_day.grid(row=0, column=3, sticky="nsew") 

            self.titlos_day = tk.Label(self.f_table, width=10, text="Πέμπτη", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_day.grid(row=0, column=4, sticky="nsew")

            self.titlos_day = tk.Label(self.f_table, width=10, text="Παρασκευή", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_day.grid(row=0, column=5, sticky="nsew") 

            self.titlos_day = tk.Label(self.f_table, width=10, text="Σάββατο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_day.grid(row=0, column=6, sticky="nsew")


            self.titlos_time = tk.Label(self.f_table, width=10, text="10:00 - 11:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=1, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="11:00 - 12:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=2, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="12:00 - 13:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=3, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="13:00 - 14:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=4, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="14:00 - 15:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=5, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="15:00 - 16:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=6, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="16:00 - 17:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=7, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="17:00 - 18:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=8, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="18:00 - 19:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=9, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="19:00 - 20:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=10, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="20:00 - 21:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=11, column=0, sticky="nsew")

            for i in range(1,7):
                for j in range(1,12):
                    self.data = tk.Label(self.f_table, width=10, text="", relief=tk.SUNKEN, borderwidth=1)
                    self.data.grid(row=j, column=i, sticky="nsew")

            
            for program in row:
                program = dict(program)
                programid = program["programid"]


                program_info, extra_info = q.find_program_by_id(self.cursor, programid)

                i=0
                fields = []
                for x in program_info:
                    if i == 0: epipedo = x; i = 1
                    else: hlikia = x; i = 0
                for y in extra_info:

                    if str(y["fieldid"]) not in fields: fields.append(str(y["fieldid"]))

                for y in extra_info:
                    y = dict(y)

                    temp = y["hmera_wra_diarkeia"].split("_")

                    if temp[0] == "Δευτέρα": day = 1
                    elif temp[0] == "Τρίτη": day = 2
                    elif temp[0] == "Τετάρτη": day = 3
                    elif temp[0] == "Πέμπτη": day = 4
                    elif temp[0] == "Παρασκευή": day = 5
                    else: day = 6

                    if temp[1][-5] == '1': time = int(temp[1][-4])+1
                    elif temp[1][-4] == '0': time = 10
                    else: time = 11

                    duration = int(temp[2][0])

                    for i in range(duration):
                        self.data = tk.Label(self.f_table, width=10, text=epipedo+" ("+hlikia+")\nΓήπεδα: "+", ".join(fields), relief=tk.SUNKEN, borderwidth=1)
                        self.data.grid(row=time+i, column=day, sticky="nsew")


                
            
            self.f_table.grid_columnconfigure(1, weight=1)
            self.f_table.grid_columnconfigure(2, weight=1)
            self.f_table.grid_columnconfigure(3, weight=1)
            self.f_table.grid_columnconfigure(4, weight=1)
            self.f_table.grid_columnconfigure(5, weight=1)
            self.f_table.grid_columnconfigure(6, weight=1)
            # invisible row after last row gets all extra space
            self.f_table.grid_rowconfigure(11+1, weight=1)


    def upcoming_matches_page(self):
        
        row = q.upcoming_matches(self, self.cursor, self.memberid)

        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΕπερχόμενοι Αγώνων")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

       
        if type(row) is int:
            if row == 1:
                self.info = tk.Label(self.f_table, text="Δεν υπάρχουν επερχόμενοι αγώνες", font=self.medium_font)
                self.info.pack()
            elif row == -1:
                pass
        else:

            self.titlos_antipalos = tk.Label(self.f_table, width=15, text="Αντίπαλος", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_antipalos.grid(row=0, column=0, sticky="nsew")

            self.titlos_date = tk.Label(self.f_table, width=10, text="Ημερομηνία", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_date.grid(row=0, column=1, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="Ώρα", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=0, column=2, sticky="nsew") 

            self.titlos_field = tk.Label(self.f_table, width=10, text="Γήπεδο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_field.grid(row=0, column=3, sticky="nsew") 

            i=1
            for match in row:
                match = dict(match)

                self.data_antipalos = tk.Label(self.f_table, width=40, text=match["onoma_antipalou"]+" "+match["epwnumo_antipalou"], relief=tk.SUNKEN, borderwidth=1)
                self.data_antipalos.grid(row=i, column=0, sticky="nsew")

                self.data_date = tk.Label(self.f_table, width=10, text=match["date"], relief=tk.SUNKEN, borderwidth=1)
                self.data_date.grid(row=i, column=1, sticky="nsew")

                self.data_time = tk.Label(self.f_table, width=10, text=match["time"], relief=tk.SUNKEN, borderwidth=1)
                self.data_time.grid(row=i, column=2, sticky="nsew")

                field = q.field_info(self, self.cursor, match["fieldid"])
                if type(field) is bool or field is None: field = {"fieldid":match["fieldid"], "tupos":"Error", "timh/h":"Error"}
                else: field = dict(field)

                self.data_field = tk.Label(self.f_table, width=10, text=str(field["fieldid"])+"  ("+field["tupos"]+")", relief=tk.SUNKEN, borderwidth=1)
                self.data_field.grid(row=i, column=3, sticky="nsew")

                i+=1
            
            self.f_table.grid_columnconfigure(1, weight=1)
            self.f_table.grid_columnconfigure(2, weight=1)
            self.f_table.grid_columnconfigure(3, weight=1)
            # invisible row after last row gets all extra space
            self.f_table.grid_rowconfigure(i+1, weight=1)


    def log_matches_page(self):

        row = q.completed_matches(self, self.cursor, self.memberid)
        rank,num_members,ratio = q.find_my_ranking(self.cursor, self.memberid)

        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΑρχείο Αγώνων")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

        self.f_rank_info = tk.Frame(root)
        self.f_rank_info.pack()
       
        if type(row) is int:
            if row == 1:
                self.data_id = tk.Label(self.f_table, text="Δεν υπάρχουν διαθέσιμοι καταχωρημένοι αγώνες", font=self.medium_font)
                self.data_id.pack()
            elif row == -1:
                pass
        else:
            self.titlos_id = tk.Label(self.f_table, width=10, text="Member ID", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=0, column=0, sticky="nsew")

            self.titlos_antipalos = tk.Label(self.f_table, width=15, text="Αντίπαλος", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_antipalos.grid(row=0, column=1, sticky="nsew")

            self.titlos_score = tk.Label(self.f_table, width=20, text="Score", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_score.grid(row=0, column=2, sticky="nsew")

            self.titlos_status = tk.Label(self.f_table, width=10, text="Status", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_status.grid(row=0, column=3, sticky="nsew")

            self.titlos_date = tk.Label(self.f_table, width=10, text="Ημερομηνία", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_date.grid(row=0, column=4, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="Ώρα", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=0, column=5, sticky="nsew")  
            i=1
            for match in row:
                match = dict(match)
                self.data_id = tk.Label(self.f_table, width=10, text="#"+str(match["memberid"]), relief=tk.SUNKEN, borderwidth=1)
                self.data_id.grid(row=i, column=0, sticky="nsew")

                self.data_antipalos = tk.Label(self.f_table, width=15, text=match["onoma_antipalou"]+" "+match["epwnumo_antipalou"], relief=tk.SUNKEN, borderwidth=1)
                self.data_antipalos.grid(row=i, column=1, sticky="nsew")

                score = match["score"].split("/")
                games = ", ".join(score[1:])
                self.data_score = tk.Label(self.f_table, width=20, text="Sets: "+score[0]+" (Games: "+games+")", relief=tk.SUNKEN, borderwidth=1)
                self.data_score.grid(row=i, column=2, sticky="nsew")

                if match["status"] == 'W': status = "Νίκη"; bg_color = "green"
                else: status = "Ήττα"; bg_color = "red"
                self.data_status = tk.Label(self.f_table, width=10, text=status, bg = bg_color, relief=tk.SUNKEN, borderwidth=1)
                self.data_status.grid(row=i, column=3, sticky="nsew")

                self.data_date = tk.Label(self.f_table, width=10, text=match["date"], relief=tk.SUNKEN, borderwidth=1)
                self.data_date.grid(row=i, column=4, sticky="nsew")

                self.data_time = tk.Label(self.f_table, width=10, text=match["time"], relief=tk.SUNKEN, borderwidth=1)
                self.data_time.grid(row=i, column=5, sticky="nsew")

                i+=1
            
            self.f_table.grid_columnconfigure(1, weight=1)
            self.f_table.grid_columnconfigure(2, weight=1)
            self.f_table.grid_columnconfigure(3, weight=1)
            self.f_table.grid_columnconfigure(4, weight=1)
            self.f_table.grid_columnconfigure(5, weight=1)
            # invisible row after last row gets all extra space
            self.f_table.grid_rowconfigure(i+1, weight=1)

            
            self.rank_info=tk.Label(self.f_rank_info,font=self.small_font,text="Η κατάταξή μου: "+str(rank)+" (Ποσοστό Επιτυχίας: "+str(ratio)+"%) - Σύνολο Μελών: "+str(num_members))
            self.rank_info.pack()


    def submit_matches_page(self):

        row = q.not_completed_matches(self, self.cursor, self.memberid)


        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΜη Καταχωρημένοι Αγώνων")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

        self.f_score_info = tk.Frame(root)
        self.f_score_info.pack()

        self.f_save_matches = tk.Frame(root)
        self.f_save_matches.pack()

        if type(row) is int:
            if row == 1:
                self.data_id = tk.Label(self.f_table, text="Δεν υπάρχουν μη καταχωρημένοι αγώνες", font=self.medium_font)
                self.data_id.pack()
            elif row == -1:
                pass
        else:
            self.titlos_id = tk.Label(self.f_table, width=10, text="Member ID", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=0, column=0, sticky="nsew")

            self.titlos_antipalos = tk.Label(self.f_table, width=15, text="Αντίπαλος", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_antipalos.grid(row=0, column=1, sticky="nsew")

            self.titlos_score = tk.Label(self.f_table, width=20, text="Score*", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_score.grid(row=0, column=2, sticky="nsew")

            self.titlos_status = tk.Label(self.f_table, width=10, text="Status", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_status.grid(row=0, column=3, sticky="nsew")

            self.titlos_date = tk.Label(self.f_table, width=10, text="Ημερομηνία", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_date.grid(row=0, column=4, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="Ώρα", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=0, column=5, sticky="nsew")  
            i=1
            status_list = []
            score_list = []
            time_list = []
            date_list = []
            for match in row:
                match = dict(match)
                
                self.data_id = tk.Label(self.f_table, width=10, text="#"+str(match["memberid"]), relief=tk.SUNKEN, borderwidth=1)
                self.data_id.grid(row=i, column=0, sticky="nsew")

                self.data_antipalos = tk.Label(self.f_table, width=15, text=match["onoma_antipalou"]+" "+match["epwnumo_antipalou"], relief=tk.SUNKEN, borderwidth=1)
                self.data_antipalos.grid(row=i, column=1, sticky="nsew")

                score_list.append(tk.StringVar(root))
                score_list[i-1].set("")
                self.score_box = tk.Entry(self.f_table, font=self.small_font, width=20, textvariable=score_list[i-1], relief=tk.SUNKEN, borderwidth=1)
                self.score_box.grid(row=i, column=2, sticky="nsew")
                #self.data_score = tk.Label(self.f_table, width=20, text=match["score"], relief=tk.SUNKEN, borderwidth=1)
                #self.data_score.grid(row=i, column=2, sticky="nsew")

                status_list.append(tk.StringVar(root))
                status_list[i-1].set("Άγνωστο")
                self.status_box = tk.OptionMenu(self.f_table, status_list[i-1], "Άγνωστο", "Νίκη", "Ήττα")
                self.status_box.grid(row=i, column=3, sticky="nsew")

                date_list.append(match["date"])
                self.data_date = tk.Label(self.f_table, width=10, text=match["date"], relief=tk.SUNKEN, borderwidth=1)
                self.data_date.grid(row=i, column=4, sticky="nsew")

                time_list.append(match["time"])
                self.data_time = tk.Label(self.f_table, width=10, text=match["time"], relief=tk.SUNKEN, borderwidth=1)
                self.data_time.grid(row=i, column=5, sticky="nsew")

                i+=1
            

            self.f_table.grid_columnconfigure(1, weight=1)
            self.f_table.grid_columnconfigure(2, weight=1)
            self.f_table.grid_columnconfigure(3, weight=1)
            self.f_table.grid_columnconfigure(4, weight=1)
            self.f_table.grid_columnconfigure(5, weight=1)
            # invisible row after last row gets all extra space
            self.f_table.grid_rowconfigure(i+1, weight=1)

            
            self.score_info=tk.Label(self.f_score_info,font=self.small_font,text="* Για την ορθή καταγραφή των σκορ, συμπληρώστε πρώτα το σκορ των sets και,\nστη συνέχεια, τα σκορ των games, διαχωριζόμενα με κενό")
            self.score_info.pack()
            self.save_info=tk.Label(self.f_score_info,font=self.small_font,text="** Αγώνες στους οποίους έχει συμπληρωθεί μόνο ένα από τα δύο πεδία (score ή status) δεν θα αποθηκεύονται")
            self.save_info.pack()

            
            self.back_button = tk.Button(self.f_save_matches, text="Αποθήκευση Αλλαγών", font=self.large_font, width=20, command=lambda: self.save_submit_matches(status_list, score_list, date_list, time_list))
            self.back_button.pack(side="left")
          
    
    def save_submit_matches(self, status, score, date, time):
        status0 = list(status); score0 = list(score); date0 = list(date); time0 = list(time)
        (status0, score0, date0, time0) = checking.submit_match(status0, score0, date0, time0)
        flag = q.submit_match(self.cursor, self.memberid, status0, score0, date0, time0)
        if flag == 0: self.page_transition(4)
        else: 
            tkm.showerror(title="Αποθήκευση Αλλαγών", message="Οι αλλαγές δεν αποθηκεύτηκαν.\nΠροσπαθήστε αργότερα")
            self.page_transition(4)


    #When you are logged in (as staff) ------------------------------------------------------------------------------------------------------------------------------------------

    def logged_in_staff(self, employeeid, job):
        self.employeeid = employeeid
        self.page_status = 0
        fd.login_destroyer(self)
        if job == "Γυμναστής":
            self.create_menu_gymnast()
        elif job == "Γραμματέας":
            self.create_menu_secretary()
        elif job == "Καθαριστής":
            self.create_menu_cleaner()
        else:
            self.initial_screen()
        self.menu.entryconfig("Προφίλ", state="disabled")
        self.view_profile_staff()


    # Gymnast ------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def create_menu_gymnast(self):
        self.menu = tk.Menu(root)
        self.members = tk.Menu(self.menu, tearoff=0)
        self.exit = tk.Menu(self.menu, tearoff=0)
        self.menu.add_command(label="Προφίλ",command= lambda: self.page_transition_gymnast(0)) #status 0
        self.menu.add_command(label="Πρόγραμμα", command=lambda: self.page_transition_gymnast(1)) #status 1
        self.menu.add_cascade(label="Μέλη", menu=self.members)
        self.menu.add_cascade(label="Έξοδος", menu=self.exit)
        self.members.add_command(label="Λίστα Μελών", command = lambda: self.page_transition_gymnast(2)) #status 2
        self.members.add_command(label="Προσθήκη Μελών", command=lambda: self.page_transition_gymnast(3)) #status 3
        self.members.add_command(label="Αφαίρεση Μελών", command= lambda: self.page_transition_gymnast(4)) #status 4
        self.exit.add_command(label="Αποσύνδεση", command=lambda: self.page_transition_gymnast(-1)) #status -1
        self.exit.add_separator()
        self.exit.add_command(label="Κλείσιμο Προγράμματος", command=self.quit_window)

        root.config(menu=self.menu)


    def page_transition_gymnast(self, next_status):
        if self.page_status == 0:
            self.menu.entryconfig("Προφίλ", state="normal")
            fd.view_profile_staff_destroyer(self)

        if self.page_status == 1:
            self.menu.entryconfig("Πρόγραμμα", state="normal")
            fd.program_destroyer(self)

        if self.page_status == 2:
            self.members.entryconfig("Λίστα Μελών", state="normal")
            fd.list_of_members_destroyer(self)

        if self.page_status == 3:
            self.members.entryconfig("Προσθήκη Μελών", state="normal")
            fd.add_member_destroyer(self)

        if self.page_status == 4:
            self.members.entryconfig("Αφαίρεση Μελών", state="normal")
            fd.remove_member_destroyer(self)

        
        if next_status == -1:
            response=tkm.askyesno("Έξοδος","Σίγουρα θέλεις να αποσυνδεθείς;")
            if response == True:
                self.page_status = 0
                emptyMenu = tk.Menu(root)
                root.config(menu=emptyMenu)
                self.initial_screen()
            else:
                next_status = self.page_status

        self.page_status = next_status

        if self.page_status == 0:
            self.menu.entryconfig("Προφίλ", state="disabled")
            self.view_profile_staff()

        if self.page_status == 1:
            self.menu.entryconfig("Πρόγραμμα", state="disabled")
            self.program_gymnast()

        if self.page_status == 2:
            self.members.entryconfig("Λίστα Μελών", state="disabled")
            self.list_of_members_page()

        if self.page_status == 3:
            self.members.entryconfig("Προσθήκη Μελών", state="disabled")
            self.add_member_to_program()

        if self.page_status == 4:
            self.members.entryconfig("Αφαίρεση Μελών", state="disabled")
            self.remove_member_from_program()


    def view_profile_staff(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΠροφίλ")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        result = q.fetch_profile_info_staff(self.cursor, self.employeeid)
        

        if type(result) is bool: 
            pass
        else:
            result = dict(result)

            self.f_member = tk.Frame(root)
            self.f_member.pack()
            self.member_label = tk.Label(self.f_member, font=self.medium_font, text="Employee ID: #"+str(self.employeeid))
            self.member_label.pack(side='left')

            self.f_blank0_5 = tk.Frame(root)
            self.f_blank0_5.pack()
            self.blanklabel0_5=tk.Label(self.f_blank0_5,text="\n")
            self.blanklabel0_5.pack()


            self.f_name = tk.Frame(root)
            self.f_name.pack()
            self.name_label = tk.Label(self.f_name, font=self.medium_font, text="Όνομα: "+result["onoma"])
            self.name_label.pack(side='left')

            self.f_blank1 = tk.Frame(root)
            self.f_blank1.pack()
            self.blanklabel1=tk.Label(self.f_blank1,text="\n")
            self.blanklabel1.pack()
            
            self.f_surname = tk.Frame(root)
            self.f_surname.pack()
            self.surname_label = tk.Label(self.f_surname, font=self.medium_font, text="Επώνυμο: "+result["epwnumo"])
            self.surname_label.pack(side='left')

            self.f_blank2 = tk.Frame(root)
            self.f_blank2.pack()
            self.blanklabel2=tk.Label(self.f_blank2,text="\n")
            self.blanklabel2.pack()

            self.f_type_job = tk.Frame(root)
            self.f_type_job.pack()
            self.type_job_label = tk.Label(self.f_type_job, font=self.medium_font, text="Τύπος Εργασίας: "+result["douleia"])
            self.type_job_label.pack(side="left")


            self.f_blank2_5 = tk.Frame(root)
            self.f_blank2_5.pack()
            self.blanklabel2_5=tk.Label(self.f_blank2_5,text="\n")
            self.blanklabel2_5.pack()

            self.f_ssn = tk.Frame(root)
            self.f_ssn.pack()
            self.ssn_label = tk.Label(self.f_ssn, font=self.medium_font, text="Αριθμός Ταυτότητας: "+result["ar_tautothtas"])
            self.ssn_label.pack(side='left')

            self.f_blank3 = tk.Frame(root)
            self.f_blank3.pack()
            self.blanklabel3=tk.Label(self.f_blank3,text="\n")
            self.blanklabel3.pack()

            self.f_address = tk.Frame(root)
            self.f_address.pack()
            self.address_label = tk.Label(self.f_address, font=self.medium_font, text="Διεύθυνση: "+result["dieu8unsh"])
            self.address_label.pack(side='left')

            self.f_blank4 = tk.Frame(root)
            self.f_blank4.pack()
            self.blanklabel4=tk.Label(self.f_blank4,text="\n")
            self.blanklabel4.pack()

            self.f_telephone = tk.Frame(root)
            self.f_telephone.pack()
            self.telephone_label = tk.Label(self.f_telephone, font=self.medium_font, text="Τηλέφωνο: "+result["thlefwno"])
            self.telephone_label.pack(side='left')

            self.f_blank5 = tk.Frame(root)
            self.f_blank5.pack()
            self.blanklabel5=tk.Label(self.f_blank5,text="\n")
            self.blanklabel5.pack()

            self.f_email = tk.Frame(root)
            self.f_email.pack()
            self.email_label = tk.Label(self.f_email, font=self.medium_font, text="Email: "+result["email"])
            self.email_label.pack(side='left')       

            self.f_blank6 = tk.Frame(root)
            self.f_blank6.pack()
            self.blanklabel6=tk.Label(self.f_blank6,text="\n")
            self.blanklabel6.pack()

            self.f_salary = tk.Frame(root)
            self.f_salary.pack()
            self.salary_label = tk.Label(self.f_salary, font=self.medium_font, text="Μισθός: "+str(result["mis8os"])+"€")
            self.salary_label.pack(side="left")

            self.f_blank6_5 = tk.Frame(root)
            self.f_blank6_5.pack()
            self.blanklabel6_5=tk.Label(self.f_blank6_5,text="\n")
            self.blanklabel6_5.pack()

            self.f_date = tk.Frame(root)
            self.f_date.pack()
            self.date_label = tk.Label(self.f_date, font=self.medium_font, text="Ημερομηνία πρόσληψης: "+result["hmeromhnia_proslhpshs"])
            self.date_label.pack(side='left')

            self.f_blank7 = tk.Frame(root)
            self.f_blank7.pack()
            self.blanklabel7=tk.Label(self.f_blank7,text="\n")
            self.blanklabel7.pack()

            self.f_simvasi = tk.Frame(root)
            self.f_simvasi.pack()
            if result["lh3h_sumvashs"] is not None:
                self.simvasi_label = tk.Label(self.f_simvasi, font=self.medium_font, text="Ημερομηνία λήξης σύμβασης: "+result["lh3h_sumvashs"])
                self.simvasi_label.pack(side='left')


    def program_gymnast(self):

        row = q.my_program_gymnast(self.cursor, self.employeeid)

        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΠρόγραμμα")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

       
        if type(row) is int:
            if row == 1:
                self.info = tk.Label(self.f_table, text="Δεν έχετε αναλάβει κάποιο πρόγραμμα", font=self.medium_font)
                self.info.pack()
            elif row == -1:
                pass
        else:

            self.titlos_day = tk.Label(self.f_table, width=10, text="Δευτέρα", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_day.grid(row=0, column=1, sticky="nsew")

            self.titlos_day = tk.Label(self.f_table, width=10, text="Τρίτη", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_day.grid(row=0, column=2, sticky="nsew")

            self.titlos_day = tk.Label(self.f_table, width=10, text="Τετάρτη", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_day.grid(row=0, column=3, sticky="nsew") 

            self.titlos_day = tk.Label(self.f_table, width=10, text="Πέμπτη", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_day.grid(row=0, column=4, sticky="nsew")

            self.titlos_day = tk.Label(self.f_table, width=10, text="Παρασκευή", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_day.grid(row=0, column=5, sticky="nsew") 

            self.titlos_day = tk.Label(self.f_table, width=10, text="Σάββατο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_day.grid(row=0, column=6, sticky="nsew")


            self.titlos_time = tk.Label(self.f_table, width=10, text="10:00 - 11:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=1, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="11:00 - 12:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=2, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="12:00 - 13:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=3, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="13:00 - 14:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=4, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="14:00 - 15:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=5, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="15:00 - 16:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=6, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="16:00 - 17:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=7, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="17:00 - 18:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=8, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="18:00 - 19:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=9, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="19:00 - 20:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=10, column=0, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text="20:00 - 21:00", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=11, column=0, sticky="nsew")

            for i in range(1,7):
                for j in range(1,12):
                    self.data = tk.Label(self.f_table, width=10, text="", relief=tk.SUNKEN, borderwidth=1)
                    self.data.grid(row=j, column=i, sticky="nsew")

            
            for program in row:
                program = dict(program)
                programid = program["programid"]


                program_info, extra_info = q.find_program_by_id(self.cursor, programid)

                i=0
                fields = []
                for x in program_info:
                    if i == 0: epipedo = x; i = 1
                    else: hlikia = x; i = 0
                for y in extra_info:
                    if str(y["fieldid"]) not in fields: fields.append(str(y["fieldid"]))
                for y in extra_info:
                    y = dict(y)

                    temp = y["hmera_wra_diarkeia"].split("_")

                    if temp[0] == "Δευτέρα": day = 1
                    elif temp[0] == "Τρίτη": day = 2
                    elif temp[0] == "Τετάρτη": day = 3
                    elif temp[0] == "Πέμπτη": day = 4
                    elif temp[0] == "Παρασκευή": day = 5
                    else: day = 6

                    if temp[1][-5] == '1': time = int(temp[1][-4])+1
                    elif temp[1][-4] == '0': time = 10
                    else: time = 11

                    duration = int(temp[2][0])

                    for i in range(duration):
                        self.data = tk.Label(self.f_table, width=10, text=epipedo+" ("+hlikia+")\nΓήπεδα: "+", ".join(fields), relief=tk.SUNKEN, borderwidth=1)
                        self.data.grid(row=time+i, column=day, sticky="nsew")


                
            
            self.f_table.grid_columnconfigure(1, weight=1)
            self.f_table.grid_columnconfigure(2, weight=1)
            self.f_table.grid_columnconfigure(3, weight=1)
            self.f_table.grid_columnconfigure(4, weight=1)
            self.f_table.grid_columnconfigure(5, weight=1)
            self.f_table.grid_columnconfigure(6, weight=1)
            # invisible row after last row gets all extra space
            self.f_table.grid_rowconfigure(11+1, weight=1) 


    def list_of_members_page(self):

        row = q.program_details(self.cursor, self.employeeid)
        options = ["----"]

        for x in row:
            x = dict(x)
            options.append(str(x["programid"])+". "+x["epipedo"]+" ("+x["hlikia"]+")")

        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΛίστα Μελών Ανά Πρόγραμμμα")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        var = tk.StringVar(root)
        var.set(options[0])
        self.f_choose_programid = tk.Frame(root)
        self.f_choose_programid.pack()
        self.choose_programid_label = tk.Label(self.f_choose_programid,font=self.medium_font,text="Επιλέξτε Πρόγραμμα: ")
        self.choose_programid_label.pack(side="left")
        self.choose_programid = tk.OptionMenu(self.f_choose_programid, var, *options, command = lambda _: self.display_members(var.get()))
        self.choose_programid.pack(side="left")

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)
  

    def display_members(self, choice):
        if choice == "----":
            return
        else:
            row = q.members_of_a_program(self.cursor, choice[0])
        
        if type(row) is int:
            if row == 1:
                self.f_table.destroy()

                self.f_table = tk.Frame(root)
                self.f_table.pack(side="top", fill="both", expand=True)
                self.data_id = tk.Label(self.f_table, text="Δεν υπάρχουν μέλη στο συγκεκριμένο πρόγραμμα", font=self.medium_font)
                self.data_id.pack()
            elif row == -1:
                pass
        else:
            self.f_table.destroy()

            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.titlos_id = tk.Label(self.f_table, width=10, text="Member ID", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=0, column=0, sticky="nsew")

            self.titlos_name = tk.Label(self.f_table, width=15, text="Όνομα", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_name.grid(row=0, column=1, sticky="nsew")

            self.titlos_surname = tk.Label(self.f_table, width=20, text="Επώνυμο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_surname.grid(row=0, column=2, sticky="nsew")

            self.titlos_telephone = tk.Label(self.f_table, width=10, text="Τηλέφωνο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_telephone.grid(row=0, column=3, sticky="nsew")

            self.titlos_win_ratio = tk.Label(self.f_table, width=10, text="Ποσοστό Επιτυχίας", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_win_ratio.grid(row=0, column=4, sticky="nsew")

            i=1
            for member in row:
                member = dict(member)
                self.data_id = tk.Label(self.f_table, width=10, text="#"+str(member["memberid"]), relief=tk.SUNKEN, borderwidth=1)
                self.data_id.grid(row=i, column=0, sticky="nsew")

                self.data_name = tk.Label(self.f_table, width=15, text=member["onoma"], relief=tk.SUNKEN, borderwidth=1)
                self.data_name.grid(row=i, column=1, sticky="nsew")

                self.data_surname = tk.Label(self.f_table, width=20, text=member["epwnumo"], relief=tk.SUNKEN, borderwidth=1)
                self.data_surname.grid(row=i, column=2, sticky="nsew")

                self.data_telephone = tk.Label(self.f_table, width=10, text=member["thlefwno"], relief=tk.SUNKEN, borderwidth=1)
                self.data_telephone.grid(row=i, column=3, sticky="nsew")

                self.data_win_ratio = tk.Label(self.f_table, width=10, text=str(member["win_ratio"])+"%", relief=tk.SUNKEN, borderwidth=1)
                self.data_win_ratio.grid(row=i, column=4, sticky="nsew")

                i+=1
            
            self.f_table.grid_columnconfigure(1, weight=1)
            self.f_table.grid_columnconfigure(2, weight=1)
            self.f_table.grid_columnconfigure(3, weight=1)
            self.f_table.grid_columnconfigure(4, weight=1)
            # invisible row after last row gets all extra space
            self.f_table.grid_rowconfigure(i+1, weight=1)

            
    def add_member_to_program(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΠροσθήκη Μέλους σε Πρόγραμμα")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_search_member = tk.Frame(root)
        self.f_search_member.pack()
        self.search_member_label = tk.Label(self.f_search_member,font=self.medium_font,text="Αναζήτηση Μέλους: ")
        self.search_member_label.pack(side="left")
        self.search_member_text = tk.Entry(self.f_search_member, font=self.small_font, width=20, relief=tk.SUNKEN, borderwidth=1)
        self.search_member_text.pack(side="left")
        self.search_member_button = tk.Button(self.f_search_member, text="Αναζήτηση", font=self.medium_font, width=10, command=lambda: self.find_member(self.search_member_text.get(), 1))
        self.search_member_button.pack()

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

        self.f_add_button = tk.Frame(root)
        self.f_add_button.pack()


    def find_member(self, memberid, flag):
        row = q.fetch_profile_info(self, self.cursor, memberid)
    

        if type(row) is bool:
            if row == False:
                self.f_table.destroy()
                self.f_add_button.destroy()

                self.f_table = tk.Frame(root)
                self.f_table.pack(side="top", fill="both", expand=True)

                self.f_add_button = tk.Frame(root)
                self.f_add_button.pack()

                self.data_id = tk.Label(self.f_table, text="Δεν υπάρχουν μέλη με αυτό το ID", font=self.medium_font)
                self.data_id.pack()
            
        else:
            sub = q.subscription_details(self, self.cursor, row[7])
            programids = q.programs_participating(self.cursor, memberid)
            my_programs = []
            if type(programids) is int:
                if programids == 1:
                    my_programs.append("-")
            else:
                for x in programids:
                    my_programs.append(str(x["programid"]))

            my_programs = ", ".join(my_programs)

            row2 = q.program_details(self.cursor, self.employeeid)

            options = ["----"]

            for x in row2:
                x = dict(x)
                options.append(str(x["programid"])+". "+x["epipedo"]+" ("+x["hlikia"]+")")

            var = tk.StringVar(root)
            var.set(options[0])

            self.f_table.destroy()
            self.f_add_button.destroy()

            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.f_add_button = tk.Frame(root)
            self.f_add_button.pack()

            self.titlos_id = tk.Label(self.f_table, width=10, text="Member ID", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=0, column=0, sticky="nsew")

            self.titlos_full_name = tk.Label(self.f_table, width=15, text="Ονοματεπώνυμο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_full_name.grid(row=0, column=1, sticky="nsew")

            self.titlos_sex = tk.Label(self.f_table, width=20, text="Φύλο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_sex.grid(row=0, column=2, sticky="nsew")

            self.titlos_subscription = tk.Label(self.f_table, width=10, text="Συνδρομή", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_subscription.grid(row=0, column=3, sticky="nsew")

            self.titlos_already_programs = tk.Label(self.f_table, width=15, text="Προγράμματα που συμμετέχει ήδη", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_already_programs.grid(row=0, column=4, sticky="nsew")

            self.titlos_choose_programs = tk.Label(self.f_table, width=10, text="Επιλογή Προγράμματος", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_choose_programs.grid(row=0, column=5, sticky="nsew")

            self.data_id = tk.Label(self.f_table, width=10, text="#"+memberid, relief=tk.SUNKEN, borderwidth=1)
            self.data_id.grid(row=1, column=0, sticky="nsew")

            self.data_full_name = tk.Label(self.f_table, width=15, text=row[0]+" "+row[1], relief=tk.SUNKEN, borderwidth=1)
            self.data_full_name.grid(row=1, column=1, sticky="nsew")
            if row[2] == 'M': sex = "Άνδρας"
            else: sex = "Γυναίκα"

            self.data_sex = tk.Label(self.f_table, width=20, text=sex, relief=tk.SUNKEN, borderwidth=1)
            self.data_sex.grid(row=1, column=2, sticky="nsew")

            self.data_already_programs = tk.Label(self.f_table, width=10, text=str(sub["id"])+". "+sub["onoma"], relief=tk.SUNKEN, borderwidth=1)
            self.data_already_programs.grid(row=1, column=3, sticky="nsew")

            self.data_choose_program = tk.Label(self.f_table, width=15, text=my_programs, relief=tk.SUNKEN, borderwidth=1)
            self.data_choose_program.grid(row=1, column=4, sticky="nsew")

            self.choose_programid = tk.OptionMenu(self.f_table, var, *options)
            self.choose_programid.grid(row=1, column=5, sticky="nsew")

            self.f_table.grid_columnconfigure(1, weight=1)
            self.f_table.grid_columnconfigure(2, weight=1)
            self.f_table.grid_columnconfigure(3, weight=1)
            self.f_table.grid_columnconfigure(4, weight=1)
            self.f_table.grid_columnconfigure(5, weight=1)
            # invisible row after last row gets all extra space
            self.f_table.grid_rowconfigure(2, weight=1)

            if flag == 1:
                self.add_button = tk.Button(self.f_add_button, text="Προσθήκη Μέλους", font=self.medium_font, width=20, command=lambda: self.add_member_event(memberid, var.get()[0], my_programs))
                self.add_button.pack()
            else:
                self.remove_button = tk.Button(self.f_add_button, text="Αφαίρεση Μέλους", font=self.medium_font, width=20, command=lambda: self.remove_member_event(memberid, var.get()[0], my_programs))
                self.remove_button.pack()


    def add_member_event(self, memberid, choice, programs_list):
        if choice == "-":
            pass
        elif choice not in programs_list:
            q.add_member(self.cursor, memberid, choice)
            tkm.showinfo(title="Προσθήκη Μέλος", message="Το μέλος προστέθηκε με επιτυχία")
            self.page_transition_gymnast(3)
        else:
            tkm.showerror(title="Προσθήκη Μέλους", message="Το μέλος ανήκει ήδη στο συγκεκριμένο πρόγραμμα")


    def remove_member_from_program(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΑφαίρεση Μέλους Από Πρόγραμμα")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_search_member = tk.Frame(root)
        self.f_search_member.pack()
        self.search_member_label = tk.Label(self.f_search_member,font=self.medium_font,text="Αναζήτηση Μέλους: ")
        self.search_member_label.pack(side="left")
        self.search_member_text = tk.Entry(self.f_search_member, font=self.small_font, width=20, relief=tk.SUNKEN, borderwidth=1)
        self.search_member_text.pack(side="left")
        self.search_member_button = tk.Button(self.f_search_member, text="Αναζήτηση", font=self.medium_font, width=10, command=lambda: self.find_member(self.search_member_text.get(), 2))
        self.search_member_button.pack()

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

        self.f_add_button = tk.Frame(root)
        self.f_add_button.pack()


    def remove_member_event(self, memberid, choice, programs_list):
        if choice == "-":
            pass
        elif choice in programs_list:
            q.remove_member(self.cursor, memberid, choice)
            tkm.showinfo(title="Αφαίρεση Μέλους", message="Το μέλος αφαιρέθηκε με επιτυχία")
            self.page_transition_gymnast(4)
        else:
            tkm.showerror(title="Αφαίρεση Μέλους", message="Το μέλος δεν ανήκει στο συγκεκριμένο πρόγραμμα")
    # Secretary ------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def create_menu_secretary(self):
        self.menu = tk.Menu(root)
        self.customers = tk.Menu(self.menu, tearoff=0)
        self.matches = tk.Menu(self.menu, tearoff=0)
        self.transactions = tk.Menu(self.menu, tearoff=0)
        self.exit = tk.Menu(self.menu, tearoff=0)
        self.menu.add_command(label="Προφίλ",command= lambda: self.page_transition_secretary(0)) 
        self.menu.add_cascade(label="Πελατολόγιο", menu=self.customers) 
        self.menu.add_cascade(label="Αγώνες", menu=self.matches)
        self.menu.add_cascade(label="Συνναλαγές", menu=self.transactions)
        self.menu.add_cascade(label="Έξοδος", menu=self.exit)
        self.customers.add_command(label="Αναζήτηση Πελάτη", command = lambda: self.page_transition_secretary(1)) 
        self.customers.add_command(label="Αναζήτηση Μέλους", command=lambda: self.page_transition_secretary(2))
        self.customers.add_command(label="Προσθήκη Πελάτη", command=lambda: self.page_transition_secretary(3))
        self.matches.add_command(label="Προσθήκη Αγώνα", command= lambda: self.page_transition_secretary(4))
        self.matches.add_command(label="Προσθήκη Ενοικίασης", command= lambda: self.page_transition_secretary(5))
        self.transactions.add_command(label="Προσθήκη Συναλλαγής", command= lambda: self.page_transition_secretary(6))
        self.transactions.add_command(label="Εκκρεμείς Συναλλαγές", command= lambda: self.page_transition_secretary(7))
        self.transactions.add_command(label="Ενημέρωση Συναλλαγής", command= lambda: self.page_transition_secretary(8))
        self.transactions.add_command(label="Ολοκληρωμένες Συναλλαγές", command= lambda: self.page_transition_secretary(9))
        self.exit.add_command(label="Αποσύνδεση", command=lambda: self.page_transition_secretary(-1)) #status -1
        self.exit.add_separator()
        self.exit.add_command(label="Κλείσιμο Προγράμματος", command=self.quit_window)

        root.config(menu=self.menu)


    def page_transition_secretary(self, next_status):
        if self.page_status == 0:
            self.menu.entryconfig("Προφίλ", state="normal")
            fd.view_profile_staff_destroyer(self)

        if self.page_status == 1:
            self.customers.entryconfig("Αναζήτηση Πελάτη", state="normal")
            fd.search_customer_destroyer(self)

        if self.page_status == 2:
            self.customers.entryconfig("Αναζήτηση Μέλους", state="normal")
            fd.search_melos_destroyer(self)

        if self.page_status == 3:
            self.customers.entryconfig("Προσθήκη Πελάτη", state="normal")
            fd.add_customer_destroyer(self)

        if self.page_status == 4:
            self.matches.entryconfig("Προσθήκη Αγώνα", state="normal")
            fd.new_match_destroyer(self)
        
        if self.page_status == 5:
            self.matches.entryconfig("Προσθήκη Ενοικίασης", state="normal")
            fd.new_rent_destroyer(self)

        if self.page_status == 6:
            self.transactions.entryconfig("Προσθήκη Συναλλαγής", state="normal")
            fd.add_new_transaction_destroyer(self)

        if self.page_status == 7:
            self.transactions.entryconfig("Εκκρεμείς Συναλλαγές", state="normal")
            fd.pending_transaction_destroyer(self)

        if self.page_status == 8:
            self.transactions.entryconfig("Ενημέρωση Συναλλαγής", state="normal")
            fd.update_transaction_destroyer(self)

        if self.page_status == 9:
            self.transactions.entryconfig("Ολοκληρωμένες Συναλλαγές", state="normal")
            fd.completed_transaction_destroyer(self)

        if next_status == -1:
            response=tkm.askyesno("Έξοδος","Σίγουρα θέλεις να αποσυνδεθείς;")
            if response == True:
                self.page_status = 0
                emptyMenu = tk.Menu(root)
                root.config(menu=emptyMenu)
                self.initial_screen()
            else:
                next_status = self.page_status

        self.page_status = next_status

        if self.page_status == 0:
            self.menu.entryconfig("Προφίλ", state="disabled")
            self.view_profile_staff()

        if self.page_status == 1:
            self.customers.entryconfig("Αναζήτηση Πελάτη", state="disabled")
            self.search_customer()

        if self.page_status == 2:
            self.customers.entryconfig("Αναζήτηση Μέλους", state="disabled")
            self.search_melos()

        if self.page_status == 3:
            self.customers.entryconfig("Προσθήκη Πελάτη", state="disabled")
            self.add_customer()

        if self.page_status == 4:
            self.matches.entryconfig("Προσθήκη Αγώνα", state="disabled")
            self.new_match()

        if self.page_status == 5:
            self.matches.entryconfig("Προσθήκη Ενοικίασης", state="disabled")
            self.new_rent()

        if self.page_status == 6:
            self.transactions.entryconfig("Προσθήκη Συναλλαγής", state="disabled")
            self.add_new_transaction()

        if self.page_status == 7:
            self.transactions.entryconfig("Εκκρεμείς Συναλλαγές", state="disabled")
            self.pending_transaction()

        if self.page_status == 8:
            self.transactions.entryconfig("Ενημέρωση Συναλλαγής", state="disabled")
            self.update_transaction()

        if self.page_status == 9:
            self.transactions.entryconfig("Ολοκληρωμένες Συναλλαγές", state="disabled")
            self.completed_transaction()


    def search_customer(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΑναζήτηση Πελάτη")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_by_name = tk.Frame(root)
        self.f_by_name.pack(anchor="nw")
        self.name_label = tk.Label(self.f_by_name,font=self.medium_font,text="Όνομα: ")
        self.name_label.pack(side="left")
        self.search_name_text = tk.Entry(self.f_by_name, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.search_name_text.pack(side="left")

        self.f_by_surname = tk.Frame(root)
        self.f_by_surname.pack(anchor="nw")
        self.surname_label = tk.Label(self.f_by_surname,font=self.medium_font,text="Επώνυμο: ")
        self.surname_label.pack(side="left")
        self.search_surname_text = tk.Entry(self.f_by_surname, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.search_surname_text.pack(side="left")

        self.f_by_telephone = tk.Frame(root)
        self.f_by_telephone.pack(anchor="nw")
        self.telephone_label = tk.Label(self.f_by_telephone,font=self.medium_font,text="Τηλέφωνο: ")
        self.telephone_label.pack(side="left")
        self.search_telephone_text = tk.Entry(self.f_by_telephone, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.search_telephone_text.pack(side="left")

        self.f_button = tk.Frame(root)
        self.f_button.pack(anchor="nw")
        self.search_member_button = tk.Button(self.f_button, text="Αναζήτηση", font=self.medium_font, width=10, command=lambda: self.find_customer(self.search_name_text.get(), self.search_surname_text.get(), self.search_telephone_text.get()))
        self.search_member_button.pack()

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)


    def find_customer(self, name, surname, telephone):
        if name == "" and surname == "" and telephone == "":
            row = q.find_all_customers(self.cursor)
        elif name != "" and surname != "" and telephone == "":
            row = q.find_customer_by_name(self.cursor, name, surname)
        elif name == "" and surname == "" and telephone != "":
            row = q.find_customer_by_phone(self.cursor, telephone)
        elif name != "" and surname != "" and telephone != "":
            row = q.find_customer_by_phone_and_name(self.cursor, name, surname, telephone)
        else:
            tkm.showerror(title="Αναζήτηση Πελάτη", message="Λανθασμένη μορφή αναζήτησης.\nΗ αναζήτηση είναι επιτυχής, αν ικανοποιείται ένα από τα εξής κριτήρια:\n- Έχουν συμπληρωθεί τα πείδα 'Όνομα' και 'Επώνυμο'.\n- Έχει συμπληρωθεί το πεδίο 'Τηλέφωνο'\n- Έχουν συμπληρωθεί όλα τα πεδία")
            row = None


        if row is None:
            self.f_table.destroy()
            
            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.data_id = tk.Label(self.f_table, text="Δεν βρέθηκε πελάτης με τα ανωτέρω στοιχεία", font=self.medium_font)
            self.data_id.pack()
        elif len(row) == 0:
            self.f_table.destroy()
            
            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.data_id = tk.Label(self.f_table, text="Δεν βρέθηκε πελάτης με τα ανωτέρω στοιχεία", font=self.medium_font)
            self.data_id.pack()
        else:
            self.f_table.destroy()

            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.titlos_id = tk.Label(self.f_table, width=10, text="ID", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=0, column=0, sticky="nsew")

            self.titlos_full_name = tk.Label(self.f_table, width=15, text="Ονοματεπώνυμο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_full_name.grid(row=0, column=1, sticky="nsew")

            self.titlos_sex = tk.Label(self.f_table, width=20, text="Φύλο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_sex.grid(row=0, column=2, sticky="nsew")

            self.titlos_subscription = tk.Label(self.f_table, width=10, text="Αριθμός Ταυτότητας", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_subscription.grid(row=0, column=3, sticky="nsew")

            self.titlos_already_programs = tk.Label(self.f_table, width=15, text="Email", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_already_programs.grid(row=0, column=4, sticky="nsew")

            self.titlos_choose_programs = tk.Label(self.f_table, width=10, text="Τηλέφωνο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_choose_programs.grid(row=0, column=5, sticky="nsew")

            i=1
            for person in row:
                person = dict(person)
                self.titlos_id = tk.Label(self.f_table, width=10, text=str(person["id_pelath"]), relief=tk.SUNKEN, borderwidth=1)
                self.titlos_id.grid(row=i, column=0, sticky="nsew")

                self.titlos_full_name = tk.Label(self.f_table, width=15, text=person["epwnumo"]+" "+person["onoma"], relief=tk.SUNKEN, borderwidth=1)
                self.titlos_full_name.grid(row=i, column=1, sticky="nsew")

                if person["sex"] == 'M': sex="Άνδρας"
                else: sex="Γυναίκα"

                self.titlos_sex = tk.Label(self.f_table, width=20, text=sex, relief=tk.SUNKEN, borderwidth=1)
                self.titlos_sex.grid(row=i, column=2, sticky="nsew")

                self.titlos_subscription = tk.Label(self.f_table, width=10, text=person["ar_tautothtas"], relief=tk.SUNKEN, borderwidth=1)
                self.titlos_subscription.grid(row=i, column=3, sticky="nsew")

                self.titlos_already_programs = tk.Label(self.f_table, width=15, text=person["email"], relief=tk.SUNKEN, borderwidth=1)
                self.titlos_already_programs.grid(row=i, column=4, sticky="nsew")

                self.titlos_choose_programs = tk.Label(self.f_table, width=10, text=person["thlefwno"], relief=tk.SUNKEN, borderwidth=1)
                self.titlos_choose_programs.grid(row=i, column=5, sticky="nsew")

                i+=1

                self.f_table.grid_columnconfigure(1, weight=1)
                self.f_table.grid_columnconfigure(2, weight=1)
                self.f_table.grid_columnconfigure(3, weight=1)
                self.f_table.grid_columnconfigure(4, weight=1)
                self.f_table.grid_columnconfigure(5, weight=1)
                # invisible row after last row gets all extra space
                self.f_table.grid_rowconfigure(i+1, weight=1)


    def search_melos(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΑναζήτηση Μέλους")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_by_name = tk.Frame(root)
        self.f_by_name.pack(anchor="nw")
        self.name_label = tk.Label(self.f_by_name,font=self.medium_font,text="Όνομα: ")
        self.name_label.pack(side="left")
        self.search_name_text = tk.Entry(self.f_by_name, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.search_name_text.pack(side="left")

        self.f_by_surname = tk.Frame(root)
        self.f_by_surname.pack(anchor="nw")
        self.surname_label = tk.Label(self.f_by_surname,font=self.medium_font,text="Επώνυμο: ")
        self.surname_label.pack(side="left")
        self.search_surname_text = tk.Entry(self.f_by_surname, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.search_surname_text.pack(side="left")

        self.f_by_telephone = tk.Frame(root)
        self.f_by_telephone.pack(anchor="nw")
        self.telephone_label = tk.Label(self.f_by_telephone,font=self.medium_font,text="Τηλέφωνο: ")
        self.telephone_label.pack(side="left")
        self.search_telephone_text = tk.Entry(self.f_by_telephone, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.search_telephone_text.pack(side="left")

        self.f_by_id = tk.Frame(root)
        self.f_by_id.pack(anchor="nw")
        self.id_label = tk.Label(self.f_by_id,font=self.medium_font,text="Member ID: ")
        self.id_label.pack(side="left")
        self.search_id_text = tk.Entry(self.f_by_id, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.search_id_text.pack(side="left")

        self.f_button = tk.Frame(root)
        self.f_button.pack(anchor="nw")
        self.search_member_button = tk.Button(self.f_button, text="Αναζήτηση", font=self.medium_font, width=10, command=lambda: self.find_melos(self.search_name_text.get(), self.search_surname_text.get(), self.search_telephone_text.get(), self.search_id_text.get()))
        self.search_member_button.pack()

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)


    def find_melos(self, name, surname, telephone, memberid):
        if name == "" and surname == "" and telephone == "" and memberid=="":
            row = q.find_all_melh(self.cursor)
        elif name != "" and surname != "" and telephone == "" and memberid=="":
            row = q.find_melos_by_name(self.cursor, name, surname)
        elif name == "" and surname == "" and telephone != "" and memberid=="":
            row = q.find_melos_by_phone(self.cursor, telephone)
        elif name != "" and surname != "" and telephone != "" and memberid=="":
            row = q.find_melos_by_phone_and_name(self.cursor, name, surname, telephone)
        elif name == "" and surname == "" and telephone == "" and memberid != "":
            row = q.find_melos_by_id(self.cursor, memberid)
        else:
            tkm.showerror(title="Αναζήτηση Μέλους", message="Λανθασμένη μορφή αναζήτησης.\nΗ αναζήτηση είναι επιτυχής, αν ικανοποιείται ένα από τα εξής κριτήρια:\n- Έχουν συμπληρωθεί τα πείδα 'Όνομα' και 'Επώνυμο'.\n- Έχει συμπληρωθεί το πεδίο 'Τηλέφωνο'\n- Έχουν συμπληρωθεί τα πεδία 'Όνομα', 'Επώνυμο' και 'Τηλέφωνο'\n- Έχει συμπληρωθεί το πεδίο 'Member ID'")
            row = None


        if row is None:
            self.f_table.destroy()
            
            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.data_id = tk.Label(self.f_table, text="Δεν βρέθηκε μέλος με τα ανωτέρω στοιχεία", font=self.medium_font)
            self.data_id.pack()
        elif len(row) == 0:
            self.f_table.destroy()
            
            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.data_id = tk.Label(self.f_table, text="Δεν βρέθηκε πελάτης με τα ανωτέρω στοιχεία", font=self.medium_font)
            self.data_id.pack()
        else:
            self.f_table.destroy()

            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.titlos_id = tk.Label(self.f_table, width=10, text="ID", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=0, column=0, sticky="nsew")

            self.titlos_full_name = tk.Label(self.f_table, width=20, text="Ονοματεπώνυμο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_full_name.grid(row=0, column=1, sticky="nsew")

            self.titlos_sex = tk.Label(self.f_table, width=20, text="Φύλο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_sex.grid(row=0, column=2, sticky="nsew")

            self.titlos_ssn = tk.Label(self.f_table, width=15, text="Αριθμός Ταυτότητας", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_ssn.grid(row=0, column=3, sticky="nsew")

            self.titlos_email = tk.Label(self.f_table, width=15, text="Email", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_email.grid(row=0, column=4, sticky="nsew")

            self.titlos_telephone = tk.Label(self.f_table, width=10, text="Τηλέφωνο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_telephone.grid(row=0, column=5, sticky="nsew")

            self.titlos_subscription = tk.Label(self.f_table, width=10, text="Συνδρομή", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_subscription.grid(row=0, column=6, sticky="nsew")

            self.titlos_programs = tk.Label(self.f_table, width=10, text="Προγράμματα", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_programs.grid(row=0, column=7, sticky="nsew")

            i=1
            for person in row:
                person = dict(person)
                sub = q.subscription_details(self, self.cursor, person["sundromh"])
                programids = q.programs_participating(self.cursor, person["memberid"])
                my_programs = []
                if type(programids) is int:
                    if programids == 1:
                        my_programs.append("-")
                else:
                    for x in programids:
                        my_programs.append(str(x["programid"]))

                my_programs = ", ".join(my_programs)
                
                
                self.titlos_id = tk.Label(self.f_table, width=10, text=str(person["id_pelath"]), relief=tk.SUNKEN, borderwidth=1)
                self.titlos_id.grid(row=i, column=0, sticky="nsew")

                self.titlos_full_name = tk.Label(self.f_table, width=20, text=person["epwnumo"]+" "+person["onoma"], relief=tk.SUNKEN, borderwidth=1)
                self.titlos_full_name.grid(row=i, column=1, sticky="nsew")

                if person["sex"] == 'M': sex="Άνδρας"
                else: sex="Γυναίκα"

                self.titlos_sex = tk.Label(self.f_table, width=20, text=sex, relief=tk.SUNKEN, borderwidth=1)
                self.titlos_sex.grid(row=i, column=2, sticky="nsew")

                self.titlos_ssn = tk.Label(self.f_table, width=15, text=person["ar_tautothtas"], relief=tk.SUNKEN, borderwidth=1)
                self.titlos_ssn.grid(row=i, column=3, sticky="nsew")

                self.titlos_email = tk.Label(self.f_table, width=15, text=person["email"], relief=tk.SUNKEN, borderwidth=1)
                self.titlos_email.grid(row=i, column=4, sticky="nsew")

                self.titlos_telephone = tk.Label(self.f_table, width=10, text=person["thlefwno"], relief=tk.SUNKEN, borderwidth=1)
                self.titlos_telephone.grid(row=i, column=5, sticky="nsew")

                self.titlos_subscription = tk.Label(self.f_table, width=10, text=str(sub["id"])+". "+sub["onoma"], relief=tk.SUNKEN, borderwidth=1)
                self.titlos_subscription.grid(row=i, column=6, sticky="nsew")

                self.titlos_choose_programs = tk.Label(self.f_table, width=10, text=my_programs, relief=tk.SUNKEN, borderwidth=1)
                self.titlos_choose_programs.grid(row=i, column=7, sticky="nsew")

                i+=1

            self.f_table.grid_columnconfigure(1, weight=1)
            self.f_table.grid_columnconfigure(2, weight=1)
            self.f_table.grid_columnconfigure(3, weight=1)
            self.f_table.grid_columnconfigure(4, weight=1)
            self.f_table.grid_columnconfigure(5, weight=1)
            self.f_table.grid_columnconfigure(6, weight=1)
            self.f_table.grid_columnconfigure(7, weight=1)
            # invisible row after last row gets all extra space
            self.f_table.grid_rowconfigure(i+1, weight=1)


    def add_customer(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΠροσθήκη Πελάτη")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_name = tk.Frame(root)
        self.f_name.pack()
        self.name_label = tk.Label(self.f_name, font=self.medium_font, text="Όνομα: ")
        self.name_label.pack(side='left')
        self.name_box = tk.Entry(self.f_name, font=self.medium_font, width=20)
        self.name_box.pack(side='left')
        
        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()
        
        self.f_surname = tk.Frame(root)
        self.f_surname.pack()
        self.surname_label = tk.Label(self.f_surname, font=self.medium_font, text="Επώνυμο: ")
        self.surname_label.pack(side='left')
        self.surname_box = tk.Entry(self.f_surname, font=self.medium_font, width=20)
        self.surname_box.pack(side='right')

        self.f_blank2 = tk.Frame(root)
        self.f_blank2.pack()
        self.blanklabel2=tk.Label(self.f_blank2,text="\n")
        self.blanklabel2.pack()

        self.f_sex = tk.Frame(root)
        self.f_sex.pack()
        self.sex_label = tk.Label(self.f_sex, font=self.medium_font, text="Φύλο: ")
        self.sex_label.pack(side="left")
        self.sex = tk.StringVar(root)
        self.sex.set("Άνδρας")
        self.sex_box = tk.OptionMenu(self.f_sex, self.sex, "Άνδρας", "Γυναίκα")
        self.sex_box.pack(side="left")

        self.f_blank2_5 = tk.Frame(root)
        self.f_blank2_5.pack()
        self.blanklabel2_5=tk.Label(self.f_blank2_5,text="\n")
        self.blanklabel2_5.pack()

        self.f_ssn = tk.Frame(root)
        self.f_ssn.pack()
        self.ssn_label = tk.Label(self.f_ssn, font=self.medium_font, text="Αριθμός Ταυτότητας: ")
        self.ssn_label.pack(side='left')
        self.ssn_box = tk.Entry(self.f_ssn, font=self.medium_font, width=20)
        self.ssn_box.pack(side='left')

        self.f_blank3 = tk.Frame(root)
        self.f_blank3.pack()
        self.blanklabel3=tk.Label(self.f_blank3,text="\n")
        self.blanklabel3.pack()

        self.f_address = tk.Frame(root)
        self.f_address.pack()
        self.address_label = tk.Label(self.f_address, font=self.medium_font, text="Διεύθυνση: ")
        self.address_label.pack(side='left')
        self.address_box = tk.Entry(self.f_address, font=self.medium_font, width=20)
        self.address_box.pack(side='left')

        self.f_blank4 = tk.Frame(root)
        self.f_blank4.pack()
        self.blanklabel4=tk.Label(self.f_blank4,text="\n")
        self.blanklabel4.pack()

        self.f_telephone = tk.Frame(root)
        self.f_telephone.pack()
        self.telephone_label = tk.Label(self.f_telephone, font=self.medium_font, text="Τηλέφωνο: ")
        self.telephone_label.pack(side='left')
        self.telephone_box = tk.Entry(self.f_telephone, font=self.medium_font, width=20)
        self.telephone_box.pack(side='left')

        self.f_blank5 = tk.Frame(root)
        self.f_blank5.pack()
        self.blanklabel5=tk.Label(self.f_blank5,text="\n")
        self.blanklabel5.pack()

        self.f_email = tk.Frame(root)
        self.f_email.pack()
        self.email_label = tk.Label(self.f_email, font=self.medium_font, text="Email: ")
        self.email_label.pack(side='left')
        self.email_box = tk.Entry(self.f_email, font=self.medium_font, width=20)
        self.email_box.pack(side='left')        

        self.f_blank6 = tk.Frame(root)
        self.f_blank6.pack()
        self.blanklabel6=tk.Label(self.f_blank6,text="\n")
        self.blanklabel6.pack()

        self.f_register = tk.Frame(root)
        self.f_register.pack()
        self.register_button = tk.Button(self.f_register, text="Προσθήκη Πελάτη", font=self.medium_font, width=20, command=self.add_customer_event)
        self.register_button.pack(side="left")

    
    def add_customer_event(self):
        flag = checking.register(self.name_box.get(), self.surname_box.get(), self.ssn_box.get(), self.address_box.get(), self.email_box.get(), self.telephone_box.get(), "admin0", "admin0")
        if flag == True:
            flag = q.add_customer(self.cursor, self.name_box.get(), self.surname_box.get(), self.sex.get(), self.ssn_box.get(), self.address_box.get(), self.email_box.get(), self.telephone_box.get())
            if flag == 0:
                tkm.showinfo(title="Προσθήκη Πελάτη", message="Η προσθήκη ήταν επιτυχής")
                self.page_transition_secretary(3)
            elif flag == 1:
                tkm.showinfo(title="Προσθήκη Πελάτη", message="Ο πελάτης υπάρχει ήδη στη βάση δεδομένων")
            else:
                tkm.showerror(title="Prosu;hkh", message="Η εγγραφή δεν ήταν επιτυχής.\nΠαρακαλούμε προσπαθήστε αργότερα")


    def new_match(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΠροσθήκη Αγώνα")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_id_player1 = tk.Frame(root)
        self.f_id_player1.pack(anchor="nw")
        self.id_player1_label = tk.Label(self.f_id_player1,font=self.medium_font,text="ID: ")
        self.id_player1_label.pack(side="left")
        self.id_player1_text = tk.Entry(self.f_id_player1, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.id_player1_text.pack(side="left")

        choice = tk.StringVar(root)
        choice.set("---")
        self.f_opponent_choice = tk.Frame(root)
        self.f_opponent_choice.pack(anchor="nw")
        self.opponent_choice_label = tk.Label(self.f_opponent_choice,font=self.medium_font,text="Ο αντίπαλος είναι: ")
        self.opponent_choice_label.pack(side="left")
        self.opponent_choice_text = tk.OptionMenu(self.f_opponent_choice, choice, "---", "Μέλος", "Πελάτης", "Τίποτα από τα παραπάνω", command=lambda _: self.player2_fields(choice.get()))
        self.opponent_choice_text.pack(side="left")

        self.f_player2 = tk.Frame(root)
        self.f_player2.pack(anchor="nw")

        self.f_player2_1 = tk.Frame(self.f_player2)
        self.f_player2_1.pack(anchor="nw")

        self.f_date = tk.Frame(root)
        self.f_date.pack(anchor="nw")
        self.date_label = tk.Label(self.f_date,font=self.medium_font,text="Ημερομηνία: ")
        self.date_label.pack(side="left")
        self.date_text = tk.Entry(self.f_date, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.date_text.pack(side="left")

        self.f_time = tk.Frame(root)
        self.f_time.pack(anchor="nw")
        self.time_label = tk.Label(self.f_time,font=self.medium_font,text="Ώρα: ")
        self.time_label.pack(side="left")
        self.time_text = tk.Entry(self.f_time, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.time_text.pack(side="left")


        row = q.all_fields(self.cursor)
        OPTIONS = ["-"]
        for x in row:
            x = dict(x)
            OPTIONS.append(str(x["fieldid"])+" ("+x["tupos"]+")")
        OPTIONS.pop(0)
        var = tk.StringVar(root)
        var.set(OPTIONS[0])

        self.f_fieldid = tk.Frame(root)
        self.f_fieldid.pack(anchor="nw")
        self.fieldid_label = tk.Label(self.f_fieldid,font=self.medium_font,text="Γήπεδο: ")
        self.fieldid_label.pack(side="left")
        self.fieldid_text = tk.OptionMenu(self.f_fieldid, var, *OPTIONS)
        self.fieldid_text.pack(side="left")

        self.f_add_button = tk.Frame(root)
        self.f_add_button.pack()
        self.add_button = tk.Button(self.f_add_button, text="Προσθήκη Αγώνα", font=self.medium_font, width=20, command=lambda: self.add_match_event(choice.get(), var.get()))
        self.add_button.pack()


    def player2_fields(self, choice):
        if choice ==  "Μέλος" or choice == "Πελάτης":
            self.f_player2_1.destroy()

            self.f_player2_1 = tk.Frame(self.f_player2)
            self.f_player2_1.pack(anchor="nw")

            self.f_player2_id = tk.Frame(self.f_player2_1)
            self.f_player2_id.pack(anchor="nw")
            self.player2_id_label = tk.Label(self.f_player2_id,font=self.medium_font,text="ID Αντιπάλου: ")
            self.player2_id_label.pack(side="left")
            self.player2_id_text = tk.Entry(self.f_player2_id, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
            self.player2_id_text.pack(side="left")


        elif choice == "Τίποτα από τα παραπάνω":
            self.f_player2_1.destroy()

            self.f_player2_1 = tk.Frame(self.f_player2)
            self.f_player2_1.pack(anchor="nw")

            self.f_player2_name = tk.Frame(self.f_player2_1)
            self.f_player2_name.pack(anchor="nw")
            self.player2_name_label = tk.Label(self.f_player2_name,font=self.medium_font,text="Όνομα Αντιπάλου: ")
            self.player2_name_label.pack(side="left")
            self.player2_name_text = tk.Entry(self.f_player2_name, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
            self.player2_name_text.pack(side="left")

            self.f_player2_surname = tk.Frame(self.f_player2_1)
            self.f_player2_surname.pack(anchor="nw")
            self.player2_surname_label = tk.Label(self.f_player2_surname,font=self.medium_font,text="Επώνυμο Αντιπάλου: ")
            self.player2_surname_label.pack(side="left")
            self.player2_surname_text = tk.Entry(self.f_player2_surname, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
            self.player2_surname_text.pack(side="left")


    def add_match_event(self, player2, fieldid):
        if fieldid != "-" and player2 != "---":
            flag = q.is_a_customer(self.cursor, self.id_player1_text.get())
            if flag == False:
                tkm.showerror(title="Προσθήκη Αγώνα", message="Δεν υπάρχει πελάτης ή μέλος με ID: "+self.id_player1_text.get())
            else:
                if player2 == "Μέλος" or player2 == "Πελάτης":
                    flag = q.is_a_customer(self.cursor, self.player2_id_text.get())
                    if flag == False:
                        tkm.showerror(title="Προσθήκη Αγώνα", message="Δεν υπάρχει πελάτης ή μέλος με ID: "+self.player2_id_text.get())
                    else:
                        flag = q.add_match_2_ids(self.cursor, self.id_player1_text.get(), self.player2_id_text.get(), self.date_text.get(), self.time_text.get(), fieldid[0])
                        if flag == False:
                            tkm.showerror(title="Προσθήκη Αγώνα", message="Ο αγώνας δεν προστέθηκε")
                        else:
                            tkm.showinfo(title="Προσθήκη Αγώνα", message="Ο αγώνας προστέθηκε με επιτυχία")
                            self.page_transition_secretary(4)
                elif player2 == "Τίποτα από τα παραπάνω":
                    flag = q.add_match_1_id(self.cursor, self.id_player1_text.get(), self.player2_name_text.get(), self.player2_surname_text.get(), self.date_text.get(), self.time_text.get(), fieldid)
                    if flag == False:
                        tkm.showerror(title="Προσθήκη Αγώνα", message="Ο αγώνας δεν προστέθηκε")
                    else:
                        tkm.showinfo(title="Προσθήκη Αγώνα", message="Ο αγώνας προστέθηκε με επιτυχία")
                        self.page_transition_secretary(4)


    def new_rent(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΕνοικίαση Γηπέδου")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_id_player1 = tk.Frame(root)
        self.f_id_player1.pack(anchor="nw")
        self.id_player1_label = tk.Label(self.f_id_player1,font=self.medium_font,text="ID: ")
        self.id_player1_label.pack(side="left")
        self.id_player1_text = tk.Entry(self.f_id_player1, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.id_player1_text.pack(side="left")

        self.f_player2_id = tk.Frame(root)
        self.f_player2_id.pack(anchor="nw")
        self.player2_id_label = tk.Label(self.f_player2_id,font=self.medium_font,text="ID Αντιπάλου: ")
        self.player2_id_label.pack(side="left")
        self.player2_id_text = tk.Entry(self.f_player2_id, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.player2_id_text.pack(side="left")

        self.f_date = tk.Frame(root)
        self.f_date.pack(anchor="nw")
        self.date_label = tk.Label(self.f_date,font=self.medium_font,text="Ημερομηνία: ")
        self.date_label.pack(side="left")
        self.date_text = tk.Entry(self.f_date, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.date_text.pack(side="left")


        hours = tk.StringVar(root)
        minutes = tk.StringVar(root)
        OPTIONS_H = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        OPTIONS_M = ["00"]
        hours.set(OPTIONS_H[0])
        minutes.set(OPTIONS_M[0])
        self.f_time = tk.Frame(root)
        self.f_time.pack(anchor="nw")
        self.time_label = tk.Label(self.f_time,font=self.medium_font,text="Ώρα: ")
        self.time_label.pack(side="left")
        self.time_text_h = tk.OptionMenu(self.f_time, hours, *OPTIONS_H)
        self.time_text_h.pack(side="left")
        self.time_label2 = tk.Label(self.f_time,font=self.medium_font,text=":")
        self.time_label2.pack(side="left")
        self.time_text_m = tk.OptionMenu(self.f_time, minutes, *OPTIONS_M)
        self.time_text_m.pack(side="left")

        duration = tk.StringVar(root)
        duration.set("1 ώρα")
        self.f_duration = tk.Frame(root)
        self.f_duration.pack(anchor="nw")
        self.duration_label = tk.Label(self.f_duration,font=self.medium_font,text="Διάρκεια: ")
        self.duration_label.pack(side="left")
        self.duration_text = tk.OptionMenu(self.f_duration, duration, "1 ώρα", "2 ώρες", "3 ώρες")
        self.duration_text.pack(side="left")

        self.f_available_fields = tk.Frame(root)
        self.f_available_fields.pack(anchor="nw")
        self.available_fields_button = tk.Button(self.f_available_fields, text="Αναζήτηση Γηπέδου", font=self.medium_font, width=20, command=lambda: self.available_fields(self.date_text.get(), hours.get()+":"+minutes.get(), duration.get()))
        self.available_fields_button.pack()

        self.f_fieldid = tk.Frame(root)
        self.f_fieldid.pack(anchor="nw")
        self.f_fieldid2 = tk.Frame(self.f_fieldid)
        self.f_fieldid2.pack(anchor="nw")

        self.f_add_button = tk.Frame(root)
        self.f_add_button.pack()
        

    def available_fields(self, date, time, duration):

        flag = checking.add_rent(date)
        if flag == True:
            num_day = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%w')

            self.f_fieldid2.destroy()
            self.f_add_button.destroy()
            self.f_fieldid2 = tk.Frame(self.f_fieldid)
            self.f_fieldid2.pack(anchor="nw")
            self.f_add_button = tk.Frame(root)
            self.f_add_button.pack()
            
            row = q.available_fields(self.cursor, date, num_day, time, duration)
            OPTIONS = ["-"]
            for x in row:
                x = dict(x)
                OPTIONS.append(str(x["fieldid"])+" - "+x["tupos"]+" - "+str(x["timh/h"])+"€/ώρα")
            if len(OPTIONS) > 1:
                OPTIONS.pop(0)
            var = tk.StringVar(root)
            var.set(OPTIONS[0])
            self.fieldid_label = tk.Label(self.f_fieldid2,font=self.medium_font,text="Γήπεδο: ")
            self.fieldid_label.pack(side="left")
            self.fieldid_text = tk.OptionMenu(self.f_fieldid2, var, *OPTIONS, command= lambda _: self.count_cost(var.get(), duration))
            self.fieldid_text.pack(side="left")
            
            self.cost = tk.StringVar(root)
            self.count_cost(OPTIONS[0], duration)
            self.blank = tk.Label(self.f_fieldid2,font=self.medium_font,text="   ")
            self.blank.pack(side="left")
            self.cost_label = tk.Label(self.f_fieldid2,font=self.medium_font,textvariable=self.cost)
            self.cost_label.pack(side="left")

            self.add_button = tk.Button(self.f_add_button, text="Ενικοίαση Γηπέδου", font=self.medium_font, width=20, command=lambda: self.add_rent_event(var.get(), date, num_day, time, duration))
            self.add_button.pack()


    def count_cost(self, field, duration):
        self.cost.set(str(float((field[-8:-5]))*int(duration[0]))+" €/άτομο")


    def add_rent_event(self, field, date, num_day, time, duration):
        if field != "-":
            flag = q.is_a_customer(self.cursor, self.id_player1_text.get())
            if flag == False:
                tkm.showerror(title="Ενοικίαση Γηπέδου", message="Δεν υπάρχει πελάτης ή μέλος με ID: "+self.id_player1_text.get())
            else:
                flag = q.is_a_customer(self.cursor, self.player2_id_text.get())
                if flag == False:
                    tkm.showerror(title="Ενοικίαση Γηπέδου", message="Δεν υπάρχει πελάτης ή μέλος με ID: "+self.player2_id_text.get())
                else:
                    flag = q.add_match_2_ids(self.cursor, self.id_player1_text.get(), self.player2_id_text.get(), date, time, field[0])
                    
                    if flag == False:
                        tkm.showerror(title="Ενοικίαση Γηπέδου", message="Η ενοικίαση δεν καταχωρήθηκε")
                    else:
                        flag = q.add_rent(self.cursor, field[0], self.id_player1_text.get(), date, time, duration[0])
                        if flag == False:
                            tkm.showerror(title="Ενοικίαση Γηπέδου", message="Η ενοικίαση δεν καταχωρήθηκε")
                        else:
                            flag1 = q.add_transaction(self.cursor, self.id_player1_text.get(), 0, int(float(field[-8:-5]))*int(duration[0]), "Ενοικίαση", "24%", "-", int(float(field[-8:-5]))*int(duration[0]))
                            flag2 = q.add_transaction(self.cursor, self.player2_id_text.get(), 0, int(float(field[-8:-5]))*int(duration[0]), "Ενοικίαση", "24%", "-", int(float(field[-8:-5]))*int(duration[0]))
                            if flag1 == False or flag2 == False:
                                tkm.showerror(title="Ενοικίαση Γηπέδου", message="Μία ή περισσότερες συναλλαγές δεν καταχωρήθηκαν")
                            else:
                                tkm.showinfo(title="Ενοικίαση Γηπέδου", message="Η ενοικίαση καταχωρήθηκε με επιτυχία")
                                self.page_transition_secretary(5)


    def add_new_transaction(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΠροσθήκης Συναλλαγής")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_id = tk.Frame(root)
        self.f_id.pack()
        self.id_label = tk.Label(self.f_id, font=self.medium_font, text="ID: ")
        self.id_label.pack(side='left')
        self.id_box = tk.Entry(self.f_id, font=self.medium_font, width=20)
        self.id_box.pack(side='left')
        
        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()
        
        self.f_deposit = tk.Frame(root)
        self.f_deposit.pack()
        self.deposit_label = tk.Label(self.f_deposit, font=self.medium_font, text="Καταβληθέν Ποσό: ")
        self.deposit_label.pack(side='left')
        self.deposit_box = tk.Entry(self.f_deposit, font=self.medium_font, width=20)
        self.deposit_box.pack(side='right')

        self.f_blank2 = tk.Frame(root)
        self.f_blank2.pack()
        self.blanklabel2=tk.Label(self.f_blank2,text="\n")
        self.blanklabel2.pack()

        self.f_reason = tk.Frame(root)
        self.f_reason.pack()
        self.reason_label = tk.Label(self.f_reason, font=self.medium_font, text="Είδος Παροχής: ")
        self.reason_label.pack(side="left")
        self.reason_box = tk.Entry(self.f_reason, font=self.medium_font, width=20)
        self.reason_box.pack(side="left")

        self.f_blank2_5 = tk.Frame(root)
        self.f_blank2_5.pack()
        self.blanklabel2_5=tk.Label(self.f_blank2_5,text="\n")
        self.blanklabel2_5.pack()

        self.f_fpa = tk.Frame(root)
        self.f_fpa.pack()
        self.fpa_label = tk.Label(self.f_fpa, font=self.medium_font, text="ΦΠΑ (%): ")
        self.fpa_label.pack(side='left')
        fpa = tk.StringVar(root)
        fpa.set("24")
        self.fpa_box = tk.Entry(self.f_fpa, font=self.medium_font, width=20, textvariable=fpa)
        self.fpa_box.pack(side='left')

        self.f_blank3 = tk.Frame(root)
        self.f_blank3.pack()
        self.blanklabel3=tk.Label(self.f_blank3,text="\n")
        self.blanklabel3.pack()

        self.f_payment_method = tk.Frame(root)
        self.f_payment_method.pack()
        self.payment_method_label = tk.Label(self.f_payment_method, font=self.medium_font, text="Τρόπος Πληρωμής: ")
        self.payment_method_label.pack(side='left')
        method = tk.StringVar(root)
        method.set("Μετρητά")
        self.payment_method_box = tk.OptionMenu(self.f_payment_method, method, "Μετρητά", "Χρεωστική/Πιστωτική Κάρτα", "Κατάθεση")
        self.payment_method_box.pack(side='left')

        self.f_blank4 = tk.Frame(root)
        self.f_blank4.pack()
        self.blanklabel4=tk.Label(self.f_blank4,text="\n")
        self.blanklabel4.pack()

        self.f_total_cost = tk.Frame(root)
        self.f_total_cost.pack()
        self.total_cost_label = tk.Label(self.f_total_cost, font=self.medium_font, text="Αρχικό Συνολικό Ποσό: ")
        self.total_cost_label.pack(side='left')
        self.total_cost_box = tk.Entry(self.f_total_cost, font=self.medium_font, width=20)
        self.total_cost_box.pack(side='left')

        self.f_blank5 = tk.Frame(root)
        self.f_blank5.pack()
        self.blanklabel5=tk.Label(self.f_blank5,text="\n")
        self.blanklabel5.pack()

        self.f_submit = tk.Frame(root)
        self.f_submit.pack()
        self.submit_button = tk.Button(self.f_submit, text="Υποβολή", font=self.medium_font, width=20, command=lambda: self.add_new_transaction_event(self.id_box.get(), self.deposit_box.get(), self.reason_box.get(), fpa.get(), method.get(), self.total_cost_box.get()))
        self.submit_button.pack(side="left")

    
    def add_new_transaction_event(self, id_customer, deposit, reason, fpa, payment, total_cost):
        flag, total_cost, deposit = checking.add_transaction(id_customer, deposit, reason, fpa, total_cost)
        if flag == True:
            flag = q.is_a_customer(self.cursor, id_customer)
            if flag == False:
                tkm.showerror(title="Υποβολή Συναλλαγής", message="Δεν υπάρχει πελάτης με ID: "+id_customer)
            else:
                flag = q.add_transaction(self.cursor, id_customer, deposit, str(float(total_cost)-float(deposit)), reason, fpa, payment, total_cost)
                if flag == True:
                    tkm.showinfo(title="Υποβολή Συναλλαγής", message="Η συναλλαγή υπεβλήθη με επιτυχία")
                    self.page_transition_secretary(6)
                else:
                    tkm.showerror(title="Υποβολή Συναλλαγής", message="Αποτυχία υποβολής συναλλαγής")


    def pending_transaction(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΕκκρεμείς Συναλλαγές")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_by_id = tk.Frame(root)
        self.f_by_id.pack(anchor="nw")
        self.id_label = tk.Label(self.f_by_id,font=self.medium_font,text="ID: ")
        self.id_label.pack(side="left")
        self.search_id_text = tk.Entry(self.f_by_id, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.search_id_text.pack(side="left")

        self.f_button = tk.Frame(root)
        self.f_button.pack(anchor="nw")
        self.search_member_button = tk.Button(self.f_button, text="Αναζήτηση", font=self.medium_font, width=10, command=lambda: self.find_pending_transaction(self.search_id_text.get()))
        self.search_member_button.pack()

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)


    def find_pending_transaction(self, id_customer):
        if id_customer == "":
            flag = True
        else:
            flag = q.is_a_customer(self.cursor, id_customer)
        if flag == False:
            self.f_table.destroy()
            
            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.data_id = tk.Label(self.f_table, text="Δεν βρέθηκε πελάτης με ID: "+id_customer, font=self.medium_font)
            self.data_id.pack()
        else:
            if id_customer == "":
                row = q.find_all_pending_transactions(self.cursor)
            else:
                row = q.find_pending_transactions_by_id(self.cursor, id_customer)


            if row is None:
                self.f_table.destroy()
                
                self.f_table = tk.Frame(root)
                self.f_table.pack(side="top", fill="both", expand=True)

                self.data_id = tk.Label(self.f_table, text="Δεν βρέθηκε συναλλαγή για το συγκεκριμένο πελάτη", font=self.medium_font)
                self.data_id.pack()
            elif len(row) == 0:
                self.f_table.destroy()
                
                self.f_table = tk.Frame(root)
                self.f_table.pack(side="top", fill="both", expand=True)

                self.data_id = tk.Label(self.f_table, text="Δεν βρέθηκε συναλλαγή για το συγκεκριμένο πελάτη", font=self.medium_font)
                self.data_id.pack()
            else:
                self.f_table.destroy()

                self.f_table = tk.Frame(root)
                self.f_table.pack(side="top", fill="both", expand=True)

                self.titlos_id = tk.Label(self.f_table, width=18, text="Κωδικός Συναλλαγής", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_id.grid(row=0, column=0, sticky="nsew")

                self.titlos_id_customer = tk.Label(self.f_table, width=15, text="ID Πελάτη", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_id_customer.grid(row=0, column=1, sticky="nsew")

                self.titlos_deposit = tk.Label(self.f_table, width=20, text="Καταβληθέν Ποσό (€)", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_deposit.grid(row=0, column=2, sticky="nsew")

                self.titlos_remain = tk.Label(self.f_table, width=10, text="Υπόλοιπο (€)", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_remain.grid(row=0, column=3, sticky="nsew")

                self.titlos_reason = tk.Label(self.f_table, width=15, text="Είδος Παροχής", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_reason.grid(row=0, column=4, sticky="nsew")

                self.titlos_total_cost = tk.Label(self.f_table, width=15, text="Αρχικό Συνολικό Ποσό (€)", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_total_cost.grid(row=0, column=5, sticky="nsew")

                self.titlos_date = tk.Label(self.f_table, width=10, text="Ημερομηνία", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_date.grid(row=0, column=6, sticky="nsew")

                self.titlos_date = tk.Label(self.f_table, width=10, text="Ώρα", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_date.grid(row=0, column=7, sticky="nsew")

                i=1
                for tr in row:
                    tr = dict(tr)
                    self.titlos_id = tk.Label(self.f_table, width=18, text=str(tr["id_sunallaghs"]), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_id.grid(row=i, column=0, sticky="nsew")

                    self.titlos_id_customer = tk.Label(self.f_table, width=15, text=str(tr["id_pelath"]), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_id_customer.grid(row=i, column=1, sticky="nsew")

                    self.titlos_deposit = tk.Label(self.f_table, width=20, text=str(tr["katavlh8en_poso"]), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_deposit.grid(row=i, column=2, sticky="nsew")

                    self.titlos_remain = tk.Label(self.f_table, width=10, text=str(tr["upoloipo"]), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_remain.grid(row=i, column=3, sticky="nsew")

                    self.titlos_reason = tk.Label(self.f_table, width=15, text=tr["eidos_paroxhs"], relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_reason.grid(row=i, column=4, sticky="nsew")

                    self.titlos_total_cost = tk.Label(self.f_table, width=15, text=str(tr["timh"]), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_total_cost.grid(row=i, column=5, sticky="nsew")

                    self.titlos_date = tk.Label(self.f_table, width=10, text=tr["hmeromhnia"], relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_date.grid(row=i, column=6, sticky="nsew")

                    self.titlos_time = tk.Label(self.f_table, width=10, text=tr["wra"], relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_time.grid(row=i, column=7, sticky="nsew")

                    i+=1

                self.f_table.grid_columnconfigure(1, weight=1)
                self.f_table.grid_columnconfigure(2, weight=1)
                self.f_table.grid_columnconfigure(3, weight=1)
                self.f_table.grid_columnconfigure(4, weight=1)
                self.f_table.grid_columnconfigure(5, weight=1)
                self.f_table.grid_columnconfigure(6, weight=1)
                self.f_table.grid_columnconfigure(7, weight=1)
                # invisible row after last row gets all extra space
                self.f_table.grid_rowconfigure(i+1, weight=1)


    def update_transaction(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΕνημέρωση Συναλλαγής")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_by_id = tk.Frame(root)
        self.f_by_id.pack(anchor="nw")
        self.id_label = tk.Label(self.f_by_id,font=self.medium_font,text="Κωδικός Συναλλαγής: ")
        self.id_label.pack(side="left")
        self.search_id_text = tk.Entry(self.f_by_id, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.search_id_text.pack(side="left")

        self.f_button = tk.Frame(root)
        self.f_button.pack(anchor="nw")
        self.search_member_button = tk.Button(self.f_button, text="Αναζήτηση", font=self.medium_font, width=10, command=lambda: self.update_transaction_event(self.search_id_text.get()))
        self.search_member_button.pack()

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

        self.f_button_submit = tk.Frame(root)
        self.f_button_submit.pack()


    def update_transaction_event(self, id_tr):
        
        row = q.find_pending_transactions_by_code(self.cursor, id_tr)


        if row is None:
            self.f_table.destroy()
            self.f_button_submit.destroy()

            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.f_button_submit = tk.Frame(root)
            self.f_button_submit.pack()

            self.data_id = tk.Label(self.f_table, text="Δεν βρέθηκε εκκρεμή συναλλαγή με κωδικό: "+id_tr, font=self.medium_font)
            self.data_id.pack()
        else:
            self.f_table.destroy()
            self.f_button_submit.destroy()

            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.f_button_submit = tk.Frame(root)
            self.f_button_submit.pack()

            self.titlos_id = tk.Label(self.f_table, width=18, text="Κωδικός Συναλλαγής", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=0, column=0, sticky="nsew")

            self.titlos_id_customer = tk.Label(self.f_table, width=15, text="ID Πελάτη", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id_customer.grid(row=0, column=1, sticky="nsew")

            self.titlos_deposit = tk.Label(self.f_table, width=20, text="Καταβληθέν Ποσό (€)", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_deposit.grid(row=0, column=2, sticky="nsew")

            self.titlos_remain = tk.Label(self.f_table, width=10, text="Υπόλοιπο (€)", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_remain.grid(row=0, column=3, sticky="nsew")

            self.titlos_reason = tk.Label(self.f_table, width=15, text="Είδος Παροχής", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_reason.grid(row=0, column=4, sticky="nsew")

            self.titlos_total_cost = tk.Label(self.f_table, width=18, text="Αρχικό Συνολικό Ποσό (€)", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_total_cost.grid(row=0, column=5, sticky="nsew")

            self.titlos_date = tk.Label(self.f_table, width=10, text="Ημερομηνία", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_date.grid(row=0, column=6, sticky="nsew")

            self.titlos_date = tk.Label(self.f_table, width=10, text="Ώρα", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_date.grid(row=0, column=7, sticky="nsew")

            self.titlos_new_deposit = tk.Label(self.f_table, width=20, text="Νέο Καταβληθέν Ποσό (€)", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_new_deposit.grid(row=0, column=8, sticky="nsew")

            self.titlos_new_deposit = tk.Label(self.f_table, width=20, text="Τρόπος Πληρωμής", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_new_deposit.grid(row=0, column=9, sticky="nsew")

            i=1

            tr = dict(row)
            self.titlos_id = tk.Label(self.f_table, width=18, text=str(tr["id_sunallaghs"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=i, column=0, sticky="nsew")

            self.titlos_id_customer = tk.Label(self.f_table, width=15, text=str(tr["id_pelath"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id_customer.grid(row=i, column=1, sticky="nsew")

            self.titlos_deposit = tk.Label(self.f_table, width=20, text=str(tr["katavlh8en_poso"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_deposit.grid(row=i, column=2, sticky="nsew")

            self.titlos_remain = tk.Label(self.f_table, width=10, text=str(tr["upoloipo"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_remain.grid(row=i, column=3, sticky="nsew")

            self.titlos_reason = tk.Label(self.f_table, width=15, text=tr["eidos_paroxhs"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_reason.grid(row=i, column=4, sticky="nsew")

            self.titlos_total_cost = tk.Label(self.f_table, width=18, text=str(tr["timh"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_total_cost.grid(row=i, column=5, sticky="nsew")

            self.titlos_date = tk.Label(self.f_table, width=10, text=tr["hmeromhnia"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_date.grid(row=i, column=6, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text=tr["wra"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=i, column=7, sticky="nsew")


            new_deposit = tk.StringVar(root)
            new_deposit.set(0.0)
            self.titlos_new_deposit = tk.Entry(self.f_table, width=20, textvariable = new_deposit, relief=tk.SUNKEN, borderwidth=1)
            self.titlos_new_deposit.grid(row=i, column=8, sticky="nsew")

            method = tk.StringVar(root)
            method.set("Μετρητά")
            self.payment_method_box = tk.OptionMenu(self.f_table, method, "Μετρητά", "Χρεωστική/Πιστωτική Κάρτα", "Κατάθεση")
            self.payment_method_box.grid(row=i, column=9, sticky="nsew")

            i+=1

            self.f_table.grid_columnconfigure(1, weight=1)
            self.f_table.grid_columnconfigure(2, weight=1)
            self.f_table.grid_columnconfigure(3, weight=1)
            self.f_table.grid_columnconfigure(4, weight=1)
            self.f_table.grid_columnconfigure(5, weight=1)
            self.f_table.grid_columnconfigure(6, weight=1)
            self.f_table.grid_columnconfigure(7, weight=1)
            self.f_table.grid_columnconfigure(8, weight=1)
            self.f_table.grid_columnconfigure(9, weight=1)
            
            # invisible row after last row gets all extra space
            self.f_table.grid_rowconfigure(i+1, weight=1)

            self.button_submit = tk.Button(self.f_button_submit, text="Ενημέρωση Συναλλαγής", font=self.medium_font, width=20, command=lambda: self.submit_updated_transaction(tr["id_sunallaghs"], tr["katavlh8en_poso"], new_deposit.get(), tr["upoloipo"], method.get()))
            self.button_submit.pack()


    def submit_updated_transaction(self, id_tr, old_deposit, new_deposit, remain, method):
        flag, new_deposit = checking.new_deposit(new_deposit, remain)
        if flag == True:
            flag = q.submit_updated_transaction(self.cursor, id_tr, old_deposit, new_deposit, remain, method)
            if flag == True:
                tkm.showinfo(title="Ενημέρωση Συναλλαγής", message="Η συναλλαγή ενημερώθηκε με επιτυχία")
                self.page_transition_secretary(8)
            else:
                tkm.showerror(title="Ενημέρωση Συναλλαγής", message="Αποτυχία ενημέρωση συναλλαγής")


    def completed_transaction(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΟλοκληρωμένες Συναλλαγές")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_by_id = tk.Frame(root)
        self.f_by_id.pack(anchor="nw")
        self.id_label = tk.Label(self.f_by_id,font=self.medium_font,text="ID: ")
        self.id_label.pack(side="left")
        self.search_id_text = tk.Entry(self.f_by_id, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.search_id_text.pack(side="left")

        self.f_button = tk.Frame(root)
        self.f_button.pack(anchor="nw")
        self.search_member_button = tk.Button(self.f_button, text="Αναζήτηση", font=self.medium_font, width=10, command=lambda: self.find_completed_transaction(self.search_id_text.get()))
        self.search_member_button.pack()

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)


    def find_completed_transaction(self, id_customer):
        if id_customer == "":
            flag = True
        else:
            flag = q.is_a_customer(self.cursor, id_customer)
        if flag == False:
            self.f_table.destroy()
            
            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.data_id = tk.Label(self.f_table, text="Δεν βρέθηκε πελάτης με ID: "+id_customer, font=self.medium_font)
            self.data_id.pack()
        else:
            if id_customer == "":
                row = q.find_all_completed_transactions(self.cursor)
            else:
                row = q.find_completed_transactions_by_id(self.cursor, id_customer)


            if row is None:
                self.f_table.destroy()
                
                self.f_table = tk.Frame(root)
                self.f_table.pack(side="top", fill="both", expand=True)

                self.data_id = tk.Label(self.f_table, text="Δεν βρέθηκε συναλλαγή για το συγκεκριμένο πελάτη", font=self.medium_font)
                self.data_id.pack()
            elif len(row) == 0:
                self.f_table.destroy()
                
                self.f_table = tk.Frame(root)
                self.f_table.pack(side="top", fill="both", expand=True)

                self.data_id = tk.Label(self.f_table, text="Δεν βρέθηκε συναλλαγή για το συγκεκριμένο πελάτη", font=self.medium_font)
                self.data_id.pack()
            else:
                self.f_table.destroy()

                self.f_table = tk.Frame(root)
                self.f_table.pack(side="top", fill="both", expand=True)

                self.titlos_id = tk.Label(self.f_table, width=18, text="Κωδικός Συναλλαγής", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_id.grid(row=0, column=0, sticky="nsew")

                self.titlos_id_customer = tk.Label(self.f_table, width=15, text="ID Πελάτη", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_id_customer.grid(row=0, column=1, sticky="nsew")

                self.titlos_deposit = tk.Label(self.f_table, width=20, text="Καταβληθέν Ποσό (€)", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_deposit.grid(row=0, column=2, sticky="nsew")

                self.titlos_remain = tk.Label(self.f_table, width=10, text="Υπόλοιπο (€)", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_remain.grid(row=0, column=3, sticky="nsew")

                self.titlos_reason = tk.Label(self.f_table, width=15, text="Είδος Παροχής", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_reason.grid(row=0, column=4, sticky="nsew")

                self.titlos_total_cost = tk.Label(self.f_table, width=18, text="Αρχικό Συνολικό Ποσό (€)", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_total_cost.grid(row=0, column=5, sticky="nsew")

                self.titlos_date = tk.Label(self.f_table, width=10, text="Ημερομηνία", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_date.grid(row=0, column=6, sticky="nsew")

                self.titlos_date = tk.Label(self.f_table, width=10, text="Ώρα", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_date.grid(row=0, column=7, sticky="nsew")

                i=1
                for tr in row:
                    tr = dict(tr)
                    self.titlos_id = tk.Label(self.f_table, width=18, text=str(tr["id_sunallaghs"]), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_id.grid(row=i, column=0, sticky="nsew")

                    self.titlos_id_customer = tk.Label(self.f_table, width=15, text=str(tr["id_pelath"]), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_id_customer.grid(row=i, column=1, sticky="nsew")

                    self.titlos_deposit = tk.Label(self.f_table, width=20, text=str(tr["katavlh8en_poso"]), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_deposit.grid(row=i, column=2, sticky="nsew")

                    self.titlos_remain = tk.Label(self.f_table, width=10, text=str(tr["upoloipo"]), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_remain.grid(row=i, column=3, sticky="nsew")

                    self.titlos_reason = tk.Label(self.f_table, width=15, text=tr["eidos_paroxhs"], relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_reason.grid(row=i, column=4, sticky="nsew")

                    self.titlos_total_cost = tk.Label(self.f_table, width=18, text=str(tr["timh"]), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_total_cost.grid(row=i, column=5, sticky="nsew")

                    self.titlos_date = tk.Label(self.f_table, width=10, text=tr["hmeromhnia"], relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_date.grid(row=i, column=6, sticky="nsew")

                    self.titlos_time = tk.Label(self.f_table, width=10, text=tr["wra"], relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_time.grid(row=i, column=7, sticky="nsew")

                    i+=1

                self.f_table.grid_columnconfigure(1, weight=1)
                self.f_table.grid_columnconfigure(2, weight=1)
                self.f_table.grid_columnconfigure(3, weight=1)
                self.f_table.grid_columnconfigure(4, weight=1)
                self.f_table.grid_columnconfigure(5, weight=1)
                self.f_table.grid_columnconfigure(6, weight=1)
                self.f_table.grid_columnconfigure(7, weight=1)
                # invisible row after last row gets all extra space
                self.f_table.grid_rowconfigure(i+1, weight=1)



    # Cleaner ------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def create_menu_cleaner(self):
        self.menu = tk.Menu(root)
        self.exit = tk.Menu(self.menu, tearoff=0)
        self.menu.add_command(label="Προφίλ", command=lambda: self.page_transition_cleaner(0))
        self.menu.add_cascade(label="Έξοδος", menu=self.exit)
        self.exit.add_command(label="Αποσύνδεση", command=lambda: self.page_transition_cleaner(-1)) #status -1
        self.exit.add_separator()
        self.exit.add_command(label="Κλείσιμο Προγράμματος", command=self.quit_window)

        root.config(menu=self.menu)

    
    def page_transition_cleaner(self, next_status):
        if self.page_status == 0:
            self.menu.entryconfig("Προφίλ", state="normal")
            fd.view_profile_staff_destroyer(self)
        
        if next_status == -1:
            response=tkm.askyesno("Έξοδος","Σίγουρα θέλεις να αποσυνδεθείς;")
            if response == True:
                self.page_status = 0
                emptyMenu = tk.Menu(root)
                root.config(menu=emptyMenu)
                self.initial_screen()
            else:
                next_status = self.page_status

        self.page_status = next_status

        if self.page_status == 0:
            self.menu.entryconfig("Προφίλ", state="disabled")
            self.view_profile_staff()


    # Admin ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def logged_in_admin(self):
        self.page_status = 14
        fd.login_destroyer(self)
        self.create_menu_admin()
        self.menu.entryconfig("Κατάταξη", state="disabled")
        self.admin_ranking()


    def create_menu_admin(self):
        self.menu = tk.Menu(root)
        self.matches = tk.Menu(self.menu, tearoff=0)
        self.employees = tk.Menu(self.menu, tearoff=0)
        self.programs = tk.Menu(self.menu, tearoff=0)
        self.control = tk.Menu(self.menu, tearoff=0)
        self.transactions = tk.Menu(self.control, tearoff=0)
        self.exit = tk.Menu(self.menu, tearoff=0)


        self.menu.add_command(label="Κατάταξη",command= lambda: self.page_transition_admin(14))

        self.menu.add_command(label="Διαγραφή Μέλους",command= lambda: self.page_transition_admin(0)) 

        #self.menu.add_cascade(label="Αγώνες", menu=self.matches) 
        self.menu.add_cascade(label="Υπάλληλοι", menu=self.employees)
        #self.menu.add_cascade(label="Προγράμματα", menu=self.programs)
        self.menu.add_cascade(label="Έλεγχος", menu=self.control)

        

        self.menu.add_cascade(label="Έξοδος", menu=self.exit)


        #self.matches.add_command(label="Αφαίρεση Αγώνα", command = lambda: self.page_transition_admin(1)) 
        #self.matches.add_command(label="Αφαίρεση Ενοικίασης", command=lambda: self.page_transition_admin(2))

        self.employees.add_command(label="Προσθήκη Υπαλλήλου", command=lambda: self.page_transition_admin(3))
        self.employees.add_command(label="Αφαίρεση Υπαλλήλου", command= lambda: self.page_transition_admin(4))

        #self.programs.add_command(label="Προσθήκη Προγράμματος σε Γυμναστή", command= lambda: self.page_transition_admin(5))
        #self.programs.add_command(label="Αφαίρεση Προγράμματος από Γυμναστή", command= lambda: self.page_transition_admin(6))
        #self.programs.add_command(label="Προσθήκη Προγράμματος", command= lambda: self.page_transition_admin(7))
        #self.programs.add_command(label="Αφαίρεση Προγράμματος", command= lambda: self.page_transition_admin(8))

        self.control.add_command(label="Πελάτες", command= lambda: self.page_transition_admin(9))
        self.control.add_command(label="Μέλη", command= lambda: self.page_transition_admin(10))
        self.control.add_command(label="Υπάλληλοι", command= lambda: self.page_transition_admin(11))
        self.control.add_command(label="Ενοικιάσεις", command= lambda: self.page_transition_admin(12))

        self.control.add_cascade(label="Συναλλαγές", menu=self.transactions)
        self.transactions.add_command(label="Όλες", command= lambda: self.page_transition_admin(13))
        self.transactions.add_command(label="Εκκρεμείς", command= lambda: self.page_transition_admin(15))
        self.transactions.add_command(label="Ολοκληρωμένες", command= lambda: self.page_transition_admin(16))

        self.exit.add_command(label="Αποσύνδεση", command=lambda: self.page_transition_admin(-1)) #status -1
        self.exit.add_separator()
        self.exit.add_command(label="Κλείσιμο Προγράμματος", command=self.quit_window)

        root.config(menu=self.menu)


    def page_transition_admin(self, next_status):

        if self.page_status == 0:
            self.menu.entryconfig("Διαγραφή Μέλους", state="normal")
            fd.admin_delete_member_destroyer(self)

        if self.page_status == 3:
            self.employees.entryconfig("Προσθήκη Υπαλλήλου", state="normal")
            fd.admin_add_employee_destroyer(self)

        if self.page_status == 4:
            self.employees.entryconfig("Αφαίρεση Υπαλλήλου", state="normal")
            fd.admin_delete_employee_destroyer(self)

        if self.page_status == 9:
            self.control.entryconfig("Πελάτες", state="normal")
            fd.admin_customers_destroyer(self)

        if self.page_status == 10:
            self.control.entryconfig("Μέλη", state="normal")
            fd.admin_members_destroyer(self)

        if self.page_status == 11:
            self.control.entryconfig("Υπάλληλοι", state="normal")
            fd.admin_employees_destroyer(self)

        if self.page_status == 12:
            self.control.entryconfig("Ενοικιάσεις", state="normal")
            fd.admin_rent_destroyer(self)

        if self.page_status == 13:
            self.transactions.entryconfig("Όλες", state="normal")
            fd.admin_all_transactions_destroyer(self)

        if self.page_status == 14:
            self.menu.entryconfig("Κατάταξη", state="normal")
            fd.admin_ranking_destroyer(self)

        if self.page_status == 15:
            self.transactions.entryconfig("Εκκρεμείς", state="normal")
            fd.admin_all_transactions_destroyer(self)

        if self.page_status == 16:
            self.transactions.entryconfig("Ολοκληρωμένες", state="normal")
            fd.admin_all_transactions_destroyer(self)

        if next_status == -1:
            response=tkm.askyesno("Έξοδος","Σίγουρα θέλεις να αποσυνδεθείς;")
            if response == True:
                self.page_status = 0
                emptyMenu = tk.Menu(root)
                root.config(menu=emptyMenu)
                self.initial_screen()
            else:
                next_status = self.page_status

        self.page_status = next_status

        if self.page_status == 0:
            self.menu.entryconfig("Διαγραφή Μέλους", state="disabled")
            self.admin_delete_member()

        if self.page_status == 3:
            self.employees.entryconfig("Προσθήκη Υπαλλήλου", state="disabled")
            self.admin_add_employee()

        if self.page_status == 4:
            self.employees.entryconfig("Αφαίρεση Υπαλλήλου", state="disabled")
            self.admin_delete_employee()

        if self.page_status == 9:
            self.control.entryconfig("Πελάτες", state="disabled")
            self.admin_customers()

        if self.page_status == 10:
            self.control.entryconfig("Μέλη", state="disabled")
            self.admin_members()

        if self.page_status == 11:
            self.control.entryconfig("Υπάλληλοι", state="disabled")
            self.admin_employees()

        if self.page_status == 12:
            self.control.entryconfig("Ενοικιάσεις", state="disabled")
            self.admin_rent()

        if self.page_status == 13:
            self.transactions.entryconfig("Όλες", state="disabled")
            self.admin_all_transactions(0)

        if self.page_status == 14:
            self.menu.entryconfig("Κατάταξη", state="disabled")
            self.admin_ranking()

        if self.page_status == 15:
            self.transactions.entryconfig("Εκκρεμείς", state="disabled")
            self.admin_all_transactions(1)

        if self.page_status == 16:
            self.transactions.entryconfig("Ολοκληρωμένες", state="disabled")
            self.admin_all_transactions(2)

        
    def admin_ranking(self):
        row = q.admin_total_ranking(self.cursor)
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΚατάταξη")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_by_id = tk.Frame(root)
        self.f_by_id.pack(anchor="nw")
        self.id_label = tk.Label(self.f_by_id,font=self.medium_font,text="ID Μέλους: ")
        self.id_label.pack(side="left")
        self.search_id_text = tk.Entry(self.f_by_id, font=self.small_font, width=15, relief=tk.SUNKEN, borderwidth=1)
        self.search_id_text.pack(side="left")

        self.f_button = tk.Frame(root)
        self.f_button.pack(anchor="nw")
        self.search_member_button = tk.Button(self.f_button, text="Αναζήτηση", font=self.medium_font, width=10, command=lambda: self.admin_find_ranking(self.search_id_text.get(), row))
        self.search_member_button.pack()

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

    
    def admin_find_ranking(self, id_member, row):
        if id_member == "":
            flag = True
        else:
            flag = q.is_a_member(self.cursor, id_member)
        if flag == False:
            self.f_table.destroy()
            
            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.data_id = tk.Label(self.f_table, text="Δεν βρέθηκε μέλος με ID: "+id_member, font=self.medium_font)
            self.data_id.pack()
        else:
            if id_member == "":
                pos = 1
            else:
                pos = 1
                for x in row:
                    x = dict(x)
                    if x["memberid"] == int(id_member):
                        row = [{"memberid":x["memberid"], "onoma":x["onoma"], "epwnumo":x["epwnumo"], "total_wins":x["total_wins"], "total_matches":x["total_matches"], "win_ratio":x["win_ratio"]}]
                        break
                    pos+=1


            if row is None:
                self.f_table.destroy()
                
                self.f_table = tk.Frame(root)
                self.f_table.pack(side="top", fill="both", expand=True)

                self.data_id = tk.Label(self.f_table, text="Δεν βρέθηκε κατάταξη", font=self.medium_font)
                self.data_id.pack()
            elif len(row) == 0:
                self.f_table.destroy()
                
                self.f_table = tk.Frame(root)
                self.f_table.pack(side="top", fill="both", expand=True)

                self.data_id = tk.Label(self.f_table, text="Δεν βρέθηκε κατάταξη", font=self.medium_font)
                self.data_id.pack()
            else:
                self.f_table.destroy()

                self.f_table = tk.Frame(root)
                self.f_table.pack(side="top", fill="both", expand=True)

                self.titlos_enum = tk.Label(self.f_table, width=18, text="Α/Α", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_enum.grid(row=0, column=0, sticky="nsew")

                self.titlos_id = tk.Label(self.f_table, width=15, text="Member ID", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_id.grid(row=0, column=1, sticky="nsew")

                self.titlos_name = tk.Label(self.f_table, width=15, text="Όνομα", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_name.grid(row=0, column=2, sticky="nsew")

                self.titlos_surname = tk.Label(self.f_table, width=20, text="Επώνυμο", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_surname.grid(row=0, column=3, sticky="nsew")

                self.titlos_total_wins = tk.Label(self.f_table, width=10, text="Σύνολο Νικών", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_total_wins.grid(row=0, column=4, sticky="nsew")

                self.titlos_total_matches = tk.Label(self.f_table, width=15, text="Σύνολο Αγώνων", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_total_matches.grid(row=0, column=5, sticky="nsew")

                self.titlos_ratio = tk.Label(self.f_table, width=18, text="Ποσοστό Επιτυχίας (%)", relief=tk.SUNKEN, borderwidth=1)
                self.titlos_ratio.grid(row=0, column=6, sticky="nsew")


                i=1
                for person in row:
                    person = dict(person)
                    self.titlos_enum = tk.Label(self.f_table, width=18, text=str(pos), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_enum.grid(row=i, column=0, sticky="nsew")

                    self.titlos_id = tk.Label(self.f_table, width=15, text=str(person["memberid"]), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_id.grid(row=i, column=1, sticky="nsew")

                    self.titlos_name = tk.Label(self.f_table, width=20, text=person["onoma"], relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_name.grid(row=i, column=2, sticky="nsew")

                    self.titlos_surname = tk.Label(self.f_table, width=10, text=person["epwnumo"], relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_surname.grid(row=i, column=3, sticky="nsew")

                    self.titlos_total_wins = tk.Label(self.f_table, width=15, text=str(person["total_wins"]), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_total_wins.grid(row=i, column=4, sticky="nsew")

                    self.titlos_total_matches = tk.Label(self.f_table, width=18, text=str(person["total_matches"]), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_total_matches.grid(row=i, column=5, sticky="nsew")

                    self.titlos_ratio = tk.Label(self.f_table, width=10, text=str(person["win_ratio"]), relief=tk.SUNKEN, borderwidth=1)
                    self.titlos_ratio.grid(row=i, column=6, sticky="nsew")

                    pos+=1
                    i+=1

                self.f_table.grid_columnconfigure(1, weight=1)
                self.f_table.grid_columnconfigure(2, weight=1)
                self.f_table.grid_columnconfigure(3, weight=1)
                self.f_table.grid_columnconfigure(4, weight=1)
                self.f_table.grid_columnconfigure(5, weight=1)
                self.f_table.grid_columnconfigure(6, weight=1)
                # invisible row after last row gets all extra space
                self.f_table.grid_rowconfigure(i+1, weight=1)


    def admin_customers(self):
        
        row = q.find_all_customers(self.cursor)

        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΛίστα Πελατών")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

        self.titlos_id = tk.Label(self.f_table, width=10, text="ID", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_id.grid(row=0, column=0, sticky="nsew")

        self.titlos_full_name = tk.Label(self.f_table, width=15, text="Ονοματεπώνυμο", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_full_name.grid(row=0, column=1, sticky="nsew")

        self.titlos_sex = tk.Label(self.f_table, width=20, text="Φύλο", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_sex.grid(row=0, column=2, sticky="nsew")

        self.titlos_subscription = tk.Label(self.f_table, width=10, text="Αριθμός Ταυτότητας", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_subscription.grid(row=0, column=3, sticky="nsew")

        self.titlos_already_programs = tk.Label(self.f_table, width=15, text="Email", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_already_programs.grid(row=0, column=4, sticky="nsew")

        self.titlos_choose_programs = tk.Label(self.f_table, width=10, text="Τηλέφωνο", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_choose_programs.grid(row=0, column=5, sticky="nsew")

        i=1
        for person in row:
            person = dict(person)
            self.titlos_id = tk.Label(self.f_table, width=10, text=str(person["id_pelath"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=i, column=0, sticky="nsew")

            self.titlos_full_name = tk.Label(self.f_table, width=15, text=person["epwnumo"]+" "+person["onoma"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_full_name.grid(row=i, column=1, sticky="nsew")

            if person["sex"] == 'M': sex="Άνδρας"
            else: sex="Γυναίκα"

            self.titlos_sex = tk.Label(self.f_table, width=20, text=sex, relief=tk.SUNKEN, borderwidth=1)
            self.titlos_sex.grid(row=i, column=2, sticky="nsew")

            self.titlos_subscription = tk.Label(self.f_table, width=10, text=person["ar_tautothtas"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_subscription.grid(row=i, column=3, sticky="nsew")

            self.titlos_already_programs = tk.Label(self.f_table, width=15, text=person["email"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_already_programs.grid(row=i, column=4, sticky="nsew")

            self.titlos_choose_programs = tk.Label(self.f_table, width=10, text=person["thlefwno"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_choose_programs.grid(row=i, column=5, sticky="nsew")

            i+=1

            self.f_table.grid_columnconfigure(1, weight=1)
            self.f_table.grid_columnconfigure(2, weight=1)
            self.f_table.grid_columnconfigure(3, weight=1)
            self.f_table.grid_columnconfigure(4, weight=1)
            self.f_table.grid_columnconfigure(5, weight=1)
            # invisible row after last row gets all extra space
            self.f_table.grid_rowconfigure(i+1, weight=1)


    def admin_members(self):

        row = q.find_all_melh(self.cursor)

        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΛίστα Μελών")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

        self.titlos_id = tk.Label(self.f_table, width=10, text="ID", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_id.grid(row=0, column=0, sticky="nsew")

        self.titlos_full_name = tk.Label(self.f_table, width=20, text="Ονοματεπώνυμο", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_full_name.grid(row=0, column=1, sticky="nsew")

        self.titlos_sex = tk.Label(self.f_table, width=20, text="Φύλο", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_sex.grid(row=0, column=2, sticky="nsew")

        self.titlos_ssn = tk.Label(self.f_table, width=15, text="Αριθμός Ταυτότητας", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_ssn.grid(row=0, column=3, sticky="nsew")

        self.titlos_email = tk.Label(self.f_table, width=15, text="Email", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_email.grid(row=0, column=4, sticky="nsew")

        self.titlos_telephone = tk.Label(self.f_table, width=10, text="Τηλέφωνο", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_telephone.grid(row=0, column=5, sticky="nsew")

        self.titlos_subscription = tk.Label(self.f_table, width=10, text="Συνδρομή", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_subscription.grid(row=0, column=6, sticky="nsew")

        self.titlos_programs = tk.Label(self.f_table, width=10, text="Προγράμματα", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_programs.grid(row=0, column=7, sticky="nsew")

        i=1
        for person in row:
            person = dict(person)
            sub = q.subscription_details(self, self.cursor, person["sundromh"])
            programids = q.programs_participating(self.cursor, person["memberid"])
            my_programs = []
            if type(programids) is int:
                if programids == 1:
                    my_programs.append("-")
            else:
                for x in programids:
                    my_programs.append(str(x["programid"]))

            my_programs = ", ".join(my_programs)
            
            
            self.titlos_id = tk.Label(self.f_table, width=10, text=str(person["id_pelath"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=i, column=0, sticky="nsew")

            self.titlos_full_name = tk.Label(self.f_table, width=20, text=person["epwnumo"]+" "+person["onoma"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_full_name.grid(row=i, column=1, sticky="nsew")

            if person["sex"] == 'M': sex="Άνδρας"
            else: sex="Γυναίκα"

            self.titlos_sex = tk.Label(self.f_table, width=20, text=sex, relief=tk.SUNKEN, borderwidth=1)
            self.titlos_sex.grid(row=i, column=2, sticky="nsew")

            self.titlos_ssn = tk.Label(self.f_table, width=15, text=person["ar_tautothtas"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_ssn.grid(row=i, column=3, sticky="nsew")

            self.titlos_email = tk.Label(self.f_table, width=15, text=person["email"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_email.grid(row=i, column=4, sticky="nsew")

            self.titlos_telephone = tk.Label(self.f_table, width=10, text=person["thlefwno"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_telephone.grid(row=i, column=5, sticky="nsew")

            self.titlos_subscription = tk.Label(self.f_table, width=10, text=str(sub["id"])+". "+sub["onoma"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_subscription.grid(row=i, column=6, sticky="nsew")

            self.titlos_choose_programs = tk.Label(self.f_table, width=10, text=my_programs, relief=tk.SUNKEN, borderwidth=1)
            self.titlos_choose_programs.grid(row=i, column=7, sticky="nsew")

            i+=1

        self.f_table.grid_columnconfigure(1, weight=1)
        self.f_table.grid_columnconfigure(2, weight=1)
        self.f_table.grid_columnconfigure(3, weight=1)
        self.f_table.grid_columnconfigure(4, weight=1)
        self.f_table.grid_columnconfigure(5, weight=1)
        self.f_table.grid_columnconfigure(6, weight=1)
        self.f_table.grid_columnconfigure(7, weight=1)
        # invisible row after last row gets all extra space
        self.f_table.grid_rowconfigure(i+1, weight=1)


    def admin_employees(self):

        row = q.admin_find_employees(self.cursor)

        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΛίστα Υπαλλήλων")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

        self.titlos_id = tk.Label(self.f_table, width=10, text="ID", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_id.grid(row=0, column=0, sticky="nsew")

        self.titlos_full_name = tk.Label(self.f_table, width=20, text="Ονοματεπώνυμο", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_full_name.grid(row=0, column=1, sticky="nsew")

        self.titlos_ssn = tk.Label(self.f_table, width=15, text="Αριθμός Ταυτότητας", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_ssn.grid(row=0, column=2, sticky="nsew")

        self.titlos_email = tk.Label(self.f_table, width=15, text="Email", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_email.grid(row=0, column=3, sticky="nsew")

        self.titlos_telephone = tk.Label(self.f_table, width=10, text="Τηλέφωνο", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_telephone.grid(row=0, column=4, sticky="nsew")

        self.titlos_address = tk.Label(self.f_table, width=10, text="Διεύθυνση", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_address.grid(row=0, column=5, sticky="nsew")

        self.titlos_job_type = tk.Label(self.f_table, width=10, text="Τύπος Εργασίας", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_job_type.grid(row=0, column=6, sticky="nsew")

        self.titlos_salary = tk.Label(self.f_table, width=10, text="Μισθός", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_salary.grid(row=0, column=7, sticky="nsew")

        self.titlos_date1 = tk.Label(self.f_table, width=10, text="Ημερομηνία Πρόσληψης", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_date1.grid(row=0, column=8, sticky="nsew")

        self.titlos_date2 = tk.Label(self.f_table, width=10, text="Ημερομηνία Λήξης Σύμβασης", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_date2.grid(row=0, column=9, sticky="nsew")

        i=1
        for person in row:
            person = dict(person)
            
            self.titlos_id = tk.Label(self.f_table, width=10, text=str(person["employeeid"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=i, column=0, sticky="nsew")

            self.titlos_full_name = tk.Label(self.f_table, width=20, text=person["epwnumo"]+" "+person["onoma"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_full_name.grid(row=i, column=1, sticky="nsew")

            self.titlos_ssn = tk.Label(self.f_table, width=15, text=person["ar_tautothtas"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_ssn.grid(row=i, column=2, sticky="nsew")

            self.titlos_email = tk.Label(self.f_table, width=15, text=person["email"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_email.grid(row=i, column=3, sticky="nsew")

            self.titlos_telephone = tk.Label(self.f_table, width=10, text=person["thlefwno"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_telephone.grid(row=i, column=4, sticky="nsew")

            self.titlos_address = tk.Label(self.f_table, width=10, text=person["dieu8unsh"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_address.grid(row=i, column=5, sticky="nsew")

            self.titlos_job_type = tk.Label(self.f_table, width=10, text=person["douleia"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_job_type.grid(row=i, column=6, sticky="nsew")

            self.titlos_salary = tk.Label(self.f_table, width=10, text=str(person["mis8os"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_salary.grid(row=i, column=7, sticky="nsew")

            self.titlos_date1 = tk.Label(self.f_table, width=10, text=person["hmeromhnia_proslhpshs"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_date1.grid(row=i, column=8, sticky="nsew")

            self.titlos_date2 = tk.Label(self.f_table, width=10, text=person["lh3h_sumvashs"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_date2.grid(row=i, column=9, sticky="nsew")


            i+=1

        self.f_table.grid_columnconfigure(1, weight=1)
        self.f_table.grid_columnconfigure(2, weight=1)
        self.f_table.grid_columnconfigure(3, weight=1)
        self.f_table.grid_columnconfigure(4, weight=1)
        self.f_table.grid_columnconfigure(5, weight=1)
        self.f_table.grid_columnconfigure(6, weight=1)
        self.f_table.grid_columnconfigure(7, weight=1)
        self.f_table.grid_columnconfigure(8, weight=1)
        self.f_table.grid_columnconfigure(9, weight=1)
        # invisible row after last row gets all extra space
        self.f_table.grid_rowconfigure(i+1, weight=1)


    def admin_rent(self):

        row = q.admin_find_rents(self.cursor)

        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΛίστα Ενοικιάσεων")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

        self.titlos_id = tk.Label(self.f_table, width=10, text="ID Πελάτη", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_id.grid(row=0, column=0, sticky="nsew")

        self.titlos_full_name = tk.Label(self.f_table, width=20, text="Ονοματεπώνυμο", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_full_name.grid(row=0, column=1, sticky="nsew")

        self.titlos_ssn = tk.Label(self.f_table, width=15, text="Γήπεδο", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_ssn.grid(row=0, column=2, sticky="nsew")

        self.titlos_email = tk.Label(self.f_table, width=15, text="Ημερομηνία", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_email.grid(row=0, column=3, sticky="nsew")

        self.titlos_telephone = tk.Label(self.f_table, width=10, text="Ώρα", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_telephone.grid(row=0, column=4, sticky="nsew")

        self.titlos_address = tk.Label(self.f_table, width=10, text="Διάρκεια (Ώρα/ες)", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_address.grid(row=0, column=5, sticky="nsew")

        i=1
        for match in row:
            match = dict(match)
            
            self.titlos_id = tk.Label(self.f_table, width=10, text=str(match["id_pelath"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=i, column=0, sticky="nsew")

            self.titlos_full_name = tk.Label(self.f_table, width=20, text=match["epwnumo"]+" "+match["onoma"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_full_name.grid(row=i, column=1, sticky="nsew")

            self.titlos_ssn = tk.Label(self.f_table, width=15, text=str(match["fieldid"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_ssn.grid(row=i, column=2, sticky="nsew")

            self.titlos_email = tk.Label(self.f_table, width=15, text=match["hmeromhnia"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_email.grid(row=i, column=3, sticky="nsew")

            self.titlos_telephone = tk.Label(self.f_table, width=10, text=match["wra"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_telephone.grid(row=i, column=4, sticky="nsew")

            self.titlos_address = tk.Label(self.f_table, width=10, text=match["diarkeia"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_address.grid(row=i, column=5, sticky="nsew")


            i+=1

        self.f_table.grid_columnconfigure(1, weight=1)
        self.f_table.grid_columnconfigure(2, weight=1)
        self.f_table.grid_columnconfigure(3, weight=1)
        self.f_table.grid_columnconfigure(4, weight=1)
        self.f_table.grid_columnconfigure(5, weight=1)
        # invisible row after last row gets all extra space
        self.f_table.grid_rowconfigure(i+1, weight=1)


    def admin_all_transactions(self, flag):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        

        if flag == 0:
            row = q.find_all_transactions(self.cursor)
            self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΛίστα Συναλλαγών")
            self.titlos.pack(expand=True)
        elif flag == 1:
            row = q.find_all_pending_transactions(self.cursor)
            self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΛίστα Εκκρεμών Συναλλαγών")
            self.titlos.pack(expand=True)
        else:
            row = q.find_all_completed_transactions(self.cursor)
            self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΛίστα Ολοκληρωμένων Συναλλαγών")
            self.titlos.pack(expand=True)

        

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

        self.titlos_id = tk.Label(self.f_table, width=18, text="Κωδικός Συναλλαγής", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_id.grid(row=0, column=0, sticky="nsew")

        self.titlos_id_customer = tk.Label(self.f_table, width=15, text="ID Πελάτη", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_id_customer.grid(row=0, column=1, sticky="nsew")

        self.titlos_deposit = tk.Label(self.f_table, width=20, text="Καταβληθέν Ποσό (€)", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_deposit.grid(row=0, column=2, sticky="nsew")

        self.titlos_remain = tk.Label(self.f_table, width=10, text="Υπόλοιπο (€)", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_remain.grid(row=0, column=3, sticky="nsew")

        self.titlos_reason = tk.Label(self.f_table, width=15, text="Είδος Παροχής", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_reason.grid(row=0, column=4, sticky="nsew")

        self.titlos_total_cost = tk.Label(self.f_table, width=18, text="Αρχικό Συνολικό Ποσό (€)", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_total_cost.grid(row=0, column=5, sticky="nsew")

        self.titlos_date = tk.Label(self.f_table, width=10, text="Ημερομηνία", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_date.grid(row=0, column=6, sticky="nsew")

        self.titlos_date = tk.Label(self.f_table, width=10, text="Ώρα", relief=tk.SUNKEN, borderwidth=1)
        self.titlos_date.grid(row=0, column=7, sticky="nsew")

        i=1
        for tr in row:
            tr = dict(tr)
            self.titlos_id = tk.Label(self.f_table, width=18, text=str(tr["id_sunallaghs"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=i, column=0, sticky="nsew")

            self.titlos_id_customer = tk.Label(self.f_table, width=15, text=str(tr["id_pelath"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id_customer.grid(row=i, column=1, sticky="nsew")

            self.titlos_deposit = tk.Label(self.f_table, width=20, text=str(tr["katavlh8en_poso"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_deposit.grid(row=i, column=2, sticky="nsew")

            self.titlos_remain = tk.Label(self.f_table, width=10, text=str(tr["upoloipo"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_remain.grid(row=i, column=3, sticky="nsew")

            self.titlos_reason = tk.Label(self.f_table, width=15, text=tr["eidos_paroxhs"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_reason.grid(row=i, column=4, sticky="nsew")

            self.titlos_total_cost = tk.Label(self.f_table, width=18, text=str(tr["timh"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_total_cost.grid(row=i, column=5, sticky="nsew")

            self.titlos_date = tk.Label(self.f_table, width=10, text=tr["hmeromhnia"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_date.grid(row=i, column=6, sticky="nsew")

            self.titlos_time = tk.Label(self.f_table, width=10, text=tr["wra"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_time.grid(row=i, column=7, sticky="nsew")

            i+=1

        self.f_table.grid_columnconfigure(1, weight=1)
        self.f_table.grid_columnconfigure(2, weight=1)
        self.f_table.grid_columnconfigure(3, weight=1)
        self.f_table.grid_columnconfigure(4, weight=1)
        self.f_table.grid_columnconfigure(5, weight=1)
        self.f_table.grid_columnconfigure(6, weight=1)
        self.f_table.grid_columnconfigure(7, weight=1)
        # invisible row after last row gets all extra space
        self.f_table.grid_rowconfigure(i+1, weight=1)


    def admin_delete_member(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΔιαγραφή Μέλους")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_search_member = tk.Frame(root)
        self.f_search_member.pack()
        self.search_member_label = tk.Label(self.f_search_member,font=self.medium_font,text="Αναζήτηση Μέλους: ")
        self.search_member_label.pack(side="left")
        self.search_member_text = tk.Entry(self.f_search_member, font=self.small_font, width=20, relief=tk.SUNKEN, borderwidth=1)
        self.search_member_text.pack(side="left")
        self.search_member_button = tk.Button(self.f_search_member, text="Αναζήτηση", font=self.medium_font, width=10, command=lambda: self.admin_delete_member_event(self.search_member_text.get()))
        self.search_member_button.pack()

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

        self.f_add_button = tk.Frame(root)
        self.f_add_button.pack()


    def admin_delete_member_event(self, memberid):
        row = q.fetch_profile_info(self, self.cursor, memberid)
    

        if type(row) is bool:
            if row == False:
                self.f_table.destroy()
                self.f_add_button.destroy()

                self.f_table = tk.Frame(root)
                self.f_table.pack(side="top", fill="both", expand=True)

                self.f_add_button = tk.Frame(root)
                self.f_add_button.pack()

                self.data_id = tk.Label(self.f_table, text="Δεν υπάρχει μέλος με ID: "+str(memberid), font=self.medium_font)
                self.data_id.pack()
            
        else:
            sub = q.subscription_details(self, self.cursor, row[7])
            programids = q.programs_participating(self.cursor, memberid)
            my_programs = []
            if type(programids) is int:
                if programids == 1:
                    my_programs.append("-")
            else:
                for x in programids:
                    my_programs.append(str(x["programid"]))

            my_programs = ", ".join(my_programs)


            self.f_table.destroy()
            self.f_add_button.destroy()

            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.f_add_button = tk.Frame(root)
            self.f_add_button.pack()

            self.titlos_id = tk.Label(self.f_table, width=10, text="Member ID", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=0, column=0, sticky="nsew")

            self.titlos_full_name = tk.Label(self.f_table, width=15, text="Ονοματεπώνυμο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_full_name.grid(row=0, column=1, sticky="nsew")

            self.titlos_subscription = tk.Label(self.f_table, width=10, text="Συνδρομή", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_subscription.grid(row=0, column=2, sticky="nsew")

            self.titlos_already_programs = tk.Label(self.f_table, width=15, text="Προγράμματα", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_already_programs.grid(row=0, column=3, sticky="nsew")


            self.data_id = tk.Label(self.f_table, width=10, text="#"+memberid, relief=tk.SUNKEN, borderwidth=1)
            self.data_id.grid(row=1, column=0, sticky="nsew")

            self.data_full_name = tk.Label(self.f_table, width=15, text=row[0]+" "+row[1], relief=tk.SUNKEN, borderwidth=1)
            self.data_full_name.grid(row=1, column=1, sticky="nsew")

            self.data_already_programs = tk.Label(self.f_table, width=10, text=str(sub["id"])+". "+sub["onoma"], relief=tk.SUNKEN, borderwidth=1)
            self.data_already_programs.grid(row=1, column=2, sticky="nsew")

            self.data_choose_program = tk.Label(self.f_table, width=15, text=my_programs, relief=tk.SUNKEN, borderwidth=1)
            self.data_choose_program.grid(row=1, column=3, sticky="nsew")


            self.f_table.grid_columnconfigure(1, weight=1)
            self.f_table.grid_columnconfigure(2, weight=1)
            self.f_table.grid_columnconfigure(3, weight=1)
            # invisible row after last row gets all extra space
            self.f_table.grid_rowconfigure(2, weight=1)


            self.remove_button = tk.Button(self.f_add_button, text="Διαγραφή Μέλους", font=self.medium_font, width=20, command=lambda: self.admin_member_deletion(memberid, my_programs))
            self.remove_button.pack()

        
    def admin_member_deletion(self, memberid, my_programs):
        
        for x in my_programs:
            q.remove_member(self.cursor, memberid, x)
        flag = q.delete_member(self.cursor, memberid)
        if flag == True:
            tkm.showinfo(title="Διαγραφή Μέλους", message="Το μέλος διαγράφηκε με επιτυχία")
            self.page_transition_admin(0)
        else:
            tkm.showerror(title="Διαγραφή Μέλους", message="Αποτυχία Διαγραφής Μέλους")

        
    def admin_delete_employee(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΔιαγραφή Υπαλλήλου")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_search_member = tk.Frame(root)
        self.f_search_member.pack()
        self.search_member_label = tk.Label(self.f_search_member,font=self.medium_font,text="Αναζήτηση Υπαλλήλου: ")
        self.search_member_label.pack(side="left")
        self.search_member_text = tk.Entry(self.f_search_member, font=self.small_font, width=20, relief=tk.SUNKEN, borderwidth=1)
        self.search_member_text.pack(side="left")
        self.search_member_button = tk.Button(self.f_search_member, text="Αναζήτηση", font=self.medium_font, width=10, command=lambda: self.find_employee(self.search_member_text.get()))
        self.search_member_button.pack()

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()

        self.f_table = tk.Frame(root)
        self.f_table.pack(side="top", fill="both", expand=True)

        self.f_add_button = tk.Frame(root)
        self.f_add_button.pack()


    def find_employee(self, employeeid):
        result = q.fetch_profile_info_staff(self.cursor, employeeid)

        if type(result) is bool: 
            self.f_table.destroy()
            self.f_add_button.destroy()

            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.f_add_button = tk.Frame(root)
            self.f_add_button.pack()

            self.data_id = tk.Label(self.f_table, text="Δεν υπάρχει υπάλληλος με ID: "+str(employeeid), font=self.medium_font)
            self.data_id.pack()
        elif result is None:
            self.f_table.destroy()
            self.f_add_button.destroy()

            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.f_add_button = tk.Frame(root)
            self.f_add_button.pack()

            self.data_id = tk.Label(self.f_table, text="Δεν υπάρχει υπάλληλος με ID: "+str(employeeid), font=self.medium_font)
            self.data_id.pack()
        else:
            result = dict(result)

            self.f_table.destroy()
            self.f_add_button.destroy()

            self.f_table = tk.Frame(root)
            self.f_table.pack(side="top", fill="both", expand=True)

            self.f_add_button = tk.Frame(root)
            self.f_add_button.pack()

            self.titlos_id = tk.Label(self.f_table, width=10, text="ID", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=0, column=0, sticky="nsew")

            self.titlos_full_name = tk.Label(self.f_table, width=20, text="Ονοματεπώνυμο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_full_name.grid(row=0, column=1, sticky="nsew")

            self.titlos_ssn = tk.Label(self.f_table, width=15, text="Αριθμός Ταυτότητας", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_ssn.grid(row=0, column=2, sticky="nsew")

            self.titlos_email = tk.Label(self.f_table, width=15, text="Email", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_email.grid(row=0, column=3, sticky="nsew")

            self.titlos_telephone = tk.Label(self.f_table, width=10, text="Τηλέφωνο", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_telephone.grid(row=0, column=4, sticky="nsew")

            self.titlos_address = tk.Label(self.f_table, width=10, text="Διεύθυνση", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_address.grid(row=0, column=5, sticky="nsew")

            self.titlos_job_type = tk.Label(self.f_table, width=10, text="Τύπος Εργασίας", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_job_type.grid(row=0, column=6, sticky="nsew")

            self.titlos_salary = tk.Label(self.f_table, width=10, text="Μισθός", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_salary.grid(row=0, column=7, sticky="nsew")

            self.titlos_date1 = tk.Label(self.f_table, width=10, text="Ημερομηνία Πρόσληψης", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_date1.grid(row=0, column=8, sticky="nsew")

            self.titlos_date2 = tk.Label(self.f_table, width=10, text="Ημερομηνία Λήξης Σύμβασης", relief=tk.SUNKEN, borderwidth=1)
            self.titlos_date2.grid(row=0, column=9, sticky="nsew")

            i=1
            person = dict(result)
            
            self.titlos_id = tk.Label(self.f_table, width=10, text=str(person["employeeid"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_id.grid(row=i, column=0, sticky="nsew")

            self.titlos_full_name = tk.Label(self.f_table, width=20, text=person["epwnumo"]+" "+person["onoma"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_full_name.grid(row=i, column=1, sticky="nsew")

            self.titlos_ssn = tk.Label(self.f_table, width=15, text=person["ar_tautothtas"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_ssn.grid(row=i, column=2, sticky="nsew")

            self.titlos_email = tk.Label(self.f_table, width=15, text=person["email"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_email.grid(row=i, column=3, sticky="nsew")

            self.titlos_telephone = tk.Label(self.f_table, width=10, text=person["thlefwno"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_telephone.grid(row=i, column=4, sticky="nsew")

            self.titlos_address = tk.Label(self.f_table, width=10, text=person["dieu8unsh"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_address.grid(row=i, column=5, sticky="nsew")

            self.titlos_job_type = tk.Label(self.f_table, width=10, text=person["douleia"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_job_type.grid(row=i, column=6, sticky="nsew")

            self.titlos_salary = tk.Label(self.f_table, width=10, text=str(person["mis8os"]), relief=tk.SUNKEN, borderwidth=1)
            self.titlos_salary.grid(row=i, column=7, sticky="nsew")

            self.titlos_date1 = tk.Label(self.f_table, width=10, text=person["hmeromhnia_proslhpshs"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_date1.grid(row=i, column=8, sticky="nsew")

            self.titlos_date2 = tk.Label(self.f_table, width=10, text=person["lh3h_sumvashs"], relief=tk.SUNKEN, borderwidth=1)
            self.titlos_date2.grid(row=i, column=9, sticky="nsew")




            self.f_table.grid_columnconfigure(1, weight=1)
            self.f_table.grid_columnconfigure(2, weight=1)
            self.f_table.grid_columnconfigure(3, weight=1)
            self.f_table.grid_columnconfigure(4, weight=1)
            self.f_table.grid_columnconfigure(5, weight=1)
            self.f_table.grid_columnconfigure(6, weight=1)
            self.f_table.grid_columnconfigure(7, weight=1)
            self.f_table.grid_columnconfigure(8, weight=1)
            self.f_table.grid_columnconfigure(9, weight=1)
            # invisible row after last row gets all extra space
            self.f_table.grid_rowconfigure(i+1, weight=1)

            self.remove_button = tk.Button(self.f_add_button, text="Διαγραφή Υπαλλήλου", font=self.medium_font, width=20, command=lambda: self.admin_staff_deletion(employeeid, result["douleia"]))
            self.remove_button.pack()


    def admin_staff_deletion(self, employeeid, job):
        if job == "Γυμναστής":
            flag = q.remove_gymnast_from_program(self.cursor, employeeid)
            flag = q.delete_employee(self.cursor, employeeid)
        elif job != "Διαχειριστής":
            flag = q.delete_employee(self.cursor, employeeid)
        else:
            tkm.showerror(title="Διαγραφή Υπαλλήλου", message="Δεν μπορείτε να διαγράψετε έναν διαχειριστή")
        
        if flag == True:
            tkm.showinfo(title="Διαγραφή Υπαλλήλου", message="Ο υπάλληλος διεγράφη με επιτυχία")
            self.page_transition(4)
        else:
            tkm.showinfo(title="Διαγραφή Υπαλλήλου", message="Αποτυχία Διαγραφής")


    def admin_add_employee(self):
        self.ftitlos=tk.Frame(root)
        self.ftitlos.pack()
        self.titlos=tk.Label(self.ftitlos,font=self.large_font,text="\nΠροσθήκη Υπαλλήλου")
        self.titlos.pack(expand=True)

        self.f_blank0 = tk.Frame(root)
        self.f_blank0.pack()
        self.blanklabel0=tk.Label(self.f_blank0,text="\n\n\n")
        self.blanklabel0.pack()

        self.f_name = tk.Frame(root)
        self.f_name.pack()
        self.name_label = tk.Label(self.f_name, font=self.medium_font, text="Όνομα: ")
        self.name_label.pack(side='left')
        self.name_box = tk.Entry(self.f_name, font=self.medium_font, width=20)
        self.name_box.pack(side='left')

        self.f_blank1 = tk.Frame(root)
        self.f_blank1.pack()
        self.blanklabel1=tk.Label(self.f_blank1,text="\n")
        self.blanklabel1.pack()
        
        self.f_surname = tk.Frame(root)
        self.f_surname.pack()
        self.surname_label = tk.Label(self.f_surname, font=self.medium_font, text="Επώνυμο: ")
        self.surname_label.pack(side='left')
        self.surname_box = tk.Entry(self.f_surname, font=self.medium_font, width=20)
        self.surname_box.pack(side='right')

        self.f_blank2 = tk.Frame(root)
        self.f_blank2.pack()
        self.blanklabel2=tk.Label(self.f_blank2,text="\n")
        self.blanklabel2.pack()

        self.f_type_job = tk.Frame(root)
        self.f_type_job.pack()
        self.type_job_label = tk.Label(self.f_type_job, font=self.medium_font, text="Τύπος Εργασίας: ")
        self.type_job_label.pack(side="left")
        type_of_job = tk.StringVar(root)
        type_of_job.set("Γυμναστής")
        self.type_job_box = tk.OptionMenu(self.f_type_job, type_of_job, "Γυμναστής", "Γραμματέας", "Καθαριστής", "Διαχειριστής")
        self.type_job_box.pack(side="left")


        self.f_blank2_5 = tk.Frame(root)
        self.f_blank2_5.pack()
        self.blanklabel2_5=tk.Label(self.f_blank2_5,text="\n")
        self.blanklabel2_5.pack()

        self.f_ssn = tk.Frame(root)
        self.f_ssn.pack()
        self.ssn_label = tk.Label(self.f_ssn, font=self.medium_font, text="Αριθμός Ταυτότητας: ")
        self.ssn_label.pack(side='left')
        self.ssn_box = tk.Entry(self.f_ssn, font=self.medium_font, width=20)
        self.ssn_box.pack(side='left')

        self.f_blank3 = tk.Frame(root)
        self.f_blank3.pack()
        self.blanklabel3=tk.Label(self.f_blank3,text="\n")
        self.blanklabel3.pack()

        self.f_address = tk.Frame(root)
        self.f_address.pack()
        self.address_label = tk.Label(self.f_address, font=self.medium_font, text="Διεύθυνση: ")
        self.address_label.pack(side='left')
        self.address_box = tk.Entry(self.f_address, font=self.medium_font, width=20)
        self.address_box.pack(side='left')

        self.f_blank4 = tk.Frame(root)
        self.f_blank4.pack()
        self.blanklabel4=tk.Label(self.f_blank4,text="\n")
        self.blanklabel4.pack()

        self.f_telephone = tk.Frame(root)
        self.f_telephone.pack()
        self.telephone_label = tk.Label(self.f_telephone, font=self.medium_font, text="Τηλέφωνο: ")
        self.telephone_label.pack(side='left')
        self.telephone_box = tk.Entry(self.f_telephone, font=self.medium_font, width=20)
        self.telephone_box.pack(side='left')

        self.f_blank5 = tk.Frame(root)
        self.f_blank5.pack()
        self.blanklabel5=tk.Label(self.f_blank5,text="\n")
        self.blanklabel5.pack()

        self.f_email = tk.Frame(root)
        self.f_email.pack()
        self.email_label = tk.Label(self.f_email, font=self.medium_font, text="Email: ")
        self.email_label.pack(side='left')       
        self.email_box = tk.Entry(self.f_email, font=self.medium_font, width=20)
        self.email_box.pack(side='left')

        self.f_blank6 = tk.Frame(root)
        self.f_blank6.pack()
        self.blanklabel6=tk.Label(self.f_blank6,text="\n")
        self.blanklabel6.pack()

        self.f_salary = tk.Frame(root)
        self.f_salary.pack()
        self.salary_label = tk.Label(self.f_salary, font=self.medium_font, text="Μισθός: ")
        self.salary_label.pack(side="left")
        self.salary_box = tk.Entry(self.f_salary, font=self.medium_font, width=10)
        self.salary_box.pack(side="left")

        self.f_blank7 = tk.Frame(root)
        self.f_blank7.pack()
        self.blanklabel7=tk.Label(self.f_blank7,text="\n")
        self.blanklabel7.pack()

        self.f_simvasi = tk.Frame(root)
        self.f_simvasi.pack()
        self.simvasi_label = tk.Label(self.f_simvasi, font=self.medium_font, text="Ημερομηνία λήξης σύμβασης (προαιρετικό πεδίο): ")
        self.simvasi_label.pack(side='left')
        self.simvasi_box = tk.Entry(self.f_simvasi, font=self.medium_font, width=15)
        self.simvasi_box.pack(side='left')

        self.f_blank8 = tk.Frame(root)
        self.f_blank8.pack()
        self.blanklabel8=tk.Label(self.f_blank8,text="\n")
        self.blanklabel8.pack()

        self.f_register = tk.Frame(root)
        self.f_register.pack()
        self.register_button = tk.Button(self.f_register, text="Προσθήκη Υπαλλήλου", font=self.medium_font, width=20, command=lambda: self.admin_add_employee_event(self.name_box.get(), self.surname_box.get(), type_of_job.get(), self.ssn_box.get(), self.address_box.get(), self.telephone_box.get(), self.email_box.get(), self.salary_box.get(), self.simvasi_box.get()))
        self.register_button.pack(side="left")


    def admin_add_employee_event(self, name, surname, type_of_job, ssn, address, telephone, email, salary, simvasi):
        flag, salary = checking.employee_form(name, surname, ssn, address, telephone, email, salary, simvasi)
        if flag == True:
            flag, employeeid, username, password = q.add_employee(self.cursor, name, surname, type_of_job, ssn, address, telephone, email, salary, simvasi)
            if flag == True:
                tkm.showinfo(title="Προσθήκη Υπαλλήλου", message="Ο υπάλληλος προστέθηκε με επιτυχία.\nΤο ID του νέου υπαλλήλου είναι: "+str(employeeid)+"\nΤο όνομα χρήστη είναι: "+username+"\nΟ κωδικός είναι: "+password)



if __name__ == '__main__':
    root=tk.Tk()
    graphics=GraphEnv(root)
    root.protocol("WM_DELETE_WINDOW", graphics.quit_window)
    root.mainloop()
