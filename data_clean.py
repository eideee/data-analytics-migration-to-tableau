class DataClean:

    def clean_flight_data(table_name):
        table_name.dropna(axis=0, how='all', inplace=True)
        table_name.dropna(axis=1, how='all', inplace=True)
    