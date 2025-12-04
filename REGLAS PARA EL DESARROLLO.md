# **REGLAS PARA EL DESARROLLO:**



0\. USAR SIEMPRE FUNCIONES GIT (PUSH, COMMIT, PULL, etc)

1\. Nombrar a las clases iniciando en mayúscula y en CamelCase (ejemplo: AutobusPlus) y los archivos y módulos con minúscula y camelCase (ejemplo: autobusPlus.py)

2\. La navegación principal se desarrolla en el main.py, las navegaciones entre cada pagina se harán dentro de los controladores

3\. Para cualquier conexión a la BD se hara dentro de carpeta dao, para las consultas se crearan archivos crud (con camelCase)

4\. Comenten su código  

5\. Funciones con snake\_case (ejemplo: def\_cargar\_autobuses) y tiene que describir la accion especifica

6\. Las validaciones se harán en otro archivo (validaciones.py) que iran en la carpeta servicios 

7\. Las validaciones deben hacerse como en modo consola, debe obtener del evento la variable, guardarla, mandarla a validaciones\_nombre.py y ahi validar, para luego regresar.

8\. Si la validación esta incorrecta, mostrar un QMessageBox explicando que esta mal

9\. Cualquier duda de como se hace algo o de que hizo algún mono, preguntar y con gusto se va a atender :D





**PARA RENOMBRAR OBJETOS**

botones = boton\_nombre

label = label\_tipo\_nombre (ejemplo: label\_estatico\_titulo, label\_consulta\_tipoAutobus)

widgets = pagina\_nombre

lineEdit  = lineEdit\_dato (ejemplo: lineEdit\_numeroAutobus)

QTableWidget = QTableWidget\_dato (ejemplo: QTableWidget\_corridas)

Comboboxes = ComboBox\_accion (ejemplo: ComboBox\_filtroCorridas, ComboBox\_filtroTiposDeServicio)



**CASES:** 

SNAKE CASE: snake\_case

PASCAL CASE: PascalCase

CAMEL CASE: camelCase



**CUALQUIER COSA NO ESPECIFICADA EN ESTE TEXTO, CONSULTAR CON EL EQUIPO.**

