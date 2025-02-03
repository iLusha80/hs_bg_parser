from utils import read_json_file


if __name__ == '__main__':
    data = read_json_file('data.json')
    prefix_dir = 'imgs/'
    for card in data:
        rus_name, lat_name, image_url, save_as = card
    print(f'Length of card: {len(data)}')
