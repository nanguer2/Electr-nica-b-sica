Aquí tienes las respuestas a tu cuestionario, basadas en los conceptos técnicos de las clases de Allen Bradley y Studio 5000:

**1) Un programa de PLC puede estar constituido por varias tareas.**

* **Respuesta:** **b) Falso**
* *Explicación:* Es al revés. Una **Tarea (Task)** es la jerarquía superior que puede contener múltiples **Programas**, y cada programa contiene sus **Rutinas**.

**2) Un programa de PLC solo puede tener rutinas del mismo lenguaje de programación.**

* **Respuesta:** **b) Falso**
* *Explicación:* Dentro de un mismo proyecto o programa puedes tener rutinas en Ladder (LD), Bloques de Función (FBD), Texto Estructurado (ST) o Sequential Function Chart (SFC) e interactuar entre ellas.

**3) Un tag de controlador se puede emplear en múltiples programas.**

* **Respuesta:** **a) Verdadero**
* *Explicación:* Los **Controller Tags** son de alcance global; cualquier rutina de cualquier programa dentro del proyecto puede verlos y usarlos.

**4) Un tag de programa se puede emplear en múltiples programas.**

* **Respuesta:** **b) Falso**
* *Explicación:* Los **Program Tags** son de alcance local. Solo son visibles para las rutinas que pertenecen al programa donde fueron creados.

**5) Un tag de programa solo puede ser de tipo base.**

* **Respuesta:** **b) Falso**
* *Explicación:* Un tag de programa puede ser de tipo **Alias**, **Consumido** o incluso estructuras complejas (como Timers), no se limita a tipos base como BOOL o DINT.

**6) Un tag de tipo alias lo puedo direccionar con una entrada o salida de PLC.**

* **Respuesta:** **a) Verdadero** (implícito)
* *Explicación:* Esta es, de hecho, la función principal del **Alias**: darle un nombre descriptivo a una dirección física de I/O (ej. `Sensor_Entrada` como alias de `Local:1:I.Data.0`).

**7) Las instrucciones de XIC, XIO, OTE solo pueden almacenar un tipo de dato BOOL.**

* **Respuesta:** **a) Verdadero**
* *Explicación:* Estas son instrucciones de bit. Solo operan con estados binarios (0 o 1), que corresponden al tipo de dato **BOOL**.

**8) Para reflejar un valor con decimales lo tengo que almacenar en un tipo de dato DINT.**

* **Respuesta:** **b) Falso**
* *Explicación:* Los DINT (Double Integer) son para números enteros. Para decimales se debe utilizar el tipo de dato **REAL** (punto flotante).

**9) Un temporizador con retardo a la conexión lleva por siglas TOF.**

* **Respuesta:** **b) Falso**
* *Explicación:* El retardo a la conexión es **TON** (Timer On Delay). El **TOF** es retardo a la desconexión (Timer Off Delay).

**10) Si desea indicar una acción pasado un tiempo con un TON ¿Qué bit debería de emplear?**

* **Respuesta:** **c) DN**
* *Explicación:* El bit **.DN (Done)** se activa únicamente cuando el valor acumulado (.ACC) alcanza el valor preestablecido (.PRE).

**11) En una instrucción MOV es posible trasladar un INT a un DINT.**

* **Respuesta:** **a) Verdadero**
* *Explicación:* El PLC realiza una conversión automática de tipos de datos compatibles. Como un DINT es más grande (32 bits) que un INT (16 bits), el valor cabe perfectamente.

**12) Las entradas y salidas analógicas solo es posible programarlas con la función SCL en una rutina FBD.**

* **Respuesta:** **b) Falso**
* *Explicación:* Aunque FBD es muy común para esto, también se pueden escalar en Ladder usando la instrucción **CPT (Compute)** con la fórmula de la recta o mediante instrucciones **AOI** (Add-On Instructions) personalizadas como el SCP.
