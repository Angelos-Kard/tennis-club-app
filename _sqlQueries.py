import sqlite3
import sys, os
import pymysql
import string
from datetime import datetime
import random as rd
from operator import itemgetter

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



def create_sqlite_connection(self):
    PATH = resource_path("./tenisclub.db")
    try:
        conn = sqlite3.connect(PATH, isolation_level=None, check_same_thread = False)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        return conn,cur
    except sqlite3.Error as e:
        print(e)

def close_connection(self, conn, cursor):
    cursor.close()
    conn.close()

def create_mysql_connection(self):
    try:
        conn = pymysql.connect(host="150.140.186.221", user="db20_up1059372", password="up1059372", db="project_db20_up1059372", charset='utf8mb4')
        cursor = conn.cursor()
        return conn,cursor
    except pymysql.Error as e:
        print(e)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

def login_checker(self, cursor, username, password):
    cursor.execute("SELECT memberid FROM melos WHERE username=? AND password=?", (username,password))
    row = cursor.fetchone()
    if row is None: 
        return False,None
    else: 
        for memberid in row:
            return True,memberid


def login_staff_checker(cursor, username, password):
    cursor.execute("SELECT employeeid,douleia FROM prosopiko WHERE username=? AND password=?", (username,password))
    row = cursor.fetchone()
    if row is None: 
        return False,None,None
    else:
        temp = [] 
        for i in row:
            temp.append(i)
        return True,temp[0],temp[1]

def login_admin_checker(self):
    print("Admin")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

def register_checker(self, cursor, name, surname, sex, ssn, address, email, telephone, subscription, username, password):
    #print("Register")
    #print(name, surname, ssn, address, email, telephone, subscription[0], username, password)
    date = datetime.today().strftime('%Y-%m-%d')
    #print(date)
    if sex=="Άνδρας": sex = 'M'
    else: sex = 'F'

    cursor.execute("SELECT username FROM melos WHERE username=?", (username,))
    row = cursor.fetchone()
    if row is not None: return 1

    cursor.execute("SELECT ar_tautothtas FROM pelaths WHERE ar_tautothtas=?", (ssn,)) #Ελέγχουμε αν το μελλοντικό μέλος υπάρχει ήδη στη βάση ως πελάτης
    row = cursor.fetchone()
    if row is None: #Πελάτης δεν υπάρχει
        while True:
            memberid = rd.randint(1000000,9999999)
            cursor.execute("SELECT id_pelath FROM pelaths WHERE id_pelath=?", (memberid,))
            row = cursor.fetchone()
            if row is None: break

        try:
            cursor.execute("INSERT INTO pelaths VALUES (?,?,?,?,?,?,?,?)", (memberid, name.upper(), surname.upper(), sex, ssn, address, email, telephone))
            print("inserted as customer")
            cursor.execute("INSERT INTO melos VALUES (?,?,?,?,?,?)", (memberid, int(subscription[0]), date, username, password, "0"))
            print("inserted as member")
            return 0
        except sqlite3.Error as e: 
            print(e)
            return -1

    else:
        try:
            cursor.execute("SELECT id_pelath FROM pelaths WHERE ar_tautothtas=?",(ssn,))
            row = cursor.fetchone()
            for x in row:
                cursor.execute("SELECT memberid FROM melos WHERE memberid=?",(x,))
                if x is not None: 
                    return 2
                else: 
                    memberid = x
                    break
            cursor.execute("UPDATE pelaths SET onoma=?,epwnumo=?,sex=?,dieu8unsh=?,email=?,thlefwno=? WHERE ar_tautothtas=?", (name.upper(),surname.upper(),sex,address,email,telephone,ssn))
            print("updated as customer")
            cursor.execute("INSERT INTO melos VALUES (?,?,?,?,?,?)",(memberid, int(subscription[0]), date, username, password, "0"))
            return 0
        except sqlite3.Error as e: 
            print(e)
            return -1
        
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

