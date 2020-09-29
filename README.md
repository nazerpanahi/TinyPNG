# TinyPNG

## Prerequisites
  - Python 3.6.9
  - Tinify Library
  - Requests Library

## Introduction
  A simple Image Editor app using TinyPNG API. You can simply resize and compress your images.

## UP and Running
  * In the terminal run the command below to install all python dependencies:
  ```bash
    pip install -r requirements.txt
  ```
  * You can use this main code to resize an image:
  ```python
    import resize

    src = input('Please enter the source directory: ')
    dst = input('Please enter the destination directory: ')
    w = int(float(input('Please enter the width: ')))
    h = int(float(input('Please enter the height: ')))
    api = input('Please enter the TinyPNG API Key: ')
    method = input('Please enter the resizing method: \n1.scale\t2.fit\t3.cover\t4.thumb ')
    resize.resize(api, src, dst, w, h, method)
  ```
  * You can use this main code to compress an image:
  
  ```python
    from tiny import tiny
    
    src = input('Please enter the source directory: ')
    dst = input('Please enter the destination directory: ')
    api = input('Please enter the TinyPNG API Key: ')
    level = int(float(input('Please enter the Level of compression: ')))
    resize.tiny(api, src, dst, level)
  ```
