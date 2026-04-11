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
Provide a concise summary (150–250 words) describing:
- your project
- progress
- future plans


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
Progress Summary

### 4.1 Hardware Progress

### 4.2 Software Progress
- **Image Mapping Progress**

  The image mapping module is now functional in the current frontend.
  
  - Current status:
    - Users can upload images and preview tactile mapping results.
    - Image resizing and threshold conversion are working properly.
    - The module has been tested using sample images.

### 4.3 Current Results
- The current system can generate tactile binary matrices from uploaded images and display the output in the browser.

## 5. Challenges and Solutions
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
- Datasheets
- Research papers
- Projects you get ideas from - GitHub repositories
- etc.

