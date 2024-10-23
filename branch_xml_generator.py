
import xml.etree.ElementTree as ET
from branch_xml_generator_types import BranchType


class BranchXMLGenerator:
    """
    BranchXMLGenerator is a class used to generate XML files that contain data about 
    company branches. The generated XML can be used for uploading to Yandex Business 
    to update branch information.
    
    Usage:
    1. Create an instance of BranchXMLGenerator.
    2. Use the add_company_branch method to add branch information.
    3. Use the generate_xml method to save the XML file to a specified path.
    """
    
    def __init__(self):
        """
        Initializes the XMLGenerator class by creating the root element of the XML file.
        """
        self.root = ET.Element("companies")

    
    def add_company_branch(self, branch: BranchType) -> None:

        # create company element
        company = ET.SubElement(self.root, "company")

        # create company-id element
        company_id_element = ET.SubElement(company, "company-id")
        company_id_element.text = branch["id"]

        # create name element with language attribute
        name_element = ET.SubElement(company, "name")
        name_element.set("lang", "ru")
        name_element.text = branch["name"]

        # create address element with language attribute
        address_element = ET.SubElement(company, "address")
        address_element.set("lang", "ru")
        address_element.text = branch["address"]

        # create country element with language attribute
        country_element = ET.SubElement(company, "country")
        country_element.set("lang", "ru")
        country_element.text = branch["country"]

        # create phone element with sub-elements for type and number
        phone_element = ET.SubElement(company, "phone")
        phone_type_element = ET.SubElement(phone_element, "type")
        phone_type_element.text = "phone"
        phone_number_element = ET.SubElement(phone_element, "number")
        phone_number_element.text = branch["phone"]
        ET.SubElement(phone_element, "info")

        # create email element
        email_element = ET.SubElement(company, "email")
        email_element.text = branch["email"]

        # create url element
        url_element = ET.SubElement(company, "url")
        url_element.text = branch["urls"]["url"]

        # create add-url element
        add_url_element = ET.SubElement(company, "add-url")
        add_url_element.text = branch["urls"]["add_url"]

        # create working-time element with language attribute
        working_time_element = ET.SubElement(company, "working-time")
        working_time_element.set("lang", "ru")
        working_time_element.text = branch["working_time"]

        # create rubric-id element
        rubric_id_element = ET.SubElement(company, "rubric-id")
        rubric_id_element.text = branch["rubric_id"]

        # create coordinates element with latitude and longitude
        coordinates_element = ET.SubElement(company, "coordinates")
        lat_element = ET.SubElement(coordinates_element, "lat")
        lat_element.text = branch["coordinates"]["latitude"]
        lon_element = ET.SubElement(coordinates_element, "lon")
        lon_element.text = branch["coordinates"]["longitude"]

        # create actualization-date element
        actualization_date_element = ET.SubElement(company, "actualization-date")
        actualization_date_element.text = branch["actualization_date"]

    def generate_xml(self, path) -> str:
        """
        Generates the XML file and writes it to the specified file path.
        
        Args:
        path (str): The file path where the XML file will be saved.
        """
        tree = ET.ElementTree(self.root)
        declaration = '<?xml version="1.0" encoding="UTF-8"?>'
        # write the XML file
        with open(path, 'wb') as file:
            file.write(declaration.encode('utf-8'))
            tree.write(file, encoding='utf-8')
        return path


