import sqlite3

def get_conn():
    '''连接数据库'''
    conn = sqlite3.connect('svrdata.db')
    return conn
 
 
def get_cursor():
    '''创建游标'''
    conn = get_conn()
    #print('执行游标')
    return conn.cursor()


def close_all(conn, cu):
    '''关闭数据库游标对象和数据库连接对象'''
    c = get_cursor()
    conn = get_conn()
    try:
        if c is not None:
            c.close()
    finally:
        if c is not None:
            c.close()
    try:
        if conn is not None:
            conn.close()
    finally:
        if conn is not None:
            conn.close()


def create_table():
    '''创建数据库表：sampleinfo testresult'''
    conn = get_conn()
    c = get_cursor()
    c.execute('''
	          create table if not exists sampleinfo
			  (sampleid varchar(20) PRIMARY KEY,pati_id varchar(20),pati_name varchar(20),
			   pati_age varchar(20),pati_gender varchar(5),status varchar(5))
			  '''	
			  )
    c.execute('''
	          create table if not exists testresult
			  (sampleid varchar(20),testname varchar(20),testvalue varchar(20))
			  '''
			  )
    c.execute('create index testresult_sid on testresult(sampleid)')
    conn.commit()
    print('创建数据库表[sampleinfo,testresult]成功!')
    conn.close()


def insert_sampleinfo(data):
    '''sampleinfo表插入数据'''
    #conn = sqlite3.connect('svrdata.db')
    conn = get_conn()
    c = conn.cursor()

    for t1 in [("111222","000001","zhangsan","1990-01-01","male","Stat"),
	          ("111333","000002","wuwu","1990-02-01","female","Stat"),
			  ("111444","000003","lisi","1990-03-01","female","Stat"),
			  ("111555","000004","wang","1990-04-01","male","Stat"),
			  ("111666","000005","liuliu","1990-05-01","male","Stat"),
			 ]:

        c.execute('insert into sampleinfo values (?,?,?,?,?,?)', t1)

    conn.commit()
    print('表[sampleinfo]数据写入成功!')
    conn.close()    


def insert_testresult(data):
    '''testresult表插入数据'''
    #conn = sqlite3.connect('svrdata.db')
    conn = get_conn()
    c = conn.cursor()   

    for t2 in [("111222","AST", "2.6"),
              ("111222","ALT", "2.67"),
              ("111222","Cl", "2.69"),
			  ("111222","Na", "22.1"),
			  ("111222","K", "22.1"),
			  ("111333","AST", "3.6"),
              ("111333","ALT", "32.67"),
              ("111333","Cl", "32.69"),
			  ("111333","Na", "322.1"),
			  ("111333","K", "33.1"),
			  ("111444","AST", "42.6"),
              ("111444","ALT", "42.67"),
              ("111444","Cl", "42.69"),
			  ("111444","Na", "422.1"),
			  ("111444","K", "43.1"),
			  ("111555","AST", "5.6"),
              ("111555","ALT", "52.67"),
              ("111555","Cl", "5.69"),
			  ("111555","Na", "55.1"),
			  ("111555","K", "55.1"),
			  ("111666","AST", "6.6"),
              ("111666","ALT", "6.67"),
              ("111666","Cl", "6.69"),
			  ("111666","Na", "66.1"),
			  ("111666","K", "66.1"),
             ]:

        c.execute('insert into testresult values (?,?,?)', t2)
        
    conn.commit()
    print('表[testresult]数据写入成功!')
    conn.close()

#sid = input('pls input sid :',)

def select_db(sid):
    '''查询结果数据'''
    conn = get_conn()
    c = get_cursor()
    sid = input('pls input sid :',)
    id = (sid,)
    list =[]
    c.execute("select 'P' as P,pati_id,pati_name,pati_age from sampleinfo where sampleid=?",id)
    #result_p=c.fetchone()
    list.append(c.fetchone())
    c.execute("select 'O' as O,sampleid,status from sampleinfo where sampleid=?",id)
    #result_o=c.fetchone
    list.append(c.fetchone())
    c.execute("select 'R' as R,testname,testvalue from testresult  where sampleid =?",id)
    for row in c.fetchall():
      #print(row)
      list.append(row)
    print(list)
    conn.commit()
    conn.close()
    

def select_test():
    '''查询结果数据'''
    conn = get_conn()
    c = get_cursor()
    rows = c.execute("select * from testresult")
    
    #print(c.fetchone())
    for row in rows:
      print(row)
    conn.commit()
    conn.close()

def update_resultvalue(data):
    '''更新数据...'''
    print('更新数据...')
    conn = get_conn()
    c = get_cursor()

    u1 = [("600",111222,"K")]
    c.execute('update testresult set testvalue = ? where sampleid = ? and testname = ?',u1)
    conn.mit()
    print('数据修改成功')
    conn.close()
    c.close()
       
class AI01(object):
    def selectData(self, sid):
        cursor = get_cursor()
        result= ()
        cursor.execute("select 'P' as P,pati_id,pati_name,pati_age,pati_gender from sampleinfo where sampleid=?", sid)
        result += (cursor.fetchone(),)
        cursor.execute("select 'O' as O,sampleid,status from sampleinfo where sampleid=?", sid)
        result += (cursor.fetchone(),)
        cursor.execute("select 'R' as R,testname,testvalue from testresult  where sampleid =?", sid)
        result += tuple(cursor.fetchall())
        cursor.close()
        return result
    
    def testConn(self, params):
        return "success"
    
    def orderEntry(self, params):
        conn = get_conn()
        c = conn.cursor()
        c.execute('insert into sampleinfo values (?,?,?,?,?,?)', (params[0],params[1],params[2],params[3],params[4],params[5]))
        conn.commit()
        print('表[sampleinfo]数据写入成功!')
        for test in params[6]:
            c.execute('insert into testresult (sampleid, testname) values (?,?)', (params[0], test))
            conn.commit()
            print('表[testresult]数据写入成功!')
        conn.close()
        test = self.selectData((params[0],))
        return '数据写入成功!, sid: ' + test