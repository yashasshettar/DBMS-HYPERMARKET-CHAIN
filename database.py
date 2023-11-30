import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yashas2003#",
    database="hypermarket_582"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS ADMIN (ANAME varchar(30), APASS varchar(30));')
    c.execute('CREATE TABLE IF NOT EXISTS dist (DID varchar(30), DNAME varchar(30), DPASS varchar(30), DTYPE varchar(30), DLOC varchar(30));')
    c.execute('CREATE TABLE IF NOT EXISTS sales (salesid varchar(30), sdate varchar(30), scost varchar(30), sid varchar(30));')
    c.execute('CREATE TABLE IF NOT EXISTS stock (cry varchar(30), scry varchar(30), quant varchar(30), sid varchar(30));')
    c.execute('CREATE TABLE IF NOT EXISTS store (sid varchar(30), spass varchar(30), sbranchname varchar(30), scity varchar(30), sregion varchar(30), sstate varchar(30), spcode varchar(30));')
    c.execute('CREATE TABLE IF NOT EXISTS st_orders (ordid varchar(30), sid varchar(30), did varchar(30), orddate varchar(30), pmystat varchar(30), shpmode varchar(30), shpstat varchar(30));')

def execute_(query):
    c.execute(query)
    result = c.fetchall()
    return result

def add_admin(ANAME, APASS):
    c.execute('INSERT INTO ADMIN (ANAME, APASS) VALUES (%s,%s);',
              (ANAME, APASS))
    mydb.commit()

def add_distributor(did, d_name, d_pass, d_type, d_loc):
    c.execute('INSERT INTO dist (DID,DNAME,DPASS,DTYPE,DLOC) VALUES (%s,%s,%s,%s,%s);',
              (did, d_name, d_pass, d_type, d_loc))
    mydb.commit()

def add_sales(salesid, sdate, scost, sid):
    c.execute('INSERT INTO sales (salesid, sdate, scost, sid) VALUES (%s,%s,%s,%s);',
              (salesid, sdate, scost, sid))
    mydb.commit()

def add_stock(cry, scry, quant, sid):
    c.execute('INSERT INTO stock (cry, scry, quant, sid) VALUES (%s,%s,%s,%s);',
              (cry, scry, quant, sid))
    mydb.commit()    

def add_store(sid, spass, sbranchname, scity, sregion, sstate, spcode):
    c.execute('INSERT INTO store (sid, spass, sbranchname, scity, sregion, sstate, spcode) VALUES (%s,%s,%s,%s,%s,%s,%s);',
              (sid, spass, sbranchname, scity, sregion, sstate, spcode))
    mydb.commit()

def add_stord(ordid, sid, did, orddate, pmystat, shpmode, shpstat):
    c.execute('INSERT INTO st_orders (ordid, sid, did, orddate, pmystat, shpmode, shpstat) VALUES (%s,%s,%s,%s,%s,%s,%s);',
              (ordid, sid, did, orddate, pmystat, shpmode, shpstat))
    mydb.commit()    

def view_admin():
    c.execute('SELECT * FROM ADMIN')
    data = c.fetchall()
    return data

def view_distributor():
    c.execute('SELECT * FROM dist')
    data = c.fetchall()
    return data

def view_sales():
    c.execute('SELECT * FROM sales')
    data = c.fetchall()
    return data 

def view_stock():
    c.execute('SELECT * FROM stock')
    data = c.fetchall()
    return data 

def view_store():
    c.execute('SELECT * FROM store')
    data = c.fetchall()
    return data

def view_stord():
    c.execute('SELECT * FROM st_orders')
    data = c.fetchall()
    return data

def view_only_admin_names():
    c.execute('SELECT ANAME FROM ADMIN')
    data = c.fetchall()
    return data

def view_only_distributor_did():
    c.execute('SELECT Did FROM dist')
    data = c.fetchall()
    return data

def view_only_sales_salesid():
    c.execute('SELECT SALESID FROM Sales')
    data = c.fetchall()
    return data


def view_only_scry():
    c.execute('SELECT scry FROM Stock')
    data = c.fetchall()
    return data

def view_only_store_sid():
    c.execute('SELECT sid FROM Store')
    data = c.fetchall()
    return data    

def view_only_ordid():
    c.execute('SELECT ordid FROM st_orders')
    data= c.fetchall()
    return data

def get_admin(id):
    c.execute(f'SELECT * FROM ADMIN WHERE ANAME="{id}";')
    data=c.fetchall()
    return data

def get_dist(id):
    c.execute(f'SELECT * FROM dist WHERE DID="{id}";')
    data=c.fetchall()
    return data

def get_store(id):
    c.execute(f'SELECT * FROM store WHERE SID="{id}";')
    data=c.fetchall()
    return data

def get_sales(id):
    c.execute(f'SELECT * FROM sales WHERE salesID="{id}";')
    data=c.fetchall()
    return data    

def get_stock(scry):
    c.execute(f'SELECT * FROM stock WHERE scry="{scry}";')
    data=c.fetchall()
    return data 

def get_stord(ordid):
    c.execute(f'SELECT * FROM st_orders WHERE ordid="{ordid}";')
    data=c.fetchall()
    return data    

def edit_admin_details(ANAME, APASS, admin_id):
    c.execute(f"UPDATE ADMIN SET ANAME='{ANAME}', APASS='{APASS}' WHERE ANAME='{admin_id}'")
    mydb.commit()

