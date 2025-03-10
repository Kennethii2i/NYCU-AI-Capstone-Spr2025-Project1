import requests
import os
import time
from tqdm import tqdm

# List of birds to download
# 麻雀, 烏鴉, 海鷗, 竹葉鶯, 杜鵑, 五色鳥, 白頭翁, 綠繡眼, 綠頭鴨, 斑鳩
birds = ["Passer montanus", "Corvus macrorhynchos", "Larus crassirostris",
         "Horornis diphone", "Cuculus canorus", "Psilopogon nuchalis",
         "Hypsipetes amaurotis", "Zosterops japonicus", "Anas platyrhynchos",
         "Streptopelia orientalis", 
         ]
# Number of recordings to download per bird
max_recordings = 100

# Create data directory
os.makedirs("data", exist_ok=True)

# Download recordings
for bird in birds:
    print(f"Downloading {bird}...")
    
    save_dir = os.path.join("data", bird.replace(" ", "_")) # Save directory
    os.makedirs(save_dir, exist_ok=True)
    url = f"https://xeno-canto.org/api/2/recordings?query={bird}"
    
    # Get recordings
    recordings = requests.get(url).json().get("recordings", [])[:max_recordings]

    for rec in recordings:
        file_url = rec.get("file")
        if not file_url:
            continue

        file_path = os.path.join(save_dir, f"{bird}_{rec['id']}.mp3")
        try:
            response = requests.get(file_url, stream=True)
            with open(file_path, "wb") as f:
                total = int(response.headers.get("content-length", 0))
                pbar = tqdm(total=total, unit="B", unit_scale=True, desc=f"File {rec['id']}", leave=False)
                for chunk in response.iter_content(1024):
                    f.write(chunk)
                    pbar.update(len(chunk))
                pbar.close()
        except Exception as e:
            print(f"Failed to download {file_path}: {e}")
        time.sleep(1)
