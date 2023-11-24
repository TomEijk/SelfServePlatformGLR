import os
import shutil

from metamodels.GT_coding import source
from metamodels.guidance_metamodel import force
from textual_generators import get_names_list, write_file, get_color_coding_command
from metamodels.guidance_metamodel import decision_solution_relation, force_impact_relation


def render_table_header_line(headers):
    text = ""
    for header in headers:
        text += "{\\bf " + header + "} & "
    text = text[:-3]
    text += "\\\\\n"
    return text


def get_color_coding_command(percentage):
    if percentage < 0.05:
        return "\\cellcolor{emerald_shape_1}"
    if percentage < 0.10:
        return "\\cellcolor{emerald_shape_2}"
    if percentage < 0.20:
        return "\\cellcolor{emerald_shape_3}"
    if percentage < 0.35:
        return "\\cellcolor{emerald_shape_4}"
    if percentage < 0.5:
        return "\\cellcolor{emerald_shape_5}"
    if percentage < 0.7:
        return "\\cellcolor{emerald_shape_6}"
    return "\\cellcolor{emerald_shape_7}"


def get_dict(data):
    result = {}
    for key, value in enumerate(data):
        result["f"+str(key+1)] = value
    return result


def get_force_relations(solution):
    result = []
    for link in solution.get_links_for_association(force_impact_relation):
        evidences = link.get_linked(role_name="evidence")
        for link_type in link.stereotype_instances:
            result.append([link.source.name, link_type.name,
                           link.target.name, evidences])
    return result


def parse_double_minus_sign(sign):
    if sign == "--":
        return "-{}-"
    else:
        return sign

def parse_binary_value(TFvalue):
    if TFvalue == True:
        return "Yes"
    else:
        return "No"

def generate_footnote_force():
    text = "{\\bf Forces Codes/Sources}: "
    for i, _force in enumerate(force.all_classes):
        force_evidences = get_names_list(_force.get_linked(role_name="evidence"))
        text += "{\\bf " + "f" + str(i+1) + "}:" +str(_force.name)+ " [" + force_evidences + "]" 
        if i < len(force.all_classes)-1:
            text += ", "
    return text

