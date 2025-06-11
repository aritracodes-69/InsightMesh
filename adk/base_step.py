import yaml
import importlib

class AgentBase:
    """
    Orchestrates a sequence of BaseStep instances, loaded from config.
    """
    def __init__(self, config_yaml_path: str, agent_config_section: str):
        # Load config and initialize steps list
        with open(config_yaml_path) as f:
            cfg = yaml.safe_load(f)
        self.steps = []
        # agent_config_section is key in config YAML listing steps
        for step_cfg in cfg.get(agent_config_section, []):
            module_path = step_cfg['module']
            class_name = step_cfg['class']
            params = step_cfg.get('params', {})
            module = importlib.import_module(module_path)
            StepClass = getattr(module, class_name)
            instance = StepClass(**params)
            self.steps.append(instance)
    
    def run(self, input_data, context: dict = None):
        if context is None:
            context = {}
        data = input_data
        for step in self.steps:
            data, context = step.apply(data, context)
        return data, context
    
    def explain(self):
        explanations = []
        for step in self.steps:
            explanations.append(step.explain())
        return "\n\n".join(explanations)
