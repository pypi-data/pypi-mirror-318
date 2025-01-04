# Nauscopia

[![Codeberg][badge-codeberg]][project-codeberg]
[![DOI][badge-doi]][project-doi]

[![Release Notes][badge-release-notes]][project-release-notes]
[![CI][badge-ci]][project-ci]
[![Downloads per month][badge-downloads-per-month]][project-downloads]

[![Package version][badge-package-version]][project-pypi]
[![License][badge-license]][project-license]
[![Status][badge-status]][project-pypi]
[![Supported Python versions][badge-python-versions]][project-pypi]

» [Documentation]
| [Changelog]
| [PyPI]
| [Issues]
| [Source code]
| [License]

## About

A little research project for exploring object detection and tracking
in maritime environments using computer vision.

## Idea

The software builds upon and remixes a wide array of outstanding work by
the CV, ML, and SAR communities, intending to support those in bundling
and shipping working code to PyPI and conda-forge, and into OCI images,
who are not used to it.

The idea is to improve usability for automation procedures in both ad hoc
and server operations. By enabling users to just play around with the
technologies and ingredients easily, and in different environments,
it intends to improve general adoption, in the spirit of [FOSS], [RORO],
[KISS], and [DWIM].

## Documentation

Please visit the Nauscopia handbook to learn about [installation]
and [usage] details.

## Synopsis

Install system-wide.
```shell
pipx install nauscopia
```
```shell
nauscopia detect --input="/path/to/sarcam_2024-03-02_12-35-50.mp4"
```
Alternatively, use the [OCI image][Nauscopia @ Codeberg Container Registry]
to run the program in a container, for example using Docker, Podman, or
Kubernetes.
```shell
docker run --rm -it codeberg.org/sarcam/nauscopia:latest nauscopia --version
```

## What's Inside

Hardware- and ROS-framework independent code fragments of the [SARCAM detector
subsystem], wrapped using a bit of adapter interfaces and glue code.

### Features

- **Tasks:** To process video streams of maritime sceneries in real time,
  applying tasks like image stabilization, horizon detection, succeeded
  by region-of-interest detection and tracking.

- **CLI:** A DWIM-like CLI interface wrapping around the Python routines,
  to support daily data wrangling exercises, both ad hoc and for automation
  purposes.

- **OCI:** The project provides OCI images per Codeberg Container Registry,
  both for releases and PR builds.

- **QA:** End-to-end software test cases on real and synthesized data,
  including a CI/CD configuration.

- **Tools:** Modern project management and packaging, already advertising
  to use `uv` and `ruff` across the board.

- **Usability:** Python API and CLI interfaces to all relevant subsystems,
  in order to encourage ad hoc use and exploration, because it is just one
  `pip install ...` away. No strict requirements on ROS or Gtk.

### Technologies

- **NumPy** is the fundamental package for scientific computing with Python. (2015)

- **Stone Soup** is a software framework for the development and testing of
  tracking and state estimation algorithms. (2017)

- **OpenCV** (Open Source Computer Vision Library) is a library of programming
  functions mainly for real-time computer vision. (2000)

- Pyramid Scene Parsing Network (**PSPNet**), ranked 1st place in ImageNet Scene
  Parsing Challenge 2016, is about semantic segmentation / scene parsing.
  It has been used for horizon detection in maritime images (2018),
  oceanic eddy detection (2021), and for underwater fish classification (2023).   

- The **OpenMMLab** framework provides open-source computer vision
  algorithms based on deep learning. (2018)

- **YOLO** seems to be all over the place, and Ultralytics provides an excellent
  Python API. (2024)

## Status

This is a pre-alpha software package, mostly remixing code from workbenches of
others.

In order to make existing and proven code more accessible to the community, the
project aims to wrap it into an easily consumable integrated package which
includes interface code to use it both as a program, server, and library,
within ROS environments, but also beyond.

Contributions are very much welcome. This is just a playground anyway,
so please don't be shy to join us, we appreciate all kinds of support.

## Prior Art

Standing on the shoulders of NumPy, OpenCV, Stone Soup, Deep Learning, all the
math behind, and [@flova] and [@julled], who pulled it all together.
- [Object Tracking @ SARCAM]
- [Image Stabilizer @ SARCAM] (OpenCV, NumPy)
- [Horizon Detector @ SARCAM] (OpenCV, NumPy)
- [ROI Boat Detector @ SARCAM (OpenCV, NumPy)]
- [ROI Boat Detector @ SARCAM (OpenCV, YOLO)]
- [ROI Boat Tracker @ SARCAM (Stone Soup, NumPy)]
- [Frame Extractor @ SARCAM]

## Project Information

### Acknowledgements
Kudos to the authors of all the many software components this library is
inheriting from and building upon.

### Contributing
The `nauscopia` package is an open source project, and is
[managed on Codeberg]. We appreciate contributions of any kind.

