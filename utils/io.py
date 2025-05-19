import pandas as pd
import numpy as np

def save_to_csv(self, results, filename="sentiment_output.csv"):
        df = pd.DataFrame(results)
        df.to_csv(filename, index=False)
        print(f"Saved {len(df)} results to {filename}")
        return df