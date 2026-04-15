import pandas as pd
from django.shortcuts import render
from pymongo import MongoClient
from .utils import generate_all_charts

def dashboard_view(request):

    # 🔹 Connect MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["pollution_db"]
    collection = db["pollution"]

    
    data = list(collection.find({}, {"_id": 0}))
    df = pd.DataFrame(data)

    # 🔹 Handle empty DB (for safety)
    if df.empty:
        return render(request, "dashboard.html", {"error": "No data found"})

    # 🔹 Generate charts
    chart1, chart2, chart3, chart4 = generate_all_charts(df)

    # 🔹 High Pollution Detection
    df['status'] = df['aqi'].apply(lambda x: "High" if x > 150 else "Normal")
    high_pollution = df[df['status'] == "High"]['region'].unique()

    # 🔹 Insights
    avg_aqi = df['aqi'].mean()

    if avg_aqi > 150:
        insight = "Overall pollution is HIGH ⚠"
    else:
        insight = "Pollution is under control ✅"

    context = {
        "aqi": int(avg_aqi),
        "pm25": int(df['pm25'].mean()),
        "chart1": chart1,
        "chart2": chart2,
        "chart3": chart3,
        "chart4": chart4,
        "high_regions": high_pollution,
        "insight": insight
    }

    return render(request, "dashboard.html", context)


def overview_view(request):
    return render(request, "overview.html")


def water_view(request):
    return render(request, "water.html")


def soil_view(request):
    return render(request, "soil.html")