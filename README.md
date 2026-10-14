<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=800&size=32&duration=3500&pause=1500&color=ffd200&center=true&vCenter=true&width=900&height=70&lines=%E2%98%80%EF%B8%8F%20Solar%20Energy%20Predictor" alt="Solar Energy Predictor"/>

<b><i>Forecast solar power generation with ML</i></b>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=36BCF7&center=true&vCenter=true&width=700&lines=%E2%98%80%EF%B8%8F%20Predict%20solar%20power%20generation;%F0%9F%8C%A4%EF%B8%8F%20Weather-driven%20ML%20model;%F0%9F%93%8A%20Interactive%20dashboard" alt="Typing SVG" />

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/> <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn"/> <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/> <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white" alt="JavaScript"/>

<img src="https://img.shields.io/github/stars/PreciousBharath/SOLAR-ENERGY-PREDICTION?style=social" alt="stars"/> <img src="https://img.shields.io/github/forks/PreciousBharath/SOLAR-ENERGY-PREDICTION?style=social" alt="forks"/> <img src="https://img.shields.io/github/last-commit/PreciousBharath/SOLAR-ENERGY-PREDICTION?style=flat-square&color=blueviolet" alt="last commit"/> <img src="https://img.shields.io/github/repo-size/PreciousBharath/SOLAR-ENERGY-PREDICTION?style=flat-square&color=success" alt="repo size"/>
</div>

---

## ☀️ About the Project

Predicts **solar power generation** from weather and environmental conditions (irradiance, temperature, humidity, wind, cloud cover...) using machine learning, presented in an interactive **Flask dashboard** with a database-backed prediction history.

## ✨ Key Features

- 🌤️ Weather-based **solar output prediction**
- 🏆 Best model auto-selected (`best_model.pkl`) with feature scaling
- 🗄️ Prediction storage in **SQLite** (`solar_energy.db`)
- 📊 Interactive UI with modals & charts
- 📚 Quick-start, setup checklist and troubleshooting guides

## 🧠 How It Works

```mermaid
flowchart LR
W["🌤️ Weather Data"] --> S["⚖️ Scaler"] --> M["🏆 Best ML Model"] --> P["⚡ Predicted kW"]
```

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Data & ML | Pandas · NumPy · scikit-learn |
| Notebook | Jupyter |
| Web App | Flask + Jinja2 templates |
| Frontend | HTML5 · CSS3 |
| Database | SQLite |
| Config | .env · config.py |

## 📂 Project Structure

```text
SOLAR ENEGY PREDICTION/
├── run.py · app.py · config.py · models.py · init_db.py
├── model.py · generate_dataset.py
├── best_model.pkl · scaler.pkl
├── solar_dataset.csv · spg.csv
├── static/ (css, js) · templates/
└── QUICKSTART.md · SETUP_CHECKLIST.md · TROUBLESHOOTING.md
```

## 🚀 Getting Started

```bash
git clone https://github.com/PreciousBharath/SOLAR-ENERGY-PREDICTION.git
cd "SOLAR-ENERGY-PREDICTION/SOLAR ENEGY PREDICTION"
pip install -r requirements.txt
cp .env.example .env
python init_db.py
python run.py
```

> 💡 See `SOLAR ENEGY PREDICTION/QUICKSTART.md` for full setup details.

## 🤝 Contributing

Contributions, issues and feature requests are welcome! Feel free to ⭐ star the repo and open a pull request.

## 👨‍💻 Author

<div align="center">

**Bharath** — Software Developer · Project Engineer · Technical Trainer

<a href="https://github.com/PreciousBharath"><img src="https://img.shields.io/badge/GitHub-PreciousBharath-181717?style=for-the-badge&logo=github"/></a>
<a href="https://linkedin.com/in/connectbharath"><img src="https://img.shields.io/badge/LinkedIn-connectbharath-0A66C2?style=for-the-badge&logo=linkedin"/></a>

### 🍔 EAT · 💻 CODE · 😴 SLEEP · 🔁 REPEAT

⭐ **If you found this project useful, give it a star!** ⭐

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%"/>

</div>
