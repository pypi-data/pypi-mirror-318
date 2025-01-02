import os
import numpy as np
import datetime
import netCDF4 as nc4

def build_netcdf_from_array(array,
                            ref_ds=None,
                            ref_lat=None,
                            ref_lon=None,
                            varname='varname',
                            start_date="YYYY-MM-DD",
                            end_date="YYYY-MM-DD",
                            save_dir='.',
                            filename='newfile.nc',
                            delete_existing_file=True,
                            ):
    
    # Squeeze the last dimension
    array = np.squeeze(array, axis=-1)
    
    def extract_date_components(date_string):
        year, month, day = map(int, date_string.split("-"))
        return year, month, day
    
    def find_lat_lon_vars(ds):
        lat_var, lon_var = None, None
        for var_name in ds.variables:
            var = ds[var_name]
            if hasattr(var, "standard_name"):
                if var.standard_name.lower() in ["latitude", "lat"]:
                    lat_var = var_name
                elif var.standard_name.lower() in ["longitude", "lon"]:
                    lon_var = var_name
            elif var_name.lower() in ["latitude", "lat"]:
                lat_var = var_name
            elif var_name.lower() in ["longitude", "lon"]:
                lon_var = var_name
        return lat_var, lon_var
    
    def date_range(start, end):
        delta = end - start
        return [start + datetime.timedelta(days=i) for i in range(delta.days + 1)]
    
    # Ensure save_dir exists
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, filename)
    
    # Remove existing file if it exists
    if delete_existing_file:
        if os.path.exists(filepath):
            os.remove(filepath)

    # Handle latitude and longitude variables
    if ref_ds is not None:
        lat_var, lon_var = find_lat_lon_vars(ref_ds)
        lat_values, lon_values = ref_ds[lat_var].data, ref_ds[lon_var].data
    elif ref_lat is not None and ref_lon is not None:
        lat_values, lon_values = ref_lat, ref_lon
    else:
        raise ValueError("Either 'ref_ds' or both 'ref_lat' and 'ref_lon' must be provided.")
    
    # Extract date components and create date range
    s_year, s_mon, s_day = extract_date_components(start_date)
    e_year, e_mon, e_day = extract_date_components(end_date)
    dates = date_range(datetime.datetime(s_year, s_mon, s_day), datetime.datetime(e_year, e_mon, e_day))
    
    # Validate input array shape
    expected_shape = (len(dates), len(lat_values), len(lon_values))
    if array.shape != expected_shape:
        raise ValueError(f"Input array shape {array.shape} does not match expected shape {expected_shape}.")
    
    # Create the NetCDF file
    ncfile = nc4.Dataset(filepath, mode='w', format='NETCDF4')
    ncfile.title = os.path.splitext(filename)[0]  # Add title
    
    # Create dimensions
    ncfile.createDimension('lat', len(lat_values))
    ncfile.createDimension('lon', len(lon_values))
    ncfile.createDimension('time', None)
    
    # Create variables
    lat = ncfile.createVariable('lat', np.float32, ('lat',))
    lat.units = 'degrees_north'
    lat.long_name = 'latitude'
    
    lon = ncfile.createVariable('lon', np.float32, ('lon',))
    lon.units = 'degrees_east'
    lon.long_name = 'longitude'
    
    time = ncfile.createVariable('time', np.float64, ('time',))
    time.units = f'days since {start_date}'
    time.long_name = 'time'
    
    var = ncfile.createVariable(varname, np.float64, ('time', 'lat', 'lon'))
    var.units = 'mm/day'  # Update unit appropriately
    
    # Write data
    lat[:] = lat_values
    lon[:] = lon_values
    var[:] = array
    time[:] = nc4.date2num(dates, time.units)
    
    ncfile.close()
    print(f'Dataset created: {filepath}')