import json
import csv
import joblib


def dump_data_to_json(data, json_path):
    # 保存数据到json文件
    with open(json_path, 'w', encoding='utf-8-sig') as f:
        json.dump(data, f)

    f.close()
    return


def load_data_from_json(json_path):
    # 从json文件中读取数据
    data = None

    with open(json_path, encoding='utf-8-sig') as f:
        data = json.load(f)

    f.close()
    return data


def load_data_from_csv(csv_path):
    # 从csv中读取训练数据
    data = []

    with open(csv_path, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) >= 1:
                data.append(row[0])

    f.close()
    return data


def dump_data_to_csv(data, csv_path):
    # 保存数据到csv文件
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)

        if data is not None:
            writer.writerows(data)

    f.close()
    return


def dump_model_to_file(model, model_path):
    # 保存模型文件到joblib文件

    joblib.dump(model, model_path)
    return


def load_model_from_file(model_path):
    # 从joblib文件读取模型

    model = joblib.load(model_path)
    return model


def load_test_data_and_target_from_csv(csv_path):
    # 从csv文件读取验证数据以及验证数据正确分类结果
    data = []
    target = []

    with open(csv_path, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)

        for row in reader:

            data.append(row[0])
            target.append(int(row[1]))

    f.close()
    return data, target
