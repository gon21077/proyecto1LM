"Realización de lectura de datos sin hacer uso de librería pandas"
def read_csv(csv_file):
    with open(csv_file, "r", encoding='utf-8') as f:
        return f.readlines()