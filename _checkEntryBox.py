import tkinter.messagebox as tkm
import datetime

import re

def register(name, surname, ssn, address, email, telephone, username, password):

    '''Checking the Entry Boxes'''

    if len(name) == 0:
        tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Όνομα' είναι κενό")
        return False
    elif name.isalpha() == False:
        tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Όνομα' πρέπει να περιέχει μόνο ελληνικούς χαρακτήρες")
        return False
    
    #elif re.match("^[Α-Ωα-ωΆάΈέΎύΫϋΰΊίϊΐΌόΉήΏώ]*$", name) is None:
    #    tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Επώνυμο' πρέπει να περιέχει μόνο ελληνικούς χαρακτήρες")
    #    return False

    if len(surname) == 0:
        tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Επώνυμο' είναι κενό")
        return False
    elif surname.isalpha() == False:
        tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Επώνυμο' πρέπει να περιέχει μόνο ελληνικούς χαρακτήρες")
        return False
    #elif re.match("^[Α-Ωα-ωΆάΈέΎύΫϋΰΊίϊΐΌόΉήΏώ]*$", surname) is None:
    #    tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Επώνυμο' πρέπει να περιέχει μόνο ελληνικούς χαρακτήρες")
    #    return False
    
    if len(ssn) == 0:
        tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Αριθμός Ταυτότητας' είναι κενό")
        return False
    elif len(ssn) != 8 and len(ssn) != 7:
        tkm.showerror(title="Εγγραφή", message="Ο Αριθμός Ταυτότητας αποτελείται από 7 (ή 8) χαρακτήρες και πρέπει να γραφεί στη μορφή: Χ(Χ)ΥΥΥΥΥΥ,\nόπου Χ: τα γράμματα και Υ: οι αριθμοί του αριθμού ταυτότητάς σας")
        return False
    elif len(ssn) == 8:
        if ssn[0].isalpha() == False or ssn[1].isalpha() == False or ssn[2:].isdigit() == False:
            tkm.showerror(title="Εγγραφή", message="Λανθασμένη μορφή.\nΟ Αριθμός Ταυτότητας πρέπει να γραφεί στη μορφή: Χ(Χ)ΥΥΥΥΥΥ,\nόπου Χ: τα γράμματα και Υ: οι αριθμοί του αριθμού ταυτότητάς σας")
            return False
    elif len(ssn) == 7:
        if ssn[0].isalpha() == False or ssn[1:].isdigit() == False:
            tkm.showerror(title="Εγγραφή", message="Λανθασμένη μορφή.\nΟ Αριθμός Ταυτότητας πρέπει να γραφεί στη μορφή: Χ(Χ)ΥΥΥΥΥΥ,\nόπου Χ: τα γράμματα και Υ: οι αριθμοί του αριθμού ταυτότητάς σας")
            return False

    if len(address) == 0:
        tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Διεύθυνση' είναι κενό")
        return False
    
    if len(telephone) == 0:
        tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Τηλέφωνο' είναι κενό")
        return False
    elif telephone.isdigit() == False:
        tkm.showerror(title="Εγγραφή", message="Το 'Τηλέφωνο' πρέπει να αποτελείται μόνο από αριθμούς")
        return False
    elif len(telephone) != 10:
        tkm.showerror(title="Εγγραφή", message="Το 'Τηλέφωνο' πρέπει να αποτελείται από 10 ψηφία")
        return False

    if len(email) == 0:
        tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Email' είναι κενό")
        return False
    elif email.count('@') != 1 or email.split('@')[1].count('.') != 1:
        tkm.showerror(title="Εγγραφή", message="Το 'Email' έχει λανθασμένη μορφή")
        return False
    
    if len(username) == 0:
        tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Όνομα Χρήστη' είναι κενό")
        return False
    elif len(username) < 4:
        tkm.showerror(title="Εγγραφή", message="Το 'Όνομα Χρήστη' πρέπει να έχει τουλάχιστον 4 χαρακτήρες")
        return False
    elif re.match("^[A-Za-z0-9_]*$", username) is None:
        tkm.showerror(title="Εγγραφή", message="Το 'Όνομα Χρήστη' μπορεί να αποτελείται μόνο από:\n- Λατινικούς χαρακτήρες (πεζά ή/και κεφαλαία)\n- Αριθμούς (0-9)\n- Κάτω παύλα ( _ )")
        return False

    if len(password) == 0:
        tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Κωδικός' είναι κενό")
        return False
    elif len(password) < 6:
        tkm.showerror(title="Εγγραφή", message="O 'Κωδικός' πρέπει να έχει τουλάχιστον 6 χαρακτήρες")
        return False
    elif re.match("^[A-Za-z0-9_#@!*()]*$", password) is None:
        tkm.showerror(title="Εγγραφή", message="Ο 'Κωδικός' μπορεί να αποτελείται μόνο από:\n- Λατινικούς χαρακτήρες (πεζά ή/και κεφαλαία)\n- Αριθμούς (0-9)\n- Κάτω παύλα (_)\n- Ειδικούς χαρακτήρες: # @ ! * ( )")
        return False

    return True


