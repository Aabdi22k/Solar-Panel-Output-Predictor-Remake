from __future__ import annotations

from datetime import date
from pathlib import Path
import os

from main.paths import ProjectPaths
from main.config import AppDefaults, TrainingConfig
from main.data_pipeline.build_dataset import build_training_dataset
from main.models.train import train_random_forest, save_artifacts


def main():
    repo_root = Path(__file__).resolve().parents[1]
    paths = ProjectPaths.from_repo_root(repo_root)
    paths.ensure_dirs()

    defaults = AppDefaults()
    training = TrainingConfig()
    lat, lon = defaults.location.latitude, defaults.location.longitude

    nrel_api_key = os.getenv("NREL_API_KEY", "")
    nrel_email = os.getenv("NREL_EMAIL", "")
    if not nrel_api_key or not nrel_email:
        raise RuntimeError("Set NREL_API_KEY and NREL_EMAIL in environment.")

    years = list(range(training.start_year, training.end_year + 1))
    tag = f"{lat}_{lon}".replace(".", "p")
    cache_csv = paths.raw_data_dir / f"nsrdb_{tag}_{training.start_year}_{training.end_year}.csv"

    df = build_training_dataset(
        latitude=lat,
        longitude=lon,
        years=years,
        nrel_api_key=nrel_api_key,
        nrel_email=nrel_email,
        open_meteo_start=date(training.start_year, 1, 1),
        open_meteo_end=date(training.end_year, 12, 31),
        cache_csv_path=cache_csv,
    )

    artifacts = train_random_forest(df, test_size=training.test_size, random_state=training.random_state)
    save_artifacts(artifacts, models_dir=paths.models_dir, tag=tag)
    print("✅ Training complete. Artifacts saved in artifacts/models/.")


if __name__ == "__main__":
    main()