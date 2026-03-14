# Tactile Pad - Proposal


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



## 3. Objectives
- Design and prototype a single functional tactile pin module
- Develop a reliable actuation and holding mechanism for stable pin movement
- Construct and test a small tactile grid
- Develop a software module to convert text input into dot-matrix tactile patterns
- Integrate mechanical, electrical, and software components into a working prototype
- Evaluate system stability, repeatability, and scalability
- Have a final demonstration that can successfully show letters and graphics



## 4. Proposed Solution
The system consists of a top surface with a grid of holes for tactile pins. Underneath, a pin tray houses magnetic-tipped pins. When a specific electromagnet is energized, it attracts or repels the pin, moving it upward. A mechanical slider then shifts to lock the pins in place. First the user input will be processed by a web application which calculates a binary map to send to the pico, which then signals the circuit board to direct power to the corresponding electromagnets.

### 4.1 Project Description
This project proposes a modular refreshable tactile display system composed of three primary layers: a mechanical actuation layer, a hardware control layer, and a software encoding layer. The overall architecture emphasizes modularity, scalability, and energy efficiency to allow future expansion into more complex tactile representations.

The mechanical layer consists of a tactile pin array designed to physically represent binary dot patterns. Each pin is designed to move vertically and remain in position through a mechanical holding or latching mechanism. The system will first validate a single-pin prototype before scaling to a small grid configuration. 

The hardware control layer includes a microcontroller-based system responsible for generating actuation signals. The microcontroller communicates with a driver board that regulates power delivery to the actuators while incorporating safety components such as flyback diodes for inductive load protection.

The software layer converts user text input into a dot-matrix representation compatible with the tactile grid. A lightweight encoding module maps characters to predefined dot patterns and transmits the formatted data to the control system. It will express the data in bitmap to represent the respective dots to be either pushed up or pushed down to present dots and blanks spaces in braille text or braille graphics.


### 4.2 Hardware Components
| Component | Description | Quantity |
|---------|-------------|----------|
| Raspberry Pi Pico W | Main controller | 1 |
| Circuit Driver Board | Directs power | 1 |
| Electromagnets | Pin actuation | per pin|
| PCB | Modulation for each braille letter | per pin |
| Micromagnets | For magnetic actuation | per letter  |
|Solenoids | Pin actuation | per pin |
| Diode | Voltage Control | X |
| Transistor | Power Switch | X |
| Resistor | Voltage Control | X |

-Schematic:

Users input their desired texts/images to an application. The application will then calculate a binary map encoding the pins to be actuated on the physical grid. The application will then send the map to the Raspberry Pi Pico. Pico then sends signals for mechanical actuation.

Candidates for mechanical actuation:

- Electromagnets + Cam: 
  - pico sends signal to circuit board
  - circuit board sends power to corresponding electromagnets to be energized
  - electric field causes magnet in cam to flip, moving the cam
  - cam is asymmetric in shape, moving the pins up
  - once cam is flipped, power is cut from the electromagnets
  - supporters on the sides of the cam holds cam and pin in place
  - to refresh, a signal is sent once again to corresponding
	  electromagnets, flipping the cam once again


- Electromagnets + Locking Plate:
	- pico sends signal to circuit board
	- circuit board sends power to corresponding electromagnets to be energized
	- once electromagnets energized, pins connected to magnets move upwards
	- pins have groves on the sides which then are locked in place by a sliding plate with slightly larger holes to fit in the grooves
  - to refresh the locking plate will slide back to the original position to release all locked pins

- Solenoids:
  - each solenoid connected to the pico by an available pin position
  - pico will signal the solenoid of the respective number placement a charge if pin assigned to solenoid is charged
  - the activated solenoids will either push up  or push down if already in pushed up stance


### 4.3 Software Components
- Libraries / Frameworks: Braille Translation([Touch Map](https://pypi.org/project/touchmap/)), Image Converter
- Communication Protocol: TCP
- Firmware: Micropython
- Data flow: image/text → translate to grid pattern → code for pico to follow → pin representation
- User interface: Frontend(tbd), Backend(tbd), Database(tbd)


## 5. Methodology
1. Requirement analysis - We begin by identifying the core technical risks and functional requirements of the system. Based on the research, the primary challenge lies in reliable pin actuation and holding mechanisms. Therefore, mechanical feasibility is prioritized before software complexity. The system must support stable vertical movement and repeatability.

2. Hardware setup - The hardware development process will proceed incrementally:
- Single Pin Prototype: Design and test a single tactile pin module with a mechanical actuation and holding mechanism.
- Small-Scale Grid Integration: Assemble multiple pin modules into a compact tactile grid.
- Driver Circuit & Power Protection: Design and test driver circuits including flyback diode protection for inductive loads.
3. Software development
- Firmware for pico
- User interface and application logic
- Communication protocols between application and pico
4. Integration and testing - Mechanical, electrical, and software components will be integrated into a unified system. Testing will evaluate:
- Stability of pin movement
- Repeatability of actuation
- Signal timing accuracy
- System power consumption
5. Deployment - A functional prototype of a digital tactile pad will be demonstrated. The system architecture will allow future expansion toward graphical and map-based representations. 


## 6. Timeline
| Phase | Activities | Duration |
|------|------------|----------|
| Phase 1 | Research & Planning | 1-2 weeks |
| Phase 2 | Development | 4-5 weeks |
| Phase 3 | Testing | 2 weeks |
| Phase 4 | Final Deployment | 1 weeks |


## 7. Expected Outcomes
- Functional prototype
  - The system consists of a top surface with a grid of holes for tactile pins. Underneath, a pin tray houses magnetic-tipped pins. When a specific electromagnet is energized, it attracts or repels the pin, moving it upward. A mechanical slider then shifts to lock the pins in place.
- Measurable performance metrics
	- Ability to display letters/shapes (number of how many)
	- Failures (percentage)
	- Fidelity of grid output to user input (percentage)
	- Scalability (based on different areas)
	- Surface area (number of pins produced)
- User or system benefits
  - A functional refreshable tactile grid
  - Stable and repeatable pin actuation mechanism
  - Modular architecture enabling scalability
  - Verified electrical safety and controlled power usage



## 8. Conclusion
This project presents a structured approach to developing a refreshable tactile display. By prioritizing mechanical practicality and incremental integration, the system reduces technical uncertainty while maintaining scalability. The proposed modular architecture ensures that the prototype can serve as a foundation for future expansion into more advanced tactile visualization systems.

## 9. Workload Distribution
Subject to change depending on progress

- Neha Kalakuntla - Software & Hardware
- Aimuan Erhabor - Hardware Prototyping
- Jojo Day - Software & Embedded Software 
- Elise Keller - Hardware Prototyping
- Jiayi Zhang - Software



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
