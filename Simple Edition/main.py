# main
import extractor
import transform
import load

if __name__ == '__main__':
	print("starting my demo ETL pipeline...")
	extracted_data = extractor.get_immunization_df()
	print("extract1")
	extracted_data2 = extractor.get_county_df()
	print("extract2")
	transformed_data = transform.transform_data(extracted_data,extracted_data2)
	print("transform")
	load.load_data(transformed_data)
	print("load")