import os
import sys
import time
import zipfile
import datetime
from os.path import basename

# Globale Variablen
backup_pfad = 'C:/backup/dbbackup/backups/'
archiv_pfad = 'C:/backup/dbbackup/archiv/'
temp_pfad = 'C:/backup/dbbackup/'
datetime_total = 0
datetime_stunde = 0
datetime_minute = 0
db_host = 'localhost'
db_user = 'root'
db_user_pw = 'john'
db_name = 'baufuchs'


def main():
    manual = True
    datetime_total = time.strftime('%Y%m%d-%H%M%S')
    datetime_stunde = time.strftime('%H')
    datetime_minute = time.strftime('%M')

    if check_time() == 0:
        backup_name = temp_pfad + db_name + "_db_" + datetime + '.sql'
        backup(backup_name)
        compress(backup_name)
    if (manual == True):
        backup(backup_name)
    age(28)
    age(14)
    return


def help():
    print ('PLACEHOLDER')
    print ('PLACEHOLDER')
    print ('PLACEHOLDER')
    sys.exit()


def backup(backup_name):
    check_backup_pfad()
    w = open(backup_name, 'w')
    w.write('Dies ist ein Testbackup!')
    w.close()
    print('Backup erfolgreich')
    return


def age(days):
    now = time.time()
    limit = now - (days * 86400)

    if days == 28:
        files = os.listdir(os.path.join(archiv_pfad))
        file_path = os.path.join(archiv_pfad)
        for xfile in files:
            if os.path.isfile(str(file_path) + xfile):
                t = os.stat(str(file_path) + xfile)
                c = t.st_ctime
                if c < limit:
                    if (t.index.hour != 20):
                        os.remove(str(file_path) + xfile)
    if days == 14:
        files = os.listdir(os.path.join(backup_pfad))
        file_path = os.path.join(backup_pfad)
        for xfile in files:
            if os.path.isfile(str(file_path) + xfile):
                t = os.stat(str(file_path) + xfile)
                c = t.st_ctime
                if c < limit:
                    os.rename(str(file_path) + xfile, archiv_pfad + xfile)
    return


def compress(backup_name):
    zip_name = backup_pfad + db_name + "_db_" + datetime_total + '.zip'
    compressed = zipfile.ZipFile(zip_name, mode='w')
    try:
        compressed.write(backup_name, basename(backup_name))
    finally:
        compressed.close()
    os.remove(backup_name)
    return


def check_backup_pfad():
    try:
        if not os.path.exists(backup_pfad):
            os.makedirs(backup_pfad)
        if not os.path.exists(archiv_pfad):
            os.makedirs(archiv_pfad)
            return 0
        elif (os.path.exists(backup_pfad) and os.path.exists(archiv_pfad)):
            print ('Pfad ist vorhanden')
            return 0
    except:
        print ('Fehler')
        exit(2)
    return


def check_time():
    if datetime_stunde == '12' or datetime_stunde == '20':
        print ('Backup Zeit')
        if datetime_minute == '00':
            print('Minute 0')
            return 1
    return 0
