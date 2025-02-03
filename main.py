import requests


def download_image(image_url: str, save_as: str) -> None:
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(save_as, 'wb') as file:
                file.write(response.content)
            print(f"Изображение успешно сохранено как {save_as}")
        else:
            print(f"Ошибка при скачивании изображения: {response.status_code}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    data = read_json_file('data.json')
    prefix_dir = 'imgs/'
    for card in data[:2]:
        rus_name, lat_name, image_url, save_as = card
        save_as = prefix_dir + save_as
        print(f'Название карты: {rus_name}, ЛатНазвание: {lat_name}')
        download_image(image_url=image_url, save_as=save_as)
        print('-' * 50)
    print(f'Length of card: {len(data)}')
