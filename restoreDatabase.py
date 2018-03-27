import os


DB_HOST=input('ip address : ')
DB_USER = input('Login : ')
DB_USER_PASSWORD = input('Password : ')
BACKUP_PATH = 'backup/dbbackup/'

DB_FOLDER = input("Enter the name of the backup directory : ")
DB_NAME = input('Enter the database name : ')

restorecmd = "mysql -u"+DB_USER+" -p" + DB_USER_PASSWORD +" "+ DB_NAME + " < " + BACKUP_PATH + DB_FOLDER +"/"+ DB_NAME+".sql"
os.system(restorecmd)
print ("Backup restored")
