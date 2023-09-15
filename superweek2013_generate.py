import custom
from diagrams import Cluster, Diagram
from custom.gmp.analytics import GA4,GA3,GTM,GDS,GoogleOptimize,ADH

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
    filename="superweek2013_generate"
    ):
    
    with Cluster("BigQuery", direction="LR"):
        store = BigQuery("IP dataset")
        grouping = SQL("SELECT site_id")
        python = Python("Python")
        

    store >> grouping >> python
    
