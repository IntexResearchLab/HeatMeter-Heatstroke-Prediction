# HeatMeter 🌡️

A mobile application designed to predict heatstroke danger based on the WBGT (Wet Bulb Globe Temperature) index, helping users stay safe during hot weather conditions.

## Features ✨

- **Real-time Heatstroke Risk Assessment**: Displays current risk level based on WBGT calculations
- **Weather Forecast**: Detailed daily weather information
- **Heatstroke Prevention**: Actionable precautions to avoid heat-related illnesses
- **Emergency Information**: Symptoms identification and first aid instructions

## Tech Stack 🛠️

- **Frontend**: Flutter for cross-platform mobile development
- **Backend**: Python-based Random Forest machine learning model
- **Data Source**: OpenWeatherMap API for weather variables (temperature, wind speed, relative humidity)

## How It Works 🔄

1. Retrieves weather variables from OpenWeatherMap API
2. Processes data through our trained Random Forest ML model
3. Calculates WBGT index and corresponding heatstroke danger level
4. Provides personalized safety recommendations

## App Screenshots 📱

<div align="center">
<p float="left">
  <img src="https://github.com/user-attachments/assets/2d68bc08-851a-4068-ba89-9804df4fcbfd" width="30%" />
  <img src="https://github.com/user-attachments/assets/dc0a9767-2c3c-40c8-9d44-3d8605680a91" width="30%" />
</p>
<p float="left">
  <img src="https://github.com/user-attachments/assets/079cf14e-fb5b-490c-a84e-0ad0209820b9" width="30%" />
  <img src="https://github.com/user-attachments/assets/e5ae5e1d-648c-4b50-a6d8-4923cbdf59e4" width="30%" />
</p>
<p float="center">
  <img src="https://github.com/user-attachments/assets/0767ac04-aaf5-4731-9e61-ad1811b8c476" width="30%" />
</p>
</div>

## Key Components 🧩

- **Home Screen**: Displays current WBGT index and risk level
- **Precautions**: Personalized recommendations based on current conditions
- **Weather Forecast**: Detailed daily weather information
- **Symptom Guide**: Helps identify heat-related illness symptoms
- **First Aid**: Emergency procedures for heat-related illnesses


## Future Enhancements 🚀

- Personalized risk profiles based on user health information
- Push notifications for dangerous heat conditions
- Offline mode for areas with limited connectivity
- Integration with wearable devices for personalized monitoring

