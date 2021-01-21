import sqlite3


class database:

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def create_table(self, table_name, cols):

        if len(cols) > 0 and bool(table_name):
            command = f'create table if not exists {table_name}('
            for col in cols.values():
                name, type, constraints = col.values()
                if constraints:
                    command += f'{name} {type} {constraints},'
                else:
                    command += f'{name} {type},'
            command = command[0:len(command)-1]
            command += ')'
            self.cur.execute(command)
            self.conn.commit()

    def insert_values(self, table_name, values):
        if table_name and values:
            for row_values in values.values():
                command = f'insert into {table_name} values('
                for value in row_values.values():
                    command += f'{value},'
                command = command[0:len(command)-1]
                command += ')'
                self.cur.execute(command)
            self.conn.commit()
        elif not table_name:
            print('Failer 1 : table name is not identified')
        elif not values:
            print('Failer 2 : no value found')
        else:
            print('Failer 1, 2 : Table name is not identified and no value found')
    def query(self,query_strcture):
        command ='select '

db_cols = {
    1: {
        'col_name': 'c1',
        'data_type': 'TEXT',
        'constraints': ''
    },
    2: {
        'col_name': 'c2',
        'data_type': 'INTEGER',
        'constraints': 'NOT NULL'
    },
    3: {
        'col_name': 'c3',
        'data_type': 'TEXT',
        'constraints': 'UNIQUE'
    },

}
db_data = {
    1: {'c1': '\'fffff\'',
        'c2': 96455,
        'c3': '"hello"'},
    2:
        {'c1': '\'qqqqqq\'',
         'c2': 65465,
         'c3': '"welcome"'},

    3:
        {'c1': '\'ffnbf g\'',
         'c2': 9849418,
         'c3': '"hai"'},


}
db_query={
    'query':'*',
    'from ':'userC',
    'where':'c2 > 1000'
}
db = database('a.sqlite3')
db.create_table(table_name='userC', cols=db_cols)
db.insert_values(table_name='userC', values=db_data)
