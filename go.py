'''Creates svg with kartograph'''
import kartograph
import yaml

def main():
    config = yaml.load(open('map_config.yaml'))
    K = kartograph.Kartograph()
    K.generate(config, 'map.svg')

if __name__ == "__main__":
    main()
