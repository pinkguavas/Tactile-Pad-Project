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
Provide a concise summary (150–250 words) describing:
- The problem you are addressing  
- Brief description about your proposed project
- Key technologies involved  
- Expected outcomes or impact

Visually impaired individuals often face significant barriers when accessing visual information such as text, graphs, and spatial layouts. Existing refreshable tactile displays and braille devices are typically expensive, making them inaccessible to many users. Our project proposes the design and development of a low cost, modular refreshable tactile display capable of translating digital text and simple visual representations into physical tactile patterns.

The primary focus of this project is to address the core mechanical challenge of reliable pin actuation. We will first develop and validate a single tactile pin module capable of stable upward and downward movement with a locking or holding mechanism. After confirming mechanical feasibility, we will implement a small-scale row-scanning architecture to construct a tactile grid (e.g., 8×8). A microcontroller-based control system will manage actuation signals, while a lightweight software layer will convert text input into corresponding dot-matrix tactile patterns.

The expected outcome is a functional small-scale tactile grid (e.g., 8×8) capable of real-time text-to-tactile conversion. This project contributes to more affordable and accessible assistive technologies.

## 3. Objectives
The main objectives of this project are:
- List the specific goals of the project

- Design and prototype a single functional tactile pin module
- Develop a reliable actuation and holding mechanism for stable pin movement
- Construct and test a small tactile grid (e.g., 8×8)
- Develop a software module to convert text input into dot-matrix tactile patterns
- Integrate mechanical, electrical, and software components into a working prototype
- Evaluate system stability, repeatability, and scalability

## 4. Proposed Solution
Describe the details about your project

### 4.1 Project Description
High-level description of the system.
As detailed as possible.

This project proposes a modular refreshable tactile display system composed of three primary layers: a mechanical actuation layer, a hardware control layer, and a software encoding layer.

The mechanical layer consists of a tactile pin array designed to physically represent binary dot patterns. Each pin is designed to move vertically and remain in position through a mechanical holding or latching mechanism. The system will first validate a single-pin prototype before scaling to a small grid configuration (e.g., 8×8). A row-scanning mechanism will be implemented to efficiently control multiple pins while minimizing actuator count and power consumption.

The hardware control layer includes a microcontroller-based system responsible for generating actuation signals. The microcontroller communicates with a driver circuit that regulates power delivery to the actuators while incorporating safety components such as flyback diodes for inductive load protection.

The software layer converts user text input into a dot-matrix representation compatible with the tactile grid. A lightweight encoding module maps characters to predefined dot patterns and transmits the formatted data to the control system.

The overall architecture emphasizes modularity, scalability, and energy efficiency to allow future expansion into more complex tactile representations.

### 4.2 Hardware Components
| Component | Description | Quantity |
|---------|-------------|----------|
| Raspberry Pi pico w | Main controller | 1 |
| Sensor / Module | Purpose | X |
| Power Supply | Rating | 1 |

- Schematic 

### 4.3 Software Components
- Libraries / Frameworks
- Communication Protocols (e.g., I2C, SPI, MQTT)
- Software structure
- Data flow
- User interface


## 5. Methodology
Explain how the project will be developed:
1. Requirement analysis  
2. Hardware setup  
3. Software development  
4. Integration and testing  
5. Deployment  


## 6. Timeline
As detail as possible.
| Phase | Activities | Duration |
|------|------------|----------|
| Phase 1 | Research & Planning | X weeks |
| Phase 2 | Development | X weeks |
| Phase 3 | Testing | X weeks |
| Phase 4 | Final Deployment | X weeks |


## 7. Expected Outcomes
- Functional prototype
- Measurable performance metrics
- User or system benefits


## 8. Conclusion
Summarize the project’s value and feasibility.


## References
- Datasheets
- Research papers
- Projects you get ideas from - GitHub repositories

