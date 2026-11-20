import matplotlib.pyplot as plt
import numpy as np

# Used AI to reorganize the code and troubleshoot the loading section.
def load_streamflow_data(filename):
    """Read dates and numeric streamflow values from a CSV file."""
    data = np.genfromtxt(filename, delimiter=",", dtype=str, skip_header=1)
    dates = data[:, 0]
    flows = data[:, 1:].astype(float)
    return dates, flows


def plot_streamflow(dates, flows):
    """Plot streamflow for each gauge."""
    colors = ["purple", "blue", "green", "yellow", "red"]
    gauge_ids = ["10163000", "10155200", "10155500", "10154200", "10155000"]

    plt.figure(figsize=(10, 6))
    for column, (color, gauge_id) in enumerate(zip(colors, gauge_ids)):
        plt.plot(dates, flows[:, column], color=color, label=gauge_id)

    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
    plt.xticks(rotation=45)

    plt.title("Provo River Streamflow Data (2021)")
    plt.xlabel("Date")
    plt.ylabel("Flowrate (cfs)")
    plt.legend(loc="upper right", fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    dates, flows = load_streamflow_data(
        "June-2021-Provo-River-Streamflow-Rates.csv"
    )
    plot_streamflow(dates, flows)
