import pandas as pd
import wikipedia as wiki
import os #For data files extraction from folder


'''file_loc = os.getcwd()

df = pd.read_csv(file_loc+"\\Project\\Data\\SourceKaggle\\complete.csv")
df_ind=df[df["ind_or_org"]=="Individual"]
people_names = df_ind['name']
#people_names[people_names == "abdul salam"].index[0]


#people_names.drop([people_names=="abdul salam"])

for name in people_names:
    page_data = wiki.page(name).content
    notes_index = page_data.find("== Notes ==")
    page_data = page_data[0:notes_index]
    with open(file_loc+"\\Project\\Data\\NewWiki\\"+name+".txt", "w", encoding="utf-8") as text_file:
        text_file.write(page_data)
        text_file.close()'''