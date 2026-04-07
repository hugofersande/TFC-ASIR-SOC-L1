# Troubleshooting y lecciones aprendidas

## 1. Problemas con el agente Wazuh en Windows 11

### Síntoma
El servicio del agente aparecía en estado `Running`, pero el endpoint no llegaba a conectar correctamente con el manager.

### Comprobaciones realizadas
- revisión de conectividad con el manager,
- verificación de puertos,
- limpieza del registro del agente,
- eliminación de claves antiguas,
- cambio del `agent_name`,
- reautenticación manual.

### Decisión
Se descartó Windows 11 y se sustituyó por Windows 10, obteniendo una integración estable.

## 2. Problemas DNS/TLS al descargar imágenes Docker

### Síntoma
Errores TLS durante el despliegue de MISP y descarga de imágenes.

### Solución aplicada
Se ajustó la configuración de Docker:

```json
{
  "ipv6": false,
  "dns": ["1.1.1.1", "8.8.8.8"]
}
```

## 3. Corrupción o reinicios de servicios del stack TheHive

### Síntoma
Problemas de arranque derivados de volúmenes de Cassandra o Elasticsearch.

### Procedimiento usado
```bash
sudo docker compose down
sudo docker volume ls | grep -Ei 'hive|cassandra|elastic'
sudo docker volume rm thehivelab_cassandradata
sudo docker volume rm thehivelab_elasticsearchdata
sudo docker compose up -d
```

## 4. Lecciones aprendidas

- separar servicios críticos en varias VMs mejora estabilidad y mantenimiento,
- documentar troubleshooting da mucho valor al proyecto,
- los nombres de agente y la autenticación manual son claves en Wazuh,
- el despliegue realista de un SOC exige pensar tanto en arquitectura como en operación.
