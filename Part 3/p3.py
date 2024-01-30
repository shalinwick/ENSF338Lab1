import json
import matplotlib.pyplot as plt

def separate_by_income(data):
    income_below_10000 = []
    income_at_or_above_10000 = []

    for country in data:
        income = country.get("incomeperperson")
        if income is not None and isinstance(income, (int, float)):
            if income < 10000:
                income_below_10000.append(country)
            else:
                income_at_or_above_10000.append(country)

    return income_below_10000, income_at_or_above_10000


def plot(data, filename, title):
    internet_usage = [country["internetuserate"] for country in data if country["internetuserate"] is not None]
    plt.figure(figsize=(10, 6))
    plt.hist(internet_usage, color='lightgreen', edgecolor='black')
    plt.title(title)
    plt.xlabel('Internet Usage Rate (%)')
    plt.ylabel('Number of Countries')
    plt.savefig(filename)
    plt.close()

with open('internetdata.json', 'r') as file:
    data = json.load(file)

income_below_10000, income_at_or_above_10000 = separate_by_income(data)

plot(income_below_10000, 'hist1.png', 'Internet Usage in Countries with Income below $10,000')
plot(income_at_or_above_10000, 'hist2.png', 'Internet Usage in Countries with Income at or above $10,000')
