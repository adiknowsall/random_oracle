from config import *
import numpy as np
import psycopg2

def connect():
    """ returns connection to database """
    # TODO: use variables from config file as connection params
    conn = psycopg2.connect(host=host, database=name, user=user, password=pswd, port=port)
    return conn

def exec_query(conn, sql):
    """ Executes sql query and returns header and rows """
    # TODO: create cursor, get header from cursor.description, and execute query to fetch rows.
    # return (header, rows)
    cur=conn.cursor()
    cur.execute(sql)
    header=[]
    try:
        header=[x[0] for x in cur.description]
    except:
        pass

    rows=[]
    try:
        rows=cur.fetchall()
    except:
        pass
    conn.commit()
    return (header,rows)

conn = connect()
query = '''drop table if exists oracle; create table oracle (query_param int, output char(64));'''
(header, rows) = exec_query(conn, query)
conn.commit()
conn.close()
arr=np.random.randint(0,2,size=16)

digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f']
def gen_str(num):
	ret=""
	for i in range(16):
		if(num[i]==arr[i]):
			ret+=np.random.choice(digits[0:8])
			for j in range(3):
				ret+=np.random.choice(digits)
		else:
			ret+=np.random.choice(digits[8:16])
			for j in range(3):
				ret+=np.random.choice(digits)
	return ret
num=0
while(num!=-1):
	print("Query:")
	num=int(input())
	if(num==-1):
		break
	conn=connect()
	cur=conn.cursor()
	cur.execute("select * from oracle where query_param=%s",(num,))
	rows=cur.fetchall()
	if(len(rows)==0):
		bin_num=str(bin(num))[2:]
		if(len(bin_num)!=16):
			bin_num="0"*(16-len(bin_num))+bin_num
		rand_str=gen_str(bin_num)
		print(rand_str)
		cur.execute('''insert into oracle values (%s,%s)''',(num,rand_str,))
		conn.commit()
		conn.close()
	else:
		print(rows[0][1])
print("exiting...")