def fetch_profile_info(self, cursor, memberid):
    try:
        cursor.execute("SELECT sundromh, prwth_eggrafh FROM melos WHERE memberid=?", (memberid,))
        row = cursor.fetchone()
        if row is None: return False
        lex1 = dict(row)
        cursor.execute("SELECT onoma,epwnumo,sex,ar_tautothtas,dieu8unsh,email,thlefwno FROM pelaths WHERE id_pelath=?", (memberid,))
        row = cursor.fetchone()
        if row is None: return False
        lex2 = dict(row)
        return (lex2["onoma"],lex2["epwnumo"], lex2["sex"], lex2["ar_tautothtas"], lex2["dieu8unsh"], lex2["email"], lex2["thlefwno"], lex1["sundromh"], lex1["prwth_eggrafh"])
        
    except sqlite3.Error as e: print(e); return False


def subscription_details(self, cursor, sub_num):
    try:
        cursor.execute("SELECT * FROM sundromh where id=?", (sub_num,))
        row = cursor.fetchone()
        row = dict(row)
        return row
    except sqlite3.Error as e: print(e); return False


def user_info(self, cursor, memberid):
    try:
        cursor.execute("SELECT username,password FROM melos WHERE memberid=?", (memberid,))
        row = cursor.fetchone()
        row = dict(row)
        return (row["username"], row["password"])
    except sqlite3.Error as e: print(e); return False,False


def edit_profile(self, cursor, username_new, password_new, memberid):
    try:
        cursor.execute("SELECT username FROM melos WHERE username=? AND memberid<>?", (username_new,memberid))
        row = cursor.fetchone()
        if row is not None: return 1

        cursor.execute("UPDATE melos SET username=?, password=? WHERE memberid=?", (username_new, password_new, memberid))
        return 0
    except sqlite3.Error as e: print(e); return -1


def completed_matches(self, cursor, memberid):
    try:
        cursor.execute("SELECT * FROM agwnas WHERE status IS NOT NULL AND memberid=? ORDER BY date;", (memberid,))
        row = cursor.fetchall()
        if len(row) == 0:
            return 1
        else:
            return row
    except sqlite3.Error as e: print(e); return -1


def upcoming_matches(self, cursor, memberid):
    try:
        cursor.execute("SELECT * FROM agwnas WHERE status IS NULL AND memberid=? AND date>CURRENT_DATE ORDER BY date;", (memberid,))
        row = cursor.fetchall()
        if len(row) == 0:
            return 1
        else:
            return row
    except sqlite3.Error as e: print(e); return -1


def field_info(self, cursor, fieldid):
    try:
        cursor.execute("SELECT * FROM ghpedo WHERE fieldid=?", (fieldid,))
        row = cursor.fetchone()
        return row
    except sqlite3.Error as e: print(e); return False


def not_completed_matches(self, cursor, memberid):
    try:
        cursor.execute("SELECT * FROM agwnas WHERE status IS NULL AND memberid=? AND date<CURRENT_DATE ORDER BY date;", (memberid,))
        row = cursor.fetchall()
        if len(row) == 0:
            return 1
        else:
            return row
    except sqlite3.Error as e: print(e); return -1


def submit_match(cursor, memberid, status, score, date, time):
    i=0; num_wins=0
    try:
        for x in status:
            if x == "Νίκη": status[i] = 'W'; num_wins+=1
            else: status[i] = 'L'
            cursor.execute("UPDATE agwnas SET score=?, status=? WHERE memberid=? AND date=? AND time=?", (score[i], status[i], memberid, date[i], time[i]))
            i+=1
        update_win_ratio(cursor, memberid)
        return 0
    except sqlite3.Error as e: print(e); return -1


def update_win_ratio(cursor, memberid):
    try:
        cursor.execute("SELECT COUNT(*) FROM agwnas WHERE memberid=? AND status is not NULL", (memberid,))
        row = cursor.fetchone()
        for x in row:
            total_matches = int(x)

        
        cursor.execute("SELECT COUNT(*) FROM agwnas WHERE memberid=? AND status='W'", (memberid,))
        row = cursor.fetchone()
        for x in row:
            total_wins = int(x)

        ratio = round(float(total_wins)/total_matches, 2) * 100
 


        cursor.execute("UPDATE melos SET win_ratio=? WHERE memberid=?",(ratio,memberid))
        return
    except sqlite3.Error as e: print(e); return


