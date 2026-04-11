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
Blind and visually impaired individuals face significant economic barriers to accessing information, as current assistive tactile displays range in price from $2,000 to over $50,000. This project proposes a refreshable tactile display designed to be an affordable, DIY alternative for sensing images by translating digital text and simple visual representations into physical tactile patterns. Utilizing a audrino nano and an electromagnetic actuation system, the device will feature a grid of pins that can be raised to provide a tactile representation of maps and images. Key technologies include electromagnets for pin movement, a mechanical locking plate for power-efficient position retention, and a driver board for power management. The goal is to create a functional, scalable prototype that exemplifies a lower-cost solution for navigation, education, and entertainment. 

The primary focus of this project is to address the core mechanical challenge of reliable pin actuation. Unlike expensive piezoelectric commercial displays, we plan to use electromagnets to push pins through a magnetic plate and a sliding locking plate to secure them in the "up" position. We will first develop and validate a single tactile pin module capable of stable upward and downward movement with a locking or holding mechanism. A microcontroller-based control system will manage actuation signals, while a lightweight software layer will convert text input into corresponding dot-matrix tactile patterns.

The expected outcome is a functional small-scale pad capable of real-time translation of data to tactile representation. This project hopes to contribute to more affordable and accessible assistive technologies. 



## 3. Project Overview

The Tactile Pad is a low-cost, refreshable tactile display system designed to convert digital text and simple visual information into a physical, touch-readable format. The system aims to provide an accessible alternative to existing high-cost tactile displays by combining electromechanical actuation, embedded control, and lightweight software processing.

At a high level, the device consists of a grid-based tactile surface populated with vertically movable pins. Each pin represents a binary state - raised or lowered, enabling the formation of braille characters and simple graphical patterns. Beneath the surface, an array of actuators controls the movement of individual pins. A mechanical locking mechanism ensures that pins remain in their designated positions without continuous power, improving overall energy efficiency.

The system operates through a multi-layer pipeline. User input, either text or basic images, is first processed by a software application, which converts the input into a binary grid representation corresponding to the tactile layout. This encoded data is transmitted to , which interprets the signal and activates the appropriate actuators via a driver circuit. The actuators then raise or lower pins to render the desired tactile output.

The design emphasizes modularity and scalability. Initial development focuses on validating a single-pin mechanism, followed by expansion to multi-cell Braille units and small grid arrays. This incremental approach reduces risk while establishing a foundation for future enhancements, such as higher-resolution displays and more complex tactile graphics.

Overall, the tactile pad integrates mechanical, electrical, and software components into a cohesive system that demonstrates the feasibility of affordable, scalable tactile interfaces for assistive technology.

### 4.1 Project Description
This project proposes a modular refreshable tactile display system composed of three primary layers: a mechanical actuation layer, a hardware control layer, and a software encoding layer. The overall architecture emphasizes modularity, scalability, and energy efficiency to allow future expansion into more complex tactile representations.

The mechanical layer consists of a tactile pin array designed to physically represent binary dot patterns. Each pin is designed to move vertically and remain in position through a mechanical holding or latching mechanism. The system will first validate a single-pin prototype before scaling to a small grid configuration. 

The hardware control layer includes a microcontroller-based system responsible for generating actuation signals. The microcontroller communicates with a driver board that regulates power delivery to the actuators while incorporating safety components such as flyback diodes for inductive load protection.

The software layer converts user text input into a dot-matrix representation compatible with the tactile grid. A lightweight encoding module maps characters to predefined dot patterns and transmits the formatted data to the control system. It will express the data in bitmap to represent the respective dots to be either pushed up or pushed down to present dots and blanks spaces in braille text or braille graphics.

### 4.2 Hardware Components
| Component | Description | Quantity |
|---------|-------------|----------|
| Audrino Nano | Main controller | 1 |
| Circuit Driver Board | Directs power | 1 |
| Electromagnets | Pin actuation | per pin|
| PCB | Modulation for each braille letter | per pin |
| Micromagnets | For magnetic actuation | per letter  |

