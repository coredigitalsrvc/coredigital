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
feature-type:dspsift
force-gps:true
gps-accuracy:.05
mesh-octree-depth:12 
mesh-size:300000
min-num-features:16000
orthophoto-resolution:1 
pc-quality:high
resize-images:no 
```

## Flag Descriptions

### force-gps
When using RTK/PPK data AND GCPs, ODM will ignore the EXIF data in images unless you use force-gps. By using this flag, both EXIF and GCP data will be used in processing. 

[Source 1](https://community.opendronemap.org/t/webodm-for-survey-usage/4869)

### gps-accuracy
When using RTK/PPK set gps-accuracy flag to either .1m or 2x the expected vertical accuracy (i.e. .05' ft = .015m and doubled is .03m).

.1m is a measurement thrown around the ODM forums when using RTK. 2x the expected vertical is from one of the maintainers of ODM but other anecdotes say tightening this up too much can cause some issues. 

[Source-1](https://community.opendronemap.org/t/odm-settings-gps-accuracy-and-textering-nadir-weight/11059)

## Windows Configuration

### Windows Page File Size

It is recommended to use a page file size (equivalent of swap in linux) of 1-2x RAM. In Windows 11:
```
1. Press Win Key
2. Type advanced system settings and press enter
3. Select 'Settings' for Performance
4. Advanced tab, 'Change...' under Virtual memory
5. Deselect automatic mgmt, make changes, click 'Set' 'Ok' and 'Apply'
6. Reboot
```

### Enable GPU Acceleration
**NOTE: GPU acceleration does not work using dpsift as of 4/2024**

To get GPU running in Windows, using Docker WSL, follow these commands:
```
1. Install latest nvidia drivers
2. Open git bash in the directory you installed WebODM, same way you launch ODM

    Install latest nvidia windows drivers

From webodm directory you installed to:

    run “docker run --gpus all nvcr.io/nvidia/k8s/cuda-sample:nbody 21 nbody -gpu -benchmark”
    This will download the docker images needed, and run a test using the gpu

    Edit webodm.sh file. Search for “export GPU_NVIDIA=false” and change it to true:

export GPU_NVIDIA=true

    Edit docker-compose.nodeodm.gpu.nvidia.yml. Ensure the “devices” section at the very bottom looks like this (with proper indentation, which the below is not using, but the main text should already be there and you should only have to update the values):

devices:
  - driver: nvidia
    count: 1
    capabilities: [gpu]

    start webodm with working GPU, ./webodm.sh start --gpu

An easy way to see if it worked is in docker, check which image node-odm-1 is using. It should say opendronemap/nodeodm:gpu with the important part being :gpu
```

[Source-1](https://community.opendronemap.org/t/windows-docker-gpu/15209/6)
