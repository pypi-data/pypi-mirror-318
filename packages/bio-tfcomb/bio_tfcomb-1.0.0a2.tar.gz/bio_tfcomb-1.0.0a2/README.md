[![Documentation Status](https://readthedocs.org/projects/tfcomb/badge/?version=latest)](https://tfcomb.readthedocs.io/en/latest/)
[![PyPI](https://img.shields.io/pypi/v/bio-tfcomb.svg)](https://pypi.org/project/bio-tfcomb)
[![Downloads](https://static.pepy.tech/badge/bio-tfcomb)](https://pepy.tech/project/bio-tfcomb)


# TFcomb
TFcomb is a computational tool for identifying reprogramming transcription factors (TF) and TF combinations. The overview framework is as below.

## Overview

We modeled the task of finding reprogramming TFs and their combinations as an inverse problem to enable searching for answers in very high dimensional space, and used Tikhonov regularization to guarantee the generalization ability of solutions. For the coefficient matrix of the model, we designed a graph attention network to augment gene regulatory networks built with single-cell RNA-seq and ATAC-seq data. Benchmarking experiments on data of human embryonic stem cells demonstrated superior performance of TFcomb against existing methods for identifying individual TFs.

<p align="center">
  <img src="https://raw.githubusercontent.com/Chen-Li-17/TFcomb/main/inst/fig1.png" width=100%>
</p>

<!-- <p align="center">
  <img src="https://raw.githubusercontent.com/Chen-Li-17/TFcomb/main/inst/overview.png" width=100%>
</p> -->

## Documents and Tutorials

The documents and tutorials of TFcomb are available through the link below.

[TFcomb Tutorial](https://tfcomb.readthedocs.io/en/latest/)

## News
- 01/03/2025: We released TFcomb version 1.0.0. We provided a detailed document describing each step.

## Citation
Wait for our official manuscript...