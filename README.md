# Karst.io Schema Repository

## Schemas
* Feature - for caves, systems, and non-qualifying features
* Entrance - entrances to features
* Coordinate - for coordinates

## Example
    {
    	"id":	"11b00c88-cfe5-4436-8254-928a2cef97ba",
    	"name":	"Not uh Cave",
    	"code": "GCW0145",
    	"length": 4055,
    	"depth": 82,
    	"entrances": [
	   		{
	   			"id": "57b00c88-cfe5-4436-8254-928a2cef97fa",
		    	"discovered": "2015-11-01",
		    	"discovered_by": "John A. Spelunker",
		    	"status": "OPEN",
		 		"ownership": "PRIVATE PROPERTY",
		 		"ownership_description": "Landowner lives at bottom of mountain below entrance",
		 		"type": "HORIZONTAL",
		 		"negotiation": "CRAWL",
		 		"formation": "NATURAL",
		 		"geoformation": "Coweta Formation",
		 		"location": "BENCH",
		 		"hazards": "UNSTABLE",
		 		"coordinates": [
		 			{
		 				"id": "62b00c88-cfe5-4436-8254-928a2cef97fa",
		 				"system": "WGS84",
		 				"latitude": 842323.33,
		 				"longitude": 12333.57,
		 				"recorded": "2015-11-01",
		 				"recorded_by": "John A. Spelunker"
		 			}
		 		],
		 		"largest_dimension": 30,
		 		"smallest_dimension": 2
		 	}
		 ]
    }