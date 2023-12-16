import pandas as pd


def cleaning_data():
    # Read the data
    df = pd.read_csv('src/presidents.tsv', sep='\t')

    # Function to swap first and last names if needed
    def swap_names(name):
        parts = name.split(' ')
        if len(parts) == 2 and ',' in parts[0]:
            return parts[1] + ' ' + parts[0].replace(',', '')
        return name

    # Clean the 'President' column
    df['President'] = df['President'].apply(
        lambda x: swap_names(x)).str.title()

    # Clean the 'Start' column and convert to integer
    df['Start'] = df['Start'].str.extract('(\d{4})').astype(int)

    # Clean the 'Last' column, replace '-' with NaN, and convert to float
    df['Last'] = pd.to_numeric(df['Last'], errors='coerce')

    # Clean the 'Seasons' column, map 'two' to 2, and convert to integer
    df['Seasons'] = df['Seasons'].replace('two', 2).astype(int)

    # Clean the 'Vice-president' column
    df['Vice-president'] = df['Vice-president'].apply(
        lambda x: swap_names(x)).str.title()

    return df


def main():
    cleaned_data = cleaning_data()
    print(cleaned_data)


if __name__ == "__main__":
    main()
