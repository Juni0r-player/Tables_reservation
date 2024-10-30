tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False},
    6: None,
    7: None,
    8: None,
    9: None,
}

def is_table_free(num_tables):
    'return true if table is free, if table is reserve, return false'
    return tables[num_tables] is None

def get_free_tables():
    'return numbers of free tables'
    return [i for i in tables if tables[i] is None]

def reserve_table(num_tables: int, clients_name: str, status: str):
    'functions for reserve table'
    if is_table_free(num_tables): # == True Если столик пустой
        tables[num_tables] = {'name': clients_name, 'is_vip': status}
    return tables

def delete_reservation(num_tables):
    'functions for delete reservation'
    tables[num_tables] = None
    return tables



