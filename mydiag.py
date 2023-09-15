from diagrams import Cluster, Diagram
from diagrams.gmp.analytics import GA4,GA3,GTM,GDS,GoogleOptimize,ADH
from diagrams.gmp.advertising import DV360
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.compute import Functions as GCF
from diagrams.generic.database import SQL
from diagrams.programming.language import Python

generalDirection=""
graph_attr = {
    "fontname": "Roboto",
    "fontsize": "24",
    "orientation": "portrait"
}

with Diagram(
    "Sample GMP/GCP diagram", 
    direction="TB", 
    graph_attr=graph_attr
    ):
    
    gdsA = GDS("Dashboard")
    gdsC = GDS("Consent")
    ga3 = GA3("UA-1234-1")
    
    gtm = GTM("Consent click event")

    with Cluster("Collection"):
        cf =  Python() >> GCF("consent\ncollection")
    with Cluster("BigQuery"):
        store = BigQuery("Consent dataset") >> SQL("query by date")
    with Cluster("BigQuery + ADH"):
        ga360 = GCF("BigQuery\nGA360")
        ga360 << DV360("Publisher data")
        ga360 << ADH("Ads Data Hub")
    gtm >> ga3

    gtm >> cf >> store >> gdsC
    gtm >> GA4("Firebase")

    ga3 >> gdsA
    gtm >> GoogleOptimize("Experiment1") >> ga3
    ga3 >> ga360
    
    