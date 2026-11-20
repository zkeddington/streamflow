import csv

import matplotlib.pyplot as plt
import numpy as np

# Used AI to reorganize the code and troubleshoot the loading section.
def load_streamflow_data(filename):
    """Read dates and numeric streamflow values from a CSV file."""
    data = np.genfromtxt(filename, delimiter=",", dtype=str, skip_header=1)
    dates = data[:, 0]
    flows = data[:, 1:].astype(float)
    return dates, flows

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
    """Print and save flow statistics for each gauge."""
    if len(sites) != flows.shape[1]:
        raise ValueError("The number of sites must match the number of flow columns.")

    headers = ("Site", "Maximum (cfs)", "Date/time", "Minimum (cfs)", "Average (cfs)")
    widths = (12, 14, 19, 14, 14)
    print(" ".join(f"{header:<{width}}" for header, width in zip(headers, widths)))
    print("-" * (sum(widths) + len(widths) - 1))

    with open("streamflow_summary.csv", "w", newline="", encoding="utf-8") as summary_file:
        writer = csv.writer(summary_file)
        writer.writerow(
            ["Site", "Maximum (cfs)", "Date/time", "Minimum (cfs)", "Average (cfs)"]
        )

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
    summarize(dates, flows, sites)
    plot_streamflow(dates, flows, sites)
