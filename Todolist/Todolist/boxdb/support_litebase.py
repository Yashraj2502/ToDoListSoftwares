'''
boxdb/support_litebase -> v0.3

This file contain code for
1)get the data from file, and get row data

[ ]get_content() speed optimization

'''

def get_content(context, target):
    """
    It gets the content from any file with
    data in it(auto generated) and returns in list
    """
    lines = []
    try:        
        with open(target,encoding='UTF-8') as file:
            for line in file:
                line = line.strip()
                lines.append(line)
    except FileNotFoundError:
        print(f"{context} file missing")
    return lines

def get_columns(table_name):
    """
    It gets the content from any file with
    data in it(auto generated) and returns in list
    """
    lines = []

    try:
        with open(f"{table_name}/{table_name}_data.txt",encoding='UTF-8') as file:
            for line in file:
                line = line.strip()
                try:
                    lines.append(line.removesuffix("-P").strip())
                except Exception:
                    lines.append(line)
    except FileNotFoundError:
        print("column file missing")
    return lines


def get_primary_column(table_name):
    """
    This gets all the primary key rows from the table
    """
    #FIXME optimization need takes 0.009 secs
    columns= get_content("row", f"{table_name}/{table_name}_data.txt")
    return [
        elements[: len(elements) - 2].strip()
        for elements in columns
        if elements.find("-P") > 0]