def find_my_ranking(cursor, memberid):
    try:
        cursor.execute("SELECT memberid, win_ratio FROM melos ORDER BY win_ratio DESC")
        row = cursor.fetchall()
        i=1
        for x in row:
            x = dict(x)
            if x["memberid"] == memberid: real_place = i; real_ratio = x["win_ratio"]; i+=1
            else: i+=1
        return real_place,i-1,real_ratio
    except sqlite3.Error as e: print(e); return -1


def my_program(cursor, memberid):
    try:
        cursor.execute("SELECT * FROM sumetexei WHERE memberid=?", (memberid,))
        row = cursor.fetchall()
        if len(row) == 0:
            return 1
        else:
            return row
    except sqlite3.Error as e: print(e); return -1


def find_program_by_id(cursor, programid):
    try:
        cursor.execute("SELECT epipedo, hlikia FROM programa WHERE programid=?", (programid,))
        row = cursor.fetchone()

        row2 = more_program_info(cursor, programid)
        return row,row2
    except sqlite3.Error as e: print(e)


def more_program_info(cursor, programid):
    try:
        cursor.execute("SELECT fieldid, hmera_wra_diarkeia FROM katalamvanei WHERE programid=?", (programid,))
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------


def fetch_profile_info_staff(cursor, employeeid):
    try:
        cursor.execute("SELECT * FROM prosopiko WHERE employeeid=?", (employeeid,))
        row = cursor.fetchone()
        return row
        
    except sqlite3.Error as e: print(e); return False


def my_program_gymnast(cursor, employeeid):
    try:
        cursor.execute("SELECT * FROM analamvanei WHERE employeeid=? AND year=strftime('%Y', CURRENT_TIMESTAMP)", (employeeid,))
        row = cursor.fetchall()
        if len(row) == 0:
            return 1
        else:
            return row
    except sqlite3.Error as e: print(e); return -1


def program_details(cursor, employeeid):
    try:
        cursor.execute("SELECT analamvanei.employeeid, programa.programid, programa.epipedo, programa.hlikia FROM(programa JOIN analamvanei ON analamvanei.programid = programa.programid) WHERE analamvanei.employeeid = ? AND analamvanei.year=strftime('%Y', CURRENT_TIMESTAMP)", (employeeid,))
        row = cursor.fetchall()
        if len(row) == 0:
            return 1
        else:
            return row
    except sqlite3.Error as e: print(e); return -1


def members_of_a_program(cursor, programid):
    try:
        cursor.execute('''SELECT sumetexei.programid, melos.memberid, pelaths.onoma, pelaths.epwnumo, pelaths.thlefwno, melos.win_ratio
                          FROM ((melos JOIN pelaths ON melos.memberid = pelaths.id_pelath) JOIN sumetexei ON melos.memberid = sumetexei.memberid) 
                          WHERE sumetexei.programid = ?;''', (programid,))
        row = cursor.fetchall()
        if len(row) == 0:
            return 1
        else:
            return row
    except sqlite3.Error as e: print(e); return -1


def programs_participating(cursor, memberid):
    try:
        cursor.execute("SELECT programid FROM sumetexei WHERE memberid = ?", (memberid,))
        row = cursor.fetchall()
        if len(row) == 0:
            return 1
        else: return row 
    except sqlite3.Error as e: print(e); return -1


def add_member(cursor, memberid, programid):
    try:
        cursor.execute("INSERT INTO sumetexei VALUES (?,?)", (memberid, programid))
        return
    except sqlite3.Error as e: print(e); return


def remove_member(cursor, memberid, programid):
    try:
        cursor.execute("DELETE FROM sumetexei WHERE memberid=? AND programid=?", (memberid,programid))
        return
    except sqlite3.Error as e: print(e); return

# ----------------------------------------------------------------------------------------------------------------------------------------