-Schematic:

Users input their desired texts/images to an application. The application will then calculate a binary map encoding the pins to be actuated on the physical grid. The application will then send the map to the audrino nano. Nano then sends signals for mechanical actuation.

Mechanical actuation:

- Electromagnets + Cam: 
  - nano sends signal to circuit board
  - circuit board sends power to corresponding electromagnets to be energized
  - electric field causes magnet in cam to flip, moving the cam
  - cam is asymmetric in shape, moving the pins up
  - once cam is flipped, power is cut from the electromagnets
  - supporters on the sides of the cam holds cam and pin in place
  - to refresh, a signal is sent once again to corresponding
	  electromagnets, flipping the cam once again


### 4.3 Software Components
- Libraries / Frameworks: Braille Translation([Touch Map](https://pypi.org/project/touchmap/)), Image Converter
- Communication Protocol: TCP
- Firmware: Micropython
- Data flow: image/text → translate to grid pattern → code for nano to follow → pin representation
- **Image Mapping Module**
  
  The image mapping module allows users to upload images through the web interface and converts them into tactile binary matrices for braille board simulation. 
  - Main functions:
    - Image upload handling through the frontend interface.
    - Automatic resizing based on board size.
    - Grayscale conversion and threshold binarization.
   - Binary tactile matrix generation.
    - Frontend tactile preview display.

    The image mapping module has been integrated into the current frontend, and the workflow has been verified with sample images.

## 5. Progress
We have made significant progress on our software side and significant setup and some progress for our hardware side. Our team has designed a complete UI for translating text to braille. The image mapping feature has been mostly completed with adaptive sizing with binary representation of most image uploads. We have gathered all components to start braille cell module production. We created some solenoids from our own solenoid coiling machine.While waiting for the braille cell parts, we created a functional LED representation instead of a solenoid pin in the meantime. 

### 5.1 Hardware Progress
We have successfully acquired all of the materials for our braille module that is based on Vijay Varada’s Electromechanical Refreshable Braille Tactile Module to at least begin one prototype. 

For electronics, we have braille module PCBs, arduino nano from Brandeis’ automation lab, and PCB evaluation board for multiple module prototyping.  For non-electronics, we have ferrite rods and copper wire for solenoids, tiny magnets and resin-printed braille cell parts, courtesy of Makerlab. 

One of the key parts of the project was to create our own solenoids with the ferrite rods and copper wire, but due to the extreme size of them, we created a coiling machine based off the design Varada used in his original project.
Despite delays, we were able to create two fully coiled solenoids as of this report recording. We are looking forward to creating six in total to test and solder into a full module. 

Due to the lack of braille pins/solenoids to test how it would handle firmware and representing braille characters and image mapping, we have used an LED prototype instead to explore how the product would look like. With resistors, six LEDs, and a raspberry pico; we were able to create a functional braille cell prototype with six pins. We are able to at least convey one braille character with our singular braille prototype.

### 5.2 Software Progress
**Braille Translation and Software Stack**

We implemented a Web app with Flask backend that will use Python to translate text to braille and other features interacting with the Tactile Pad, including the image mapping. The app has a RESTful API that is able to handle image and text uploading. We designed a cohesive user interface for both testing and users with limited vision. 

To assist with testing, we also implemented a simulation of what the braille would look like once translated into text as well as bitstring mapping that can be used for the hardware translation of the braille to the pins.

**Image Mapping Progress**

  The image mapping module is now functional in the current frontend.
  
  Current status:
  - Users can upload images and preview tactile mapping results.
  - Image resizing and threshold conversion are working properly.
  - The module has been tested using sample images.


### 5.3 Current Results
We have a fully functional User Interface that can translate any text to American English braille, and a singular representational braille pin module with LEDs instead of solenoids. LED braille module can fully represent all 6-pin braille characters. The image mapping mechanism is fully functional that can convert compatible images to human-recongizable binary representations but has yet to be expressed upon any available hardware. 

## 6. Challenges and Solutions
**Hardware**

One challenge we had with hardware was producing good quality braille module 3d prints. Based off of Varada’s design, they were too small to be produced consistently by the Makerlab PLA student available printers. After talking with the director of Makerlab, we have access to a Resin 3D printer that has successfully printed high-quality parts necessary for one braille cell.

One significant challenge we had to deal with was designing the coiling machine itself. The CAD design did not match the DC motor we had or even the type of step motor we had available that the CAD was designed for. 

After altering the coiling machine 3D print for the motor, we also had to alter one of the parts that is attached to the motor to spin the rod due to the change. These modifications took weeks and efforts of multiple team members, due to the general unfamiliarity with 3D printing but overall we achieved in a functional solenoid coiling machine. 

The delay in creating solenoids caused a delay for creating a braille prototype. This was a great issue; despite the functionality of the software if there is no hardware. One of our solutions was to have an LED representational display instead until we are able to complete a braille module. This is what we plan to use to see if software and hardware integration works as the ideal hardware scale is not available.

**Modifications**

In order to achieve our goal to create a braille display we also need to design a new PCB module with drivers that can control a matrix of braille cells. The project we are expanding from already has a circuit board which is capable of an 8 braille-cell array. This is extremely helpful, but in order to have a display of cells,many structural elements must be changed. Interpreting the logic for the original PCB was the first challenge, especially because a lot of the choices seemed completely random (unnecessary components and arrangements that seemed inefficient). 

We tried designing a schematic from scratch but as we were researching the reasoning for why certain things/techniques were used, we realized that a lot of it had to do with safety or taking precautions against the board breaking and becoming unusable. Because our team had a great gap in knowledge in electrical engineering and circuit design, we decided to work from the existing board and try to change it as minimally as possible because we know for certain that the existing one works. 

A big challenge we need to deal with is that we have concerns about things that cannot be tested until we already have the board physically in our hands to test. We have done research into how we need to deal with trace resistance, minimising crosstalk, etc. But we do not know if it will be enough in the end and we are trying to reduce that chance by using spacing/height/thinknesses well above the stuff that is calculated with impedance formulas. We know a few things like adding a copper pour to assist with thermal dissipation, and the BAV99 diodes will be kept to reduce spikes in the electromagnetic fields when moving the dots. We also know that the 12V driver running right next to the arduino logic is not ideal, and should add a dedicated bulky capacitor to the ICs to avoid noise coupling.

We still need to determine if the logic for the multiplexing (how the matrix is controlled) will not have timing issues before things are ordered and changes can’t be made. Another concern we had that unexpectedly became a bigger problem was how to eliminate the gaps caused by the vias in the current design with the PCB braille cells. To do this we will add inter-layer of electrical isolation to make certain there is no accidental noise, we will of course be gentle when handling the device, and because this is a proof of concept, we will not delve into how to address issues like how one might fix it if one cell were to break and need repair. 


**Image Mapping**

One challenge was dealing with images with different resolutions and could not be directly mapped to the square tactile board. To overcome this, an automatic resizing mechanism was implemented to normalize uploaded images based on the board resolution.
Another challenge was the frontend structure being changed during development, so the previous image mapping logic no longer fit the new interface structure. We solved this issue by adjusting the image upload and preview logic to match the new frontend structure while maintaining the original image processing flow.


## 7. Updated Plans

With the development of having LED braille cell representations, we are incorporating that development into our project to see what can be done with scalability of the actual braille module and what can’t be completed in the time scope of the budget. Given time constraints we might not get the chance to implement our modifications to our original inspiration project however we have developed our own designs in preparation.
Regarding the power source considerations for a full image display or a braille cell array, we plan to use an outlet source or a rechargeable power battery to distribute the power necessary. It will be less costly for the LED display but it is more necessary once we achieve any multiple braille cell display.

### 7.1 Updated Timeline
| Phase            | Activities                                                                 | Duration     |
|------------------|---------------------------------------------------------------------------|--------------|
| Development      | - solenoid production                                                       |              |
|                  | - assemble at least 1 braille pin module                                   |              |
|                  | - scale LED representation to two - four braille cells                     |              |
|                  | - create 4 by 4 cell LED display for image display                         | 3 weeks      |
| Testing          | - test braille pin module                                                  |              |
|                  | - test software integration with hardware                                  |              |
|                  | - test Wireless and Wired Connection with Tactile Pad                      | < 1 week     |
| Final Deployment | - Assembling the braille and LED matrixes/arrays together in a presentable product | 2 - 4 days   |

### 7.2 Updated Workload Distributions
- Neha Kalakuntla - Hardware
- Aimuan Erhabor - Firmware, Hardware, Prototyping
- Jojo Day - Hardware, Fullstack/Embedded Software 
- Elise Keller -  Fullstack Software
- Jiayi Zhang -  Fullstack Software


## 8. Demo Plan
For our live demo we plan on showcasing all of the features we have implemented including:
- Text to braille actuation on the pad
- Image Conversion to dot representation on LED display
- Refresh capabilities
- Physical model of the tactile visual display (without the matrix working because we might not have the time to wind 96 solenoids)

We will use a sample text or article to display the text to braille conversion for the braille display. 
We may have accompanying slides or text to show how well the display and braille conversion translate the text for audience visibility

Once that sequence is done, we will transfer to the image display presentation with cultivated images that can transfer to the available image display resolution of either 4 by 4 or 8 by 8.
If we do not have a working image display, we can always display the preview to show that we have a working conversion for future features. 


## 9. Contributions
**Jiayi Zhang**
  - Designed and implemented the image-to-tactile mapping module
  - Built image preprocessing functions, including resizing and threshold binarization
  - Added image upload and tactile preview support in the frontend
  - Integrated the module into the updated UI and tested with sample images

**Aimuan Erhabor**
- Assisted with research into materials and methodologies
- Assisted with the development of coiling machine with 3D printing and design revision
- Designed and created LED representation braille module
- Designed firmware to express braille characters through LED module 


**Jojo Day**
- Assisted with research into materials and methodologies
- Assisted with the design revision of coiling machine
- Sourcing hardware materials
- 3D Fabrication of braille modules in collaboration with Makerlab
- Assisted with integrating all components together


**Elise Keller**
- Implemented Braille to Text Translation
- Implemented Visual Simulation of Braille Translation
- Designed Software Stack and implemented Web app 
- Designed functional UI 


**Neha Kalakuntla**
- Assisted with research into materials and methodologies
- Modified schematic, PCB files, and CAD files 
- Assisted with integrating all components together

## 10. Conclusion
We have made significant progress with software development with fully functional braille to text translation and image mapping. However, the hardware development did not result in a fully functional braille pin module prototype at this time but had a functional LED alternative and components for the braille module available. 

Regarding hardware, a few of our challenges are the assembly of the braille pin module, testing and designing firmware of said module, and seeing if scalability of at least four cells is possible. Another challenge would be the design of the multiple character display and  image display of braille cells, and if not possible then, of LED braille cells. With software mainly complete, challenges involving that would be integrating with the available hardware and making it more accessible for blind people.

Our current plan is to design an image display matrix with LEDs if we are not capable of delivering with all of the goals for the braille. Our most reasonable goal is to create a workable 4 - 8 character braille refreshable tactile display. We are continuing solenoid production in order to begin braille cell production . Once we have a successful prototype, we will work on the greater challenge of scalability with our limited knowledge of circuit design.


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

