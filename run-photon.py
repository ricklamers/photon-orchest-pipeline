import orchest
import os
from urllib.parse import urlparse

step_params, _ = orchest.get_params()
url = step_params.get("url", "https://tweakers.net")

print(f"Crawling URL: {url}")

domain = urlparse(url).netloc
output_dir = f"/data/photon/{domain}"
os.makedirs(output_dir, exist_ok=True)

exit_code = os.system(f'python /photon/photon.py -u "{url}" -o {output_dir}')

print(exit_code)