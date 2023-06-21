import xml.etree.ElementTree as ET

def extract_rdf_about(xml_data):
    root = ET.fromstring(xml_data)

    rdf_descriptions = root.findall(".//{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description")

    # Among the rdf:Description elements, find the one that has the second to last element of the rdf:about attribute equal to "cellar"
    for rdf_description in rdf_descriptions:
        rdf_about = rdf_description.attrib["{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"]
        rdf_about_split = rdf_about.split("/")
        if rdf_about_split[-2] == "cellar":
            return rdf_about_split[-1]

    return None


def extract_rdf_about_from_file(file_path):
    with open(file_path, "r") as f:
        xml_data = f.read()
        return extract_rdf_about(xml_data)
    
    return None