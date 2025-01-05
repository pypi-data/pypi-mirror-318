# Deep Experiment Manager

Deep Experiment Manager is a flexible and modular framework for training, testing, and managing deep learning experiments in PyTorch. It provides a clear structure for organizing your models, datasets, transforms, and training pipelines, enabling easy configuration and experimentation with different settings.

## Features

- **Config-Driven Setup**: All parameters (model, dataset, training, testing, loss, preprocessing, visualization, and exporting losses) are configured via a YAML file, making experiments reproducible and easily adjustable.
- **Dynamic Loading**: Models, datasets, and preprocessing functions are loaded dynamically from user-specified modules, allowing you to integrate your own code without modifying the core framework.
- **Task Agnostic**: Supports various tasks such as classification, regression, or generation by specifying different models, losses, and transforms.
- **Optional Features**:
  - **Visualization**: Plot training and validation loss curves and save them as images.
  - **Exporting Results**: Save recorded losses, experiment configuration, and test results to yaml files for further analysis.
- **Clear and Modular Code Structure**: Separation of concerns into modules (`manager`, `trainer`, `tester`, `datasets`, `utils`, etc.) for improved maintainability and scalability.

## Installation
You can install DeepExperimentManager easily using `pip`. This package is compatible with Python 3.9 and later.

1. Install via pip
    To install the latest version of DeepExperimentManager from PyPI, run the following command:
    ```bash
    pip install DeepExperimentManager
    ```
    This will automatically handle the installation of any required dependencies.

2. Verify Installation
    After the installation, you can verify that the package is successfully installed by running:
    ```bash
    python -c "import DeepExperimentManager; print('DeepExperimentManager installed successfully!')"
    ```
    Make sure PyTorch and other dependencies (such as torchvision, yaml, matplotlib) are installed. Adjust the requirements as needed.

3. Using Virtual Environments (Recommended)
    It is a good practice to install Python packages in a virtual environment to avoid dependency conflicts with other projects. You can create and activate a virtual environment as follows:
    1. Create a virtual environment:
      ```bash
      python -m venv venv
      ```
    2. Activate the virtual environment:
      - On Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
      - On Windows:
        ```bash
        venv/Scripts/activate
        ```
    3. install the package:
      ```bash
      pip install DeepExperimentManager
      ```

4. Upgrading the package
    To ensure you have the latest version of `DeepExperimentManager`, you can upgrade it using the following command:
    ```bash
    pip install --upgrade DeepExperimentManager
    ```
## Usage
1. **Define Required Object Classes and functions**
Model modules, dataset classes, and preprocessing functions must be defined first.

- **Model**
You should define your own model to experiment.
Following is the simple example of PyTorch Neural Network model.
```python
import torch.nn as nn

class TestModel(nn.Module):
    def __init__(self, output_size):
        super(TestModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.dropout = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, output_size)

    def forward(self, x):
        x = nn.functional.relu(nn.functional.max_pool2d(self.conv1(x), 2))
        x = nn.functional.relu(nn.functional.max_pool2d(self.dropout(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = nn.functional.relu(self.fc1(x))
        x = nn.functional.dropout(x, training=self.training)
        x = self.fc2(x)
        return nn.functional.log_softmax(x, dim=1)
```

- **Dataset**
You can use your own custom dataset or built-in datasets of PyTorch.
Following is a simple example of custom dataset class.
```python
import torch
from torch.utils.data import Dataset

class BasicDataset(Dataset):
    def __init__(self, x_tensor, y_tensor):
        super(BasicDataset, self).__init__()

        self.x = x_tensor
        self.y = y_tensor
        
    def __getitem__(self, index):
        return self.x[index], self.y[index]

    def __len__(self):
        return len(self.x)
```