def login(username, password):
    
    if len(username) == 0:
        tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Όνομα Χρήστη' είναι κενό.")
        return False
    elif re.match("^[A-Za-z0-9_]*$", username) is None or len(username) < 4:
        tkm.showerror(title="Εγγραφή", message="Το 'Όνομα Χρήστη' έχει λανθασμένη μορφή.")
        return False

    if len(password) == 0:
        tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Κωδικός' είναι κενό.")
        return False
    elif re.match("^[A-Za-z0-9_#@!*()]*$", password) is None or len(password) < 6:
        tkm.showerror(title="Εγγραφή", message="O 'Κωδικός' έχει λανθασμένη μορφή.")
        return False

    return True


def edit_profile(username, password):
    if len(username) == 0:
        tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Όνομα Χρήστη' είναι κενό")
        return False
    elif len(username) < 4:
        tkm.showerror(title="Εγγραφή", message="Το 'Όνομα Χρήστη' πρέπει να έχει τουλάχιστον 4 χαρακτήρες")
        return False
    elif re.match("^[A-Za-z0-9_]*$", username) is None:
        tkm.showerror(title="Εγγραφή", message="Το 'Όνομα Χρήστη' μπορεί να αποτελείται μόνο από:\n- Λατινικούς χαρακτήρες (πεζά ή/και κεφαλαία)\n- Αριθμούς (0-9)\n- Κάτω παύλα ( _ )")
        return False

    if len(password) == 0:
        tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Κωδικός' είναι κενό")
        return False
    elif len(password) < 6:
        tkm.showerror(title="Εγγραφή", message="O 'Κωδικός' πρέπει να έχει τουλάχιστον 6 χαρακτήρες")
        return False
    elif re.match("^[A-Za-z0-9_#@!*()]*$", password) is None:
        tkm.showerror(title="Εγγραφή", message="Ο 'Κωδικός' μπορεί να αποτελείται μόνο από:\n- Λατινικούς χαρακτήρες (πεζά ή/και κεφαλαία)\n- Αριθμούς (0-9)\n- Κάτω παύλα (_)\n- Ειδικούς χαρακτήρες: # @ ! * ( )")
        return False

    return True


def submit_match(status, score, date, time):
    newstatus = []; newscore = []; newdate = []; newtime = []
    i=0
    for x in status:
        if x.get() == "Άγνωστο" or score[i].get()=="":
            i+=1
        else:

            temp = score[i].get().split(" ")
            temp = '/'.join(temp)
            newscore.append(temp)
            newstatus.append(status[i].get())
            newdate.append(date[i])
            newtime.append(time[i])
            i+=1
    
    return (newstatus, newscore, newdate, newtime)


