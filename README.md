# black-white

------

## 环境要求

- python3.5
- numpy
- matplotlib
- PIL

## 使用说明

- python run.py random #机机对战（随机落子版）
- python run.py 2 # 人人对战
- python run.py 1 # 人机对战，人执黑
- python run.py -1 # 人机对战，人执白
- python run.py test # 测试10万次机机对战及时间(耗时较久，慎用，未使用并行计算)

## 一次随机10W次对战结果

黑胜:35020

白胜:60745

平局:4235

用时:13028

貌似执白会有一些先天优势。