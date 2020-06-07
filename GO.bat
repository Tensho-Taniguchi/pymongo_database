@IF EXIST GO.log DEL /Q GO.log

@ECHO.                                        > GO.log
@ECHO ***********************************     >>GO.log
@ECHO CS499_001.py                            >>GO.log
@ECHO ***********************************     >>GO.log
python.exe CS499_001.py                       >>GO.log

@ECHO.                                        >>GO.log
@ECHO ***********************************     >>GO.log
@ECHO CS499_002.py                            >>GO.log
@ECHO ***********************************     >>GO.log
python.exe CS499_002.py                       >>GO.log
PAUSE