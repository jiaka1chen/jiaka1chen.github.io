import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

outdir = Path("figures")
outdir.mkdir(exist_ok=True)

np.random.seed(7)

n_ring = 120
n_center = 70

theta = np.random.uniform(0, 2*np.pi, n_ring)
r = 2.0 + np.random.normal(0, 0.10, n_ring)
x1 = r * np.cos(theta)
x2 = r * np.sin(theta)

c1 = np.random.normal(0, 0.45, n_center)
c2 = np.random.normal(0, 0.45, n_center)

z_ring_center = 1.2
z_center_center = -1.0
z_ring = np.full(n_ring, z_ring_center) + np.random.normal(0, 0.03, n_ring)
z_center = np.full(n_center, z_center_center) + np.random.normal(0, 0.03, n_center)

t_ring = np.random.normal(z_ring_center, 0.06, n_ring)
t_center = np.random.normal(z_center_center, 0.06, n_center)

# Collapse fully onto the single feature axis
x_ring_axis = np.zeros(n_ring)
x_center_axis = np.zeros(n_center)

blue = "#3B82F6"
purple = "#8B5CF6"

plt.rcParams.update({
    "font.size": 13,
    "axes.titlesize": 16,
    "axes.labelsize": 13,
    "figure.dpi": 220,
})

def clean_axes_2d(ax):
    ax.set_aspect("equal")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.12)
    ax.set_xlim(-2.8, 2.8)
    ax.set_ylim(-2.8, 2.8)
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$")
    ax.set_xticks([])
    ax.set_yticks([])

# Panel 3 only
fig3, ax3 = plt.subplots(figsize=(4.1, 5.4))
ax3.scatter(x_ring_axis, t_ring, marker="x", s=42, linewidths=1.5, color=blue, label="class 1", zorder=3)
ax3.scatter(x_center_axis, t_center, facecolors="none", edgecolors=purple, marker="o", s=48, linewidths=1.4, label="class 2", zorder=3)
ax3.axvline(0.0, linewidth=1.0, color="black", alpha=0.7, zorder=1)

ax3.set_xlim(-0.03, 0.03)
ax3.set_ylim(-1.5, 1.6)
ax3.set_xticks([])
ax3.set_yticks([])
ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)
ax3.spines["bottom"].set_visible(False)
ax3.spines["left"].set_visible(False)
ax3.grid(axis="y", alpha=0.10)
ax3.set_ylabel(r"$\phi_3(x)$", labelpad=2)
ax3.legend(frameon=False, loc="upper right")
fig3.tight_layout()
fig3.savefig(outdir / "kernel_effect_3_feature_only.png", bbox_inches="tight")
plt.close(fig3)

# Combined panel
fig = plt.figure(figsize=(14.0, 4.9))

ax = fig.add_subplot(131)
ax.scatter(x1, x2, marker="x", s=34, linewidths=1.3, color=blue)
ax.scatter(c1, c2, facecolors="none", edgecolors=purple, marker="o", s=38, linewidths=1.2)
clean_axes_2d(ax)

ax = fig.add_subplot(132, projection="3d")
ax.scatter(x1, x2, z_ring, marker="x", s=24, linewidths=1.0, color=blue, depthshade=False)
ax.scatter(c1, c2, z_center, facecolors="none", edgecolors=purple, marker="o", s=28, linewidths=1.0, depthshade=False)
xx = np.linspace(-2.2, 2.2, 10)
yy = np.linspace(-2.2, 2.2, 10)
XX, YY = np.meshgrid(xx, yy)
ZZ_ring = np.full_like(XX, z_ring_center)
ZZ_center = np.full_like(XX, z_center_center)
ax.plot_surface(XX, YY, ZZ_ring, color=blue, alpha=0.10, linewidth=0, shade=False)
ax.plot_surface(XX, YY, ZZ_center, color=purple, alpha=0.10, linewidth=0, shade=False)
ax.set_xlim(-2.8, 2.8)
ax.set_ylim(-2.8, 2.8)
ax.set_zlim(-1.6, 1.6)
ax.set_xlabel(r"$x_1$")
ax.set_ylabel(r"$x_2$")
ax.set_zlabel(r"$\phi_3(x)$", labelpad=2)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.view_init(elev=23, azim=-55)

