import pandas as pd
from pathlib import Path
from performance.models import StudentPerformance


def run():
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / 'dataset.csv'

    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        StudentPerformance.objects.create(
            hours_studied=row['Hours Studied'],
            previous_scores=row['Previous Scores'],
            extracurricular=row['Extracurricular Activities'] == 'Yes',
            sleep_hours=row['Sleep Hours'],
            sample_papers=row['Sample Question Papers Practiced'],
            performance_index=row['Performance Index'],
        )
