import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def csv_to_df(csv_file: str):
    dataframe = pd.read_csv(csv_file)
    return dataframe


def combining_analytic_column(dataframe):
    filter_col_analytic = [col for col in dataframe if col.startswith('Analy')]
    dataframe['Analytic'] = dataframe[filter_col_analytic].values.tolist()
    return dataframe


def combining_independent_column(dataframe):
    filter_col_independent = [col for col in dataframe if col.startswith('Indep')]
    dataframe['Independent'] = dataframe[filter_col_independent].values.tolist()
    return dataframe


def combining_determined_column(dataframe):
    filter_col_determined = [col for col in dataframe if col.startswith('Deter')]
    dataframe['Determined'] = dataframe[filter_col_determined].values.tolist()
    return dataframe


def combining_professional_column(dataframe):
    filter_col_professional = [col for col in dataframe if col.startswith('Prof')]
    dataframe['Professional'] = dataframe[filter_col_professional].values.tolist()
    return dataframe


def combining_studious_column(dataframe):
    filter_col_studious = [col for col in dataframe if col.startswith('Studious')]
    dataframe['Studious'] = dataframe[filter_col_studious].values.tolist()


def combining_imaginative_column(dataframe):
    filter_col_imaginative = [col for col in dataframe if col.startswith('Imagi')]
    dataframe['Imaginative'] = dataframe[filter_col_imaginative].values.tolist()
    return dataframe


def exploding_created_columns(dataframe):
    dataframe = dataframe.explode(['Analytic', 'Independent', 'Determined', 'Professional', 'Studious', 'Imaginative'])
    return dataframe


def adding_week_column(dataframe):
    dataframe['Week'] = dataframe['Week'] = dataframe.groupby(['name']).cumcount().add(1)
    return dataframe


def sorting_values(dataframe):
    dataframe = dataframe.sort_values(by=['Week', 'name'])
    return dataframe


def selecting_specific_columns(dataframe):
    dataframe = dataframe.reset_index()
    dataframe = dataframe[
        ['name', 'trainer', 'Week', 'Analytic', 'Independent', 'Determined', 'Professional', 'Studious', 'Imaginative']]
    return dataframe


def transformed_dataframe(dataframe):
    combining_analytic_column(dataframe)
    combining_independent_column(dataframe)
    combining_determined_column(dataframe)
    combining_professional_column(dataframe)
    combining_studious_column(dataframe)
    combining_imaginative_column(dataframe)
    dataframe = exploding_created_columns(dataframe)
    adding_week_column(dataframe)
    dataframe = sorting_values(dataframe)
    dataframe = selecting_specific_columns(dataframe)

    return dataframe


df = csv_to_df('Data_31_2019-05-20.csv')
df = transformed_dataframe(df)
df.to_csv('new_data.csv', sep=',')
