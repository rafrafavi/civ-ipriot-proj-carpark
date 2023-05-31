import smartpark.parse_config as pc
import smartpark.parking_lot as lot

if __name__ == "__main__":
    config_file = "config.toml"
    section = "parking_lot"
    config_data = pc.load_config(config_file, section)
    config_dict = pc.parse_config(config_data)
    parking = lot.ParkingLot(config_dict)
