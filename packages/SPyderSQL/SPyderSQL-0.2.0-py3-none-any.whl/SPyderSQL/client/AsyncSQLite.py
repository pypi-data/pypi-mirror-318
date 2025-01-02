import aiosqlite
from typing import Optional, List, Union, Dict, Any


def makeup_columns(arguments: dict, columns: str = '') -> str:
    """
    Создание макета столбцов для таблиц базы данных

    :param arguments: Словарь аргументов столбцов таблицы. Ключи - названия столбцов, значения - их типы.
    :param columns: Уже существующие колонки
    :return: отформатированные столбцы в типе данных str
    """
    if columns and not columns.endswith(', '):
        columns += ', '
    columns += ", ".join(
        f"{column_name} {column_type}"
        for column_name, column_type in arguments.items()
    )
    return columns


class AsyncSQLite:

    def __init__(self, db_path: str):
        """
        Инициализация асинхронного SQLite класса.

        :param db_path: Путь к файлу базы данных SQLite.
        """
        self.db_path = db_path
        self.query = ""
        self.parameters: List[Any] = []  # Список для хранения параметров запроса


    def __str__(self):
        return self.query


    def create(self, name_table: str, append_columns: dict, id_primary_key: bool = False):
        """
        Создает SQL-запрос для создания таблицы, если она не существует.

        :param name_table: Название создаваемой таблицы.
        :param append_columns: Словарь столбцов таблицы. Ключи - названия столбцов, значения - их типы.
        :param id_primary_key: Добавить ли в начале таблицы уникальный id. По умолчанию False.
        :return: Экземпляр класса AsyncSQLite.
        """
        columns = ''

        if id_primary_key:
            columns = 'id INTEGER PRIMARY KEY AUTOINCREMENT, '

        columns = makeup_columns(append_columns, columns)

        # Создание SQL-запроса
        self.query = f"CREATE TABLE IF NOT EXISTS {name_table} ({columns})"

        return self


    def alter(self, name_table: str, add_column: dict):
        """
        Создает SQL-запрос для изменения таблицы. Добавляет новые колонки.

        :param name_table: Название таблицы.
        :param add_column: Словарь нового столбца. Ключи - название столбца, значения - его тип.
        :return: Экземпляр класса AsyncSQLite.
        """
        column = makeup_columns(add_column)

        # Создание SQL-запроса
        self.query = f"ALTER TABLE {name_table} ADD {column}"

        return self


    def drop(self, name_table: str):
        """
        Создает SQL-запрос для удаления существующей таблицы.

        :param name_table: Название таблицы, которую нужно удалить.
        :return: Экземпляр класса AsyncSQLite.
        """
        # Создание SQL-запроса
        self.query = f"DROP TABLE IF EXISTS {name_table}"

        return self


    def insert(self, name_table: str, names_columns: List[str]):
        """
        Создает INSERT запрос для заполнения таблицы новыми данными.

        :param name_table: Название таблицы.
        :param names_columns: Названия колонок таблицы.
        :return: Экземпляр класса AsyncSQLite.
        """
        # Выписывание названий колонок
        names_columns_str = ", ".join(names_columns)

        # Подсчет колонок, с которыми будут взаимодействовать
        count_columns = len(names_columns)

        values_columns = ["?"] * count_columns

        # Преобразование списка знаков "?" в str
        values_columns_str = ', '.join(values_columns)

        # Создание SQL-запроса
        self.query = f"INSERT INTO {name_table} ({names_columns_str}) VALUES ({values_columns_str})"

        return self


    def select(self, name_table: str, names_columns: Union[List[str], str] = '*'):
        """
        Создает базовый SELECT запрос для выборки данных из таблицы.

        :param name_table: Название таблицы.
        :param names_columns: Список названий столбцов для выборки или строка "*" для всех столбцов.
        :return: Экземпляр класса AsyncSQLite.
        """
        if isinstance(names_columns, list):
            names_columns = ", ".join(names_columns)

        # Создание SQL-запроса
        self.query = f"SELECT {names_columns} FROM {name_table}"

        return self


    def where(self, conditions: dict):
        """
        Добавляет WHERE условия в запрос для поиска записей.

        :param conditions: Словарь условий.
        :return: Экземпляр класса AsyncSQLite.
        """
        placeholders = []

        for key, value in conditions.items():
            placeholders.append(f"{key} = ?")
            self.parameters.append(value)

        cond = " AND ".join(placeholders)
        self.query += f" WHERE {cond}"

        return self


    def limit(self, count: int):
        """
        Добавляет LIMIT в запрос.

        :param count: Количество строк для ограничения выборки.
        :return: Экземпляр класса AsyncSQLite.
        """
        self.query += f" LIMIT {count}"

        return self


    def order_by(self, columns: List[str], order: str = "ASC"):
        """
        Добавляет ORDER BY в запрос.

        :param columns: Список колонок для сортировки.
        :param order: Порядок сортировки, "ASC" или "DESC".
        :return: Экземпляр класса AsyncSQLite.
        """
        columns_str = ", ".join(columns)

        self.query += f" ORDER BY {columns_str} {order}"

        return self


    def update(self, name_table: str, data_set: dict, conditions: Optional[dict] = None):
        """
        Создает UPDATE запрос для обновления данных.

        :param name_table: Название таблицы.
        :param data_set: Словарь данных для обновления.
        :param conditions: Условия для обновления.
        :return: Экземпляр класса AsyncSQLite.
        """
        updates = ", ".join(f"{key} = ?" for key in data_set.keys())
        self.parameters.extend(data_set.values())  # Добавляем значения для обновления

        self.query = f"UPDATE {name_table} SET {updates}"

        if conditions:
            self.where(conditions)

        return self


    def delete(self, name_table: str, conditions: Optional[dict] = None):
        """
        Создает DELETE запрос для удаления записи из таблицы.

        :param name_table: Название таблицы.
        :param conditions: Условия для удаления.
        :return: Экземпляр класса AsyncSQLite.
        """
        self.query = f"DELETE FROM {name_table}"

        if conditions:
            self.where(conditions)

        return self


    def reset(self):
        """
        Сбрасывает текущий запрос.
        """
        self.query = ""
        self.parameters = []

        return self


    def build(self) -> str:
        """
        Возвращает финальный SQL запрос.

        :return: Строка SQL-запроса.
        """
        query = self.query
        self.reset()

        return query


    async def execute(self, parameters: Optional[tuple] = None) -> Optional[List[Dict[str, Any]]]:
        """
        Асинхронно выполняет текущий SQL запрос.

        :param parameters: Кортеж параметров для запроса. Если None, используются self.parameters.
        :return: Результаты выполнения запроса для SELECT, иначе None.
        """
        try:
            async with aiosqlite.connect(self.db_path) as db:
                db.row_factory = aiosqlite.Row  # Для доступа к столбцам по имени
                async with db.execute(self.query, parameters or tuple(self.parameters)) as cursor:
                    if self.query.strip().upper().startswith("SELECT"):
                        result = await cursor.fetchall()
                        # Преобразование Row объектов в обычные словари
                        return [dict(row) for row in result]
                    else:
                        await db.commit()
                        return None
        except aiosqlite.Error as error:
            print(f"Ошибка при выполнении запроса: {error}")
            return None
        finally:
            self.reset()


    async def executemany(self, parameters_list: List[tuple]):
        """
        Асинхронно выполняет текущий SQL запрос для множества параметров.

        :param parameters_list: Список кортежей параметров для запроса.
        :return: None
        """
        try:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.executemany(self.query, parameters_list):
                    await db.commit()
        except aiosqlite.Error as error:
            print(f"Ошибка при выполнении множественного запроса: {error}")
        finally:
            self.reset()


    async def fetch_one(self, parameters: Optional[tuple] = None) -> Optional[Dict[str, Any]]:
        """
        Асинхронно выполняет текущий SQL запрос и возвращает первую найденную запись.

        :param parameters: Кортеж параметров для запроса. Если None, используются self.parameters.
        :return: Первый результат выполнения запроса для SELECT, иначе None.
        """
        try:
            async with aiosqlite.connect(self.db_path) as db:
                db.row_factory = aiosqlite.Row
                async with db.execute(self.query, parameters or tuple(self.parameters)) as cursor:
                    if self.query.strip().upper().startswith("SELECT"):
                        row = await cursor.fetchone()
                        if row:
                            return dict(row)
                        else:
                            return None
                    else:
                        await db.commit()
                        return None
        except aiosqlite.Error as error:
            print(f"Ошибка при выполнении запроса: {error}")
            return None
        finally:
            self.reset()
