import os
import matplotlib.pyplot as plt


def generate_all_charts(df):
    image_dir = os.path.join("dashboard", "static", "images")
    os.makedirs(image_dir, exist_ok=True)

    # 🔹 1. Region Analysis
    region_data = df.groupby("region")["aqi"].mean()

    plt.figure()
    region_data.plot(kind='bar', title="AQI by Region")
    path1 = os.path.join(image_dir, "region.png")
    plt.savefig(path1)
    plt.close()

    # 🔹 2. Pollutant Comparison
    plt.figure()
    df[['pm25', 'pm10', 'co2']].mean().plot(kind='bar', title="Pollutant Levels")
    path2 = os.path.join(image_dir, "pollutants.png")
    plt.savefig(path2)
    plt.close()

    # 🔹 3. Trend Analysis
    trend = df.groupby("date")["aqi"].mean()

    plt.figure()
    trend.plot(marker='o', title="AQI Trend")
    path3 = os.path.join(image_dir, "trend.png")
    plt.savefig(path3)
    plt.close()

    # 🔹 4. Correlation Heatmap
    corr = df[['aqi', 'pm25', 'pm10', 'co2']].corr()

    plt.figure()
    plt.imshow(corr)
    plt.colorbar()
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.title("Correlation Heatmap")
    path4 = os.path.join(image_dir, "corr.png")
    plt.savefig(path4)
    plt.close()

    return path1, path2, path3, path4