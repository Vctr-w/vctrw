import peewee as pw
import datetime
from config2 import DATABASES
import os

db = pw.MySQLDatabase(
	DATABASES['default']['NAME'], 
	host = DATABASES['default']['HOST'], 
	port = int(DATABASES['default']['PORT']), 
	user = DATABASES['default']['USER'], 
	passwd = DATABASES['default']['PASSWORD'])

class BaseModel(pw.Model):
    class Meta:
        database = db

class Blog(BaseModel):
	title = pw.CharField()
	urlTitle = pw.CharField(unique=True)
	content = pw.TextField()
	timestamp = pw.DateTimeField(default = datetime.datetime.utcnow(), index = True)
	class Meta:
		order_by = ('timestamp',)

def create_tables():
	db.connect()
	db.create_tables([Blog])



	
