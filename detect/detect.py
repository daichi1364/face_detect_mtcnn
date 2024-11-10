import mtcnn
import cv2
import inspect as ins
import matplotlib.pyplot as plt


arg = input('顔が写っている、顔部分を検出したい画像のパスを入れて下さい')

while True:
    try:
        numPict = cv2.imread(arg)
        if numPict is None:
            raise FileNotFoundError("画像が読み込めません。パスを確認してください。")
        
        changeColorRGB = cv2.cvtColor(numPict, cv2.COLOR_BGR2RGB)
        detect = mtcnn.mtcnn.MTCNN()
        pointerInfo = detect.detect_faces(changeColorRGB)


        for i in pointerInfo:
            (x, y, w, h) = i['box']
            x, y, w, h
            cv2.rectangle(changeColorRGB, (x, y), (x+w, y+h), (0, 0, 255), thickness=2)

        plt.imshow(changeColorRGB)
        plt.show()    
        
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        
    arg = input('他に顔部分を検出したい画像が有ればパスを入力して下さい')
    if not arg:
        break
    
    