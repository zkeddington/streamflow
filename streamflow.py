import csv

import matplotlib.pyplot as plt
import numpy as np

# Used AI to reorganize the code and troubleshoot the loading section.
def load_streamflow_data(filename):
    data = np.genfromtxt(filename, delimiter=",", dtype=str, skip_header=1)
    dates = data[:, 0]
    flows = data[:, 1:].astype(float)
    return dates, flows

#AI added the threshold parameter to the function
def report_hours_above_threshold(flows, sites, threshold):
    if len(sites) != flows.shape[1]:
        raise ValueError("The number of sites must match the number of flow columns.")

    print(f"Hours above {threshold:g} cfs:")
    for column, site in enumerate(sites):
        hours_above = np.sum(flows[:, column] > threshold) * 0.25
        print(f"{site}: {hours_above:.2f} hours")


def plot_streamflow(dates, flows, sites):
    """Plot streamflow for each gauge."""
    colors = ["purple", "blue", "green", "yellow", "red"]

    plt.figure(figsize=(10, 6))
    for column, (color, site) in enumerate(zip(colors, sites)):
        plt.plot(dates, flows[:, column], color=color, label=site)

    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
    plt.xticks(rotation=45)

    plt.title("Provo River Streamflow Data (2021)")
    plt.xlabel("Date")
    plt.ylabel("Flowrate (cfs)")
    plt.legend(loc="upper right", fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()

#AI created this new function to summarize the data
#Excel max is 131 and the average is 56.95
def summarize(dates, flows, sites):
    #This part prints and saves flow statistics for each gauge.
    if len(sites) != flows.shape[1]:
        raise ValueError("The number of sites must match the number of flow columns.")
    #This part prints the header and separator for the summary table
    headers = ("Site", "Maximum (cfs)", "Date/time", "Minimum (cfs)", "Average (cfs)")
    widths = (12, 14, 19, 14, 14)
    print(" ".join(f"{header:<{width}}" for header, width in zip(headers, widths)))
    print("-" * (sum(widths) + len(widths) - 1))
    #This part writes the summary to a CSV file
    with open("streamflow_summary.csv", "w", newline="", encoding="utf-8") as summary_file:
        writer = csv.writer(summary_file)
        writer.writerow(
            ["Site", "Maximum (cfs)", "Date/time", "Minimum (cfs)", "Average (cfs)"]
        )
        #This part calculates and prints the statistics for each gauge, and writes them to the CSV file
        for column, site in enumerate(sites):
            gauge_flows = flows[:, column]
            max_index = np.argmax(gauge_flows)
            maximum = np.max(gauge_flows)
            minimum = np.min(gauge_flows)
            average = np.mean(gauge_flows)
            max_date = dates[max_index]

            print(
                f"{site:<12} {maximum:14.1f} {max_date:<19} "
                f"{minimum:14.1f} {average:14.1f}"
            )
            writer.writerow([f"Site: {site}, Maximum: {maximum}, Date/Time: {max_date}, Minimum: {minimum}, Average: {average}"])
    

if __name__ == "__main__":
    dates, flows = load_streamflow_data(
        "June-2021-Provo-River-Streamflow-Rates.csv"
    )
    sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
    threshold = float(input("Enter a flow threshold (cfs): "))
    report_hours_above_threshold(flows, sites, threshold)
    summarize(dates, flows, sites)
    plot_streamflow(dates, flows, sites)