def add_transaction(id_customer, deposit, reason, fpa, total_cost):
    
    if len(id_customer) == 0:
        tkm.showerror(title="Υποβολή Συναλλαγής", message="Το πεδίο 'ID' είναι κενό")
        return False, total_cost, deposit
    elif re.match("^[0-9]*$", id_customer) is None:
        tkm.showerror(title="Υποβολή Συναλλαγής", message="Το 'ID' πρέπει να περιέχει μόνο αριθμούς")
        return False, total_cost, deposit

    if len(deposit) == 0:
        tkm.showerror(title="Υποβολή Συναλλαγής", message="Το πεδίο 'Καταβληθέν Ποσό' είναι κενό")
        return False, total_cost, deposit
    elif re.match("^[0-9.,]*$", deposit) is None:
        tkm.showerror(title="Υποβολή Συναλλαγής", message="Το 'Καταβληθέν Ποσό' πρέπει να περιέχει μόνο αριθμούς")
        return False, total_cost, deposit
    else:
        if ',' in deposit and '.' not in deposit:
            if deposit.count(',') != 1:
                tkm.showerror(title="Υποβολή Συναλλαγής", message="Το πεδίο 'Καταβληθέν Ποσό' έχει λανθασμένη μορφή")
                return False, total_cost, deposit
            elif deposit[0] == ',' or deposit[-1] == ',':
                tkm.showerror(title="Υποβολή Συναλλαγής", message="Το πεδίο 'Καταβληθέν Ποσό' έχει λανθασμένη μορφή")
                return False, total_cost, deposit
            else:
                deposit = deposit.replace(",", ".")
        elif '.' in deposit and ',' not in deposit:
            if deposit.count('.') != 1:
                tkm.showerror(title="Υποβολή Συναλλαγής", message="Το πεδίο 'Καταβληθέν Ποσό' έχει λανθασμένη μορφή")
                return False, total_cost, deposit
            elif deposit[0] == '.' or deposit[-1] == '.':
                tkm.showerror(title="Υποβολή Συναλλαγής", message="Το πεδίο 'Καταβληθέν Ποσό' έχει λανθασμένη μορφή")
                return False, total_cost, deposit
    
    if len(reason) == 0:
        tkm.showerror(title="Υποβολή Συναλλαγής", message="Το πεδίο 'Είδος Παροχής' είναι κενό")
        return False, total_cost, deposit
    
    if len(fpa) == 0:
        tkm.showerror(title="Υποβολή Συναλλαγής", message="Το πεδίο 'ΦΠΑ' είναι κενό")
        return False, total_cost, deposit
    elif fpa.isdigit() == False:
        tkm.showerror(title="Υποβολή Συναλλαγής", message="Το 'ΦΠΑ' πρέπει να περιέχει μόνο αριθμούς")
        return False, total_cost, deposit

    if len(total_cost) == 0:
        tkm.showerror(title="Υποβολή Συναλλαγής", message="Το πεδίο 'Αρχικό Συνολικό Ποσό' είναι κενό")
        return False, total_cost, deposit
    elif re.match("^[0-9.,]*$", total_cost) is None:
        tkm.showerror(title="Υποβολή Συναλλαγής", message="Το 'Αρχικό Συνολικό Ποσό' πρέπει να περιέχει μόνο αριθμούς")
        return False, total_cost, deposit
    else:
        if ',' in total_cost and '.' not in total_cost:
            if total_cost.count(',') != 1:
                tkm.showerror(title="Υποβολή Συναλλαγής", message="Το πεδίο 'Αρχικό Συνολικό Ποσό' έχει λανθασμένη μορφή")
                return False, total_cost, deposit
            elif total_cost[0] == ',' or total_cost[-1] == ',':
                tkm.showerror(title="Υποβολή Συναλλαγής", message="Το πεδίο 'Αρχικό Συνολικό Ποσό' έχει λανθασμένη μορφή")
                return False, total_cost, deposit
            else:
                total_cost = total_cost.replace(",", ".")
        elif '.' in total_cost and ',' not in total_cost:
            if total_cost.count('.') != 1:
                tkm.showerror(title="Υποβολή Συναλλαγής", message="Το πεδίο 'Αρχικό Συνολικό Ποσό' έχει λανθασμένη μορφή")
                return False, total_cost, deposit
            elif total_cost[0] == '.' or total_cost[-1] == '.':
                tkm.showerror(title="Υποβολή Συναλλαγής", message="Το πεδίο 'Αρχικό Συνολικό Ποσό' έχει λανθασμένη μορφή")
                return False, total_cost, deposit

    if float(total_cost) < float(deposit):
        tkm.showerror(title="Υποβολή Συναλλαγής", message="Δεν επιτρέπεται το 'Αρχικό Συνολικό Ποσό' να είναι μικρότερο από το 'Καταβληθέν Ποσό'")
        return False, total_cost, deposit

    return True, total_cost, deposit


