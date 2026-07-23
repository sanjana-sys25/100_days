import webbrowser
import requests

def track_the_iss():
    # Public API tracking the space station in real-time
    url = "https://api.wheretheiss.at/v1/satellites/25544"
    
    print("🛰️ Connecting to the International Space Station...")
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract the cool metrics
            lat = data["latitude"]
            lon = data["longitude"]
            altitude = round(data["altitude"], 2)  # In kilometers
            velocity = round(data["velocity"], 2)  # In km/h
            
            # Convert to mph/miles for quick reading
            miles_high = round(altitude * 0.621371, 1)
            mph = round(velocity * 0.621371)
            
            print("\n✨ --- ISS LOCATION FOUND --- ✨")
            print(f"EARTH Coordinates: Latitude {lat}, Longitude {lon}")
            print(f"ISS Speed:        {mph:,} mph ({velocity:,} km/h)")
            print(f" Altitude:     {miles_high} miles above Earth ({altitude} km)")
            print("---------------------------------\n")
            
            # Create a Google Maps URL with the coordinates
            maps_url = f"https://www.google.com/maps?q={lat},{lon}"
            
            print("🗺️ Opening Google Maps to show you where it's flying over right now...")
            webbrowser.open(maps_url)
            
        else:
            print(f"Mission control error: Code {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Failed to reach orbit. Check internet connection. Error: {e}")

if __name__ == "__main__":
    track_the_iss()