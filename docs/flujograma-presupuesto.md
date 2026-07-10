# Flujograma: gestión de presupuesto y fondos

Proceso completo con los dos caminos: **fondo común de proyectos** y **caja chica**.

> Para ver el diagrama renderizado, abrir `flujograma-presupuesto.html` en el navegador.

---

## 1. Asignación inicial y bifurcación

```mermaid
flowchart TB
    subgraph GERENCIAS["GERENCIAS"]
        G1["Asignar presupuesto a todos los fondos"]
        G2["Fondo común de proyectos"]
        G3["Cajas chicas (3 fondos)"]
        G1 --> G2
        G1 --> G3
    end

    subgraph USUARIO["USUARIO / TÉCNICO"]
        U1["Solicitar presupuesto"]
        U2{"¿De qué fondo solicita?"}
        U1 --> U2
    end

    G2 -.-> U2
    G3 -.-> U2
    U2 -->|"Fondo común"| FC["CAMINO A"]
    U2 -->|"Caja chica"| CC["CAMINO B"]
```

---

## 2. Camino A — Fondo común de proyectos

| Paso | Rol | Acción |
|------|-----|--------|
| 1 | Usuario | Solicita presupuesto del fondo común |
| 2 | Jefe inmediato | Aprueba o rechaza según fondos del cliente |
| 3 | Cajera | Cobra presupuesto y entrega dinero (efectivo o transferencia) |
| 4 | Usuario | Realiza viaje/actividad y registra facturas en el sistema |
| 5 | Contabilidad | Recibe resumen de facturas |
| 6 | Usuario | Entrega facturas físicas a la cajera |
| 7 | Cajera | Verifica facturas con el sistema |
| 8 | Cajera | Ajusta saldo: sobrante a favor del proyecto o registra faltante |
| 9 | Contabilidad | Cierra la solicitud |

```mermaid
flowchart TB
    A1["Solicitar presupuesto"] --> A2["Jefe aprueba / rechaza"]
    A2 -->|"Aprueba"| A3["Cajera cobra y entrega dinero"]
    A3 --> A4["Usuario realiza actividad"]
    A4 --> A5["Registrar facturas → Contabilidad"]
    A5 --> A6["Entregar facturas a cajera"]
    A6 --> A7["Cajera verifica en sistema"]
    A7 --> A8{"¿Saldo?"}
    A8 -->|"Sobrante"| A9["Saldo a favor del proyecto"]
    A8 -->|"Faltante"| A10["Registrar dinero adicional"]
    A8 -->|"Cuadrado"| A11["Cerrar solicitud"]
    A9 --> A11
    A10 --> A11
```

---

## 3. Camino B — Caja chica

| Paso | Rol | Acción |
|------|-----|--------|
| 1 | Usuario | Solicita presupuesto de una de las 3 cajas chicas |
| 2 | Cajera | Pregunta para qué es y de qué caja pide |
| 3 | Cajera | Acepta, niega o consulta con su jefe inmediato |
| 4 | Cajera | Entrega dinero de la caja chica |
| 5 | Usuario | Realiza las compras |
| 6 | Usuario | Entrega facturas y sobrante a la cajera |
| 7 | Cajera | Registra todo en el sistema |

```mermaid
flowchart TB
    B1["Solicitar presupuesto caja chica"] --> B2["Cajera evalúa solicitud"]
    B2 -->|"Niega"| B3["Fin — rechazado"]
    B2 -->|"Consulta jefe"| B4["Jefe decide"]
    B4 -->|"No"| B3
    B4 -->|"Sí"| B5["Entregar dinero"]
    B2 -->|"Acepta"| B5
    B5 --> B6["Usuario hace compras"]
    B6 --> B7["Entregar facturas y sobrante"]
    B7 --> B8["Cajera registra en sistema"]
```

---

## Roles involucrados

| Rol | Camino A (Fondo común) | Camino B (Caja chica) |
|-----|------------------------|------------------------|
| Gerencias | Asignan presupuesto a fondos | Asignan presupuesto a fondos |
| Usuario / Técnico | Solicita, registra y entrega facturas | Solicita, compra y entrega facturas |
| Jefe inmediato | Aprueba solicitud del usuario | — |
| Cajera | Cobra, verifica y liquida | Evalúa, entrega dinero y registra |
| Jefe de cajera | — | Aprueba si la cajera consulta |
| Contabilidad | Recibe resumen y cierra solicitud | — |
