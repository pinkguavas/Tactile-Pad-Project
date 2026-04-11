# Tactile Pad - Progress


## 1. Team Information
- **Team Name:** TechTile
- **Team Members:**
  - Neha Kalakuntla (nehakalakuntla@brandeis.edu)
  - Aimuan Erhabor (aimuanerhabor@brandeis.edu)
  - Jojo Day (jojoday@brandeis.edu)
  - Elise Keller (elisekeller@brandeis.edu)
  - Jiayi Zhang (jzhang1166@brandeis.edu)
- **Github Repository:** https://github.com/sd1166/Tactile-Pad-Project


## 2. Abstract
Blind and visually impaired individuals face significant economic barriers to accessing information, as current assistive tactile displays range in price from $2,000 to over $50,000. This project proposes a refreshable tactile display designed to be an affordable, DIY alternative for sensing images by translating digital text and simple visual representations into physical tactile patterns. Utilizing a Raspberry Pi Pico and an electromagnetic actuation system, the device will feature a grid of pins that can be raised to provide a tactile representation of maps and images. Key technologies include electromagnets for pin movement, a mechanical locking plate for power-efficient position retention, and a driver board for power management. The goal is to create a functional, scalable prototype that exemplifies a lower-cost solution for navigation, education, and entertainment. 

The primary focus of this project is to address the core mechanical challenge of reliable pin actuation. Unlike expensive piezoelectric commercial displays, we plan to use electromagnets to push pins through a magnetic plate and a sliding locking plate to secure them in the "up" position. We will first develop and validate a single tactile pin module capable of stable upward and downward movement with a locking or holding mechanism. A microcontroller-based control system will manage actuation signals, while a lightweight software layer will convert text input into corresponding dot-matrix tactile patterns.

The expected outcome is a functional small-scale pad capable of real-time translation of data to tactile representation. This project hopes to contribute to more affordable and accessible assistive technologies. 


## 3. Project Overview

### 3.1 Project Description
High-level description of the system.
As detailed as possible.

### 3.2 Hardware Components

### 3.3 Software Components
- **Image Mapping Module**
  
  The image mapping module allows users to upload images through the web interface and converts them into tactile binary matrices for braille board simulation. 
  - Main functions:
    - Image upload handling through the frontend interface.
    - Automatic resizing based on board size.
    - Grayscale conversion and threshold binarization.
    - Binary tactile matrix generation.
    - Frontend tactile preview display.

    The image mapping module has been integrated into the current frontend, and the workflow has been verified with sample images.

## 4. Progress

### 4.1 Hardware Progress
- Braille Modules
- Circuit Boards
- Electromagents

### 4.2 Software Progress
- **UI**
- **Text to Braille Mapping defined**

- **Image Mapping Progress**

  The image mapping module is now functional in the current frontend.
  
  - Current status:
    - Users can upload images and preview tactile mapping results.
    - Image resizing and threshold conversion are working properly.
    - The module has been tested using sample images.

### 4.3 Current Results
- The current system can generate tactile binary matrices from uploaded images and display the output in the browser.

## 5. Challenges and Solutions
- **Updating preexisting circuit board and braille module layout to our modificaitons**
- **Image Mapping Module**

  - Challenge 1: Uploaded images had different resolutions and could not be directly mapped to the tactile board.
  - Solution: An automatic resizing machanism was implemented to normalize uploaded images based on the board resolution before thresholding.
  - Challenge 2: The frontend structure was changed during development, so the previous image mapping logic no longer fit the new interface structure.
  - Solution: The image upload and preview logic were adjusted to match the new frontend structure while keeping the original image processing flow.

## 6. Updated Plans

### 6.1 Updated Timeline
As detail as possible.
| Phase | Activities | Duration |
|------|------------|----------|

### 6.2 Updated Workload Distributions
- **Image Mapping Module**
  - Current contribution:
    - Image upload and tactile mapping pipeline development.
    - Frontend image integration and testing.
  
  - Remaining tasks:
    - Pico communication integration for image output.
    - Real hardware testing.

## 7. Demo Plan
For the demo, our team presented the current web interface and software workflow. Users were able to upload images, and the system generated binary tactile patterns with browser-based preview.

## 8. Contributions
- **Jiayi Zhang**
  - Designed and implemented the image-to-tactile mapping module.
  - Built image preprocessing functions, including resizing and threshold binariztion.
  - Added image upload and tactile preview support in the frontend.
  - Integrated the module into the updated UI and tested with sample images.

## 9. Conclusion
Brief reflection on current status, remaining challenges and plans.

## References
- Inspiration Project: [Electromechanical Refreshable Braille Module](https://hackaday.io/project/191181-electromechanical-refreshable-braille-module)
- Research papers
  - [MagnePins](https://dl.acm.org/doi/10.1145/3746059.3747692)
  - [Shape Clip](https://dl.acm.org/doi/10.1145/2702123.2702599)
  - [Haptic Edge Display for Mobile Tactile Interaction](https://dl.acm.org/doi/abs/10.1145/2858036.2858264)
  - [Tilt Displays](https://dl.acm.org/doi/10.1145/2371574.2371600)
  - [MagTics](https://dl.acm.org/doi/10.1145/3126594.3126609)
- On the market:
  - [Dot Pad X](https://www.dotincorp.com/en/product/dotpadx)
  - [Monarch](https://www.aph.org/product/monarch/)
  - [Braille Pad En](https://www.4blind.com/braillepad-en)
  - [Graphiti](http://www.orbitresearch.com/product/graphiti/)

