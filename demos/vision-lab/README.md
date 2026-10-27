\# Vision Lab — Azure AI Vision



Aplicación web de demostración que permite cargar una imagen y analizarla con Azure AI Vision Image Analysis 4.0. Muestra una descripción, objetos detectados y etiquetas visuales.



\## Requisitos



\- Python 3.10 o posterior

\- Un recurso de Azure AI Vision activo

\- Una clave y un endpoint de ese mismo recurso



La función \*\*Caption\*\* requiere que el recurso esté en una región compatible. Esta demo se preparó con un recurso en East US.



\## Configurar en Windows PowerShell



Desde la carpeta `demos/vision-lab`:



```powershell

python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

python -m pip install -r requirements.txt

Copy-Item .env.example .env

notepad .env

