# Arquitectura general

## Bloque 1: SIEM y monitorización
- Wazuh Manager
- Elastic Stack
- Endpoints Windows y Ubuntu
- Suricata IDS

## Bloque 2: Gestión e inteligencia
- TheHive
- Cortex
- MISP

## Flujo operativo
1. Los endpoints generan eventos.
2. Wazuh los centraliza y correlaciona.
3. Las alertas relevantes se envían a TheHive.
4. Cortex y MISP enriquecen el análisis.
