# BetaBot

An autonomous robot navigation system for climbing gyms, combining real-time hold detection with optimal pathfinding.

## Overview

BetaBot uses a YOLOv8 object detection model to identify climbing holds from camera input, then applies A* pathfinding to compute the optimal route from a start node to an end node across the detected holds.

## Architecture

- **Detection** — YOLOv8 model trained on a custom dataset collected across climbing gyms, identifying climbing holds in real time using OpenCV
- **Pathfinding** — A* algorithm computes the optimal route between holds from a defined start node to end node
- **Integration** — detection outputs feed into the pathfinding module to plan traversable routes across live or static input

## Results

- **74.1% mAP** on held-out validation set (evaluated via Roboflow)
- Custom dataset collected from real climbing gym environments

## Tech Stack

- Python
- YOLOv8 (Ultralytics)
- OpenCV

## Status

Detection pipeline and A* pathfinding implemented. Route planning integration and visualisation in progress.

## Setup

```bash
git clone https://github.com/Silloh23/Betabot.git
cd betabot
pip install -r requirements.txt
```