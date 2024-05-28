Version de Python: 3.10.14
Versión de LabVIEW: 2024 Q1 (64-Bit)

Punto 1: Guardar la carpeta localmente (no en la nube)

1. Ejecutar el archivo "NMW.py", pero antes de hacerlo, hay que abrirlo y cambiar la ruta del archivo "MNIST_CLASSIFIER.pb" donde se encuentre el mismo en tu computadora.

2. Abrir el archivo "estructura basica video tiempo real reconocimiento patrones extraccion de imagen 2.0.vi", posteriormente seleccionar la cámara a utilizar (Session In), en el control "Template File Path"
   seleccionar la ruta del archivo "C4.png", y colocar en el control "Array_2" los valores de las esquinas de las zonas de interes para detectar el digito manuscrito (se colocan de forma vertical).

3. En la seccion de abrir anaconda y ejecutar codigo de python a traves de LabVIEW, hay que cambiar los path y strings de acuerdo a la ruta donde se tengan los archivos mismos, asi como la ruta donde se tenga
   instalado anaconda.
