from netCDF4 import Dataset
OUTPUT_PATH = 'data'
OUTPUT_FILE_NAME = 'Biome-BGC-annual-output.nc'
NC_PATH = OUTPUT_PATH + '/' + OUTPUT_FILE_NAME

dataset = Dataset(NC_PATH, 'r+', format='NETCDF4')
variables = dataset.variables
dataset.close()