import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

import pandas as pd

from prettytable import PrettyTable

#Reads data from a provided file and stores it as a pandas table
def readData(file):
    return pd.read_csv(file)

#Sorts data by the quarter, and then sorts data of same quarter by amount
def sortData(data):
    return data.sort_values(by=['Quarter', 'VALUE'])

#Removes duplicate values
def removeDuplicates(data):
    return data.drop_duplicates()


#Prints the data as a well formated table
def printData(data):
    table = PrettyTable()
    table.field_names = data.columns

    for row in data.itertuples(index=False):
        table.add_row(row)

    return table

#Generates a bar graph of the data set, taking one value from first quarter of each year. 
def barGraph(data):
    #Stores values from quarters and amounts columns as lists
    years = data.iloc[:, 1].tolist()
    data['VALUE'] = pd.to_numeric(data['VALUE'])
    amounts = data.iloc[:, -1].tolist()

    #Extracting only one value per year from the first quarter
    selected_quarters = []
    selected_amounts = []
    seen_years = set()

    #Picks one value from each year, from the first quarter
    for quarter, amount in zip(years, amounts):
        year = quarter.split()[0]
        if year[-2:] == 'Q1' and year not in seen_years:
            selected_quarters.append(quarter)
            selected_amounts.append(amount)
            seen_years.add(year)

    #Sets the axis and data values for the graph
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.bar(selected_quarters, selected_amounts)
    ax.set_xlabel('Year')
    ax.set_ylabel('Amount')
    ax.set_title('Yearly Amount')


    plt.xticks(rotation=45)
    plt.ylim(0, max(selected_amounts) + 1000)

    plt.tight_layout()

    plt.savefig('graph.png')

# #Generates a line graph of the data set with the same conditions as the bar graph, taking one value from first quarter of each year. 
def lineGraph(data):
    #Stores values from quarters and amounts columns as lists
    years = data.iloc[:, 1].tolist()
    data['VALUE'] = pd.to_numeric(data['VALUE'])
    amounts = data.iloc[:, -1].tolist()

    # Extracting only one value per year from the first quarter
    selected_quarters = []
    selected_amounts = []
    seen_years = set()

    #Picks one value from each year, from the first quarter
    for quarter, amount in zip(years, amounts):
        year = quarter.split()[0]
        if year[-2:] == 'Q1' and year not in seen_years:
            selected_quarters.append(quarter)
            selected_amounts.append(amount)
            seen_years.add(year)

    #Sets the axis and data values for the graph
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.plot(selected_quarters, selected_amounts, marker='o', linestyle='-')
    ax.set_xlabel('Year')
    ax.set_ylabel('Amount')
    ax.set_title('Yearly Amount')

    plt.xticks(rotation=45)
    plt.ylim(0, max(selected_amounts) + 1000)

    plt.tight_layout()

    plt.savefig('line_graph.png')




def main():
    data = readData("data.csv")
    data = removeDuplicates(data)
    data = sortData(data)
    barGraph(data)
    lineGraph(data)
    print(printData(data))


if __name__=='__main__':
    main()