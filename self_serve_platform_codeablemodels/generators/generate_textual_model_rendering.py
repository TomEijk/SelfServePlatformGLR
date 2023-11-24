import os
import shutil
from metamodels.guidance_metamodel import decision_solution_relation, decision, force
from textual_generators import get_names_list, write_file, _get_all_sub_classes_helper
from metamodels.guidance_metamodel import positive, negative, force_impact_relation
from self_serve_platform_models.sources_and_codes_model import s1


class TextualModelRenderer(object):
    def __init__(self):
        self.directory = "../_generated/textual_model_rendering"
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.makedirs(self.directory)

    @staticmethod
    def render_linked_relation(from_class, relation):
        text = ""
        for link in from_class.get_links_for_association(relation):
            for link_type in link.stereotype_instances:
                target = link.source
                if link.source == from_class:
                    target = link.target
                text += "  - " + from_class.name + " --" + link_type.name + "-- " + target.name
                text += ": " + get_names_list(link.get_linked(role_name="evidence")) + "\n"
                # text += "\n"
        return text

    def generate_guidance_evidences(self, decision_list, file_name):
        text = "# " + "API design" + "\n"
        text += "\n\n"

        for _decision in decision_list:
            text += "## Decision: " + _decision.name + "\n"
            decision_evidences = _decision.get_linked(role_name="evidence")
            text += "**Evidences:** " + get_names_list(decision_evidences) + "\n\n"
            text += "**Context:** " + get_names_list(_decision.get_linked(role_name="context")) + "\n"
            text += "\n### **Solution Options**\n"
            for i, _option in enumerate(_decision.get_linked(association=decision_solution_relation)):
                text += "#### Solution " + str(i + 1) + ": " + str(_option.name) + "\n"
                option_evidences = _option.get_linked(role_name="evidence")
                text += "**Evidences:** " + get_names_list(option_evidences) + "\n\n"
                for option_evidence in option_evidences:
                    if option_evidence not in decision_evidences:
                        print(f"WARNING: evidence '{option_evidence!s}' for option '{_option!s}'" +
                              f" not in decision evidences of '{_decision}'")
                if _option.get_linked(role_name="forces"):
                    text += "**Forces:**" + "\n"
                    for force_link in _option.get_links_for_association(force_impact_relation):
                        _force = force_link.get_opposite_object(_option)
                        text += "- " + _force.name
                        for link_type in force_link.stereotype_instances:
                            text += " (" + link_type.name + ")"
                        force_evidences_per_decision = []
                        all_force_evidences = _force.get_linked(role_name="evidence")
                        for force_evidence in all_force_evidences:
                            if force_evidence in decision_evidences:
                                # include here only those evidences where the decision is discussed in the source.
                                force_evidences_per_decision.append(force_evidence)
                        text += " [" + ", ".join([e.name for e in force_evidences_per_decision]) + "]\n"
                text += "\n"
            for _next_decision in _decision.get_linked(role_name="next decision"):
                text += "#### **Next Decision**: " + _next_decision.name + "\n"
            text += "\n\n"

        text += "# Forces: \n"
        for _force in force.all_classes:
            all_force_evidences = get_names_list(_force.get_linked(role_name="evidence"))
            text += "- " + _force.name + " [" + all_force_evidences + "]" + "\n"

        text += "\n\n"

        write_file(self.directory, file_name + ".md", text)


if __name__ == "__main__":
    textual_model_renderer = TextualModelRenderer()
    decisions = [d for d in decision.all_classes]
    textual_model_renderer.generate_guidance_evidences(decisions, "api_design")
