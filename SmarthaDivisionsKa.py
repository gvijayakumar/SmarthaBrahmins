import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.backends.backend_pdf import PdfPages

# Set Kannada font (ensure this is installed on your system)
rcParams['font.family'] = 'Tunga'  # Or 'Lohit Kannada', 'Nudi', etc.

# Kannada community names
kannada_groups = [
    "ಬಬ್ಬೂರು ಕಮ್ಮೆ", "ಪಂಚಗ್ರಾಮ", "ನಂದವರೀಕ", "ಚಿತ್ಪಾವನ", "ಕಸಲಕಾಡು",
    "ಕೋಟ", "ಕರಡ", "ಕರಣಕಮ್ಮೆ", "ಕಂಬಲೂರು", "ಅರಮ ದ್ರಾವಿಡ", "ಆರಾಧ್ಯ",
    "ಅಪ್ಪಸಹಸ್ತ", "ಸೀರ್ಯನಾಡು", "ಶಿವಳ್ಳಿ", "ಮುತ್ತೂರು ಸೋಸಲೆ ಕರ್ನಾಟಕ", "ಬಡಗನಾಡು",
    "ಪ್ರಥಮಶಾಖೆ", "ದೇಶಸ್ಥ", "ಜಿ.ಎಸ್.ಬಿ", "ಕಂದಾವರ", "ಕನ್ನಡಕಮ್ಮೆ", "ಉಳಚುಕಮ್ಮೆ",
    "ಅರವೇಳು ನಿಯೋಗಿ", "ಅರವತ್ತುಕ್ಕುಲು", "ಹೊಯ್ಸಳ ಕರ್ನಾಟಕ", "ಸ್ತಾನಿಕ", "ಸರಸ್ವತ",
    "ಸಂಕೇತಿ", "ಶೃಂಗೇರಿ ಶಿವಳ್ಳಿ", "ವಳನಾಡು", "ವೆಂಗಿನಾಡು", "ವಡಮ", "ಮೂಲೂಕುನಾಡು",
    "ಮಲೆನಾಡು ಹೆಬ್ಬರ", "ಭಾಗವತ ಪರಂಪರೆ", "ಬ್ರಹ್ಮಚಾರಣ"
]

# Groups to highlight with yellow (Smartha and Madhva)
highlighted_kannada = {
    "ಸೀರ್ಯನಾಡು", "ಶಿವಳ್ಳಿ", "ಮುತ್ತೂರು ಸೋಸಲೆ ಕರ್ನಾಟಕ", "ಬಡಗನಾಡು",
    "ಪ್ರಥಮಶಾಖೆ", "ದೇಶಸ್ಥ", "ಜಿ.ಎಸ್.ಬಿ", "ಕಂದಾವರ", "ಕನ್ನಡಕಮ್ಮೆ",
    "ಉಳಚುಕಮ್ಮೆ", "ಅರವೇಳು ನಿಯೋಗಿ", "ಅರವತ್ತುಕ್ಕುಲು"
}

# Circle layout parameters
num_groups = len(kannada_groups)
angles = [2 * np.pi * i / num_groups for i in range(num_groups)]
radius = 10
x = [radius * np.cos(angle) for angle in angles]
y = [radius * np.sin(angle) for angle in angles]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 15))  # Extra height for note
ax.set_xlim(-radius-4, radius+4)
ax.set_ylim(-radius-6, radius+4)  # Lower limit for disclosure note
ax.set_aspect('equal')
ax.axis('off')

# Draw connections and text
for i in range(num_groups):
    ax.plot([0, x[i]], [0, y[i]], 'gray', linewidth=0.5)
    name = kannada_groups[i]
    if name in highlighted_kannada:
        ax.text(x[i], y[i], name, ha='center', va='center', fontsize=9,
                rotation=np.degrees(angles[i]),
                bbox=dict(facecolor='yellow', edgecolor='none', boxstyle='round,pad=0.3'))
    else:
        ax.text(x[i], y[i], name, ha='center', va='center', fontsize=9,
                rotation=np.degrees(angles[i]))

# Central circle
center_circle = plt.Circle((0, 0), 1, color='black')
ax.add_patch(center_circle)
ax.text(0, 0, "ಬ್ರಾಹ್ಮಣ\nಸ್ಮಾರ್ತ\nಸಮುದಾಯಗಳು", color='white', ha='center', va='center', fontsize=11)

# Title
plt.title("ಬ್ರಾಹ್ಮಣ ಸ್ಮಾರ್ತ ಸಮುದಾಯಗಳ ಚಕ್ರ ಆಕಾರ ನಕ್ಷೆ", fontsize=14)

# Disclosure note at bottom
ax.text(0, -radius-4.5, "ಹಳದಿ ಹಿನ್ನೆಲೆಯವರು ಸ್ಮಾರ್ತ ಮತ್ತು ಮಧ್ವ ಇಬ್ಬರನ್ನೂ ಹೊಂದಿದ್ದಾರೆ",
        fontsize=11, ha='center', va='center', color='black')

plt.tight_layout()

# Save as PDF
with PdfPages("Brahmin_Smartha_Communities_Kannada.pdf") as pdf:
    pdf.savefig(fig)

# Save as JPG
fig.savefig("Brahmin_Smartha_Communities_Kannada.jpg", dpi=300)
plt.close()

print("Saved Kannada diagram as PDF and JPG with yellow-highlight disclosure.")
