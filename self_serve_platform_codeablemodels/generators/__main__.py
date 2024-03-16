# from plant_uml_renderer import PlantUMLGenerator
from CodeableModels.plant_uml_renderer import PlantUMLGenerator
from self_serve_platform_codeablemodels.self_serve_platform_models.self_serve_platform_model import self_serve_platform_views

# UMLgenerator
generator = PlantUMLGenerator(delete_gen_dir_during_init=True)
generator.object_model_renderer.name_break_length = 45
generator.object_model_renderer.left_to_right = False

object_models = {'self_serve_platform_models': self_serve_platform_views}
for key, value in object_models.items():
    generator.generate_object_models(key, value)

if __name__ == "__main__":
    pass

#%%
