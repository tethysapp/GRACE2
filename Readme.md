# GRACE 2.0

Readme is under edits. Please use this information with caution. 

### Dependencies

```bash
conda install -c conda-forge gdal numpy netCDF4 fiona shapely pyshp rtree geojson
pip install area
```

### Known Issues

- You need to restart the portal hosting the GRACE app if custom settings are changed. This is because the way config.py is setup. It reads in the values when the app loads up and continues to use them. This is a bad approach. We should fetch the values dynamically each time we need them. 

### Installation Notes

1. it has a persistent store database.  the name is gracefo_db.  this is different from the previous database that is currently on the server (grace_db) . so you'll have to set it up in admin and do the tethys syncstores command

1. even though the folder is GRACE2 the app name is technically newgrace.  just haven't gotten around to changing it yet.
1. some of the layers appear to be glitching intermittently on my end.  like the grids shift between time steps.  let me know if this is happening with you guys as well.  not sure if it's my thredds server or the files themselves.  

1. custom settings:  there are 2 custom settings.  one of them is the thredds base url and should end in grace/ (ie https://tethys.byu.edu/thredds/)
1. The other setting is the path to the mounted folder where the grace files are stored (ie /Users/tmcstraw/thredds_data/grace/) . This one should end in ...../grace/

### Thredds Installation Notes

1. We need to copy the .pal file included in the root of this repo to our thredds server. It needs to be places at /apache-tomcat-8.5.42/webapps/thredds/WEB-INF/palettes