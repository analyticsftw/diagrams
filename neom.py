from diagrams import Cluster, Diagram
from diagrams.clients.clients import Neom
from diagrams.adobe import MarketingCloud
from diagrams.alibabacloud.web import Domain
from diagrams.saas.tagmanagement import Tealium
from diagrams.gmp.analytics import GA3
from diagrams.onprem.analytics import PowerBI
from diagrams.aws.storage import S3

graph_attr = {
    "fontname": "Roboto",
    "fontsize": "24",
    "orientation": "portrait"
}

with Diagram("NEOM Analytics - AEM MVP"):
    
    neom = Neom()
    
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
    
    