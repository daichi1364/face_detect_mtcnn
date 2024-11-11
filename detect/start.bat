@echo off
python detect.py
echo エラーコード: %errorlevel%
echo 顔が写った画像パスを入力して下さい
pause >nul
