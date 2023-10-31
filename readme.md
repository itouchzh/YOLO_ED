<center> <h1> EDN-YOLO✈️</h1> </center>

We proposed EDN-YOLO, a model for multi-scale traffic sign detection, which has been verified on different data sets and achieved good detection results.

## Train and Detect:

<details>
<summary>Train</summary>

`python train.py --data TT100K.yaml --epochs 150 --weights '' --cfg yolov5s.yaml  --batch-size 32`

</details>

<details>
<summary>Val</summary>

`python val.py --data TT100K.yaml --weights 'xxxx' --cfg yolov5s.yaml  --batch-size 1`

</details>

<details>
<summary>Inference with detect.py</summary>

`python detect.py --weights xxx.pt path/    # directory`

</details>


## Detection results
| YOLOv5s    | EDN-YOLO     | YOLOv5s       | EDN-YOLO |
| ------- | ------- | -------------- |-------|
| <img src="./images/1_1.jpg" width="100">    | <img src="./images/1_2.jpg" width="100">    | <img src="./images/1_3.jpg" width="100"> |<img src="./images/1_4.jpg" width="100"> |
| <img src="./images/2_1.jpg" width="100">    | <img src="./images/2_2.jpg" width="100">    | <img src="./images/2_3.jpg" width="100"> |<img src="./images/2_4.jpg" width="100"> |
| <img src="./images/3_1.png" width="100">    | <img src="./images/3_2.png" width="100">    | <img src="./images/3_3.png" width="100"> |<img src="./images/3_4.png" width="100"> |


