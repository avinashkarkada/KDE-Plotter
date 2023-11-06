#Violin plot script
import seaborn
import pandas as pd
import os
import glob 
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


directory_path = os.getcwd()

result_df = pd.DataFrame()

xvg_files = glob.glob(os.path.join(directory_path, '*.xvg'))

name_order = ["Native", "N370S-V394L", "N370S", "L444P", "S364T"]

for file_path in xvg_files:
    df = pd.read_csv(file_path, skiprows=24, header=None, delimiter='\s+')
    column_name = os.path.basename(file_path.split(".")[0])
    df = df[[1]]  
    df.columns = [column_name]

    if result_df.empty:
        result_df = df
    else:
        result_df = pd.concat([result_df, df], axis=1)



sns.set(style='whitegrid', font_scale=1)
ax = sns.violinplot(data=result_df, order= name_order)
ax.tick_params(axis='x', rotation=90)
ax.set_ylabel("RMSD")
plt.savefig('RMSD_violin.eps', format='eps', bbox_inches = 'tight')
plt.savefig('RMSD_violin.png', format='png', dpi = 1200, bbox_inches = 'tight')
#plt.figure(figsize=(9, 11))
#plt.show()

