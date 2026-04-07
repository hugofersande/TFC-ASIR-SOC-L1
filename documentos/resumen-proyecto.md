# Resumen del proyecto

## Qué es este proyecto

Este proyecto implementa un **SOC de Nivel 1** en un laboratorio virtualizado, combinando una capa de detección basada en **Wazuh + Elastic Stack** con una capa de gestión e inteligencia formada por **TheHive, Cortex y MISP**.

## Qué problema resuelve

Muchas PYMEs no disponen de presupuesto ni personal especializado para desplegar soluciones SOC complejas. Esta propuesta busca ofrecer una arquitectura **viable, profesional y basada en software libre** para mejorar la capacidad de monitorización y respuesta ante incidentes.

## Componentes principales

### Capa SIEM
- Wazuh Manager
- Elastic Stack
- Agentes en Windows y Ubuntu
- Suricata
- FIM
- YARA
- VirusTotal

### Capa de gestión e inteligencia
- TheHive
- Cortex
- MISP

## Flujo resumido

1. Los endpoints generan eventos.
2. Wazuh centraliza y correlaciona los logs.
3. Se generan alertas en el SIEM.
4. Las alertas relevantes se envían a TheHive.
5. Cortex y MISP aportan contexto e inteligencia.

## Resultado

La solución demuestra que es posible desplegar una infraestructura SOC funcional, modular y de bajo coste para escenarios tipo PYME.
