# HeatMeter - Heatstroke Prediction 🇧🇩

### A context-aware mobile solution for heatstroke prevention using machine learning and the WBGT index.

This repository accompanies the study:

**"A Context-Aware Mobile Solution for Heatstroke Prediction Using WBGT Index and Machine Learning"**  
*Md Saidur Rahman Kohinoor, Fahad Ahmed Ruhan, Md Istiaque Khalique, Tajwar Elahi Choudhury, Md Mahfuzur Rahman, Mohammad Shorfuzzaman*  
📜 DOI: *(To be updated when available)*

---


## 📁 Repository Structure

```plaintext
Heatstroke-Prediction-BD/
├── Data/               # Dataset access info and metadata
├── Models/             # Machine learning training scripts
├── Scripts/            # Data preprocessing & utilities
├── App/                # Mobile app (Flutter) and backend API (Flask)
├── Notebooks/          # (Optional) Jupyter notebooks for experiments
├── Docs/               # Figures, diagrams, and methodology illustrations
├── requirements.txt    # Python dependencies
├── LICENSE
└── README.md
```

---


## 📊 Dataset

### 📂 Dataset access is provided in the [`Data/`](./Data) folder.

- **Source**: NASA POWER and OpenWeatherMap APIs  
- **Region**: 8 divisions of Bangladesh  
- **Period**: January 2013 – September 2022  
- **Frequency**: Hourly  
- **Features**: Temperature, relative humidity, wind speed, and more  
- **Target**: Wet Bulb Globe Temperature (WBGT)

---


## 🧠 Machine Learning Models

Training scripts are located in the [`Models/`](./Models) folder.

Available models:
- Linear Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest


---



## 📱 HeatMeter Mobile App

📂 `App/` folder includes:
- `flutter_app/` – Flutter-based mobile frontend  
- `flask_api/` – Python-based backend API for WBGT prediction


### 🔑 Key Features:
- Real-time WBGT estimation from live weather feeds  
- Risk level visualization and hourly trend insights  
- Health symptoms logging and precaution suggestions 
- Precaution advice and emergency first-aid guidance


---



## 🖼 Visuals and Figures

📂 [`Docs/`](./Docs): Contains system diagrams, workflow illustrations, and mobile UI mockups used in the paper.


---


## 📌 Citation

If you use this dataset, code, or mobile interface, please cite the paper as follows:  
📄 *(Citation details will be updated upon DOI assignment)*


---


## 📨 Contact

For questions, collaborations, or technical issues, please contact:

**InteX Research Lab**  
📧 [intexresearchlab@gmail.com](mailto:intexresearchlab@gmail.com)


---


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

