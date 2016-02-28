import sqlite3

class OperationDB(object):
	def get_conn(self):
		'''连接数据库'''
		conn = sqlite3.connect('cltdata.db')
		return conn

	def get_cursor(self):
		'''创建游标'''
		conn = self.get_conn()
		#print('执行游标')
		return conn.cursor()

	def close_all(self, conn, cu):
		'''关闭数据库游标对象和数据库连接对象'''
		try:
			if cu is not None:
				cu.close()
		finally:
			if conn is not None:
				conn.close()


	def create_table(self):
		'''创建数据库表：sampleinfo testresult'''
		conn = self.get_conn()
		c = self.get_cursor()
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


	def insert_sampleinfo(self, data):
		'''sampleinfo表插入数据'''
		#conn = sqlite3.connect('svrdata.db')
		conn = self.get_conn()
		conn.execute('insert into sampleinfo values (?,?,?,?,?,?)', data)
		conn.commit()
		print('表[sampleinfo]数据写入成功!')
		conn.close()    


	def insert_testresult(self, data):
		'''testresult表插入数据'''
		#conn = sqlite3.connect('svrdata.db')
		conn = self.get_conn()
		conn.execute('insert into testresult (sampleid, testvalue) values (?,?)', data)
		conn.commit()
		print('表[testresult]数据写入成功!')
		conn.close()
		
	def update_resultvalue(self, data):
		'''更新数据...'''
		print('更新数据...')
		conn = self.get_conn()
		conn.execute('update testresult set testvalue = ? where sampleid = ? and testname = ?', data)
		conn.commit()
		print('数据修改成功')
		conn.close()
		
	#sid = input('pls input sid :',)

	def select_db(self, sid):
		cursor = self.get_cursor()
		result= ()
		cursor.execute("select 'P' as P,pati_id,pati_name,pati_age,pati_gender from sampleinfo where sampleid=?", sid)
		result += (cursor.fetchone(),)
		cursor.execute("select 'O' as O,sampleid,status from sampleinfo where sampleid=?", sid)
		result += (cursor.fetchone(),)
		cursor.execute("select 'R' as R,testname,testvalue from testresult  where sampleid =?", sid)
		result += tuple(cursor.fetchall())
		cursor.close()
		self.get_conn().close()
		return result

	def select_test(self):
		'''查询结果数据'''
		conn = self.get_conn()
		c = self.get_cursor()
		c.execute("select * from testresult")
		rows = c.fetchall()
		conn.close()
		return rows
		
	def select_data(self, sid):
		'''查询结果数据'''
		conn = self.get_conn()
		c = self.get_cursor()
		c.execute('''select sampleinfo.sampleid,pati_id,pati_name,pati_age,status,testname,testvalue
                             from sampleinfo left outer join testresult on sampleinfo.sampleid = testresult.sampleid where sampleinfo.sampleid=?''', sid)
		rows = c.fetchone()
		c.close()
		conn.close()
		return rows
	
	def testConn(self, params):
		return "success"	

	def orderEntry(self, params):
		conn = self.get_conn()
		c = conn.cursor()
		c.execute('insert into sampleinfo values (?,?,?,?,?,?)', (params[0],params[1],params[2],params[3],params[4],params[5]))
		conn.commit()
		print('表[sampleinfo]数据写入成功!')
		for test in params[6]:
			c.execute('insert into testresult (sampleid, testname) values (?,?)', (params[0], test))
			conn.commit()
			print('表[testresult]数据写入成功!')
		conn.close()
		test = self.select_data((params[0],))
		return '数据写入成功!, sid: ' + str(test)
	
	def selectTest(self, sid):
		cursor = self.get_cursor()
		result= ()
		cursor.execute("select 'P' as P,pati_id,pati_name,pati_age,pati_gender from sampleinfo where sampleid=?", sid)
		result += (cursor.fetchone(),)
		cursor.execute("select 'O' as O,sampleid,status from sampleinfo where sampleid=?", sid)
		result += (cursor.fetchone(),)
		cursor.execute("select 'R' as R,testname,testvalue from testresult  where sampleid =?", sid)
		result += tuple(cursor.fetchall())
		cursor.close()
		return result