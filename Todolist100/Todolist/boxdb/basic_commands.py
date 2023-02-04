'''
boxdb/basic_commands -> v0.4

This file contain code for
1)row , column creation and deletion
2)and gettting table

[ ]get_table() doesnt crash if there is not table made
[ ]create_columns() works better now 
'''

from os import remove
from os.path import exists
from filemod import writer, delete_specific_line, remove_word, word_find,word_search_line,write_specific_line
from tabulate import tabulate
from boxdb.support_litebase import get_content, get_primary_column, get_columns


def create_columns(table_name, rows, unique=False):
    """creates files under table so that data can be stored"""

    # get all the column names
    content = get_columns(table_name)
    column_lenght = [len(get_content(f"{table_name}/tables/{columns}.txt",
                         f"{table_name}/tables/{columns}.txt",)) for columns in content] if content else [0]

    make_columns = []
    # write to data file and make files if in list
    if not isinstance(rows, list):
        make_columns.append(rows)
    else:
        make_columns = rows

    for elements in make_columns:
        # this check redundancy in the table and avoid it
        if elements in content:
            print(f"COLUMN :  {elements} already exists")
            if len(rows) == 1:
                return False
            continue
        # fill all the empty void with putting null in the file if there is already columns
        try:
            writer(f"./{table_name}/tables/{elements}.txt",
                   "null \n"*max(column_lenght), "w")
        except FileNotFoundError:
            print('COLUMN : could not create')

        # checks if file exists
        if exists(f"./{table_name}/tables/{elements}.txt"):
            # update the data file
            writer(f"./{table_name}/{table_name}_data.txt",
                                 f"{elements} {'-P'if unique else ''} \n","a")
        else:
            print(f"COLUMN : {elements} could not be created")
   
   # FIXME try cutting read and write time
    
    # with open(f"./{table_name}/{table_name}_data.txt", 'r+', encoding="UTF-8") as file:
    #     lines = file.readlines()
    #     file.seek(0)
    #     file.writelines(line for line in lines if line.strip())
    #     file.truncate()

    print(f"Created {len(content)} Column sucessfully")
    return True


def remove_column(table_name, column):
    """removes files under table so that data can be released"""
# FIXME cant remove the -p evertime 

    content = get_columns(table_name)
# list input
    if isinstance(column, list):
        # element extractiion from the list
        for elements in column:
            # writing into file when the file is present into data file
            if content.count(elements) == 1:
                remove_word(f"{table_name}/{table_name}_data.txt", elements)
                remove(f"./{table_name}/tables/{elements}.txt")
            else:
                print(f"ERROR : {elements} not present in table")

# string input
    elif content.count(column) == 1:
        remove_word(f"{table_name}/{table_name}_data.txt", column)
        remove(f"./{table_name}/tables/{column}.txt")

    else:
        print(f'ERROR : {column} not present in table')


def add_row(table_name, data_in_array):
    """removes files under table so that data can be released"""

    #TODO addrow() function is way too complicated

    content = get_columns(table_name)

    # get all the primary column to detect dublication
    primary_key = get_primary_column(table_name)

    # writing into file and check for the actually number of row and inputs
    if len(content) == len(data_in_array):
        catch_rows = []
        catch_col = []

        for column, rows in zip(content, data_in_array):

            # this checks for the double entry in table of primary column
            if column in primary_key:
                # if dublication is found
                if word_find(f"./{table_name}/tables/{column}.txt", rows):
                    print(f"PRIMARY KEY : {rows} exits in the {column}")
                    continue
            # if its not forund then stored in classs
                else:
                    catch_rows.append(rows)
                    catch_col.append(column)

        # this is for non primary column
            else:
                catch_rows.append(rows)
                catch_col.append(column)

        # this tally all the catch row and actualy column
        if len(content) == len(catch_col):
            for c_col, c_row in zip(catch_rows, catch_col):
                writer(
                    f"./{table_name}/tables/{c_row}.txt", f"{c_col} \n", "a")
        else:
            print("ERROR")
    else:
        print("Imblance number of rows")


def get_table(table_name, columns=None):
    """
    It is used to display table in terminal or even filture
    out some rows according to the convience
    """

    table = []

    if columns is None:
        columns = []

    # get the number of columns
    content = get_columns(table_name)
    if len(content) <= 0:
        print(f"TABLE : {table_name} has no structure yet")
        return False

    # if no column input assume it to be content
    if columns != []:
        content = columns

    # get the amount of rows in column and calculate the higest
    for column in content:
        row_content = get_content(
            f"{column}.txt", f"./{table_name}/tables/{column}.txt")
        table.append(row_content)
    higest_col = max(map(len, table))

    # filter the empty or half filled list to replace with null
    for item in table:
        if len(item) < higest_col:
            for _ in range(higest_col):
                if len(item) != higest_col:
                    item.append("null")
    result = [[table[j][i]
               for j in range(len(table))] for i in range(len(table[0]))]

    print(tabulate(result, headers=content, tablefmt="fancy_grid"),
          f"\nTable config = {len(get_columns(table_name))}x{higest_col}")
    return True


def remove_row_number(table_name, row_number):
    """
    removing colums with refrence of the number
    """
    content = get_columns(table_name)
    for column in content:
        try:
            delete_specific_line(
                f"./{table_name}/tables/{column}.txt", row_number)
        except Exception:
            print(f"ERROR : ROW number {row_number} not found")

def get_elements(table_name,column):
    """
    get values from column
    """
    with open(f'.\\{table_name}\\tables\\{column}.txt','r+',encoding="UTF-8") as files:
        line=files.readlines()
    return [elements.removesuffix('\n').strip() for elements in line]


def remove_rows(table_name,column,row_element):
    rows=get_columns(table_name)
    primary=get_primary_column(table_name)
    if column not in primary:
        return False
    row_to_remove=word_search_line(f'.\\{table_name}\\tables\\{column}.txt',row_element)
    for elements in rows:
        delete_specific_line(f'.\\{table_name}\\tables\\{elements}.txt',row_to_remove)
    return True

def update_row(table_name,prii_column,primary_element,column,element):
    row_to_update=word_search_line(f'.\\{table_name}\\tables\\{prii_column}.txt',primary_element)
    print("row u: ",row_to_update)
    write_specific_line(f'.\\{table_name}\\tables\\{column}.txt',row_to_update,element)
    return True