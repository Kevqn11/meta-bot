@echo off
title TERMINAL
:start
echo.
echo You are currently in the folder - %~dp0
echo.
echo [TERMINAL] WHAT PYTHON FILE WOULD YOU LIKE TO RUN?

dir "%~dp0"\*.py /A :S /B /O :N

set /p name=?

:run

if "%name%"=="TERMINATE" (goto end)


if not exist "%~dp0"\"%name%" (
	echo.
	echo [TERMINAL] THE FILE COULD NOT BE FOUND. MAKE SURE THE NAME IS CORRECT. PLEASE WRITE THE EXTENSION AS WELL.
	echo.	
	goto start
) else (
	cls
	python "%~dp0\"%name%
	pause
)
	
:again
	
set /p again="[TERMINAL] RUN AGAIN? (Y/N) "?
	if "%again%"=="Y" (goto run)
	if "%again%"=="y" (goto run)
	if "%again%"=="n" (goto no)
	if "%again%"=="N" (goto no) else (
		echo [TERMINAL] INPUT IS NOT IDENTIDIED. TRY AGAIN.
		goto again
)

:no

echo.
set /p end="[TERMINAL] TERMINATE? (Y/N) "?
	if "%end%"=="y" (goto end)
	if "%end%"=="Y" (goto end)
	if "%end%"=="N" (
		cls
		goto start
		)
	if "%end%"=="n" (
		cls
		goto start
		) else (
		echo [TERMINAL] INPUT IS NOT IDENTIFIED. TRY AGAIN.
		goto no
		)

:end

end