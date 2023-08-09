"""import csv


def csv_to_txt(csv_file, txt_file):
    with open(txt_file, "w", encoding='utf-8') as my_output_file:
        with open(csv_file, "r", encoding='utf-8') as my_input_file:
            [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()"""



def read_csv(csv_file):
    with open(csv_file, "r", encoding='utf-8') as f:
        return f.readlines()







