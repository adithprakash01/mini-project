@echo off
cd env\Scripts
call activate
cd ../..
streamlit run "main 2.py"
pause
