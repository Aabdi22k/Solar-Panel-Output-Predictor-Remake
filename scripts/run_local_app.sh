#!/usr/bin/env bash
set -e

echo "Starting Solar Output Predictor..."

REPO_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
cd "$REPO_ROOT"

# Load .env safely
if [ -f ".env" ]; then
  echo "Loading environment variables from .env..."
  set -a
  source .env
  set +a
fi

# Validate required variables
if [ -z "$NREL_API_KEY" ]; then
  echo "Error: NREL_API_KEY not set."
  exit 1
fi

if [ -z "$NREL_EMAIL" ]; then
  echo "Error: NREL_EMAIL not set."
  exit 1
fi

# FORCE python (not python3)
PYTHON_BIN="python"

echo "Using Python: $($PYTHON_BIN --version)"

# Create venv if missing
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  $PYTHON_BIN -m venv .venv
fi

# Activate venv (Windows Git Bash compatible)
if [ -f ".venv/Scripts/activate" ]; then
  source .venv/Scripts/activate
elif [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
else
  echo "Error: Could not find virtual environment activate script."
  exit 1
fi

$PYTHON_BIN -m pip install --upgrade pip
$PYTHON_BIN -m pip install -r requirements.txt

export PYTHONPATH="$REPO_ROOT/src"

streamlit run src/main/app/streamlit_app.py