def find_all_customers(cursor):
    try:
        cursor.execute("SELECT * FROM pelaths WHERE id_pelath NOT IN (SELECT memberid FROM melos) ORDER BY epwnumo, onoma")
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def find_customer_by_name(cursor, name, surname):
    try:
        cursor.execute("SELECT * FROM pelaths WHERE onoma=? AND epwnumo=? AND id_pelath NOT IN (SELECT memberid FROM melos) ORDER BY epwnumo", (name, surname))
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def find_customer_by_phone(cursor, telephone):
    try:
        cursor.execute("SELECT * FROM pelaths WHERE thlefwno=? AND id_pelath NOT IN (SELECT memberid FROM melos) ORDER BY epwnumo", (telephone,))
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def find_customer_by_phone_and_name(cursor, name, surname, telephone):
    try:
        cursor.execute("SELECT * FROM pelaths WHERE onoma=? AND epwnumo=? AND thlefwno = ? AND id_pelath NOT IN (SELECT memberid FROM melos) ORDER BY epwnumo", (name, surname,telephone))
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def find_all_melh(cursor):
    try:
        cursor.execute("SELECT * FROM (pelaths JOIN melos ON id_pelath=memberid) ORDER BY epwnumo, onoma")
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def find_melos_by_name(cursor, name, surname):
    try:
        cursor.execute("SELECT * FROM (pelaths JOIN melos ON id_pelath=memberid) WHERE onoma=? AND epwnumo=?", (name, surname))
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def find_melos_by_phone(cursor, telephone):
    try:
        cursor.execute("SELECT * FROM (pelaths JOIN melos ON id_pelath=memberid) WHERE thlefwno=?", (telephone,))
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def find_melos_by_phone_and_name(cursor, name, surname, telephone):
    try:
        cursor.execute("SELECT * FROM (pelaths JOIN melos ON id_pelath=memberid) WHERE onoma=? AND epwnumo=? AND thlefwno=?", (name, surname, telephone))
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def find_melos_by_id(cursor, memberid):
    try:
        cursor.execute("SELECT * FROM (pelaths JOIN melos ON id_pelath=memberid) WHERE memberid=?", (memberid,))
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def add_customer(cursor, name, surname, sex, ssn, address, email, telephone):
    if sex=="Άνδρας": sex = 'M'
    else: sex = 'F'

    cursor.execute("SELECT ar_tautothtas FROM pelaths WHERE ar_tautothtas=?", (ssn,)) #Ελέγχουμε αν το μελλοντικό μέλος υπάρχει ήδη στη βάση ως πελάτης
    row = cursor.fetchone()
    if row is None: #Πελάτης δεν υπάρχει
        while True:
            memberid = rd.randint(1000000,9999999)
            cursor.execute("SELECT id_pelath FROM pelaths WHERE id_pelath=?", (memberid,))
            row = cursor.fetchone()
            if row is None: break

        try:
            cursor.execute("INSERT INTO pelaths VALUES (?,?,?,?,?,?,?,?)", (memberid, name, surname, sex, ssn, address, email, telephone))
            return 0
        except sqlite3.Error as e: 
            print(e)
            return -1
    else:
        return 1


def all_fields(cursor):
    try:
        cursor.execute("SELECT * FROM ghpedo")
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def is_a_customer(cursor, id_pelath):
    try:
        cursor.execute("SELECT id_pelath FROM pelaths WHERE id_pelath=?", (id_pelath,))
        row = cursor.fetchone()
        if row is None:
            return False
        else:
            return True
    except sqlite3.Error as e: print(e); return False


def add_match_2_ids(cursor, id_player1, id_player2, date, time, fieldid):
    try:
        cursor.execute('''INSERT INTO agwnas (memberid, onoma_antipalou, epwnumo_antipalou, fieldid, date, time)
                          VALUES (?, (SELECT onoma FROM pelaths WHERE id_pelath=?), (SELECT epwnumo FROM pelaths WHERE id_pelath=?), ?, ?, ?),
                          (?, (SELECT onoma FROM pelaths WHERE id_pelath=?), (SELECT epwnumo FROM pelaths WHERE id_pelath=?), ?, ?, ?)''', (id_player1, id_player2, id_player2, fieldid, date, time, id_player2, id_player1, id_player1, fieldid, date, time))
        return True
    except sqlite3.Error as e: print(e); return False


