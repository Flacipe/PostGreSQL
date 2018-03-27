import os


DB_HOST='localhost'
DB_USER = 'appll_web'
DB_USER_PASSWORD = 'erty'
DB_NAME = ''
BACKUP_PATH = 'backup/dbbackup/'

DB_NAME = input("Enter backup'name in format 'DDMMYYYY-HHMMSS' which is the backup's timecode :")

restorecmd = "mysql -u"+DB_USER+"-p" + DB_USER_PASSWORD + "postgre < " + DB_NAME + ".sql"
print ("Backup restored")
