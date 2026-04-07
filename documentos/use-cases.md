# Casos de uso validados

## Caso 1. Intento de acceso SSH con autenticación incorrecta

### Objetivo
Comprobar la capacidad del sistema para detectar intentos de acceso no autorizados mediante SSH en el endpoint Ubuntu.

### Flujo
1. Se ejecuta un acceso SSH con contraseña incorrecta.
2. El endpoint Ubuntu registra eventos de autenticación fallida.
3. Wazuh recoge los logs y aplica correlación.
4. Se generan alertas en el dashboard.
5. Las alertas relevantes se envían a TheHive.

### Resultado
- detección de intentos de autenticación fallida,
- registro de eventos en el SIEM,
- generación automática de alertas,
- envío de alertas a la plataforma de gestión de incidentes.

## Caso 2. Creación de fichero en Windows y análisis con VirusTotal

### Objetivo
Comprobar la detección de cambios en un directorio monitorizado y el enriquecimiento automático de la alerta mediante VirusTotal.

### Flujo
1. Se crea un fichero de prueba en `Downloads`.
2. FIM detecta la creación del archivo.
3. Wazuh procesa el evento y genera una alerta.
4. VirusTotal aporta contexto adicional a partir del hash.
5. TheHive recibe la alerta para análisis y triaje.

### Resultado
- detección de creación de fichero,
- registro en el SIEM,
- enriquecimiento automático,
- disponibilidad de la alerta dentro del flujo habitual del SOC.
