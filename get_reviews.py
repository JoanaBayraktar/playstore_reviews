
from google_play_scraper import Sort, reviews_all
import pandas as pd
from iso639 import languages


df_all = pd.DataFrame()

for i in range(len(list(languages.part1))):
    review_language = list(languages.part1)[i]
    print("Language: " + str(review_language))

    result = reviews_all(
        'de.rki.coronawarnapp',
        sleep_milliseconds=9,
        lang=review_language,
        sort=Sort.MOST_RELEVANT)

    df_res = pd.DataFrame(result)

    for item in df_res.items():
        df_res["lang"] = review_language
        df_res["country"] = review_country

    df_all = pd.concat([df_all, df_res]) #append is deprecated and will be removed from pandas in a future version

df_all.to_csv("de.rki.coronawarnapp_rev.csv", sep='\t', encoding='utf-8')


