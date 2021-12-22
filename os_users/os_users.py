import json
from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def read_users_data(file_path):
    with open("os_users_info.txt") as f:
        frame = pd.DataFrame(json.loads(row) for row in f)

    return frame


def clean_timezones(frame):
    frame['tz'].fillna('Missing', inplace=True)
    frame[frame['tz'] == ''] = 'Unknown'


def get_user_agents(frame):
    return pd.Series(x.split()[0] for x in frame.a.dropna())


def get_user_os(frame):
    os_frame = frame[frame.a.notnull()]
    os_frame['os'] = np.where(os_frame.a.str.contains('Windows'), 'Windows', 'Not Windows')

    os_counts = os_frame.groupby(['tz', 'os']).size().unstack().fillna(0)
    top_os = os_counts.sum(1).nlargest(10)
    os_subset = os_counts.loc[top_os.index]
    os_subset = os_subset.stack()
    os_subset.name = 'total'
    os_subset = os_subset.reset_index()
    os_subset['normed_total'] = os_subset.total / os_subset.groupby('tz').total.transform('sum')
    return os_subset


def main():
    df = read_users_data("os_users_info.txt")
    pprint(f"Timezones overview: {df['tz'].value_counts()[:10]}")

    clean_timezones(df)
    pprint(f"Timezones after cleaning: {df['tz'].value_counts()[:10]}")

    user_agents = get_user_agents(df)
    pprint(f"Top user agents: {user_agents.value_counts()[:8]}")

    user_os = get_user_os(df)

    fig, ax = plt.subplots(figsize=(15, 10))
    sns.barplot(x='normed_total', y='tz', data=user_os, ax=ax, hue='os')
    fig.savefig('os_users.png')


if __name__ == "__main__":
    main()
