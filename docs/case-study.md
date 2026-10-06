# Caso de estudio: Gestión y Control Presupuestario

## Necesidad

Organizar presupuestos por propietario y centro, conservar versiones y diferenciar borradores privados, entregas y decisiones de revisión.

## Aportación documentada

Este caso organiza la revisión de fuentes, pruebas sintéticas, arquitectura y límites de una solución asociada al portafolio. Se preservan las reservas sobre autoría exclusiva de todos sus componentes y componentes de terceros. Las responsabilidades personales en el relevamiento de necesidades, ciclo de estados (*Borrador → Entrega → Revisión → Validación*), reglas de validación en servidor y control de versiones han sido confirmadas en el README.

## Decisiones observadas

Separar borrador y entrega conserva el contexto revisado. El control de versión evita aplicar cambios sobre una edición desactualizada. Los permisos visibles en la interfaz requieren comprobación independiente en el servidor.

## Evidencia

El 5 de octubre de 2026 se ejecutaron 19 pruebas sintéticas seleccionadas del servidor: 19 correctas. Cubren presupuesto nativo, programa, capacidades y alta de participantes. Se registró una advertencia de deprecación en una dependencia de pruebas. Esta selección no sustituye la suite completa.

El [recorrido ilustrativo](../demo/index.html) usa datos inventados y no demuestra ejecución de la aplicación original. La imagen conserva esa identificación explícita.

## Aprendizajes

Una prueba sintética acredita comportamiento técnico acotado. La aceptación financiera y la operación de una entrega requieren evidencia propia y no se infieren de un build o una suite.

## Próxima fase

- Aceptación funcional con responsables de Finanzas.
- Comprobación de la entrega y entorno operativo vigente antes de una intervención.
- Validación de reglas, catálogos y condiciones de operación aplicables a cada versión.
- Recuperación, acceso desde dispositivos y licencia en su fase propia.
