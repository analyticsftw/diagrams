from diagrams import Cluster, Diagram
from diagrams.programming.language import Bash, Python 
from diagrams.gcp.analytics import Bigquery
from diagrams.aws.database import Aurora

graph_attr = {
    "fontname": "Roboto",
    "fontsize": "24",
    "orientation": "portrait"
}

with Diagram("Content Security Policy Scanner"):
    
    shell = Bash("cURL from shell")
    headers_parser = Python("Header parser,\nsends to BigQuery")
    headers_file = Aurora("Headers, CSV")
    header_data = Bigquery("BigQuery")
    
    shell >> headers_file >> headers_parser >> header_data

    """
        AA = MarketingCloud.Analytics("Adobe Analytics")
        ga = GA3("Google Analytics")
        pbi = PowerBI("PowerBI")

        with Cluster("Websites"):
            www_neom = Domain("www.neom.com")
            careers_neom = Domain("careers.neom.com")
            csr_neom = Domain("impact.neom.com")
            websites = [
                www_neom,
                careers_neom,
                csr_neom
            ]  
        neom >> websites
        
        www_neom >> tealium >> ga >> pbi
        tealium >> S3("Form submissions")
        careers_neom >> ga
        csr_neom >> ga
    """
    