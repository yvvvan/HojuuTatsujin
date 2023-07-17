## How to install YOLO on Ri
>After spending several hours trying to install YOLOv8 on Pi, I gave up, and chose YOLOv5.

**Attention**: Need a 64-bit OS and 64-bit Python 3.8 !!! <br>

1. **CONDA for Python3.8** To install YOLO on Pi, this project will need Python 3.8 (required in the follwing artical. otherwise unexpected errors). With current Raspi OS, it will use Python 3.9 by default. So Conda is needed. I learned from this vedio [Install anaconda on Raspberry pi
](https://www.youtube.com/watch?v=X-zfDZ6hdkM) to install miniforge3(conda) on Pi. After installed, create an env with Python 3.8.<br>
🎪Repo [Miniforge](https://github.com/conda-forge/miniforge)


2. **PyTorch on Pi** Read this artical [Tutorial: Running YOLOv5 Machine Learning Detection on a Raspberry Pi 4](https://jordan-johnston271.medium.com/tutorial-running-yolov5-machine-learning-detection-on-a-raspberry-pi-4-3938add0f719) to install YOLOv5 on Pi (Keypoint is PyTorch).<br>
The Yolo5 Repo in this artical is outdated and may cause errors, use the ofiicial Repo.<br>
🎪Repo [Tutorial: yolov5-on-rpi4-2020](https://github.com/jordan-johnston271/yolov5-on-rpi4-2020)<br>
🎪Repo [yolov5](https://github.com/ultralytics/yolov5)

---
After these two steps, the YOLOv5 should be useable. Can be tested, using the code in the artical. Now we need to add our own custom model, which means `best.pt` from training.

There are some tips for **possible errors**:
- If there is something wrong with a lib : `libstdc++.so.6: version 'GLIBCXX_3.4.xx' not found`. Say `xx` is `29`. Do the following:
    - Check both the conda env and the real env, which `libstdc` has `GLIBXCC_3.4.29`. The conda env path should be `.conda/envs/%env_name%/lib/libstdc++.so.6`. The real env path should be `/usr/lib/aarch64-linux-gnu/libstdc++.so.6` (Please check the actual path with command `which python`). So:
        ```sh
        strings /home/%USER%/.conda/envs/%ENV_NAME%/lib/libstdc++.so.6 | grep GLIBCXX_3.4.29

        strings /usr/lib/aarch64-linux-gnu/libstdc++.so.6 | grep GLIBCXX_3.4.29
        ```
    - replace the non-existent version with the existent version. (First make a copy of the original file)
        ```sh
        cp /usr/lib/aarch64-linux-gnu/libstdc++.so.6 /usr/lib/aarch64-linux-gnu/libstdc++.so.6.old
        cp /home/%USER%/.conda/envs/%ENV_NAME%/lib/libstdc++.so.6 /usr/lib/x86_64-linux-gnu/libstdc++.so.6 
        ```
- if it alway give you `OpenBLAS Warning : Detect OpenMP Loop and this application may hang. Please rebuild the library with USE_OPENMP=1 option` while prediction, add `export OMP_NUM_THREADS=1` to `.bashrc`.
- if model gives `no detection` by prediction: means numpy, scipy and torch versions are not compatible. Use the following requirements, and force install
    ```txt
    matplotlib>=3.2.2
    numpy==1.20.0
    opencv-python>=4.1.2
    Pillow
    PyYAML>=5.3.1
    scipy>=1.4.1
    torch==1.8.0
    torchvision==0.9.1
    tqdm>=4.41.0
    ```

