import umap
from sklearn.datasets import fetch_mldata
import matplotlib
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams.update({'font.size': 25})


mnist = fetch_mldata("MNIST original")

reducer = umap.UMAP(random_state=42)
embedding = reducer.fit_transform(mnist.data)

plt.figure()

plt.scatter(embedding[:, 0], embedding[:, 1], c=mnist.target, cmap="Spectral", s=0.1)

plt.gca().get_xaxis().set_ticklabels([])
plt.gca().get_yaxis().set_ticklabels([])

ax = plt.gca()
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')

fig1 = plt.gcf()

fig1.subplots_adjust(top = 0.98, bottom = 0.1, right = 0.98, left = 0.08, hspace = 0, wspace = 0)
fig1.savefig('../../Illustrations/UMAP-MNIST.eps', format='eps', dpi=1000, bbox_inches = 'tight', pad_inches = 0)
fig1.savefig('../../Illustrations/UMAP-MNIST.pdf', format='pdf', dpi=1000, bbox_inches = 'tight', pad_inches = 0)
fig1.savefig('../../Illustrations/UMAP-MNIST.png', dpi=1000, bbox_inches = 'tight', pad_inches = 0)

plt.show()
