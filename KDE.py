import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def processxvg(filename):
    x, y = [], []
    with open(filename) as f:
        for line in f:
            if line[0] != "#" and line[0] != "@":
                cols = line.split()
                x.append(float(cols[0]))
                y.append(float(cols[1]))
    return y
    
    
# Load the data from the Rg and SASA XVG files
RG = processxvg("Protein1-0-500ns-RG.xvg")
SASA = processxvg("Protein1-0-500ns-SASA.xvg")
y = pd.DataFrame(RG)
x = pd.DataFrame(SASA)

ax = sns.kdeplot(x=SASA, y = RG, shade=True, cmap="mako")
ax.set_title('4OAR-CMP6', fontsize=20)
plt.xlabel(r'$SASA\ (nm^{2})$', fontsize=18)
plt.ylabel('$Rg (nm)$', fontsize=18)
plt.savefig('RG-SASA_KDE.jpg', dpi=300)
