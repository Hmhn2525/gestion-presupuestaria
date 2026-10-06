from pathlib import Path
import json
from decimal import Decimal

data = json.loads(Path(__file__).with_name('scenario.json').read_text(encoding='utf-8'))
assert data['synthetic'] is True
assert sum((Decimal(x) for x in data['month_values']), Decimal('0')) == Decimal(data['expected_total'])
assert data['illustrative_only'] is True
assert data['center'].startswith('DEMO-')
print('Ejemplo sintético coherente; no ejecuta ni valida el sistema operativo.')
print(f"Centro: {data['center']} | Responsable: {data['owner']} | Versión: {data['version']} | Estado: {data['state']}")
print(f"Meses: {', '.join(data['month_values'])} {data['currency']} | Total verificado: {data['expected_total']} {data['currency']}")