class LatexTableRenderer(object):
    def __init__(self):
        self.directory = "../_generated/latex_files"
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.makedirs(self.directory)

    def generate_sources_table(self):
        text = "\\begin{tabular}{|c|p{0.4\linewidth}|l|l|c|c|}\n"
        text += "\\hline\n"
        text += render_table_header_line(
            ["ID", "Title", "Tiny URL", "Source Type", "Example", "Source Code"])
        text += "\\hline\n"
        for source_class in source.classes:
            text += str(source_class.name)
            text += " & "
            text += " {\\em " + str(source_class.get_value("title"))+ "}"
            text += " & "

            href_link = ""
            # the broken link in the TinyURL
            if source_class.name in ["s2","s12", "s18"]:
                href_link = "\\href{" +str(source_class.get_value("url")) + "}"
            else:
                href_link = "\\href{https://" +str(source_class.get_value("tiny url"))+ "}"

            text += href_link + "{"+str(source_class.get_value("tiny url"))+"}"
            text += " & "
            text += str(source_class.get_value("type"))
            text += " & "
            text += parse_binary_value(source_class.get_value("example"))
            text += " & "
            text += parse_binary_value(source_class.get_value("source code"))
            text += "\\\\\n"
        text += "\\bottomrule\n"
        text += "\\end{tabular}\n"
        write_file(self.directory, "sources_table.tex", text)

    def generate_force_table(self):
        text = "\\begin{tabular}{|c|p{0.48\columnwidth}|p{0.37\columnwidth}|}\n"
        text += "\\hline\n"
        text += render_table_header_line(
            ["ID", "Force", "Evidences"])
        text += "\\hline\n"
        sum_all_force_evidences = len(force.classes)
        for i, _force in enumerate(force.all_classes):
            force_evidences = get_names_list(
                _force.get_linked(role_name="evidence"))
            sum_force_evidences = len(_force.get_linked(role_name="evidence"))
            proportion = sum_force_evidences/sum_all_force_evidences
            text += "f" + str(i+1)
            text += " & "
            text += str(_force.name)
            text += " & " + get_color_coding_command(proportion) + " {"
            text += force_evidences + "}"
            text += "\\\\\n"
        text += "\\hline\n"
        text += "\\end{tabular}\n"
        write_file(self.directory, "force_table.tex", text)

    def generate_overview_table(self, decisions):
        total_number_of_sources = len(source.classes)
        text = "\\begin{tabular}{|p{0.12\linewidth}|p{0.015\linewidth}|p{0.3\linewidth}|p{0.15\linewidth}|p{0.31\linewidth}|}\n"
        text += "\\hline\n"
        text += render_table_header_line(["Design Decision", "\#", "Solution", "Evidences", "Forces"])
        text += "\\hline\n"
        
        for decision in decisions:
            total_number_of_evidences = len(decision.get_linked(role_name="evidence"))
            proportion_decision = total_number_of_evidences / total_number_of_sources
            number_of_solutions = len(decision.get_linked(association=decision_solution_relation))
            text += "\\multirow{" + str(number_of_solutions) + "}{\linewidth}{" + str(decision.name) + "} &"
            color_command_decision = get_color_coding_command(proportion_decision)
            if number_of_solutions == 1:
                text += "\\multirow{" + str(number_of_solutions) + "}{\linewidth}{ " + color_command_decision + "{" + str(
                    total_number_of_evidences) + "}} &"
            else:
                text += color_command_decision + "{} &"

            current = -1  
            force_list =[]
            for i, option in enumerate(decision.get_linked(association=decision_solution_relation)):
                current = current + 1
                if number_of_solutions != 1 and current is number_of_solutions - 1:
                    text += " & \\multirow{-" + str(number_of_solutions) + "}{\linewidth}{ " + color_command_decision + "{" + str(
                        total_number_of_evidences) + "}} &"
                elif current != 0:
                    text += " & " + color_command_decision + "{} & "
                
                text += str(i + 1) + "." + str(option.name) + "&"

                total_number_of_option_evidences = len(option.get_linked(role_name="evidence"))
                proportion_option = total_number_of_option_evidences / total_number_of_evidences
                text += get_color_coding_command(proportion_option) + "{" + get_names_list(option.get_linked(role_name="evidence")) + "} & "

                _forces = get_force_relations(option)
                for _force in _forces:
                    for key, value in get_dict(force.all_classes).items():
                        if _force[2] == value.name and _forces.index(_force) < len(_forces)-1:
                            if _forces.index(_force) != 0:
                                text += " "
                            text += key + "(" + parse_double_minus_sign(_force[1]) + "),"
                        elif _force[2] == value.name and _forces.index(_force) is len(_forces)-1:
                            if _forces.index(_force) != 0:
                                text += " "
                            text += key + "(" + parse_double_minus_sign(_force[1]) + ")"

                text += "\\\\\n"
        text += "\\hline\n"
        text += "\\multicolumn{5}{l}{\\parbox{\\textwidth}{\\smallskip\n"+ generate_footnote_force() +"}}"
        text += "\n\\end{tabular}\n"
        write_file(self.directory, "overview_table.tex", text)

    def generate_itemize_info(self, _decision):
        text = "\\begin{itemize}\n"
        text += "\\item \\textbf{Decision}: " + _decision.name + "\n"
        decision_evidences = _decision.get_linked(role_name="evidence")
        text += "\\item \\textbf{Evidences}: " + \
            get_names_list(decision_evidences) + "\n"
        text += "\\item \\textbf{Context}: " + \
            get_names_list(_decision.get_linked(role_name="context")) + "\n"
        text += "\\item \\textbf{Solution}: " + "\n"
        force_list = []
        text += "\\begin{enumerate}\n"
        for _option in _decision.get_linked(association=decision_solution_relation):
            text += "\\item " + str(_option.name) + "\n"
            for _force in _option.get_linked(role_name="forces"):
                if _force not in force_list:
                    force_list.append(_force)
        text += "\\end{enumerate}\n"
        text += "\\item \\textbf{Forces}: " + get_names_list(force_list) + "\n"
        if _decision.get_linked(role_name="next decision"):
            text += "\\item \\textbf{NextDecision}: " + "\n"
            text += "\\begin{itemize}\n"
            for _next_decision in _decision.get_linked(role_name="next decision"):
                text += "\\item " + _next_decision.name + "\n"
            text += "\\end{itemize}\n"
        text += "\\end{itemize}\n"
        filename = _decision.name.replace(" ", "")[:-1].upper()
        write_file(self.directory, filename+".tex", text)

    def generate(self, decision_list):
        self.generate_sources_table()
        self.generate_force_table()
        self.generate_overview_table(decision_list)

if __name__ == "__main__":
   source_table_renderer = LatexTableRenderer()
   source_table_renderer.generate()
   import distutils.dir_util

   to_path = "../../../../paper/drafts/coupling_code_smells_grey_literature_based_gt/generated_tables"
   distutils.dir_util.copy_tree("../_generated/latex_tables", to_path)
