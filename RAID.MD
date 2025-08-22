# Investigación sobre RAID

## 1. Introducción
RAID (Redundant Array of Independent/Inexpensive Disks) es una tecnología que permite combinar varios discos duros físicos en una sola unidad lógica, con el fin de mejorar el **rendimiento**, aumentar la **tolerancia a fallos** y optimizar el uso de **almacenamiento**.  

El concepto de RAID fue introducido en 1987 por **David A. Patterson, Garth A. Gibson y Randy H. Katz** en su artículo *"A Case for Redundant Arrays of Inexpensive Disks"*. Su propósito era aprovechar múltiples discos pequeños y económicos para obtener un desempeño y seguridad similares a los de discos grandes y costosos.  

En la actualidad, RAID se utiliza tanto en entornos **empresariales** (servidores, centros de datos) como en **usuarios domésticos avanzados** (NAS caseros, estaciones de trabajo).

---

## 2. Objetivos de RAID
- **Rendimiento**: Aumentar la velocidad de lectura y escritura dividiendo o paralelizando los datos.
- **Redundancia**: Proteger la información replicándola en varios discos.
- **Disponibilidad**: Garantizar que los datos sigan accesibles incluso si un disco falla.
- **Escalabilidad**: Permitir el uso de múltiples discos como un solo sistema de almacenamiento.

---

## 3. Niveles de RAID

### 3.1 RAID 0 (Striping)
- **Funcionamiento**: Los datos se dividen en bloques y se distribuyen entre los discos.
- **Ventajas**:
  - Máximo rendimiento en lectura y escritura.
  - Aprovecha el 100% de la capacidad de los discos.
- **Desventajas**:
  - No existe redundancia. Si un disco falla, se pierde toda la información.
- **Uso típico**: Juegos, edición de video, trabajos donde el rendimiento es más importante que la seguridad.

---

### 3.2 RAID 1 (Mirroring)
- **Funcionamiento**: Los datos se copian de manera idéntica en dos discos.
- **Ventajas**:
  - Alta tolerancia a fallos: si un disco falla, los datos permanecen en el otro.
  - Recuperación rápida en caso de fallo.
- **Desventajas**:
  - Solo se aprovecha el 50% del almacenamiento.
- **Uso típico**: Servidores pequeños, sistemas que requieren seguridad de datos pero no grandes capacidades.

---

### 3.3 RAID 5
- **Funcionamiento**: Combina striping con **paridad distribuida**. La información de paridad permite reconstruir datos en caso de que falle un disco.
- **Ventajas**:
  - Buen equilibrio entre capacidad, rendimiento y seguridad.
  - Puede tolerar la falla de un disco.
- **Desventajas**:
  - Escritura más lenta por el cálculo de paridad.
  - La reconstrucción de datos puede ser lenta.
- **Uso típico**: Servidores de archivos, sistemas empresariales de almacenamiento.

---

### 3.4 RAID 6
- **Funcionamiento**: Similar a RAID 5 pero con doble paridad.
- **Ventajas**:
  - Tolerancia a la falla de dos discos.
  - Mayor seguridad que RAID 5.
- **Desventajas**:
  - Rendimiento de escritura más bajo.
  - Requiere al menos 4 discos.
- **Uso típico**: Centros de datos y entornos críticos donde la seguridad es prioritaria.

---

### 3.5 RAID 10 (o 1+0)
- **Funcionamiento**: Combina striping (RAID 0) y mirroring (RAID 1).
- **Ventajas**:
  - Alta velocidad y redundancia.
  - Recuperación rápida ante fallos.
- **Desventajas**:
  - Costoso, ya que requiere mínimo 4 discos.
- **Uso típico**: Bases de datos transaccionales, sistemas que requieren alto rendimiento y seguridad.

---

## 4. Comparación de Niveles RAID

| Nivel RAID | Redundancia | Rendimiento | Capacidad Utilizable | Tolerancia a fallos | Nº mínimo de discos |
|------------|-------------|-------------|-----------------------|----------------------|----------------------|
| RAID 0     | ❌          | ⭐⭐⭐⭐       | 100%                  | 0 discos            | 2                    |
| RAID 1     | ✅          | ⭐⭐          | 50%                   | 1 disco             | 2                    |
| RAID 5     | ✅          | ⭐⭐⭐        | n-1 discos            | 1 disco             | 3                    |
| RAID 6     | ✅          | ⭐⭐          | n-2 discos            | 2 discos            | 4                    |
| RAID 10    | ✅          | ⭐⭐⭐⭐       | 50%                   | Depende del par      | 4                    |

---

## 5. Ventajas y Desventajas Generales de RAID

### Ventajas
- Mejora el rendimiento de lectura y escritura.
- Permite tolerancia a fallos y disponibilidad continua.
- Escalabilidad: fácil de ampliar agregando más discos.
- Optimiza recursos al trabajar con discos económicos.

### Desventajas
- No sustituye a las **copias de seguridad** externas.
- Puede ser costoso (más discos necesarios).
- Mayor complejidad en configuración y administración.
- En caso de fallos múltiples, la recuperación puede ser difícil o imposible.

---

## 6. Aplicaciones Prácticas de RAID
- **Servidores de bases de datos**: Para evitar pérdida de información y mantener operaciones críticas.
- **Sistemas de videovigilancia**: Grandes volúmenes de datos requieren velocidad y redundancia.
- **Centros de datos**: Uso masivo de RAID 5/6 en almacenamiento empresarial.
- **NAS domésticos**: Usuarios que buscan almacenar fotos, videos y documentos de forma segura.
- **Entornos de edición multimedia**: RAID 0 y RAID 10 para manejar grandes archivos de video.

---

## 7. Consideraciones Finales
- RAID **no es un reemplazo de los backups**. Aunque proporcione redundancia, no protege contra desastres como incendios, borrados accidentales o ataques de ransomware.
- La elección del nivel RAID depende del **equilibrio deseado entre rendimiento, seguridad y costo**.
- Para usuarios domésticos que buscan seguridad, **RAID 1** puede ser suficiente.
- Para empresas, RAID 5/6 y RAID 10 son las configuraciones más utilizadas.

---

## 8. Conclusión
RAID es una tecnología clave en la administración de sistemas de almacenamiento. Permite lograr un balance entre velocidad, redundancia y capacidad, adaptándose a distintos escenarios: desde computadoras personales hasta grandes centros de datos.  

Sin embargo, RAID no garantiza una protección absoluta. Por lo tanto, es fundamental complementarlo con **estrategias de respaldo externas** para asegurar la integridad de la información a largo plazo.

---

## 9. Referencias
- Patterson, D. A., Gibson, G., & Katz, R. H. (1988). *A Case for Redundant Arrays of Inexpensive Disks (RAID)*. ACM SIGMOD.
- Stallings, W. (2017). *Computer Organization and Architecture*. Pearson.
- Red Hat. (s.f.). [Introduction to RAID](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/storage_administration_guide/ch-raid).
- WD. (2023). [What is RAID Storage?](https://www.westerndigital.com/).
- Kingston Technology. (2023). [RAID Levels Explained](https://www.kingston.com/).
