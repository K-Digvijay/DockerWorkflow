# DockerWorkflow

# 🐳 Dockerized Machine Learning Environment

A clean, modular, and containerized setup for Machine Learning, Deep Learning, and NLP workflows using **Docker** and **VS Code Jupyter notebooks**.

This setup helps you:
- Avoid Conda clutter and dependency hell 🧹
- Keep projects reproducible and portable 🔁
- Work locally, run code in Linux containers 🧠

---

## 📦 Supported Workloads

| Category         | Included Libraries                                                   |
|------------------|------------------------------------------------------------------------|
| 💡 Daily ML       | scikit-learn, pandas, numpy, matplotlib, seaborn, xgboost, lightgbm   |
| 🧠 Deep Learning  | TensorFlow, Keras, PyTorch, torchvision, segmentation-models, etc.     |
| 📚 NLP           | transformers, spaCy, nltk, gensim, textblob                            |
| 📈 Time Series   | statsmodels, pmdarima                                                  |
| 🔊 Audio/Image    | librosa, opencv-python, pillow, soundfile                             |
| 🧪 Utility/Dev    | jupyterlab, tqdm, ipykernel, VS Code support                           |

---

## 🛠️ Folder Structure you can follow seperate ML libs.

```
docker-ml-setup/
├── Dockerfile.ml         # ML-only stack
├── Dockerfile.nlp        # NLP stack
├── Dockerfile.dl         # Deep learning stack
├── notebooks/            # Sample .ipynb files
└── README.md             # This file
```

---

## 🚀 Quickstart

### 🔨 1. Build an Image (example: ML stack)
```bash
docker build -f Dockerfile.ml -t ml-env .
```

### 🧪 2. Run the Container and Mount Code
```bash
docker run -it --rm -p 8888:8888 -v %cd%:/workspace ml-env
```

- On macOS/Linux:
```bash
docker run -it --rm -p "$(pwd):/workspace" ml-env
```

### 🌐 3. Open in Browser
Copy the URL printed in terminal (e.g. `http://127.0.0.1:8888/lab?token=...`)  
Open it to access **JupyterLab** running inside the container.

---

## ⚙️ Features

- 🔁 Reproducible ML environment with Docker
- 📦 No need to pollute host with Conda or pip
- 🧠 Modular images: one per task (ML, NLP, DL)
- 📝 Full support for `.ipynb` in VS Code or browser
- 🧹 Disk-space optimized (you can remove containers/images anytime)

---

## ✅ Why Use This Setup?

| 🔥 Pain Point             | ✅ Solved By This |
|--------------------------|------------------|
| Conda conflicts & bloat  | Docker isolation |
| Reinstalling libraries   | One reusable image |
| Different Python versions| Just change base image |
| Disk full on C drive     | Move Docker data to D:/ |
| Notebook portability     | Mount code into container |

---

## 📚 Notes

- Requires Docker Desktop (Windows/macOS) or Docker Engine (Linux)
- Optional: move Docker storage to another drive via Docker Desktop → Settings → Resources → Advanced
- Works great with VS Code + Remote - Containers

---

## 🧠 Bonus: Use in Production

Once ready, this setup can be extended to:
- Serve models via FastAPI + Uvicorn
- Deploy containers to Kubernetes, ECS, or Azure ML
- Use with CI/CD or MLflow

---

## 🙌 Author

Crafted with ❤️ by [Digvijay K]  
If this helps, feel free to ⭐ the repo or connect on [LinkedIn](www.linkedin.com/in/digvijaykewale)

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).
