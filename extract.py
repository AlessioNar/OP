import xml.etree.ElementTree as ET

def extract_rdf_about(xml_data):
    root = ET.fromstring(xml_data)

    rdf_descriptions = root.findall(".//{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description")

    if len(rdf_descriptions) >= 2:
        second_rdf_description = rdf_descriptions[1]
        rdf_about = second_rdf_description.attrib.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about")
        return rdf_about

    return None


def extract_rdf_about_from_file(file_path):
    with open(file_path, "r") as f:
        xml_data = f.read()
        return extract_rdf_about(xml_data)
    
    return None

if __name__ == "__main__":
    rdf_about = extract_rdf_about_from_file("data/31968L0193.rdf")
    print(rdf_about)