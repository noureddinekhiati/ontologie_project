import rdflib


g = rdflib.Graph()
g.parse("onotlogie_transport.rdf")


tranport_mode = g.query("""
		SELECT DISTINCT ?s
		WHERE
		{ ?s a :TransportMode }
		""")
print(len(tranport_mode))
for i in tranport_mode : 
    print(len(i))


tranport_mode = g.query("""
		SELECT DISTINCT ?s
		WHERE
		{ ?s a :ValuePartition }
		""")
tranport_mode = g.query("""
    SELECT DISTINCT ?s
    WHERE
    { ?s a :Public }
    """)
tranport_mode = g.query("""
    SELECT DISTINCT ?s
    WHERE
    { ?s a :TwoWheelaer }
    """)