def add_match_1_id(cursor, id_player1, player2_name, player2_surname, date, time, fieldid):
    try:
        cursor.execute('''INSERT INTO agwnas (memberid, onoma_antipalou, epwnumo_antipalou, fieldid, date, time)
                          VALUES (?, ?, ?, ?, ?, ?)''', (id_player1, player2_name, player2_surname, fieldid, date, time))
        return True
    except sqlite3.Error as e: print(e); return False


def available_fields(cursor, date, num_day, time, duration):
    if num_day == '0': day = "Κυριακή"
    elif num_day == '1': day = "Δευτέρα"
    elif num_day == '2': day = "Τρίτη"
    elif num_day == '3': day = "Τετάρτη"
    elif num_day == '4': day = "Πέμπτη"
    elif num_day == '5': day = "Παρασκευή"
    elif num_day == '6': day = "Σάββατο"
    else: day = "Σφάλμα"

    end_time = str(int(time[0:2])+int(duration[0]))+time[2:]
    int_end_time = int(end_time[0:2])
    int_time = int(time[0:2])


    try:
        cursor.execute('''
                        SELECT fieldid, tupos, `timh/h` FROM ghpedo WHERE 
                        fieldid NOT IN (SELECT fieldid FROM katalamvanei WHERE hmera=? AND ((arxh>=? AND arxh<?) OR (lh3h>? AND lh3h<=?)))
                        AND fieldid NOT IN (SELECT fieldid FROM enoikiazei WHERE hmeromhnia = ? AND ((wra>=? AND wra<?) OR (wra+diarkeia>? AND wra+diarkeia<=?)))
                        ''', (day, time, end_time, time, end_time, date, time, end_time, int_time, int_end_time))
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def add_rent(cursor, fieldid, id_player1, date, time, duration):
    try:
        cursor.execute("INSERT INTO enoikiazei VALUES (?, ?, ?, ?, ?)", (fieldid, id_player1, date, time, duration))
        return True
    except sqlite3.Error as e: print(e); return False


def add_transaction(cursor, id_customer, deposit, remain, reason, fpa, payment_method, total_cost):
    while True:
        id_tr = rd.randint(1,9999999)
        cursor.execute("SELECT id_sunallaghs FROM sunallages WHERE id_sunallaghs=?", (id_tr,))
        row = cursor.fetchone()
        if row is None: break
    try:
        cursor.execute('''
        INSERT INTO sunallages
        VALUES (?, ?, ?, ?, CURRENT_DATE, CURRENT_TIME, ?, ?, ?, ?)
        ''', (id_tr, id_customer, deposit, remain, reason, fpa, payment_method, total_cost))
        return True
    except sqlite3.Error as e: print(e); return False


def find_all_pending_transactions(cursor):
    try:
        cursor.execute("SELECT * FROM sunallages WHERE upoloipo > 0 ORDER BY hmeromhnia DESC, wra")
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def find_pending_transactions_by_id(cursor, id_customer):
    try:
        cursor.execute("SELECT * FROM sunallages WHERE id_pelath = ? AND upoloipo > 0 ORDER BY hmeromhnia DESC, wra", (id_customer,))
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def find_all_completed_transactions(cursor):
    try:
        cursor.execute("SELECT * FROM sunallages WHERE upoloipo = 0 ORDER BY hmeromhnia DESC, wra")
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def find_completed_transactions_by_id(cursor, id_customer):
    try:
        cursor.execute("SELECT * FROM sunallages WHERE id_pelath = ? AND upoloipo = 0 ORDER BY hmeromhnia DESC, wra", (id_customer,))
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def find_pending_transactions_by_code(cursor, id_tr):
    try:
        cursor.execute("SELECT * FROM sunallages WHERE id_sunallaghs = ? AND upoloipo > 0", (id_tr,))
        row = cursor.fetchone()
        return row
    except sqlite3.Error as e: print(e); return


