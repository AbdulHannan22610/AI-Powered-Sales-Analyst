import matplotlib.pyplot as plt

def line_chart(df):
    data = df.groupby("date")["total_sales"].sum()

    plt.figure()
    plt.plot(data.index, data.values)
    plt.xticks(rotation=45)
    plt.title("Sales Trend (Line)")
    return plt


def bar_chart(df):
    data = df.groupby("product")["total_sales"].sum()

    plt.figure()
    plt.bar(data.index, data.values)
    plt.title("Product Sales (Bar)")
    return plt


def pie_chart(df):

    data = df.groupby("product")["total_sales"].sum()

    plt.figure(figsize=(8,8))

    plt.pie(
        data.values,
        labels=data.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Product Distribution")

    return plt