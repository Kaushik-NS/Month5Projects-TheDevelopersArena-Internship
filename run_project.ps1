Write-Host "================================="
Write-Host "AI WEATHER FORECASTING SYSTEM"
Write-Host "================================="

# --------------------------------
# STEP 1 - CREATE VENV IF MISSING
# --------------------------------

if (!(Test-Path "venv")) {

    Write-Host "[INFO] Creating virtual environment..."

    python -m venv venv
}

# --------------------------------
# STEP 2 - ACTIVATE VENV
# --------------------------------

Write-Host "[INFO] Activating virtual environment..."

& .\venv\Scripts\Activate.ps1

# --------------------------------
# STEP 3 - INSTALL REQUIREMENTS
# --------------------------------

Write-Host "[INFO] Installing dependencies..."

pip install -r requirements.txt

# --------------------------------
# STEP 4 - CHECK TRAINED MODELS
# --------------------------------

$modelsExist =
    (Test-Path "min_temp_model.h5") -and
    (Test-Path "max_temp_model.h5") -and
    (Test-Path "mean_temp_model.h5") -and
    (Test-Path "rainfall_model.h5")

if (!$modelsExist) {

    Write-Host "[INFO] Training AI models..."

    python -m src.training.train
}

# --------------------------------
# STEP 5 - START FASTAPI
# --------------------------------

Write-Host "[INFO] Starting FastAPI backend..."

Start-Process powershell -ArgumentList "
cd '$PWD';
.\venv\Scripts\Activate.ps1;
uvicorn src.api.main:app --reload
"

# --------------------------------
# STEP 6 - START STREAMLIT
# --------------------------------

Write-Host "[INFO] Starting Streamlit frontend..."

Start-Process powershell -ArgumentList "
cd '$PWD';
.\venv\Scripts\Activate.ps1;
streamlit run ui/simple_app.py
"

# --------------------------------
# FINAL MESSAGE
# --------------------------------

Write-Host ""
Write-Host "================================="
Write-Host "APPLICATION STARTED SUCCESSFULLY"
Write-Host "================================="
Write-Host ""
Write-Host "Frontend:"
Write-Host "http://localhost:8501"
Write-Host ""
Write-Host "Backend:"
Write-Host "http://127.0.0.1:8000"