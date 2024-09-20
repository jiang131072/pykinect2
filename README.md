# Pykinect2

Enables writing Kinect applications, games, and experiences using Python.  Inspired by the original [PyKinect project on CodePlex](http://pytools.codeplex.com/wikipage?title=PyKinect).

Only color, depth, body and body index frames are supported in this version. PyKinectBodyGame is a sample game. It demonstrates how to use Kinect color and body frames.

> [!NOTE]
> This is a maintained version of Microsoft's Pykinect2, with new versinon numpy and pygame compatibility.
> But I don't have the source typelib, so no new feature could be added.

## Usage

Since Kinect SDK only supports Windows, Pykinect2 will also only support Windows platform. Pykinect2 use `comtypes`'s IUnknown to do FFI works.

Examples are written using `pygame`

## Installation

TL;DR

```bash
pip install pykinect2
```

or use other environment and project manager