def edit_dist_details(new_dname, new_dpass, new_dtype,new_dloc, did):
    c.execute(f"UPDATE dist SET DNAME='{new_dname}', DPASS='{new_dpass}',DTYPE='{new_dtype}', DLOC='{new_dloc}' WHERE did={did}")
    mydb.commit()

def edit_sales_details(salesid,new_sdate, new_scost,sid):
    c.execute(f"UPDATE sales SET scost='{new_scost}', Sdate='{new_sdate}' WHERE salesid={salesid}")
    mydb.commit()

def edit_stock_details(scry,new_cry, new_quant,sid):
    c.execute(f"UPDATE stock SET cry = '{new_cry}',quant={new_quant} WHERE SCRY ='{scry}'")
    mydb.commit()

def edit_store_details(sid, new_spass, new_sbranchname,new_scity, new_sregion,new_sstate,new_spcode):
    c.execute(f"UPDATE store SET spass = '{new_spass}',sbranchname='{new_sbranchname}',scity='{new_scity}',sregion='{new_sregion}',sstate='{new_sstate}',spcode={new_spcode} WHERE SID ='{sid}'")
    mydb.commit()

def edit_stord_details(ordid,new_orddate,new_shpmode,new_shpstat,new_pmystat):
    c.execute(f"UPDATE st_orders SET orddate = '{new_orddate}',shpmode='{new_shpmode}',shpstat='{new_shpstat}',pmystat='{new_pmystat}' WHERE ORDID ='{ordid}'")
    mydb.commit()

def delete_admin_data(selected_admin):
    c.execute('DELETE FROM ADMIN WHERE ANAME="{}"'.format(selected_admin))
    mydb.commit()

def delete_dist_data(selected_did):
    c.execute('DELETE FROM dist WHERE did="{}"'.format(selected_did))
    mydb.commit()   


def delete_sales_data(selected_salesid):
    c.execute('DELETE FROM sales WHERE salesid="{}"'.format(selected_salesid))
    mydb.commit()      

def delete_stock_data(scry):
    c.execute('DELETE FROM stock WHERE scry="{}"'.format(scry))
    mydb.commit() 

def delete_store_data(sid):
    c.execute('DELETE FROM store WHERE sid="{}"'.format(sid))
    mydb.commit()     

def delete_stord_data(ordid):
    c.execute('DELETE FROM st_orders WHERE ordid="{}"'.format(ordid))
    mydb.commit()    

def create_trigger_delete_sale():
    c.execute('''
        CREATE TRIGGER update_stock_after_delete_sale
        AFTER DELETE ON sales
        FOR EACH ROW
        BEGIN
            UPDATE stock
            SET quant = quant + OLD.scost
            WHERE sid = OLD.sid;
        END;
    ''')
    mydb.commit()

def create_procedures():
    # Procedure for adding an admin
    c.execute('''
        CREATE PROCEDURE add_admin_proc(IN ANAME_param varchar(30), IN APASS_param varchar(30))
        BEGIN
            INSERT INTO ADMIN (ANAME, APASS) VALUES (ANAME_param, APASS_param);
        END;
    ''')

    # Procedure for adding a distributor
    c.execute('''
        CREATE PROCEDURE add_distributor_proc(IN did_param varchar(30), IN d_name_param varchar(30), IN d_pass_param varchar(30), IN d_type_param varchar(30), IN d_loc_param varchar(30))
        BEGIN
            INSERT INTO dist (DID, DNAME, DPASS, DTYPE, DLOC) VALUES (did_param, d_name_param, d_pass_param, d_type_param, d_loc_param);
        END;
    ''')

    # Procedure for adding sales
    c.execute('''
        CREATE PROCEDURE add_sales_proc(IN salesid_param varchar(30), IN sdate_param varchar(30), IN scost_param varchar(30), IN sid_param varchar(30))
        BEGIN
            INSERT INTO sales (salesid, sdate, scost, sid) VALUES (salesid_param, sdate_param, scost_param, sid_param);
        END;
    ''')

    # Procedure for adding stock
    c.execute('''
        CREATE PROCEDURE add_stock_proc(IN cry_param varchar(30), IN scry_param varchar(30), IN quant_param varchar(30), IN sid_param varchar(30))
        BEGIN
            INSERT INTO stock (cry, scry, quant, sid) VALUES (cry_param, scry_param, quant_param, sid_param);
        END;
    ''')

    # Procedure for adding store
    c.execute('''
        CREATE PROCEDURE add_store_proc(IN sid_param varchar(30), IN spass_param varchar(30), IN sbranchname_param varchar(30), IN scity_param varchar(30), IN sregion_param varchar(30), IN sstate_param varchar(30), IN spcode_param varchar(30))
        BEGIN
            INSERT INTO store (sid, spass, sbranchname, scity, sregion, sstate, spcode) VALUES (sid_param, spass_param, sbranchname_param, scity_param, sregion_param, sstate_param, spcode_param);
        END;
    ''')

    # Procedure for adding st_orders
    c.execute('''
        CREATE PROCEDURE add_stord_proc(IN ordid_param varchar(30), IN sid_param varchar(30), IN did_param varchar(30), IN orddate_param varchar(30), IN pmystat_param varchar(30), IN shpmode_param varchar(30), IN shpstat_param varchar(30))
        BEGIN
            INSERT INTO st_orders (ordid, sid, did, orddate, pmystat, shpmode, shpstat) VALUES (ordid_param, sid_param, did_param, orddate_param, pmystat_param, shpmode_param, shpstat_param);
        END;
    ''')

    mydb.commit()