def submit_updated_transaction(cursor, id_tr, old_deposit, new_deposit, remain, payment):
    try:
        cursor.execute("UPDATE sunallages SET katavlh8en_poso = ?, upoloipo = ?, hmeromhnia=CURRENT_DATE, wra=CURRENT_TIME, tropos_plhrwmhs = ? WHERE id_sunallaghs=?", (float(old_deposit)+float(new_deposit), float(remain)-float(new_deposit), payment, id_tr))
        return True
    except sqlite3.Error as e: print(e); return False


def is_a_member(cursor, id_member):
    try:
        cursor.execute("SELECT memberid FROM melos WHERE memberid=?", (id_member,))
        row = cursor.fetchone()
        if row is None:
            return False
        else:
            return True
    except sqlite3.Error as e: print(e); return False


def admin_total_ranking(cursor):
    try:
        cursor.execute('''
        SELECT melos.memberid, pelaths.onoma, pelaths.epwnumo,  melos.win_ratio, 
        SUM(CASE WHEN status IS NOT NULL THEN 1 ELSE 0 END) AS 'total_matches',
        SUM(CASE WHEN status = 'W' THEN 1 ELSE 0 END) AS 'total_wins'
        FROM ((melos JOIN pelaths ON id_pelath = melos.memberid) LEFT JOIN agwnas ON melos.memberid = agwnas.memberid) 
        GROUP BY agwnas.memberid 
        ORDER BY melos.win_ratio DESC''')
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def admin_find_employees(cursor):
    try:
        cursor.execute("SELECT * FROM prosopiko WHERE douleia <> 'Διαχειριστής' ORDER BY epwnumo, onoma")
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def admin_find_rents(cursor):
    try:
        cursor.execute('''
        SELECT enoikiazei.*, pelaths.onoma, pelaths.epwnumo 
        FROM enoikiazei JOIN pelaths ON enoikiazei.id_pelath=pelaths.id_pelath 
        ORDER BY enoikiazei.hmeromhnia DESC, wra, epwnumo, onoma''')
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def find_all_transactions(cursor):
    try:
        cursor.execute("SELECT * FROM sunallages ORDER BY hmeromhnia DESC, wra")
        row = cursor.fetchall()
        return row
    except sqlite3.Error as e: print(e); return


def delete_member(cursor, memberid):
    try:
        cursor.execute("DELETE FROM melos WHERE memberid=?", (memberid,))
        return True
    except sqlite3.Error as e: print(e); return False


def delete_employee(cursor, employeeid):
    try:
        cursor.execute("DELETE FROM prosopiko WHERE employeeid=?", (employeeid,))
        return True
    except sqlite3.Error as e: print(e); return False


def remove_gymnast_from_program(cursor, employeeid):
    try:
        cursor.execute("DELETE FROM analamvanei WHERE employeeid=?", (employeeid,))
        return True
    except sqlite3.Error as e: print(e); return False


def add_employee(cursor, name, surname, type_of_job, ssn, address, telephone, email, salary, simvasi):
    while True:
        employeeid = rd.randint(100,999)
        cursor.execute("SELECT employeeid FROM prosopiko WHERE employeeid=?", (employeeid,))
        row = cursor.fetchone()
        if row is None: break
    username = random_username(employeeid)
    password = random_password()
    try:
        cursor.execute("INSERT INTO prosopiko VALUES (?, CURRENT_DATE, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (employeeid, ssn, name, surname, address, email, telephone, simvasi, type_of_job, salary, username, password))
        return True, employeeid, username, password
    except sqlite3.Error as e: print(e); return False, "nothing", "nothing", "nothing"




def random_username(employeeid):
    characters = string.ascii_letters
    username = []
    for _ in range(4):
        username.append(rd.choice(characters))
    username.append("_")
    username.append(employeeid)
    username = "".join(username)
    return username


def random_password():
    characters = string.ascii_letters + string.digits
    password = []
    for _ in range(10):
        password.append(rd.choice(characters))
    
    password = "".join(password)

    return password