ax = fig.add_subplot(133)
ax.scatter(x_ring_axis, t_ring, marker="x", s=34, linewidths=1.3, color=blue, zorder=3)
ax.scatter(x_center_axis, t_center, facecolors="none", edgecolors=purple, marker="o", s=38, linewidths=1.2, zorder=3)
ax.axvline(0.0, linewidth=1.0, color="black", alpha=0.7, zorder=1)
ax.set_xlim(-0.03, 0.03)
ax.set_ylim(-1.5, 1.6)
ax.set_xticks([])
ax.set_yticks([])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.grid(axis="y", alpha=0.10)
ax.set_ylabel(r"$\phi_3(x)$", labelpad=1)

fig.subplots_adjust(wspace=0.28, left=0.04, right=0.98, top=0.88, bottom=0.11)
fig.savefig(outdir / "kernel_effect_combined.png", bbox_inches="tight")
plt.close(fig)

# Update script
script = outdir / "generate_kernel_effect_figures.py"
script.write_text(r'''
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

outdir = Path(".")
np.random.seed(7)

n_ring = 120
n_center = 70

theta = np.random.uniform(0, 2*np.pi, n_ring)
r = 2.0 + np.random.normal(0, 0.10, n_ring)
x1 = r * np.cos(theta)
x2 = r * np.sin(theta)

c1 = np.random.normal(0, 0.45, n_center)
c2 = np.random.normal(0, 0.45, n_center)

z_ring_center = 1.2
z_center_center = -1.0
z_ring = np.full(n_ring, z_ring_center) + np.random.normal(0, 0.03, n_ring)
z_center = np.full(n_center, z_center_center) + np.random.normal(0, 0.03, n_center)

t_ring = np.random.normal(z_ring_center, 0.06, n_ring)
t_center = np.random.normal(z_center_center, 0.06, n_center)

x_ring_axis = np.zeros(n_ring)
x_center_axis = np.zeros(n_center)

blue = "#3B82F6"
purple = "#8B5CF6"

plt.rcParams.update({
    "font.size": 13,
    "axes.titlesize": 16,
    "axes.labelsize": 13,
    "figure.dpi": 220,
})

def clean_axes_2d(ax):
    ax.set_aspect("equal")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.12)
    ax.set_xlim(-2.8, 2.8)
    ax.set_ylim(-2.8, 2.8)
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$")
    ax.set_xticks([])
    ax.set_yticks([])

fig1, ax1 = plt.subplots(figsize=(5.6, 5.2))
ax1.scatter(x1, x2, marker="x", s=42, linewidths=1.5, color=blue, label="class 1")
ax1.scatter(c1, c2, facecolors="none", edgecolors=purple, marker="o", s=48, linewidths=1.4, label="class 2")
clean_axes_2d(ax1)
ax1.legend(frameon=False, loc="upper right")
fig1.tight_layout()
fig1.savefig(outdir / "kernel_effect_1_R2.png", bbox_inches="tight")

fig2 = plt.figure(figsize=(6.4, 5.6))
ax2 = fig2.add_subplot(111, projection="3d")
ax2.scatter(x1, x2, z_ring, marker="x", s=32, linewidths=1.2, color=blue, depthshade=False, label="class 1")
ax2.scatter(c1, c2, z_center, facecolors="none", edgecolors=purple, marker="o", s=36, linewidths=1.0, depthshade=False, label="class 2")
xx = np.linspace(-2.2, 2.2, 10)
yy = np.linspace(-2.2, 2.2, 10)
XX, YY = np.meshgrid(xx, yy)
ZZ_ring = np.full_like(XX, z_ring_center)
ZZ_center = np.full_like(XX, z_center_center)
ax2.plot_surface(XX, YY, ZZ_ring, color=blue, alpha=0.10, linewidth=0, shade=False)
ax2.plot_surface(XX, YY, ZZ_center, color=purple, alpha=0.10, linewidth=0, shade=False)
ax2.set_xlim(-2.8, 2.8)
ax2.set_ylim(-2.8, 2.8)
ax2.set_zlim(-1.6, 1.6)
ax2.set_xlabel(r"$x_1$")
ax2.set_ylabel(r"$x_2$")
ax2.set_zlabel(r"$\phi_3(x)$", labelpad=4)
ax2.view_init(elev=23, azim=-55)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_zticks([])
ax2.legend(frameon=False, loc="upper left")
fig2.tight_layout()
fig2.savefig(outdir / "kernel_effect_2_R3.png", bbox_inches="tight")

fig3, ax3 = plt.subplots(figsize=(4.1, 5.4))
ax3.scatter(x_ring_axis, t_ring, marker="x", s=42, linewidths=1.5, color=blue, label="class 1", zorder=3)
ax3.scatter(x_center_axis, t_center, facecolors="none", edgecolors=purple, marker="o", s=48, linewidths=1.4, label="class 2", zorder=3)
ax3.axvline(0.0, linewidth=1.0, color="black", alpha=0.7, zorder=1)
ax3.set_xlim(-0.03, 0.03)
ax3.set_ylim(-1.5, 1.6)
ax3.set_xticks([])
ax3.set_yticks([])
ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)
ax3.spines["bottom"].set_visible(False)
ax3.spines["left"].set_visible(False)
ax3.grid(axis="y", alpha=0.10)
ax3.set_ylabel(r"$\phi_3(x)$", labelpad=2)
ax3.legend(frameon=False, loc="upper right")
fig3.tight_layout()
fig3.savefig(outdir / "kernel_effect_3_feature_only.png", bbox_inches="tight")

fig = plt.figure(figsize=(14.0, 4.9))

ax = fig.add_subplot(131)
ax.scatter(x1, x2, marker="x", s=34, linewidths=1.3, color=blue)
ax.scatter(c1, c2, facecolors="none", edgecolors=purple, marker="o", s=38, linewidths=1.2)
clean_axes_2d(ax)

ax = fig.add_subplot(132, projection="3d")
ax.scatter(x1, x2, z_ring, marker="x", s=24, linewidths=1.0, color=blue, depthshade=False)
ax.scatter(c1, c2, z_center, facecolors="none", edgecolors=purple, marker="o", s=28, linewidths=1.0, depthshade=False)
ax.plot_surface(XX, YY, ZZ_ring, color=blue, alpha=0.10, linewidth=0, shade=False)
ax.plot_surface(XX, YY, ZZ_center, color=purple, alpha=0.10, linewidth=0, shade=False)
ax.set_xlim(-2.8, 2.8)
ax.set_ylim(-2.8, 2.8)
ax.set_zlim(-1.6, 1.6)
ax.set_xlabel(r"$x_1$")
ax.set_ylabel(r"$x_2$")
ax.set_zlabel(r"$\phi_3(x)$", labelpad=2)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.view_init(elev=23, azim=-55)

ax = fig.add_subplot(133)
ax.scatter(x_ring_axis, t_ring, marker="x", s=34, linewidths=1.3, color=blue, zorder=3)
ax.scatter(x_center_axis, t_center, facecolors="none", edgecolors=purple, marker="o", s=38, linewidths=1.2, zorder=3)
ax.axvline(0.0, linewidth=1.0, color="black", alpha=0.7, zorder=1)
ax.set_xlim(-0.03, 0.03)
ax.set_ylim(-1.5, 1.6)
ax.set_xticks([])
ax.set_yticks([])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.grid(axis="y", alpha=0.10)
ax.set_ylabel(r"$\phi_3(x)$", labelpad=1)

fig.subplots_adjust(wspace=0.28, left=0.04, right=0.98, top=0.88, bottom=0.11)
fig.savefig(outdir / "kernel_effect_combined.png", bbox_inches="tight")
'''.strip())

print("Updated files:")
for p in sorted(outdir.iterdir()):
    print(p.name)
