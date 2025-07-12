# Gerador de Heatmaps de Endereços

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Licença](https://img.shields.io/badge/Licença-MIT-green)](LICENSE)

```Os dados servem o propósito de exemplo e somente de exemplo, não tendo sido coletados de usuários e não mantém nenhuma relação com nenhuma informação.```

Este projeto é um script Python que converte listas de endereços em mapas de calor interativos (heatmaps) usando a biblioteca Folium. Ele geocodifica endereços com o Nominatim (OpenStreetMap) e gera um arquivo HTML visualizável em qualquer navegador. O código pode ser abastecido com os endereços que forem de interesse para utilização, por exemplo endereços de clientes ou de alunos de uma escola para mapeamento.

## Funcionalidades
- **Geocodificação automática**: Converte endereços em coordenadas latitude/longitude.
- **Limpeza de dados**: Remove endereços inválidos (ex.: contendo "null_rua" ou formatos vazios).
- **Geração de heatmap**: Cria mapas de calor com densidade de pontos, centrados na cidade selecionada.
- **Configuração flexível**: Abasteça com dados de datasheets existentes ou escolha entre fontes de dados de exemplo como "cdc_2021" (Capão da Canoa 2021), "cdc_2025" (Capão da Canoa 2025) ou "mn_2025" (Montenegro 2025).
- **Cache de geocodificação**: Otimiza chamadas repetidas para evitar timeouts.

## Requisitos
- Python 3.8 ou superior.
- Bibliotecas necessárias:
  - `folium`
  - `geopy`
  - `uuid` (já incluso no Python padrão)

Instale as dependências com:
pip install folium geopy


## Como Usar
1. **Clone o repositório**:
git clone https://github.com/fxlipe124/heatmap_generator.git
cd heatmap_generator


2. **Configure a fonte de dados**:
- Abra o arquivo principal (ex.: `main.py`) e defina a variável `DATA_SOURCE` para uma das opções (ou outra estabelecida pelo usuário): `"cdc_2021"`, `"cdc_2025"` ou `"mn_2025"`.

3. **Execute o script**:
python mapa_de_calor.py

- Isso gerará um arquivo HTML como `heatmap_capao_da_canoa_cdc_2025.html` (dependendo da configuração).
- Abra o arquivo no navegador para visualizar o mapa.

4. **Exemplo de saída**:
- Se não houver coordenadas válidas, o script exibe uma mensagem de erro.
- O mapa é centrado na cidade escolhida, com zoom inicial de 13 e raio de calor ajustável (atualmente 15).

## Estrutura do Código
- **Arquivos de endereços**: `addresses_cdc_2021.py`, `addresses_cdc_2025.py`, `addresses_mn_2025.py` (contêm listas de endereços importadas como módulos).
- **Configurações**: Dicionário `city_settings` define centros de mapa e prefixos por cidade.
- **Funções principais**:
- `clean_address()`: Filtra endereços inválidos.
- `geocode_address()`: Geocodifica com cache e retry para timeouts.
- **Geração do mapa**: Usa Folium para criar o mapa base e adicionar a camada de heatmap.

## Limitações
- Dependente da API Nominatim (OpenStreetMap), que pode ter limites de taxa (rate limiting). Use com moderação.
- Endereços devem estar formatados corretamente para geocodificação precisa.
- Não inclui visualizações avançadas; o output é um HTML simples.

## Contribuições
Sinta-se à vontade para abrir issues ou pull requests! Sugestões para adicionar mais cidades ou melhorar a geocodificação são bem-vindas.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).
