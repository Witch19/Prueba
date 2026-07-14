# Flujograma: gestión de presupuesto y fondos

Proceso completo con tres caminos: **fondo común de proyectos**, **caja chica** y **compra/gasto importante previsto**.

> Para ver el diagrama renderizado, abrir `flujograma-presupuesto.html` en el navegador.
> Imagen lista para enviar: `flujograma-presupuesto.png` · PDF: `flujograma-presupuesto.pdf`

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

    subgraph ENTRADA["TIPOS DE SOLICITUD"]
        U1["Solicitar anticipo de presupuesto"]
        U2{"¿De qué fondo?"}
        U3["Compra o gasto importante previsto"]
        U1 --> U2
    end

    G2 -.-> U2
    G3 -.-> U2
    U2 -->|"Fondo común"| FC["CAMINO A"]
    U2 -->|"Caja chica"| CC["CAMINO B"]
    U3 --> CG["CAMINO C"]
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

## 4. Camino C — Compra o gasto importante previsto

Nace de una compra o gasto importante **ya previsto**. No se pide anticipo: se parte de la **factura**.

| Paso | Rol | Acción |
|------|-----|--------|
| 1 | Usuario | Tiene compra/gasto importante previsto y obtiene la factura |
| 2 | Jefe inmediato | Recibe la factura y aprueba o rechaza el gasto |
| 3 | Caja | Recibe el gasto aprobado |
| 4 | Jefa inmediata de cajera | Escoge de qué fondo debe cubrirse el gasto |
| 5 | Cajera | Recibe el PIN y realiza el pago |
| 6 | Cajera | Registra el pago y cierra |

```mermaid
flowchart TB
    C1["Compra/gasto importante previsto"] --> C2["Factura"]
    C2 --> C3["Jefe inmediato recibe factura"]
    C3 --> C4{"¿Aprueba?"}
    C4 -->|"No"| C5["Rechazar"]
    C4 -->|"Sí"| C6["Enviar a caja"]
    C6 --> C7["Jefa de cajera escoge el fondo"]
    C7 --> C8["Asignar fondo"]
    C8 --> C9["Cajera recibe PIN"]
    C9 --> C10["Pagar factura"]
    C10 --> C11["Registrar y cerrar"]
```

---

## Roles involucrados

| Rol | Camino A | Camino B | Camino C |
|-----|----------|----------|----------|
| Gerencias | Asignan presupuesto | Asignan presupuesto | Fondos disponibles para cubrir |
| Usuario / Técnico | Solicita anticipo y factura al final | Solicita anticipo y factura al final | Inicia con factura del gasto |
| Jefe inmediato | Aprueba solicitud | — | Aprueba el gasto/factura |
| Cajera | Cobra, verifica y liquida | Evalúa, entrega dinero y registra | Recibe PIN y paga |
| Jefa / Jefe de cajera | — | Aprueba si la cajera consulta | Escoge el fondo que cubre el gasto |
| Contabilidad | Recibe resumen y cierra | — | — |
