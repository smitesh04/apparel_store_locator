import csv

import pandas as pd
import requests
import hashlib
from db_config import DbConfig
obj = DbConfig()
def create_md5_hash(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

def download_csv(url, local_filename):
    # Send a GET request to the URL
    with requests.get(url, stream=True) as response:
        response.raise_for_status()  # Check for request errors
        # Open a local file with write mode
        with open(local_filename, 'wb') as f:
            # Write the response content in chunks
            for chunk in response.iter_content():
                f.write(chunk)
    print(f"CSV file downloaded: {local_filename}")
input_df = pd.read_excel(r"C:\Users\Actowiz\Desktop\Smitesh_Docs\Project\apparel_store_locator\input.xlsx")

for i,j in input_df.iterrows():
    url = j['download_sample_url']
    r = requests.get(url)

    hashid = create_md5_hash(url)
    # download_csv(url, hashid)
    # file = open(fr"C:/Users/Actowiz/Desktop/Smitesh_Docs/Project/apparel_store_locator/csv/{hashid}.csv", "w", encoding='utf8')
    print()
    with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            print(row)
        df = pd.DataFrame(my_list)
        df.to_csv(fr"C:/Users/Actowiz/Desktop/Smitesh_Docs/Project/apparel_store_locator/csv/{hashid}.csv", index=False)
        print(df)