# ODM Study and Reference

## Setting Groups
Based on these findings, setting groups and parameters for WebODM / ODM to experiment and find optimal parameters based on input / collection type.

Current platforms:
- DJI Mavic 3E RTK (using PPK workflow for processing)

### HiRes-PPK

Output: hi-res orthomosaic and model of 3D structures. Absolute accuracy below .1' targeted. Orthomosaics crisp building edges and no missing data targeted. Including RTK/PPK tagging of images AND Ground Control Points (GCPs) for ODM.

```
auto-boundary:enable
camera-lens:brown 
dem-resolution:1 
dsm:enable
dtm:enable
feature-quality:ultra
gps-accuracy:.1
mesh-octree-depth:12 
mesh-size:300000
min-num-features:18000
orthophoto-resolution:1 
pc-quality:high
resize-to:disable
```

## Flag Descriptions

### gps-accuracy
When using RTK/PPK set gps-accuracy flag to either .1m or 2x the expected vertical accuracy (i.e. .05' ft = .015m and doubled is .03m).

.1m is a measurement thrown around the ODM forums when using RTK. 2x the expected vertical is from one of the maintainers of ODM but other anecdotes say tightening this up too much can cause some issues. 

[Source-1](https://community.opendronemap.org/t/odm-settings-gps-accuracy-and-textering-nadir-weight/11059)
