from diagrams import Cluster, Diagram
from diagrams.gmp.analytics import GA4,GA3,GTM,GDS,GoogleOptimize,ADH
from diagrams.gmp.advertising import DV360
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.compute import Functions as GCF
from diagrams.generic.database import SQL
from diagrams.programming.language import Python
from diagrams.oci.connectivity import DNS

generalDirection=""
graph_attr = {
    "fontname": "Roboto",
    "fontsize": "24pt",
    "orientation": "portrait",
    "bgcolor": "transparent"
}

with Diagram(
    direction="LR", 
    graph_attr=graph_attr,
    filename="superweek_fraud"
    ):
    
    
    gtm = GTM("Detect 0-bit color depth")
    
    acl = DNS("streamingsite.com")
    # with Cluster("Detection"):

    with Cluster("Cloud Function", direction="TB"):
        # cf >> python >> store >> grouping >> gtm
        python = Python("Python")
        cf = GCF("IP logging")
        python >> cf
    
    with Cluster("BigQuery", direction="LR"):
        store = BigQuery("IP dataset")
        grouping = SQL("GROUP BY `ìp`")

    gtm >> cf >> store >> grouping >> acl
    
