# Coffee can colorbur anomaly detection
 Using patchcore for anomaly detection with colorburred coffee cans

## PatchCore Large Architecture
![image](https://github.com/user-attachments/assets/1bf49396-9467-4ed5-84be-82c4ba05a5ff)

The main idea of PatchCore is to extract as much useful features as possible to save them to the memory bank. Then those features will be filtered out to reduce the memory bank size using Coreset Subsampling. Then when new sample comes in, each feature patch will have its anomaly score calculated based on the distance to the samples in the memory banks, the anomalies will be stand out strongly.

## Dataset
The dataset will have picture of coffee can, the anomalies are parts which being drawed on by a red marker.
![dis7_lux4_res1920x1080_fps8_right_1_ 2](https://github.com/user-attachments/assets/658b8469-59f9-4156-b17c-b13eb097f189)

