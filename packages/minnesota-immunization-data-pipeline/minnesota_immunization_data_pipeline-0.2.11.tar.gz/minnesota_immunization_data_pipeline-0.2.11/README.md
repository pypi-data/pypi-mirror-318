<h1 align="center">🩺⚙️ Immunization Records Pipeline 🩺⚙️</h1>

<h4 align="center">A data pipeline that minimizes manual effort when extracting immunization records from the Minnesota Department of Health, transforming them, and loading them into the student information system, Infinite Campus.</h4>

## Running the AISR to Infinite Campus CSV Transformation
1. Make sure you have Python 3 and Pip installed on your computer. Run the following commands in the command line to check:
   ```bash
   python --version

   pip --version
   ```
1. Open your terminal and paste the command below:

   ```bash
   pip install minnesota-immunization-data-pipeline

   # If you get an error about 'pip not found', just replace pip with pip3.
   ```
1. Then you can run the project with 
   ```bash
   minnesota-immunization-data-pipeline --input_folder "<input_folder_path>" --output_folder "<output_folder_path>"
   ```

## Developer Setup
Developer setup is easy with Dev Containers!
1. [Download the code locally](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
1. Ensure [VS Code](https://code.visualstudio.com/) is installed
1. Open the repository in VS Code
1. Follow the tutorial [here](https://code.visualstudio.com/docs/devcontainers/tutorial) to set up Dev Containers.
1. Run the command (View->Command Palette) `Dev Containers: Reopen in Container`
   - This may take several minutes the first time