import cv2
import math
import numpy as np

cv2.namedWindow('src')
cap = cv2.VideoCapture(0)

while True:
	ret, img_src = cap.read() # カメラ映像の読み込み
	
	cv2.imshow('src', img_src) # 入力画像を表示
	ch = cv2.waitKey(1) # キー入力待ち

	# qをトリガーにプログラムを停止
	if ch == ord('q'):
		break

#キャプチャオブジェクトの開放
cap.release()

#nameWindowsオブジェクトの解放
cv2.destroyAllWindows()