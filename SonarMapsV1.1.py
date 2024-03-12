import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.extra.rate_limiter import RateLimiter

entrada = 'museusSP.ods'            # Caso não abra verifique as dependencias necessarias ou salve em outro formato. 
saida = "ordenado.ods"              # "planilha em ordem de distancia.formato"
ponto0 = "estação da luz, são paulo"# Ponto de referencia    

# Lendo a tabela com os endereços
df = pd.read_excel(entrada,engine="odf")  
df = df.fillna("xxx")

# Instanciando o geocodificador
geolocator = Nominatim(user_agent="my_geocoder")
delay = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Função para obter as coordenadas de uma rua
def get_coordinates(address):
    location = delay(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Calcular a distância entre duas coordenadas
def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

# Obtendo as coordenadas de cada rua e calculando a distância até o ponto de referência
reference_point =  get_coordinates(ponto0)
df['Coordenadas'] = df['rua'].apply(lambda x: get_coordinates(x))
df['Distancia'] = df['Coordenadas'].apply(lambda x: calculate_distance(reference_point, x) if x[0] else None)

# Ordenando as ruas por distância
df_sorted = df.dropna().sort_values(by='Distancia')

# Imprimindo a lista
print(df_sorted)
df_sorted.to_excel(saida, index=False)
