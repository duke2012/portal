from  atmb.utils import  dbHelper
import json

def  getIndexMenuList():
	sql='select * from atmb_atmb'
	data=dbHelper.readDb(sql)
	return json.dumps(data)
