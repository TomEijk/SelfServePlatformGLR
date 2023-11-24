from generate_latex_files import LatexTableRenderer
from generate_textual_model_rendering import TextualModelRenderer
from metamodels.guidance_metamodel import decision
from plant_uml_renderer import PlantUMLGenerator
from self_serve_platform_models.self_serve_platform_model import self_serve_platform_views

# UMLgenerator
generator = PlantUMLGenerator(delete_gen_dir_during_init=True)
generator.object_model_renderer.name_break_length = 45
generator.object_model_renderer.left_to_right = False

object_models = {'self_serve_platform_models': self_serve_platform_views}
for key, value in object_models.items():
    generator.generate_object_models(key, value)

# TextualInfo
textual_model_renderer = TextualModelRenderer()
decisions = [d for d in decision.all_classes]
textual_model_renderer.generate_guidance_evidences(decisions, "self_serve_platform_design")

# Latex
source_table_renderer = LatexTableRenderer()
source_table_renderer.generate(decisions)

#%%
