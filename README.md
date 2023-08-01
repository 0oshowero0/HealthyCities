# Healthy Cities: A Comprehensive Dataset of Environmental Determinants of Health in England Cities

## Introduction

This repo is the code for generating the dataset discribed in Nature Scientific Data paper: [Healthy Cities, A comprehensive dataset for environmental determinants of health in England cities](https://www.nature.com/articles/s41597-023-02060-y).


## Folder Structure
```none
├── HealthyCities
│   ├── air_pollution (original air pollution data)
│   ├── city_defination_and_LUTs (original defination of cities and geographical lookup tables)
│   ├── GoogleStreetView_Perform_Segmentation (segmentation code for Google Street View images)
│   │   ├── ViT-Adapter-main-mine (fork from https://github.com/czczup/ViT-Adapter and make changes)
│   │   │   ├── detection (not used in our proj)
│   │   │   ├── segmentation (for semantic segmentaion)
│   │   │   │   ├── GoogleStreetView (directory to store Google Street View images)
│   │   │   │   ├── process_streetview.py (entry code to process street view images)
│   ├── house_price (original house price data)
│   ├── life_expectancy (original life_expectancy data)
│   ├── msoa_pop (original population data)
│   ├── NACIS_Code (original POI category code data)
│   ├── osm (original OpenStreetMap data)
│   ├── POI (original SafeGraph POI data)
│   ├── prescribing (code and results for collection prescribing data)
│   │   ├── get_data.py (download prescribing data)
│   │   ├── original_data (directory for save the prescribing data files)
│   ├── temp_output (directory to store the temp files)
│   ├── output (directory to store the final output dataset)
```

## System Requirement

### Example System Information
Operating System: Ubuntu 18.04.5 LTS
CPU: AMD Ryzen Threadripper 2990WX 32-Core Processor
Memory: 128G DDR4 Memory

### Installation Guide
Typically, a modern computer with fast internet can complete the installation within 10 mins.

1. Download Anaconda according to [Official Website](https://www.anaconda.com/products/distribution), which can be done by the following command (newer version of anaconda should also work)
``` bash
wget -c https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
```
2. Install Anaconda through the commandline guide. Permit conda init when asked.
``` bash
./Anaconda3-2022.10-Linux-x86_64.sh
```
3. Quit current terminal window and open a new one. You should be able to see (base) before your command line. 

4. Use the following command to install pre-configured environment through the provided `.yml` file (you should go to the directory of this project before performing the command). Note: for the segmentation code in `GoogleStreetView_Perform_Segmentation` and `whatisthis`, please refer to the corresponding official repo [ViT-Adapter](https://github.com/czczup/ViT-Adapter) and [GeoSeg](https://github.com/WangLibo1995/GeoSeg) to check detailed installation guide.
``` bash
conda env create -f ./anaconda_env_healthy_cities.yml
```

5. Finally, activate the installed environment. Now you can run the example code through the following chapter.
``` bash
conda activate healthycities
```

(Optional) If you need to exit the environment for other project, use the following command.

``` bash
conda deactivate 
```

(Optional) Command for creating our environment without the .yml file. Note: for the segmentation code in `GoogleStreetView_Perform_Segmentation` and `whatisthis`, please refer to the corresponding official repo [ViT-Adapter](https://github.com/czczup/ViT-Adapter) and [GeoSeg](https://github.com/WangLibo1995/GeoSeg) to check detailed installation guide.
``` bash
conda create -n healthycities python==3.8
pip install numpy ipython pandas matplotlib seaborn datetime pathlib shapely geopandas pyrosm h5netcdf haversine requests urllib3 tqdm scipy scikit-learn
```


## Run the code
### Generate Lookup Tables
Note: we have compressed the original lookup tables in `city_defination_and_LUTs`. Please unzip it first.
``` bash
cd ../
python make_city_msoa_lut.py
```
### Generate Basic Statistic Subsection
``` bash
python process_boundary_city.py
python process_boundary_msoa.py
python process_geo_centroid_city.py
python process_geo_centroid_msoa.py
python process_area_city.py
python process_area_msoa.py
python process_pop_city.py
python process_pop_msoa.py
```

### Generate Behavioural Environment Subsection
Note: behavioural environment data requires Safegraph POI data, which cannot be provided here. To reproduce the data, you need to purchase Safegraph POI data and put it in `POI` folder. The NACIS code are provided in `NACIS_Code` folder.
``` bash
python process_poi.py
python process_poi_post_availability_city.py
python process_poi_post_availability_msoa.py
```


### Generate Built Environment Subsection
Note: built environment data requires Safegraph POI data, Google Street View images, and ArcGIS satellite images, which cannot be provided here. To reproduce the data, you need to purchase the correspongding data.

For building density and road density
``` bash
python process_osm_city.py
python process_osm_city_post_building_density.py
python process_osm_msoa_post_building_density.py
python process_osm_city_post_road_density.py
python process_osm_msoa_post_road_density.py
```

For house price
``` bash
python process_house_price_city.py
python process_house_price_msoa.py
```

For walkability
``` bash
python process_osm_city_post_road_intersections.py
python process_osm_msoa_post_road_intersections.py
python process_poi_post_density_city.py
python process_poi_post_density_msoa.py
python process_walkability_city.py
python process_walkability_msoa.py
```

For street view image segmentaion
Note: please refer to [ViT-Adapter](https://github.com/czczup/ViT-Adapter) to see how to install the dependencies. To run the codes, we need to download the provided model weights for Cityscapes described in [Official Readme](https://github.com/czczup/ViT-Adapter/tree/main/segmentation), and put it in `GoogleStreetView_Perform_Segmentation/ViT-Adapter-main-mine/segmentation`. Google Street View images are not provided here.
``` bash
cd GoogleStreetView_Perform_Segmentation/ViT-Adapter-main-mine/segmentation
python process_streetview.py
```

For satellite image segmentaion


### Generate Natural Environment Subsection
Note: we provide 12km level weather data in 12km.zip, please unzip it first. Due to the large size of the 1km level data, please download from [Met Office](https://www.metoffice.gov.uk/research/climate/maps-and-data/data/haduk-grid/haduk-grid) and organize the directory according to the 12 km example.
``` bash
python weather_city.py
python weather_msoa.py
```


### Generate Health Outcomes Subsection
For life expectancy data
``` bash
python process_life_expectancy_msoa
```

For covid data
``` bash
python covid_city.py
python covid_msoa.py
```

For prescribing data
``` bash
cd prescribing
python get_data.py
cd ../
python process_prescribing_mental_city.py
python process_prescribing_mental_msoa.py
python process_prescribing_other_diseases_city.py
python process_prescribing_other_diseases_msoa.py
```


### Generate Comprehensive Dataset
``` bash
python process_merge_all_data.py
```

### Reproducing Figures
Refer to the .py codes begin with `analyses_`