### License
The project uses the AGPL license, like other projects where it is building
upon and deriving from.

### Etymology
> [nauscopy]: The ability to sight land or ships at a distance. ([1], [2], [3], [4]).

[1]: https://www.amusingplanet.com/2020/09/etienne-bottineau-and-lost-art-of.html
[2]: https://www.smithsonianmag.com/history/naval-gazing-the-enigma-of-etienne-bottineau-104350154/
[3]: https://www.faena.com/aleph/nauscopie-the-art-of-detecting-ships-on-the-horizon-at-impossible-distances
[4]: https://es.wikipedia.org/wiki/Nauscopia
[@flova]: https://gitlab.com/flova
[@julled]: https://gitlab.com/julled
[DWIM]: https://en.wikipedia.org/wiki/DWIM
[FOSS]: https://en.wikipedia.org/wiki/FOSS
[Frame Extractor @ SARCAM]: https://gitlab.com/sar-eye/HorizonScanner/-/blob/master/labeling_processing/data_extraction/extract_frames.py
[Horizon Detector @ SARCAM]: https://gitlab.com/sar-eye/HorizonScanner/-/blob/master/sarcam_detector/src/horizon_scanner/modules/horizon_algorithms.py
[Image Stabilizer @ SARCAM]: https://gitlab.com/sar-eye/HorizonScanner/-/blob/master/sarcam_detector/src/horizon_scanner/modules/image_stabilizer.py
[installation]: https://nauscopia.readthedocs.io/install/
[KISS]: https://en.wikipedia.org/wiki/KISS_principle
[managed on Codeberg]: https://codeberg.org/sarcam/nauscopia
[nauscopy]: https://www.thefreedictionary.com/nauscopy
[Nauscopia @ Codeberg Container Registry]: https://codeberg.org/sarcam/-/packages/container/nauscopia
[Nauscopia Handbook]: https://codeberg.org/sarcam/nauscopia/src/branch/main/docs/index.md
[Object Tracking @ SARCAM]: https://gitlab.com/sar-eye/HorizonScanner/-/issues/16
[ROI Boat Detector @ SARCAM (OpenCV, NumPy)]: https://gitlab.com/sar-eye/HorizonScanner/-/blob/master/sarcam_detector/src/horizon_scanner/modules/boat_detector.py
[ROI Boat Detector @ SARCAM (OpenCV, YOLO)]: https://gitlab.com/sar-eye/HorizonScanner/-/issues/89
[ROI Boat Tracker @ SARCAM (Stone Soup, NumPy)]: https://gitlab.com/sar-eye/HorizonScanner/-/blob/master/sarcam_detector/src/horizon_scanner/modules/boat_tracker.py
[RORO]: https://en.wikipedia.org/wiki/Release_early,_release_often
[SARCAM detector subsystem]: https://gitlab.com/sar-eye/HorizonScanner/-/tree/master/sarcam_detector/src/horizon_scanner/modules
[usage]: https://nauscopia.readthedocs.io/usage/


[Changelog]: https://codeberg.org/sarcam/nauscopia/src/branch/main/CHANGES.md
[Documentation]: https://sarcam.flova.de/
[Issues]: https://codeberg.org/sarcam/nauscopia/issues
[License]: https://codeberg.org/sarcam/nauscopia/src/branch/main/LICENSE
[PyPI]: https://pypi.org/project/nauscopia/
[Source code]: https://codeberg.org/sarcam/nauscopia

[badge-ci]: https://ci.codeberg.org/api/badges/14031/status.svg
[badge-codeberg]: https://img.shields.io/badge/Codeberg-2185D0?logo=codeberg&logoColor=fff
[badge-doi]: https://zenodo.org/badge/DOI/10.5281/zenodo.14597602.svg
[badge-downloads-per-month]: https://pepy.tech/badge/nauscopia/month
[badge-license]: https://img.shields.io/pypi/l/nauscopia
[badge-package-version]: https://img.shields.io/pypi/v/nauscopia.svg
[badge-python-versions]: https://img.shields.io/pypi/pyversions/nauscopia.svg
[badge-release-notes]: https://img.shields.io/gitea/v/release/sarcam/nauscopia?gitea_url=https://codeberg.org/&label=Release+Notes
[badge-status]: https://img.shields.io/pypi/status/nauscopia.svg
[project-ci]: https://ci.codeberg.org/repos/14031
[project-codeberg]: https://docs.codeberg.org/
[project-doi]: https://doi.org/10.5281/zenodo.14597602
[project-downloads]: https://pepy.tech/project/nauscopia/
[project-license]: https://codeberg.org/sarcam/nauscopia/src/branch/main/LICENSE
[project-pypi]: https://pypi.org/project/nauscopia
[project-release-notes]: https://codeberg.org/sarcam/nauscopia/releases
