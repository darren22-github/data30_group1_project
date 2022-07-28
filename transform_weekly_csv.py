import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def csv_to_df(csv_file: str):
    dataframe = pd.read_csv(csv_file)
    return dataframe


def combining_analytic_column(dataframe):
    dataframe['Analytic'] = dataframe.apply(
        lambda row: [row.Analytic_W1, row.Analytic_W2, row.Analytic_W3, row.Analytic_W4, row.Analytic_W5,
                     row.Analytic_W6,
                     row.Analytic_W7, row.Analytic_W8], axis=1)
    return dataframe


def combining_independent_column(dataframe):
    dataframe['Independent'] = dataframe.apply(
        lambda row: [row.Independent_W1, row.Independent_W2, row.Independent_W3, row.Independent_W4, row.Independent_W5,
                     row.Independent_W6, row.Independent_W7, row.Independent_W8], axis=1)
    return dataframe


def combining_determined_column(dataframe):
    dataframe['Determined'] = dataframe.apply(
        lambda row: [row.Determined_W1, row.Determined_W2, row.Determined_W3, row.Determined_W4, row.Determined_W5,
                     row.Determined_W6, row.Determined_W7, row.Determined_W8], axis=1)
    return dataframe


def combining_professional_column(dataframe):
    dataframe['Professional'] = dataframe.apply(
        lambda row: [row.Professional_W1, row.Professional_W2, row.Professional_W3, row.Professional_W4,
                     row.Professional_W5, row.Professional_W6, row.Professional_W7, row.Professional_W8], axis=1)
    return dataframe


def combining_studious_column(dataframe):
    dataframe['Studious'] = dataframe.apply(
        lambda row: [row.Studious_W1, row.Studious_W2, row.Studious_W3, row.Studious_W4, row.Studious_W5,
                     row.Studious_W6,
                     row.Studious_W7, row.Studious_W8], axis=1)
    return dataframe


def combining_imaginative_column(dataframe):
    dataframe['Imaginative'] = dataframe.apply(
        lambda row: [row.Imaginative_W1, row.Imaginative_W2, row.Imaginative_W3, row.Imaginative_W4, row.Imaginative_W5,
                     row.Imaginative_W6, row.Imaginative_W7, row.Imaginative_W8], axis=1)
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

print(df)