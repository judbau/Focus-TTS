##### create matedata file #####

import pandas as pd
import os
import glob

#loop over several csv files
for file in os.listdir('/content/drive/MyDrive/session_csvs'):
  f = pd.read_csv(f'/content/drive/MyDrive/session_csvs/{file}')

# remove superfluent columns
  keep_col = ['group','type','answer']
  new_f = f[keep_col]

# if uppercase then <F> before the word
  new_f['answer'] = new_f['answer'].str.replace(r'(?<![A-Z])[A-Z](?=[A-Z])', r'<F>\g<0>')

# everything from answer column in lower case
  new_f['answer']=new_f['answer'].str.lower()

# making the <F> uppercase again
  new_f['answer'] = new_f['answer'].str.replace(r'<f>', r'<F>')

# <Q> before type = 2 ,i.e., questions
  new_f.loc[new_f['type'] == 2, 'answer'] = '<Q>' + new_f['answer']

# remove punctuation
  new_f['answer'] = new_f['answer'].str.replace(r'\.|\?', r'')

# duplicate sentence (add | and same sentence)
  new_f['answer'] = new_f['answer'] + '|' + new_f['answer']

# add file name (filname = 1_F_[group]_ + [referent of the type number (normal etc.)]|)
  ## referent of type number
  new_f.loc[new_f['type'] == 1, 'answer'] = 'neutral|' + new_f['answer']
  new_f.loc[new_f['type'] == 2, 'answer'] = 'question|' + new_f['answer']
  new_f.loc[new_f['type'] == 3, 'answer'] = 'focus_subject|' + new_f['answer']
  new_f.loc[new_f['type'] == 4, 'answer'] = 'focus_verb|' + new_f['answer']
  new_f.loc[new_f['type'] == 5, 'answer'] = 'focus_object|' + new_f['answer']

  ## 1_F_[group]_
  new_f['answer'] = new_f.apply(lambda row: '1_F_' + str(row.group) + '_' + row.answer, axis=1)
  
  ## remove superfluent columns
  keep_col_final = ['answer']
  final_f = new_f[keep_col_final]

# save without index and column header
  new_path = f'/content/drive/MyDrive/input_metadata_csvs_new/{file}'
  final_f.to_csv(new_path, header=False, index=False)

# merge all csv files from input_metadata_csvs_new to one metadata.csv file

path = '/content/drive/MyDrive/input_metadata_csvs_new'
all_files = glob.glob(os.path.join(path, 'session_*.csv'))
df_from_each_file = (pd.read_csv(f) for f in all_files)
df_merged = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv('merged_new.csv', header=False, index=False)
