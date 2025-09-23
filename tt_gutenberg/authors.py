def load_data():
    """Creating a function to load the data and make a copy."""
    
    # importing libraries
    import pandas as pd
    import numpy as np
    
    # loading data and making a copy
    df = pd.read_csv('gutenberg_authors.csv')
    df_copy = df.copy()
    
    # returning the dataframe
    return df

def clean_alias(df):
    """Creating a function to clean the alias column by removing NaN values and
    other messy values."""
    
    # Removing NaN values
    df = df[df['alias'].notna()]
    
    # Removing messy values
    df = df[~df['alias'].str.contains('NA', case = False, na = False)]
    
    return df

def count_alias_translations(df):
    """Creating a function to count the number of translations for each alias
    and grouping by the alias column."""
    
    # importing libraries
    import pandas as pd
    import numpy as np
    
    # grouping the data by the alias column and counting the number of translations
    alias_counts = df.groupby('alias').size().reset_index(name = 'translation_count')
    
    # Sort by 'translation_count' in descending order
    alias_counts = alias_counts.sort_values(by='translation_count', ascending=False)
    
    # returning the alias counts
    return alias_counts
    
    # checking the unique values in the translation_count column
    # unique_values = alias_counts['translation_count'].unique()
    
    # returning the unique values
    # return unique_values

def list_authors(by_languages = False, alias = True):
    """Creating a function to list authors by languages or aliases."""

    # loading data
    df = load_data()
    
    # cleaning the alias column
    df = clean_alias(df)
    
    # grouping by the alias translation counts
    df = count_alias_translations(df)
    
    # returning the sorted dataframe
    return df