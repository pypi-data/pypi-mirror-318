# <img src="https://gitlab.com/alex-carvalho-dockeration/doimbu/-/raw/master/img/doimbu.png" alt="doimbu" width="30" style="vertical-align: middle;"> | doimbu - Docker Image Builder  

Lightweight tool for docker image creation with multiple variants.  

<a href="https://gitlab.com/alex-carvalho-dockeration/doimbu"><img src="https://gitlab.com/alex-carvalho-dockeration/doimbu/-/raw/master/img/doimbu.png" alt="doimbu" width="720" style="horiz-align: center;"></a>


## Quick summary  

This project has two main goals:  
- prevent typing long dokcer commands to create docker images  
- build all image variants in single run  
    (optionally pass a param specifying a single image variant to build)  

Every image variant is a Dockerfile placed inside subdir of `variants/`.  


## Table of contents

- [Dependencies](#dependencies)
- [Image Tag Pattern](#image-tag-pattern)
<!--
- [Usage](#usage)
- [How to run tests](#how-to-run-tests)
-->
- [Contributing](#contributing)
- [Contact](#contact)
## Dependencies

Required installed software:  
<sup>(not covered in these instructions)</sup>  

- docker 27.3.1+
- python 3.12.7+
- poetry 1.8.4+ (optional)

<sup>*(developement and testing versions, it may be compatible with previous versions)*</sup>  


## Image Tag Pattern

`[root/tag(file_content)]-[variants/dir_name]`  

Example:  
`root/tag` content:  
```bash
0.1.0
```
Dockerfile location:  
`variants/noble/Dockerfile`

resulting dorcker image tags:  
- `0.1.0-noble`  

<!--
## Usage

To run the project, use the following command:

```bash
python somthing.py
```

## How to run tests

To execute the tests, execute the following command:  

```
pytest
```
-->


## Contributing

Contributing instructions can be found [here](CONTRIBUTING.md).

## Contact

alex carvalho - [linkedin.com/in/alex-carvalho-big-data](https://www.linkedin.com/in/alex-carvalho-big-data/)

