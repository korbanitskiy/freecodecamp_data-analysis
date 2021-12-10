import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    race_count = df.value_counts(['race'])
    average_age_men = round(df[df['sex'] == "Male"]['age'].mean(), 1)
    percentage_bachelors = round(df[df['education'] == "Bachelors"].index.size / df.index.size * 100, 1)

    # percentage with salary >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    more_50k = df['salary'] == ">50K"

    higher_education_rich = round(df[higher_education & more_50k].index.size / df[higher_education].index.size * 100, 1)
    lower_education_rich = round(df[~higher_education & more_50k].index.size / df[~higher_education].index.size * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df['hours-per-week'] == df['hours-per-week'].min()
    rich_percentage = df[min_workers & more_50k].index.size / df[min_workers].index.size * 100

    # What country has the highest percentage of people that earn >50K?
    people_per_country = df.value_counts('native-country')
    top_earning_countries = df[more_50k].value_counts('native-country') / people_per_country * 100

    highest_earning_country = top_earning_countries.idxmax()
    highest_earning_country_percentage = round(top_earning_countries[highest_earning_country], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_occupations = df[more_50k & (df['native-country'] == 'India')].value_counts('occupation').sort_values(ascending=False)
    top_occupation = list(india_occupations.keys())[0]

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
        print("Top occupations in India:", top_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_occupation
    }
