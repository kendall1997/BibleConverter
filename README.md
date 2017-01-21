# BibleConverter
##Español  
Este script de python convierte la biblia desde un archivo SQL (importando en un servidor) a XML, para el Software Quelea (Software de proyección para iglesias).

**Dependencias:**  

 * [MySQL Connector para Python](http://dev.mysql.com/doc/connector-python/en/) (Tested on Python 3.5 64 bits)

**¿Cómo utilizarlo?**  
1. Crear una base de datos en un servidor MySQL, utilizando phpMyAdmin (https://www.phpmyadmin.net/) es sencillo,  luego importe el archivo bible.sql  
2. El diccionario al comienzo del script debe ser cambiado acorde a la identificación del servidor (IP, Nombre de Host, etc), nombre de usuario, contraseña, nombre de la base de datos.  
3. Si está en Windows, abra el IDLE de python e importe el archivo script.py, luego ejecútelo. Si está en Linux, abra la terminal y escriba 'python3 script.py' (Debe estar ubicado en el mismo directorio donde está el script).  
4. Un archivo llamado Biblia 'BibliaRVR1960.xml' será creado en el mismo directorio donde el script está, si existe otro archivo con el mismo nombre será sobreescrito.  

**Nota.**
Cuando la biblia ha sido importado en Quelea y se observan caracteres extraños (como esto ?) se resuelve abriendo el archivo 'BibliaRVR1960.xml' en un editor de texto y volviéndolo a guardar utilizando la codificación utf-8 con BOM.

<hr>  

##English
This python script converts the bible from SQL file (imported on a server) to XML, for Quelea Software (church projection software).

**Dependencies:**

* [MySQL Connector for Python](http://dev.mysql.com/doc/connector-python/en/) (Tested on Python 3.5 64 bits)

**Usage**  
1. Create a Database in a MySQL Server, use phpMyAdmin (https://www.phpmyadmin.net/) is very useful, and then import bible.sql.  
2. The config dict at the beggining must be changed according to the server identificacion name (IP, HostName, etc), username, password and database of the MySQL Server.  
3. If you are on Windows, open the Python IDLE and import the script.py file, then execute it. If you're on linux, open terminal and type 'python3 script.py' (you should be in the directory where the script is)  
4. A file called 'BibliaRVR1960.xml' will be created in the same directory where script.py is. If another file with the same name exists, will be override.  

**Note.**  When is already imported in Quelea and you see bad characteres (like this '?') you can solve that problem by opening BibliaRVR1960.xml into a Text Editor and resave it by using utf-8 with BOM encoding.

If you only want to use the RVR 1960 bible, just download the file 'BibliaRVR1960.xml' that is ready to be imported.
