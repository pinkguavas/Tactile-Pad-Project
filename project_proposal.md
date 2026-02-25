# Tactile Pad - Proposal


## 1. Team Information
- **Team Name:** N/A
- **Team Members:**
  - Neha Kalakuntla (nehakalakuntla@brandeis.edu)
  - Aimuan Erhabor (aimuanerhabor@brandeis.edu)
  - Jojo Day (jojoday@brandeis.edu)
  - Elise Keller (elisekeller@brandeis.edu)
  - Jiayi Zhang (jzhang1166@brandeis.edu)
- **Github Repository:** https://github.com/sd1166/Tactile-Pad-Project


## 2. Abstract
Visually impaired individuals often face significant barriers when accessing visual information such as text, graphs, and spatial layouts. Existing refreshable tactile displays and braille devices are typically expensive, making them inaccessible to many users. Our project proposes the design and development of a low cost, modular refreshable tactile display capable of translating digital text and simple visual representations into physical tactile patterns.

The primary focus of this project is to address the core mechanical challenge of reliable pin actuation. We will first develop and validate a single tactile pin module capable of stable upward and downward movement with a locking or holding mechanism. After confirming mechanical feasibility, we will implement a small-scale row-scanning architecture to construct a tactile grid. A microcontroller-based control system will manage actuation signals, while a lightweight software layer will convert text input into corresponding dot-matrix tactile patterns.

The expected outcome is a functional small-scale pad capable of real-time translation of data to tactile representation. This project hopes to contribute to more affordable and accessible assistive technologies.


## 3. Objectives
- Design and prototype a single functional tactile pin module
- Develop a reliable actuation and holding mechanism for stable pin movement
- Construct and test a small tactile grid
- Develop a software module to convert text input into dot-matrix tactile patterns
- Integrate mechanical, electrical, and software components into a working prototype
- Evaluate system stability, repeatability, and scalability


## 4. Proposed Solution

### 4.1 Project Description
This project proposes a modular refreshable tactile display system composed of three primary layers: a mechanical actuation layer, a hardware control layer, and a software encoding layer.

The mechanical layer consists of a tactile pin array designed to physically represent binary dot patterns. Each pin is designed to move vertically and remain in position through a mechanical holding or latching mechanism. The system will first validate a single-pin prototype before scaling to a small grid configuration.

The hardware control layer includes a microcontroller-based system responsible for generating actuation signals. The microcontroller communicates with a driver board that regulates power delivery to the actuators while incorporating safety components such as flyback diodes for inductive load protection.

The software layer converts user text input into a dot-matrix representation compatible with the tactile grid. A lightweight encoding module maps characters to predefined dot patterns and transmits the formatted data to the control system.

The overall architecture emphasizes modularity, scalability, and energy efficiency to allow future expansion into more complex tactile representations.

### 4.2 Hardware Components
| Component | Description | Quantity |
|---------|-------------|----------|
| Raspberry Pi Pico W | Main controller | 1 |
| Driver Board | Directs Power | 1 |
| Electromagnets | Braille Dot Actuation | X |

### 4.3 Software Components
- Libraries / Frameworks
- Communication Protocols
- Firmware
- User interface


## 5. Methodology
1. Requirement analysis
We begin by identifying the core technical risks and functional requirements of the system. Based on the research, the primary challenge lies in reliable pin actuation and holding mechanisms. Therefore, mechanical feasibility is prioritized before software complexity. The system must support stable vertical movement and repeatability.
2. Hardware setup
The hardware development process will proceed incrementally:
- Single Pin Prototype: Design and test a single tactile pin module with a mechanical actuation and holding mechanism.
- Small-Scale Grid Integration: Assemble multiple pin modules into a compact tactile grid.
- Driver Circuit & Power Protection: Design and test driver circuits including flyback diode protection for inductive loads.
3. Software development
- Firmware for pico
- User interface and application logic
- Communication protocols between application and pico
4. Integration and testing
Mechanical, electrical, and software components will be integrated into a unified system. Testing will evaluate:
- Stability of pin movement
- Repeatability of actuation
- Signal timing accuracy
- System power consumption
5. Deployment
A functional prototype of a digital tactile pad will be demonstrated. The system architecture will allow future expansion toward graphical and map-based representations. 


## 6. Timeline
| Phase | Activities | Duration |
|------|------------|----------|
| Phase 1 | Research & Planning | 2 weeks |
| Phase 2 | Development | 6 weeks |
| Phase 3 | Testing | 3 weeks |
| Phase 4 | Final Deployment | 1 weeks |


## 7. Expected Outcomes
- A functional refreshable tactile grid
- Stable and repeatable pin actuation mechanism
- Modular architecture enabling scalability
- Verified electrical safety and controlled power usage


## 8. Conclusion
This project presents a structured approach to developing a refreshable tactile display. By prioritizing mechanical feasibility and incremental integration, the system reduces technical uncertainty while maintaining scalability. The proposed modular architecture ensures that the prototype can serve as a foundation for future expansion into more advanced tactile visualization systems.


## References
- Research papers
  - [MagnePins](https://dl.acm.org/doi/10.1145/3746059.3747692)
- Prior Works:
  - [Electromechanical Refreshable Braille Module](https://hackaday.io/project/191181-electromechanical-refreshable-braille-module)
  - [Dot Pad X](https://www.dotincorp.com/en/product/dotpadx)