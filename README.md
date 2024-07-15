# Automated-Storyboard-Synthesis-Digital-Advertisin

## Overviw
This project uses smart computer techniques to automatically turn simple text descriptions into detailed visual storyboards for ads. This innovative approach has the potential to streamline the ad creation process, making it quicker, cheaper, and more efficient.

## Business Objective
The business objective of this challenge, as defined by Adludio, is to leverage machine learning, image and text generation, and LLM-based agents to automate the storyboard creation process. This automation aims to expedite the ad creation process, reduce turnaround time, and enhance the conceptualization of digital campaigns.


## Data
The data used was a collection of real-world advertising data from Adludio, a leading mobile advertising platform. This dataset includes:

* **Assets Folder**: Contains images used in various ad creatives, organized into subfolders for each project. Key images like 'landing' (initial) and 'endframe' (final) are included.

* **Sample Concepts (JSON)**: Outlines creative concepts with frame-by-frame breakdowns, explanations, and asset suggestions.

* **Storyboard Examples**: Provides sample storyboards showcasing different composition and design approaches used by Adludio.

* **Performance Data (CSV)**: Includes engagement rate (ER) and click-through rate (CTR) data for a set of ads, potentially allowing you to analyze the effectiveness of different creative elements.

## Project Structure
The project is structured as follows:

- `notebooks/`: Contains Jupyter notebooks for data exploration, analysis, and model development.
- `data/`: Contains the dataset used in the project.
- `models/`: Contains trained models and model artifacts.
- `src/`: Contains source code for the project.
- `requirements.txt`: Contains the required dependencies for the project.

## Getting Started
1. **Prerequisites:**
   - Docker and Docker Compose
   - Python 3.9+ (with required dependencies: see `requirements.txt`)

2. **Installation:**
    - Clone the repository you just forked using `git clone`
    ```bash
    git clone git@github.com:hillaryke/Automated-Storyboard-Synthesis-Digital-Advertising.git
    ```
    - Change directory to the project root
    ```bash
    cd Automated-Storyboard-Synthesis-Digital-Advertising
    ```
3. **Environment Setup:**
    - Create a virtual environment
    ```bash
    python3 -m venv venv
    ```
    - Activate the virtual environment
    ```bash
    source venv/bin/activate
    ```
    - Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
## Usage
The code and implementation can be explored in the notebooks provided in the `notebooks` directory.

## Contributors
- [Hillary Kipkemoi](https://github.com/hillaryke)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
