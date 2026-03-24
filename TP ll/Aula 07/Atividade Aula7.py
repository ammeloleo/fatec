import csv
import json
from io import StringIO

class SistemaCSV:
  def get_dados_csv(self):
    return "nome, idade\nAna, 18\nPedro, 20"

class InterfaceJSON:
    def get_dados(self):
      raise NotImplementedError("Método deve ser implementado.")

class CSVparaJSONAdapter(InterfaceJSON):
  def __init__(self, sistema_csv):
    self.sistema_csv = sistema_csv

  def get_dados(self):
    csv_data = self.sistema_csv.get_dados_csv()
    
    csvfile = StringIO(csv_data)
    
    reader = csv.DictReader(csvfile)


    dados_list = []
    for row in reader:
        dados_list.append(row)

    
    return json.dumps(dados_list, indent=2)

sistema_legado = SistemaCSV()
adaptador = CSVparaJSONAdapter(sistema_legado)

print(adaptador.get_dados())