
def write_data_backup(filename, data):
    f = open("backup/"+filename, "w")
    f.write(data)
