import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)



    # Identifying people with higher education (Bachelors, Masters, Doctorate)
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    # People without higher education
    lower_education = ~higher_education

    # Calculate the percentage of people with higher education earning >50K
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)


    # Calculate the percentage of people without higher education earning >50K
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)



    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = (num_min_workers['salary'] == '>50K' ).mean() * 100

    # What country has the highest percentage of people that earn >50K?
   # Calculate the percentagev of people earning >50K for each country
    country_earning_data = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)

    # Find the country with the highest percentage of people earning >50K
    highest_earning_country = country_earning_data.idxmax()

    # Get the highest percentage of people earning >50K
    highest_earning_country_percentage = round(country_earning_data.max(), 1)


    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
