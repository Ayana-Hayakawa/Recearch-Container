import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from ctapipe.visualization import CameraDisplay
from ctapipe_io_lst import load_camera_geometry


# =========================
# 1. データを読む
# =========================

df = pd.read_csv(
    "src/AcLast.dat",
    sep=r"\s+"
)

print(df.head())


# =========================
# 2. LSTカメラ形状を読む
# =========================

camera_geom = load_camera_geometry()

print("number of camera pixels =", camera_geom.n_pixels)


# =========================
# 3. pixel_id → CameraDisplayの配列番号
#    の対応を作る
# =========================

pixel_to_index = {
    int(pixel_id): i
    for i, pixel_id in enumerate(camera_geom.pix_id)
}


# =========================
# 4. 1855 pixel分の配列を作る
# =========================

cumulative_image = np.full(camera_geom.n_pixels, np.nan)
average_image = np.full(camera_geom.n_pixels, np.nan)


# データを正しいpixel位置に格納する
for _, row in df.iterrows():

    pixel_id = int(row["pixel_id"])

    if pixel_id in pixel_to_index:

        index = pixel_to_index[pixel_id]

        cumulative_image[index] = row["cumulative_anode_current"]
        average_image[index] = row["average_anode_current"]


# =========================
# 5. Cumulative anode current
# =========================

plt.figure(figsize=(8, 7))

camdisplay = CameraDisplay(
    camera_geom,
    cumulative_image,
    title="Cumulative Anode Current"
)

camdisplay.add_colorbar()

plt.tight_layout()
plt.show()


# =========================
# 6. Average anode current
# =========================

plt.figure(figsize=(8, 7))

camdisplay = CameraDisplay(
    camera_geom,
    average_image,
    title="Average Anode Current"
)

camdisplay.add_colorbar()

plt.tight_layout()
plt.show()