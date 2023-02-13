import maps


def remove_columns(dataframe):
    """
    Removes all unnessary columns for Power BI dashboard
    :param dataframe: pandas dataframe
    :return: dataframe with dropped columns
    """
    drop_columns = dataframe.keys().tolist()
    drop_columns.remove('detection_time')
    drop_columns.remove('probability')
    drop_columns.remove('detection_count')
    drop_columns.remove('drone_lat')
    drop_columns.remove('drone_lon')
    drop_columns.remove('surveyID')
    drop_columns.remove('KML')
    drop_columns.remove('species_category')
    drop_columns.remove('species_name')
    return dataframe.drop(columns=drop_columns)

def standardise_species_name(dataframe):
    # Strip text, remove underscores and add capitalised first letters
    dataframe['species_name'] = dataframe['species_name'].str.strip()
    dataframe['species_name'] = dataframe['species_name'].str.title()
    dataframe['species_name'] = dataframe['species_name'].str.replace('_', ' ')

    # Cycle through the species_name column and correct alternate spelling
    remove_indices = []
    for idx, name in dataframe['species_name'].items():
        if name in maps.to_remove:
            remove_indices.append(idx)
            continue
        for correct_name, alias_list in maps.species_name_map.items():
            if name in alias_list:
                dataframe.at[idx, 'species_name'] = correct_name
                break

    # Remove vague detections
    return dataframe.drop(index=remove_indices)


def standardise_probability(dataframe):
    # Trim whitespace and add capitalised first letters
    dataframe['probability'] = dataframe['probability'].str.strip()
    dataframe['probability'] = dataframe['probability'].str.title()

    # Cycle through the probability column and correct alternate spelling
    for idx, name in dataframe['probability'].items():
        for correct_name, alias_list in maps.probability_map.items():
            if (name in alias_list):
                dataframe.at[idx, 'probability'] = correct_name
                break

    return dataframe


def standardise_species_category(dataframe):
    # Trim whitespace and add capitalised first letters
    dataframe['species_category'] = dataframe['species_category'].str.strip()
    dataframe['species_category'] = dataframe['species_category'].str.title()
    dataframe['species_category'] = dataframe['species_category'].str.replace('_', ' ')

    # Cycle through the probability column and correct alternate spelling
    for idx, name in dataframe['species_category'].items():
        for correct_name, alias_list in maps.species_category_map.items():
            if name in alias_list:
                dataframe.at[idx, 'species_category'] = correct_name
                break

    return dataframe


def correct_species_categories(dataframe):
    for idx, name in dataframe['species_name'].items():
        for correct_category, alias_list in maps.species_category_corrections.items():
            if name in alias_list:
                dataframe.at[idx, 'species_category'] = correct_category
                break
    return dataframe


def clean_data(dataframe):
    dataframe = remove_columns(dataframe)
    dataframe = standardise_species_name(dataframe)
    dataframe = standardise_probability(dataframe)
    dataframe = standardise_species_category(dataframe)
    dataframe = correct_species_categories(dataframe)
    return dataframe
