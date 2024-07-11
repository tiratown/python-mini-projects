import json

if __name__ == '__main__':
    try:
        # with open('input.json', 'r') as f:
        with open('input.json', 'rb') as f:
            data = json.loads(f.read())

        output = ','.join([*data[0]])
        for obj in data:
            # output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'
            output += f'\n{obj["id"]},{obj["area_pid"]},{obj["area_id"]},{obj["bankname"]},{obj["hanghao"]},{obj["bank_id"]},{obj["tel"]},{obj["address"]},{obj["create_time"]}'

        # with open('output.csv', 'w') as f:
        with open('output.csv', 'w', encoding='UTF-8') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')
