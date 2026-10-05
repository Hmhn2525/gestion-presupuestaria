# Gestión y Control Presupuestario

Captura, revisión y trazabilidad por centro de costo.

**Estado:** caso de estudio documental de una implementación local revisada. El código operativo y sus datos no se distribuyen en este repositorio. Se publican documentación nueva y un recorrido ilustrativo con datos ficticios.

## Problema y solución

Organizar presupuestos por propietario y centro, conservar versiones y diferenciar borradores privados, entregas y decisiones de revisión.

La fuente local implementa plantillas y presupuestos nativos, asignaciones por centro, revisión y control de versiones. La autorización se comprueba en el servidor.

## Funciones observadas en la fuente

- Plantillas versionadas y asignaciones por propietario y centro.
- Borrador privado, entrega, revisión, devolución y validación.
- Control de concurrencia mediante la versión esperada.
- Conservación de entregas, cambios y referencias históricas.
- Capacidades de lectura global y captura comprobadas por el servidor.

## Tecnologías verificadas

React, TypeScript, Python, FastAPI, SQLAlchemy, SQLite, Alembic. Consulte la [arquitectura](docs/architecture.md) para su función.

## Evidencia y resultados

El 5 de octubre de 2026 se ejecutaron 19 pruebas sintéticas seleccionadas del servidor: 19 correctas. Cubren presupuesto nativo, programa, capacidades y alta de participantes. Se registró una advertencia de deprecación en una dependencia de pruebas. Esta selección no sustituye la suite completa.

No se publican métricas de ahorro, adopción o productividad. La [verificación](docs/verification.md) explica su alcance. La aportación personal detallada y la autoría integral del código operativo no están acreditadas públicamente; este caso presenta la revisión técnica y la documentación del proyecto asociado al portafolio.

## Demostración y capturas

Abra [demo/index.html](demo/index.html) localmente. El recorrido funciona sin servidor, instalación ni conexión a servicios. Su tabla representa [datos sintéticos](examples/scenario.json), no una captura de la aplicación original. El botón recorre textos ilustrativos; no ejecuta operaciones de negocio.

![Recorrido documental con datos ficticios](docs/images/recorrido-demo.png)

Puede verificar los datos usando Python 3: `python examples/verify.py`.

## Caso de estudio

Consulte [problema, decisiones y aprendizajes](docs/case-study.md).

## Seguridad y limitaciones

Publicación independiente sin historial operativo. No incluye credenciales, identificadores de servicios, catálogos empresariales, datos personales, archivos de respaldo ni configuración productiva. Las pruebas de la fuente se ejecutaron con simulación o temporales aislados; el recorrido público es una explicación independiente.

## Pendientes

- Aceptación funcional con responsables de Finanzas.
- Comprobación de la entrega y entorno operativo vigente antes de una intervención.
- Validación de reglas, catálogos y condiciones de operación aplicables a cada versión.
- Recuperación, acceso desde dispositivos y licencia en su fase propia.

## Licencia

Pendiente de decisión expresa. No se asigna una licencia de software ni se atribuyen derechos sobre el código operativo.
