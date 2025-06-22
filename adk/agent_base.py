# adk/agent_base.py

import yaml
import importlib

class AgentBase:
    """
    Base class to orchestrate a sequence of steps (BaseStep instances) from a YAML config.
    """

    def __init__(self, config_yaml_path: str, agent_config_section: str):
        """
        :param config_yaml_path: Path to shared/config.yaml
        :param agent_config_section: Key under which this agent's steps are listed (e.g., 'feedback_agent')
        """
        with open(config_yaml_path, 'r') as f:
            cfg = yaml.safe_load(f)

        self.steps = []
        self.step_names = []

        for step_cfg in cfg.get(agent_config_section, []):
            module_path = step_cfg['module']
            class_name = step_cfg['class']
            params = step_cfg.get('params', {})

            try:
                module = importlib.import_module(module_path)
                StepClass = getattr(module, class_name)
                instance = StepClass(**params)
                self.steps.append(instance)
                self.step_names.append(class_name)
            except (ImportError, AttributeError) as e:
                raise ImportError(f"Failed to load {class_name} from {module_path}: {e}")

    def run(self, input_data, context: dict = None):
        """
        Executes the pipeline by passing data through each step in sequence.
        :param input_data: Initial input dictionary
        :param context: Optional context shared between steps
        :return: (final_output_data, updated_context)
        """
        if context is None:
            context = {}

        data = input_data
        for step in self.steps:
            data, context = step.apply(data, context)
        return data, context

    def explain(self):
        """
        Collects and returns a human-readable explanation of each step's operation.
        """
        return "\n\n".join([step.explain() for step in self.steps])
