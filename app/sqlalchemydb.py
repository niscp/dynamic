from sqlalchemy import Table, MetaData, create_engine, exc, VARCHAR, BOOLEAN, Column, TEXT, INT, DATETIME, and_, select, \
    INTEGER, Enum, FLOAT, NUMERIC, DATE, DECIMAL
from sqlalchemy import asc, desc
import manage
from app.log import Log

class AlchemyDB:
    engine = None
    _table = dict()

    def __init__(self):
        self.conn = AlchemyDB.get_connection()
        self.trans = None

    @staticmethod
    def init():
        try:
            mysql_string = manage.app.config['DATABASE_URI'] + 'happay_data'

            AlchemyDB.engine = create_engine(mysql_string,
                                             paramstyle='format',
                                             isolation_level="READ UNCOMMITTED")

            meta = MetaData()


            AlchemyDB.question_value = Table('question_value', meta,
                                            Column('aid', INT),
                                            Column('question', TEXT),
                                            Column('option_one', VARCHAR(255)),
                                            Column('option_two', VARCHAR(255)),
                                            Column('option_three', VARCHAR(255)),
                                            Column('option_four', VARCHAR(255)),
                                            Column('soft_delete', INT)
                                            )
            AlchemyDB._table['question_value'] = AlchemyDB.question_value


            meta.create_all(AlchemyDB.engine)

        except exc.SQLAlchemyError as error:
            Log.log_error("CreateConnectionPool Exception: %s" % error)

    @staticmethod
    def get_connection():
        try:
            return AlchemyDB.engine.connect()
        except Exception as exception:
            print exception

    @staticmethod
    def get_table(name):
        return AlchemyDB._table[name]

    def begin(self):
        self.trans = self.conn.begin()

    def commit(self):
        self.trans.commit()

    def rollback(self):
        self.trans.rollback()

    @staticmethod
    def args_to_where(table, args):
        clause = []
        for k, v in args.items():
            if isinstance(v, (list, tuple)):
                clause.append(table.c[k].in_(v))
            else:
                clause.append(table.c[k] == v)
        return and_(*clause)

    def insert_row(self, table_name, **values):
        table = AlchemyDB.get_table(table_name)
        insert = table.insert().values(values)
        self.conn.execute(insert)

    def update_row(self, table_name, *keys, **row):
        table = AlchemyDB.get_table(table_name)
        try:
            if not isinstance(keys, (list, tuple)):
                keys = [keys]
            if not keys or len(keys) == len(row):
                return False
            clause = dict()
            for k in keys:
                clause[k] = row[k]
            clean_row = row.copy()
            for key in keys:
                if key in clean_row.keys():
                    del clean_row[key]
            clauses = AlchemyDB.args_to_where(table, clause)
            update = table.update(clauses, clean_row)
            self.conn.execute(update)
            return True
        except Exception as err:
            Log.log_error("update error %s" % err)
            return False

    def delete_row(self, table_name, **where):
        table = AlchemyDB.get_table(table_name)
        try:
            delete = table.delete().where(AlchemyDB.args_to_where(table, where))
            self.conn.execute(delete)
        except exc.SQLAlchemyError as err:
            Log.log_error("delete error %s" % err)
            return False

    def find_one(self, table_name, **where):
        table = AlchemyDB.get_table(table_name)
        try:
            sel = select([table]).where(AlchemyDB.args_to_where(table, where))
            row = self.conn.execute(sel)
            tup = row.fetchone()
            return dict(tup)
        except exc.SQLAlchemyError as err:
            Log.log_error("find error %s" % err)
            return False

    def test(self, q, _limit=None, _offset=None):
        try:
            if _limit or _offset:
                sel = q + " LIMIT " + str(_limit) + " OFFSET " + str(_offset)
            else:
                sel = q
            Log.log_error(sel)
            row = self.conn.execute(sel)
            tup = row.fetchall()
            list = []
            for r in tup:
                list.append(dict(r))
            return list
        except exc.SQLAlchemyError as err:
            Log.log_error("find error %s" % err)
            return False

    def find(self, table_name, order_by=None, _limit=None, _offset=None, _group_by=None, **where):
        table = AlchemyDB.get_table(table_name)

        try:
            func = asc
            if order_by and order_by.startswith('_'):
                order_by = order_by[1:]
                func = desc
            if _limit or _offset:
                sel = select([table]).where(AlchemyDB.args_to_where(table, where)).order_by(func(order_by)).limit(
                    _limit).offset(_offset)
            elif _group_by:
                sel = select([table]).where(AlchemyDB.args_to_where(table, where)).order_by(func(order_by)).group_by(
                    func(_group_by))

            else:
                sel = select([table]).where(AlchemyDB.args_to_where(table, where)).order_by(func(order_by))
            row = self.conn.execute(sel)
            tup = row.fetchall()
            list = []
            for r in tup:
                list.append(dict(r))
            return list
        except exc.SQLAlchemyError as err:
            Log.log_error("find error %s" % err)
            return False