def new_deposit(deposit, remain):
    if len(deposit) == 0:
        tkm.showerror(title="Ενημέρωση Συναλλαγής", message="Το πεδίο 'Καταβληθέν Ποσό' είναι κενό")
        return False, deposit
    elif re.match("^[0-9.,]*$", deposit) is None:
        tkm.showerror(title="Ενημέρωση Συναλλαγής", message="Το 'Καταβληθέν Ποσό' πρέπει να περιέχει μόνο αριθμούς")
        return False, deposit
    else:
        if ',' in deposit and '.' not in deposit:
            if deposit.count(',') != 1:
                tkm.showerror(title="Ενημέρωση Συναλλαγής", message="Το πεδίο 'Καταβληθέν Ποσό' έχει λανθασμένη μορφή")
                return False, deposit
            elif deposit[0] == ',' or deposit[-1] == ',':
                tkm.showerror(title="Ενημέρωση Συναλλαγής", message="Το πεδίο 'Καταβληθέν Ποσό' έχει λανθασμένη μορφή")
                return False, deposit
            else:
                deposit = deposit.replace(",", ".")
        elif '.' in deposit and ',' not in deposit:
            if deposit.count('.') != 1:
                tkm.showerror(title="Ενημέρωση Συναλλαγής", message="Το πεδίο 'Καταβληθέν Ποσό' έχει λανθασμένη μορφή")
                return False, deposit
            elif deposit[0] == '.' or deposit[-1] == '.':
                tkm.showerror(title="Ενημέρωση Συναλλαγής", message="Το πεδίο 'Καταβληθέν Ποσό' έχει λανθασμένη μορφή")
                return False, deposit

    
    if float(remain) < float(deposit):
        tkm.showerror(title="Ενημέρωση Συναλλαγής", message="Δεν επιτρέπεται το 'Νέο Καταβληθέν Ποσό' να είναι μεγαλύτερο από το 'Υπόλοιπο'")
        return False, deposit

    return True, deposit




