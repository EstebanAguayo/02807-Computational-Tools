import pandas as pd
import wikipedia as wiki
import os #For data files extraction from folder


exception_list = []
file_loc = os.getcwd()

#exclude_list = ["Abdus Salam","Abiy Ahmed Ali","Akira Suzuki","Al Gore"] 

df = pd.read_csv(file_loc+"\\Project\\Data\\SourceKaggle\\complete.csv")
df_ind=df[df["ind_or_org"]=="Individual"]
people_names = df_ind['name']
print(len(people_names))
#people_names.drop("Abdus Salam")

#people_names.drop([people_names=="abdul salam"])
while True:
    for name in people_names:
        try:
            print(name)
            page_data = wiki.page(name).content
            notes_index = page_data.find("== Notes ==")
            if notes_index == -1:
                notes_index = page_data.find("== See also ==")
            elif notes_index == -1:
                notes_index = page_data.find("== References ==")
            page_data = page_data[0:notes_index]
            with open(file_loc+"\\Project\\Data\\NewWiki\\"+name+".txt", "w", encoding="utf-8") as text_file:
                text_file.write(page_data)
                text_file.close()
        except wiki.exceptions.PageError:
            print("Catched")
            exception_list.append(name)
            continue
        except wiki.exceptions.DisambiguationError:
            print("Catched")
            exception_list.append(name)
            continue
    print(exception_list)