# Mirshahi CT Analysis Toolkit (MirCAT)
A python package designed for rapid analysis of CT images. Convert dicom series to NiFTi, segment body structures, and quantify values within the original image.

## Usage
The recommended usage for this repository is directly through the docker image. Use 
```bash
docker pull idinsmore1/mircat:latest
```
 to get the most recent version. 
This will easily handle all dependencies, especially with CUDA. MirCAT works with both CPU and GPU for segmentation, but GPU is recommended for the best/fastest results.

If you want a python-based distribution, you can use  
```bash
pip install mircat  # All libraries
pip install mircat-stats # Statistics only library. Useful if you segment on another machine that has CUDA.
```
No guarantee that dependencies will be easy to solve. In a fresh python environment, it should be fine.

## Commands
For docker
```bash
docker run idinsmore1/mircat:latest -h 
usage: mircat [-h] [-q] {convert,segment,stats,update} ...

Mirshahi CT Analysis Toolkit (MirCAT) CLI tool. Convert dicoms to niftis,
segment niftis, and calculate statistics.

positional arguments:
  {convert,segment,stats,update}
    convert             Convert DICOM files
    segment             Segment NIfTI files using neural network models
    stats               Calculate statistics for NIfTI files
    update              Update the header and stats data for a NIfTI file to
                        the latest version

options:
  -h, --help            show this help message and exit
  -q, --quiet           Decrease output verbosity
```
For python
```bash
# From the command line
mircat -h
# Same output
mircat-copy-models input_dir  # This will copy model weights to the proper directory. 
```
Currently the four commands are `convert`, `segment`, `stats` and `update`.

### Convert
This command allows you to convert DICOM series to into NiFTi files. It uses the `multiprocessing` module for parallelization. The converted NiFTi files will be stored in subfolders in `output_dir` corresponding to their unique DICOM identifiers. 
```markdown
usage: mircat convert [-h] [-n NUM_WORKERS] [-ax] [-nm] [-th THREADS] dicoms output_dir

positional arguments:
  dicoms                Path to DICOM files
  output_dir            Output directory

options:
  -h, --help            show this help message and exit
  -n NUM_WORKERS, --num-workers NUM_WORKERS
                        Number of workers for converting dicom folders.
  -ax, --axial-only     Only convert axial dicom series
  -nm, --no-mip         Do not convert likely mip series
  -th THREADS, --threads THREADS
                        Number of threads for each worker
```

### Segment
This command allows you to segment structrues from NiFTi files. You can specify what tasks you want to run with the `--tasks` flag. To see the list of outputs for each of the tasks, look at the config file in 
in `packages/mircat-stats/src/mircat_stats/configs/models.py`. Default is to run segmentation on the GPU. If you would like the model weights for these operations please email me at **irdinsmore1@geisinger.edu**. The docker image will already come with them by default.  
If you install with python, you can use `mircat-copy-models` to copy the directory where you store the model weights to the proper library location. 

All segmentations will be stored in a folder next to the give input NiFTi files. For example if I run `segment niftis/ex_nifti.nii.gz`, the output will be stored in `niftis/ex_nifti_segs/ex_nifti_taskname.nii.gz`.
```markdown
usage: mircat segment [-h] [-t TASK_LIST [TASK_LIST ...]] [-th THREADS] [-d DEVICE] [-c CACHE_NUM] [-s SW_BATCH_SIZE] [-n NUM_WORKERS] niftis

positional arguments:
  niftis                NIfTI file or a text file containing paths to multiple NIfTI files to segment

options:
  -h, --help            show this help message and exit
  -t TASK_LIST [TASK_LIST ...], --task-list TASK_LIST [TASK_LIST ...]
                        List of segmentation tasks to perform. Default = ["total", "tissues", "body"]
  -th THREADS, --threads THREADS
                        Number of threads to use for multi-threaded operations. Default=4
  -d DEVICE, --device DEVICE
                        Device to use. Default: "cuda:0". Can use "cpu" or "cuda:(other N)"
  -c CACHE_NUM, --cache-num CACHE_NUM
                        the number of niftis to cache at once in RAM. Default=10
  -s SW_BATCH_SIZE, --sw-batch-size SW_BATCH_SIZE
                        Batch size for sliding windows. Default: 4
  -n NUM_WORKERS, --num-workers NUM_WORKERS
                        Number of workers to load imaging data. Default=4
```

### Stats
This command allows you to calculate statistics from the segmented nifti files. 
It is recommended to give the same input file that you gave to segment once it has been completed. 
If you only want the output from a specific segmentation task, make sure to pass the `-t` flag to the `stats` command.  
This command will output a statistics `json` file in the segmentations directory. So if you input `example_nifti.nii.gz`, then the output will be in `example_nifti_segs/example_nifti_stats.json`. The output will be ordered in the listed order in `packages/mircat-stats/src/mircat_stats/configs/statistics.py` if all tasks are ran or `--mark-complete` flag is used.  

The possible tasks to be passed to `--task-list` are `total`, `contrast`, `aorta`, and `tissues`.
- `total` will give you the total volume and average intensities for all structures segmented from the `total` segmentation task.
- `contrast` will used a pretrained model to predict the presence of contrast within the CT.
- `aorta` will measure the maximum, middle, and proximal diameters of the ascending, arch, descending and abdominal regions of the aorta using a centerline (if they exist in the image).
- `tissues` will measure the total volume and average intensities for the adipose tissues and skeletal muscle from the `tissues` segmentation task as well as the areas at the L1, L3, and L5 vertebral levels.
  - It will also measure body circumference and area at those vertebral levels.

```markdown
usage: mircat stats [-h] [-t TASK_LIST [TASK_LIST ...]] [-n NUM_WORKERS] [-th THREADS] [-mc] [-g] niftis

positional arguments:
  niftis                NIfTI file or a text file containing paths to multiple NIfTI files to calculate statistics for

options:
  -h, --help            show this help message and exit
  -t TASK_LIST [TASK_LIST ...], --task-list TASK_LIST [TASK_LIST ...]
                        List of statistics tasks to perform. Default = ["total", "contrast", "aorta", "tissues"]
  -n NUM_WORKERS, --num-workers NUM_WORKERS
                        Number of workers to use for multi-process operations. Default=1
  -th THREADS, --threads THREADS
                        Number of threads each worker will use. Default=4
  -mc, --mark-complete  Mark the statistics as complete regardless of stats performed
  -g, --gaussian        Apply a gaussian smoothing to the label segmentations. Will be slower but more precise upon scaling
```

### Update
This command is usually not needed. Only needs to be used to update the format of the NiFTi `header_info.json` file when the `mircat` version changes.
```
usage: mircat update [-h] [-n NUM_WORKERS] [-th THREADS] niftis

positional arguments:
  niftis                Path to NIfTI files

options:
  -h, --help            show this help message and exit
  -n NUM_WORKERS, --num-workers NUM_WORKERS
                        Number of workers
  -th THREADS, --threads THREADS
                        Number of threads
```