- **Preprocessing or Trasform**
When you apply Transform object defined in PyTorch, You should define a function that returns defined Transform object:
```python
from torchvision import transforms

def get_transform():
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    return transform
```
Or, When you apply your own custom data preprocessing function. just keep the following format:
```python
def processing(data):
    "Preprocessing code for your data"
    return processed data
```
Also, your custom dataset must have argument for preprocessing function:
```python
import torch
from torch.utils.data import Dataset

class BasicDataset(Dataset):
    def __init__(self, x_tensor, y_tensor, processing=None):
        super(BasicDataset, self).__init__()

        self.x = x_tensor
        self.y = y_tensor
        
        if processing is not None:
          self.x = processing(self.x)

    def __getitem__(self, index):
        return self.x[index], self.y[index]

    def __len__(self):
        return len(self.x)
```
2. **Edit the config.yaml:**
Update paths, model modules, dataset classes, preprocessing functions, training parameters, and so forth to match your project. 
You can also check the example codes in `/test` directory. 
Example:
```yaml
model:
  module: 'tests.model'
  class: 'TestModel'
  args: # Input Arguments of your model
    output_size: 10

device: 'cuda' # If None, default is CPU
task: "classification" # regression, multi_label, etc.

training:
  epochs: 10
  learning_rate: 0.001
  optimizer:
    type: 'Adam'
    args:
      weight_decay: 0.0001

testing:
  metrics: # Get metric functions from sklearn
    - "sklearn.metrics.accuracy_score" 
    - "sklearn.metrics.r2_score"
    # - "custom_metrics.yourmetrics" or you can import your own custom metrics

loss:
  module: 'torch.nn'
  type: 'CrossEntropyLoss'
  args: {}

dataset:
  module: 'torchvision.datasets'
  class: 'MNIST'
  preprocessing_arg: 'transform'
  args:
    preprocessing:
      module: 'tests.preprocessing'
      function: 'get_transform'

    train:
      args: # Input Arguments of your custom dataset
        root: './tests/data'
        train: True
        download: True
      loader: # Arguments of DataLoader
        batch_size: 64
        shuffle: True
    #valid:
    #  args: {}
    #  loader: {}
    test:
      args: # Input Arguments of your custom dataset
        root: './tests/data'
        train: False
        download: True
      loader: # Arguments of DataLoader
        batch_size: 1000
        shuffle: False

visualization:
  enabled: True
  plot_dir: './tests/plots'
  log_scale: True

export_results:
  enabled: True
  export_dir: './tests/results'
```

2. **Write the Model Experiment Code:**
For example, this would be code for main.py

```python
import argparse
from experiment_manager import ExperimentManager

def main():
    """
    Main entry point for running the experiment.

    This script will:
    - Parse command-line arguments.
    - Initialize and run the ExperimentManager with the given config file.
    """
    parser = argparse.ArgumentParser(description="Run experiment using ExperimentManager.")
    parser.add_argument('--config', type=str, required=True, help='Path to the YAML configuration file.')
    args = parser.parse_args()

    # Initialize ExperimentManager with the given config
    manager = ExperimentManager(config_path=args.config)
    # Run the full experiment (training and optional testing)
    manager.run_experiment()

if __name__ == '__main__':
    main()
```

3. **Run the main code:**
```bash
python main.py --config "path of config.yaml"
```
in this case, config.yaml must be placed in root directory.

this will:
- Load the specified model, dataset, and transforms.
- Run training for the specified number of epochs.
- Optionally validate after each epoch.
- Save checkpoints, plot loss curves, and export results if enabled.

4. **Check Outputs:**
- Checkpoints: Stored in `./checkpoints/` by default.
- Loss plots: Stored in the path you write in config if visualization is enabled.
- results files: Stored in the path you write in config if exporting is enabled.
- Logs: Training and validation logs displayed in the terminal.

Here is the example of the results file:
```yaml
records:
-   model_config:
        module: test.model
        class: TestModel
        args:
            output_size: 10
    training_config:
        epochs: 10
        learning_rate: 0.001
        optimizer:
            type: Adam
            args:
                weight_decay: 0.0001
        batch_size: 64
    loss_func:
        type: CrossEntropyLoss
        args: {}
    num_parameters: 21840
    total_time: 85.88482213020325
    valid_time: 0
    train_losses:
    - 0.5216201075168052
    - 0.24523054485890403
    - 0.20145633446572941
    - 0.1797466142696819
    - 0.16584936341743417
    - 0.1538330529377595
    - 0.1499541729374894
    - 0.14426758698324785
    - 0.13845630399962225
    - 0.1345993925982129
    valid_losses: []
    test_results:
        accuracy: 0.9894
-   model_config:
        module: test.model
        class: TestModel
        args:
            output_size: 10
    training_config:
        epochs: 10
        learning_rate: 0.001
        optimizer:
            type: Adam
            args:
                weight_decay: 0.0001
        batch_size: 64
    loss_func:
        type: CrossEntropyLoss
        args: {}
    num_parameters: 21840
    total_time: 84.3278419971466
    valid_time: 0
    train_losses:
    - 0.5215464325776613
    - 0.24535706221882594
    - 0.20132130482939006
    - 0.18052261650586116
    - 0.16633369837766454
    - 0.1533887283896396
    - 0.1472813178922163
    - 0.14270564404997363
    - 0.13906002168490023
    - 0.1365545368048428
    valid_losses: []
    test_results:
        accuracy: 0.9888
```
And here is the example of loss plot:
![lossplot](./tests/plots/TestModel_loss_curve.png)
## License
This project is provided under the MIT License.