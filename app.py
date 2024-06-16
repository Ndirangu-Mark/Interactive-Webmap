import folium

# Coordinates for Mt. Kenya Forest
map_center = [-0.1521, 37.3084]  # Approximate center of Mt. Kenya Forest

# Create a map centered around Mt. Kenya Forest
my_map = folium.Map(location=map_center, zoom_start=10)

# Define marker locations, popup contents with images
marker_data = [
    {
        "location": [-0.1521, 37.3084],
        "popup": "<b>Mt. Kenya</b><br><img src='https://www.google.com/imgres?q=mt%20kenya&imgurl=https%3A%2F%2Fafar.brightspotcdn.com%2Fdims4%2Fdefault%2F87c3bbe%2F2147483647%2Fstrip%2Ftrue%2Fcrop%2F728x500%2B36%2B0%2Fresize%2F660x453!%2Fquality%2F90%2F%3Furl%3Dhttps%253A%252F%252Fk3-prod-afar-media.s3.us-west-2.amazonaws.com%252Fbrightspot%252F52%252F27%252F75e5a780203adc8e148104996ede%252Foriginal-925782c19d188263e00bf14985b940b2.jpg&imgrefurl=https%3A%2F%2Fwww.afar.com%2Fplaces%2Fmount-kenya-nyeri-county&docid=-Han-5yLpuRk4M&tbnid=p0jH-HuYROtewM&vet=12ahUKEwjN2fe88t-GAxWG9AIHHcMjB24QM3oECGUQAA..i&w=660&h=453&hcb=2&ved=2ahUKEwjN2fe88t-GAxWG9AIHHcMjB24QM3oECGUQAA' width='150'>",
        "icon": folium.Icon(color="blue")
    },
    {
        "location": [-0.1351, 37.2924],
        "popup": "<b>Chogoria Gate</b><br><img src='https://www.google.com/imgres?q=chogoria%20gate&imgurl=https%3A%2F%2Fwww.hikingadventures.net%2Fwp-content%2Fuploads%2F2020%2F09%2FMount-Kenya-Day-One-i-scaled.jpg&imgrefurl=https%3A%2F%2Fwww.hikingadventures.net%2Fhike-041-mount-kenya%2F&docid=mwjN3z9PRaAtOM&tbnid=z5CFhTYmjdjw6M&vet=12ahUKEwjSrNrO8t-GAxUR3wIHHdwDCrQQM3oECB0QAA..i&w=2560&h=1920&hcb=2&ved=2ahUKEwjSrNrO8t-GAxUR3wIHHdwDCrQQM3oECB0QAA' width='150'>",
        "icon": folium.Icon(color="green")
    },
    {
        "location": [-0.1673, 37.2974],
        "popup": "<b>Old Moses Camp</b><br><img src='https://example.com/old_moses_camp.jpg' width='150'>",
        "icon": folium.Icon(color="red")
    }
]

# Add markers to the map
for data in marker_data:
    folium.Marker(
        location=data["location"],
        popup=folium.Popup(data["popup"], max_width=300),
        icon=data["icon"]
    ).add_to(my_map)

# Save the map to an HTML file
my_map.save("Interactive Web Map/map.html")
