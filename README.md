# Gestión y Control Presupuestario

Caso documental y demo pública sintética para captura mensual, control de versiones y revisión por centro de costo.

> [!NOTE]
> **Repositorio documental.** El código y la operación originales permanecen fuera de este repositorio. La demo pública es independiente, usa datos inventados y no se conecta a servicios ni bases de datos.

[Abrir demo local](demo/index.html) · [Verificar fixture](#reproducir-el-ejemplo) · [Caso de estudio](docs/case-study.md) · [Arquitectura](docs/architecture.md) · [Verificación y límites](docs/verification.md)

![Mockup sintético del estado inicial de dos centros; no es captura del piloto](docs/images/mockup-synthetic.svg)

*Mockup estático generado desde la fixture pública. Fecha y alcance están rotulados en el gráfico; no representa la interfaz original ni ejecuta el backend.*

## Problema

La integración de presupuestos anuales desde hojas dispersas dificulta distinguir borradores de entregas, conservar observaciones y saber qué versión se revisó.

## Aportación documentada

Relevé necesidades de captura y consolidación para definir un ciclo de borrador, entrega, revisión, devolución y validación. Estructuré reglas de validación en servidor y control de versiones para prevenir sobreescrituras accidentales. Esta descripción corresponde al trabajo con la solución original; la demo pública no implementa ni acredita su backend.

## Demo pública reproducible

Abre `demo/index.html` en un navegador moderno. La página funciona desde disco y contiene su fixture; no requiere instalación ni conexión a internet.

- Dos centros ficticios, tres partidas por centro y doce meses por partida.
- Importes editables, subtotales mensuales y anuales, celdas pendientes y ceros capturados.
- Perfil de captura asignado a un centro y perfil de revisión asignado a ambos. Las asignaciones solo simulan permisos dentro de JavaScript del navegador.
- Entrega bloqueada mientras existan celdas pendientes o importes inválidos. Una devolución requiere observación; después se puede editar y entregar otra versión.
- Historial de snapshots conserva cada entrega anterior durante la sesión. La validación, la devolución y el rechazo con versión obsoleta se muestran en el registro de actividad.
- Reiniciar escenario restaura datos y estados iniciales. Cerrar la página también descarta todos los cambios.

La interfaz no autentica personas, aplica controles en servidor, guarda datos de forma persistente ni acredita autorización, concurrencia o aceptación de Finanzas. Véanse los [límites](docs/verification.md).

## Reproducir el ejemplo

Requiere Python 3 y Node.js 20, ambos con biblioteca estándar. Desde la raíz:

```text
python examples/verify.py
node examples/verify_state.js
node examples/render_mockup.js --check
```

Python confirma que la fixture de `examples/scenario.json` coincide con los datos incrustados en la demo y el mockup. Comprueba estructura, partidas y meses, asignaciones ficticias, montos, totales, ceros y pendientes. Node.js verifica cálculos, bloqueo por pendiente, rechazo obsoleto, devolución, nueva entrega, validación y conservación de snapshots. El tercer comando comprueba que el SVG coincide con la fixture; ejecútalo sin `--check` para regenerarlo.

## Evidencia de la fuente original

El 5 de octubre de 2026 se ejecutaron 19 pruebas sintéticas seleccionadas del servidor local privado: 19 correctas. Cubrieron presupuesto nativo, asignaciones, capacidades y alta de participantes. Esa ejecución es evidencia histórica acotada; sus pruebas no se distribuyen y no puede repetirse con esta demo.

No se publican métricas de ahorro de tiempo ni resultados de aceptación funcional. No hay evidencia pública de operación actual.

## Tecnologías y alcance

| Alcance | Tecnologías |
|---|---|
| Fuente local revisada | React, TypeScript, Python, FastAPI, SQLAlchemy, SQLite, Alembic |
| Ejemplo público reproducible | HTML, CSS, JavaScript del navegador y Node.js 20; Python 3 para verificar la fixture |

- La fuente original y sus credenciales operativas no forman parte de este repositorio.
- Los permisos de la demo no son seguridad: el usuario puede modificar JavaScript y datos locales.
- La demo guarda el historial solo en memoria; recargar, cerrar o reiniciar elimina cambios.
- Aceptación funcional, operación productiva, recuperación y acceso móvil siguen sin acreditarse aquí.
- No se asigna licencia; queda pendiente de decisión expresa.

Más detalle: [arquitectura](docs/architecture.md), [caso de estudio](docs/case-study.md) y [verificación y límites](docs/verification.md).
