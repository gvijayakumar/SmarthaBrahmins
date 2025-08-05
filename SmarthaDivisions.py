import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# List of all Brahmin Smartha communities
groups = [
    "Babburu kamme", "Panchagrama", "Nandavareeka", "Chitpavana", "Kasalakaadu",
    "Kota", "Karada", "Karanakamme", "Kambalooru", "Arama dravida", "Aaradhya",
    "Appasahasta", "Seeryanaadu", "Shivalli", "Muturu sosale Karnataka", "Badaganadu",
    "Prathamashaake", "Deshasta", "GSB", "Kandavara", "Kannadakamme", "Uluchukamme",
    "Aravelu niyogi", "Aravathokkulu", "Hoysala Karnataka", "Stanika", "Saraswatha",
    "Sankethi", "Shengeri shivalli", "Valanadu", "Venginaadu", "Vadama", "Mulukunaadu",
    "Malenaadu hebbara", "Bhagavatha sampradaya", "Brahmachharana","Havyaka"
]

# Communities to be highlighted with yellow background
highlighted = {
    "Seeryanaadu", "Shivalli", "Muturu sosale Karnataka", "Badaganadu",
    "Prathamashaake", "Deshasta", "GSB", "Kandavara", "Kannadakamme",
    "Uluchukamme", "Aravelu niyogi", "Aravathokkulu"
}

# Circle parameters
num_groups = len(groups)
angles = [2 * np.pi * i / num_groups for i in range(num_groups)]
radius = 10
x = [radius * np.cos(angle) for angle in angles]
y = [radius * np.sin(angle) for angle in angles]

# Create the figure
fig, ax = plt.subplots(figsize=(14, 14))
ax.set_xlim(-radius-4, radius+4)
ax.set_ylim(-radius-4, radius+4)
ax.set_aspect('equal')
ax.axis('off')

# Draw connections and labels
for i in range(num_groups):
    ax.plot([0, x[i]], [0, y[i]], 'black', linewidth=0.5)

    # Determine if the group should be highlighted
    if groups[i] in highlighted:
        ax.text(x[i], y[i], groups[i],
                ha='center', va='center', fontsize=24,
                rotation=np.degrees(angles[i]),
                bbox=dict(facecolor='yellow', edgecolor='none', boxstyle='round,pad=0.3'))
    else:
        ax.text(x[i], y[i], groups[i],
                ha='center', va='center', fontsize=24,
                rotation=np.degrees(angles[i]))

# Central circle
circle = plt.Circle((0, 0), 1, color='orange')
ax.add_patch(circle)
ax.text(0, 0, "Brahmin\nSmartha\ncommunities", color='black', ha='center', va='center', fontsize=24)
ax.text(0, -radius-4.5, "In yellow has both Smartha and Madhva traditions",
        fontsize=11, ha='center', va='center', color='black')

plt.title("Brahmin Smartha Communities - Cycle Diagram", fontsize=26)
plt.tight_layout()


# Save to PDF
with PdfPages("Brahmin_Smartha_Communities_Cycle_Diagram.pdf") as pdf:
    pdf.savefig(fig)

# Save to JPG
fig.savefig("Brahmin_Smartha_Communities_Cycle_Diagram.jpg", dpi=300)

plt.close()

print("Saved as 'Brahmin_Smartha_Communities_Cycle_Diagram.pdf' and '.jpg'")