def employee_form(name, surname, ssn, address, telephone, email, salary, simvasi):
    if len(name) == 0:
        tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το πεδίο 'Όνομα' είναι κενό")
        return False, salary
    elif name.isalpha() == False:
        tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το πεδίο 'Όνομα' πρέπει να περιέχει μόνο ελληνικούς χαρακτήρες")
        return False, salary
    
    #elif re.match("^[Α-Ωα-ωΆάΈέΎύΫϋΰΊίϊΐΌόΉήΏώ]*$", name) is None:
    #    tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το πεδίο 'Επώνυμο' πρέπει να περιέχει μόνο ελληνικούς χαρακτήρες")
    #    return False

    if len(surname) == 0:
        tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το πεδίο 'Επώνυμο' είναι κενό")
        return False, salary
    elif surname.isalpha() == False:
        tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το πεδίο 'Επώνυμο' πρέπει να περιέχει μόνο ελληνικούς χαρακτήρες")
        return False, salary
    #elif re.match("^[Α-Ωα-ωΆάΈέΎύΫϋΰΊίϊΐΌόΉήΏώ]*$", surname) is None:
    #    tkm.showerror(title="Εγγραφή", message="Το πεδίο 'Επώνυμο' πρέπει να περιέχει μόνο ελληνικούς χαρακτήρες")
    #    return False
    
    if len(ssn) == 0:
        tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το πεδίο 'Αριθμός Ταυτότητας' είναι κενό")
        return False, salary
    elif len(ssn) != 8 and len(ssn) != 7:
        tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Ο Αριθμός Ταυτότητας αποτελείται από 7 (ή 8) χαρακτήρες και πρέπει να γραφεί στη μορφή: Χ(Χ)ΥΥΥΥΥΥ,\nόπου Χ: τα γράμματα και Υ: οι αριθμοί του αριθμού ταυτότητάς σας")
        return False, salary
    elif len(ssn) == 8:
        if ssn[0].isalpha() == False or ssn[1].isalpha() == False or ssn[2:].isdigit() == False:
            tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Λανθασμένη μορφή.\nΟ Αριθμός Ταυτότητας πρέπει να γραφεί στη μορφή: Χ(Χ)ΥΥΥΥΥΥ,\nόπου Χ: τα γράμματα και Υ: οι αριθμοί του αριθμού ταυτότητάς σας")
            return False, salary
    elif len(ssn) == 7:
        if ssn[0].isalpha() == False or ssn[1:].isdigit() == False:
            tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Λανθασμένη μορφή.\nΟ Αριθμός Ταυτότητας πρέπει να γραφεί στη μορφή: Χ(Χ)ΥΥΥΥΥΥ,\nόπου Χ: τα γράμματα και Υ: οι αριθμοί του αριθμού ταυτότητάς σας")
            return False, salary

    if len(address) == 0:
        tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το πεδίο 'Διεύθυνση' είναι κενό")
        return False, salary
    
    if len(telephone) == 0:
        tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το πεδίο 'Τηλέφωνο' είναι κενό")
        return False, salary
    elif telephone.isdigit() == False:
        tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το 'Τηλέφωνο' πρέπει να αποτελείται μόνο από αριθμούς")
        return False, salary
    elif len(telephone) != 10:
        tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το 'Τηλέφωνο' πρέπει να αποτελείται από 10 ψηφία")
        return False, salary

    if len(email) == 0:
        tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το πεδίο 'Email' είναι κενό")
        return False, salary
    elif email.count('@') != 1 or email.split('@')[1].count('.') != 1:
        tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το 'Email' έχει λανθασμένη μορφή")
        return False, salary

    if len(salary) == 0:
        tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το πεδίο 'Μισθός' είναι κενό")
        return False, salary
    elif re.match("^[0-9.,]*$", salary) is None:
        tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Ο 'Μισθός' πρέπει να περιέχει μόνο αριθμούς")
        return False, salary
    else:
        if ',' in salary and '.' not in salary:
            if salary.count(',') != 1:
                tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το πεδίο 'Μισθός' έχει λανθασμένη μορφή")
                return False, salary
            elif salary[0] == ',' or salary[-1] == ',':
                tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το πεδίο 'Μισθός' έχει λανθασμένη μορφή")
                return False, salary
            else:
                salary = salary.replace(",", ".")
        elif '.' in salary and ',' not in salary:
            if salary.count('.') != 1:
                tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το πεδίο 'Μισθός' έχει λανθασμένη μορφή")
                return False, salary
            elif salary[0] == '.' or salary[-1] == '.':
                tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Το πεδίο 'Μισθός' έχει λανθασμένη μορφή")
                return False, salary

    if simvasi != "":
        try:
            datetime.datetime.strptime(simvasi, '%Y-%m-%d')
        except ValueError:
            tkm.showerror(title="Προσθήκη Υπαλλήλου", message="Η ημερομηνία πρέπει να έχει την μορφή: YYYY-MM-dd, όπου:\nYYYY: Η χρονολογία\nMM: Ο μήνας\ndd: Η μέρα")
            return False, salary

            
    return True, salary


def add_rent(date):

    try:
        datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%w')
        return True
    except ValueError:
        tkm.showerror(title="Προσθήκη Ενοικίασης", message="Η ημερομηνία πρέπει να έχει την μορφή: YYYY-MM-dd, όπου:\nYYYY: Η χρονολογία\nMM: Ο μήνας\ndd: Η μέρα")
        return False