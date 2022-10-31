"""
Pastas
out.22
"""


from pathlib import Path


# Project Path
project_path = Path(__file__).parents[1]

scrapy_path = project_path / "scrapy"
scrapy_path.mkdir(exist_ok=True)

logs_path = scrapy_path / "logs"
logs_path.mkdir(exist_ok=True)

adds_path = scrapy_path / "adds"
adds_path.mkdir(exist_ok=True)


# Package Path
package_path = project_path / "outorgas"
package_path.mkdir(exist_ok=True)

data_path = package_path / "data"
data_path.mkdir(exist_ok=True)

input_path = data_path / "input"
input_path.mkdir(exist_ok=True)

input_path_brutos = input_path / "brutos"
input_path_brutos.mkdir(exist_ok=True)

output_path = data_path / "output"
output_path.mkdir(exist_ok=True)

output_path_geo = output_path / "geo"
output_path_geo.mkdir(exist_ok=True)

output_path_gpkg = output_path / "gpkg"
output_path_gpkg.mkdir(exist_ok=True)

output_path_tab = output_path / "tab"
output_path_tab.mkdir(exist_ok=True)

output_path_map = output_path / "map"
output_path_map.mkdir(exist_ok=True)


if __name__ == "__main__":
    print(project_path)
