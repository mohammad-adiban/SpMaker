# SpMaker
Implementation a programmatic API that consumes "building limits" and "height plateaus", splits up the building limits according to the height plateaus, and
stores these three entities (building limits, height plateaus and split building limits) in a persistent way.

# Validation
The height plateaus should completely cover the building limits. Therefore, inaccuracies in the
inputs are validated if there are inaccuracies including gaps or overlaps between height plateaus. Also height plataus are double cheked and resized in a case they exeed the building limits.

# Error handling
The API gives meaningful error messages when errors occur.

# Concurrency
The API also deals with concurrent updates.

# Deployment
The API are deployed to Googe cloud service.

# Requisite
Python >= 3.6
shapely
geopandas
mysql
