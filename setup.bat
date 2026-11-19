@echo off
set "DirView_path=%USERPROFILE%\capybara\DirView"
mkdir %DirView_path%
echo %DirView_path%

cd /d "%~dp0"

@REM MOVE TO CAPYBARA
for %%i in (*) do (
    copy "%%i" "%DirView_path%\"
)

for /D %%i in (*) do (
    copy "%%i" "%DirView_path%\"
)

@REM INSTALL
@echo on
pip install -e %DirView_path%