import mysql.connector
from faker import Faker
import random
fake = Faker()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shingha",
  database="onncall"
)

mycursor = mydb.cursor()

for x in range(50):
""" 
 *todo Jobs

 jobId = random.randint(0,99999)
 serviceId = random.randint(0,99999)
 jobName = fake.word()
 stdTime = random.randint(0, 1000)
 stdPrice = random.randint(0, 100)
 staffQty = random.randint(0, 50)
 user = random.randint(0, 50)
 flag = ""
 status = "O"

 sql = "INSERT INTO jobs (jobId, serviceId, jobName, stdTime, stdPrice, staffQty, user, flag, status, created, modified, xguid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)"
 val = (jobId, serviceId, jobName, stdTime, stdPrice, staffQty, user, flag, status, "2020-07-21 08:14:07", "2020-07-21 08:14:07", "")

  """

refnum = "JOR-"+random.randint(0,99999)
requestRefNo = "SRQ-"+random.randint(0,99999)
companyId = fake.word()
jobId = "S-"+random.randint(0, 999)
jobStatus = random.randint(0, 999)
siteId = "N-"+random.randint(0, 999999)
problemDesc = fake.word()
reportDate = "2020-07-21 02:52:00"
urgencyLevel = fake.word()
poc = fake.first_name()
mobile = fake.phone_number()
tel = fake.phone_number()
email = fake.ascii_safe_email()
designation = fake.word()


 sql = "INSERT INTO jobs (jobId, serviceId, jobName, stdTime, stdPrice, staffQty, user, flag, status, created, modified, xguid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)"
 val = (jobId, serviceId, jobName, stdTime, stdPrice, staffQty, user, flag, status, "2020-07-21 08:14:07", "2020-07-21 08:14:07", "")




 mycursor.execute(sql, val)
 mydb.commit()