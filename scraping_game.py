# scraping_steam_reviews.py
import pandas as pd
from steamreviews import download_reviews_for_app_id
from tqdm import tqdm

# RE Biohazard
app_ids = [418370]

# Dataset final
all_reviews = []

for app_id in tqdm(app_ids):
    result, _ = download_reviews_for_app_id(
        app_id,
        chosen_request_params={'language': 'english'}, 
        verbose=True
    )
    for review_id, review_data in result['reviews'].items():
        review_text = review_data.get('review', '')
        voted_up = review_data.get('voted_up', False)
        
        sentiment = 'positive' if voted_up else 'negative'
        
        all_reviews.append({
            'review': review_text,
            'sentiment': sentiment
        })

# Simpan ke CSV
df = pd.DataFrame(all_reviews)
df.to_csv('dataset_init.csv', index=False)

print("Scraping selesai!.")