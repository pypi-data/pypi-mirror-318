import os
from urllib.parse import urlparse, parse_qs
import yaml
import csv

from loguru import logger


class QGFile:
    @staticmethod
    def save_to_file(file_path, log):
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f'{log}\n')
            f.close()


    @staticmethod
    def save_to_file_deduplicate(file_path, log):
        """去重插入行"""
        # 判断文件是否存在，没有存在就新建，然后直接返回
        if not os.path.exists(file_path):
            QGFile.save_to_file(file_path, "")
            return
        # 打开输入文件并读取所有行
        with open(f'{file_path}', 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        # 确保新行末尾有换行符
        if not log.endswith('\n'):
            log += '\n'
        # 将新行插入到行列表中
        lines.append(log)
        # 去除重复行，并保持原有顺序
        unique_lines = list(dict.fromkeys(lines))
        # 将去重后的行写入输出文件
        with open(f'{file_path}', 'w', encoding='utf-8') as outfile:
            outfile.writelines(unique_lines)
            outfile.close()

    @staticmethod
    def txt_to_array(file_path: object, split: object = '----') -> list:
        lines = open(file_path, 'r', encoding='utf-8').readlines()
        arr = [[z.strip() for z in x.split(split)] for x in lines]
        return arr

    @classmethod
    def get_row_from_file_index(cls, file_path: object, split: object = '----', index: int = 1):
        return cls.txt_to_array(file_path, split)[index - 1]

    @staticmethod
    def array_to_txt(arr, to_file_path) -> list:
        with open(to_file_path, 'a', encoding='utf-8') as f:
            for cols in arr:
                log = "----".join(cols)
                f.write(f'{log}\n')
            f.close()
        lines = open(to_file_path, 'r', encoding='utf-8').readlines()
        arr = [[z.strip() for z in x.split(to_file_path)] for x in lines]
        return arr

    @staticmethod
    def read_yaml(file_path):
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                # 你可以在这里写入一些初始内容，或者留空
                pass
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    @staticmethod
    def url_params_to_object(url, keyword=None):
        # 解析URL
        parsed_url = urlparse(url)
        # 获取查询字符串参数并转换为字典对象
        query_params = parse_qs(parsed_url.query)
        # 处理字典对象，将每个参数的值转换为单个值而不是数组
        for key, value in query_params.items():
            query_params[key] = value[0]
        # 返回转换后的字典对象
        if keyword:
            return query_params.get(keyword)
        return query_params

    @staticmethod
    def csv_to_array(file_path, has_header=True, delimiter=','):
        """解汇csv文件，返回数组对象"""
        with open(file_path, 'r') as f:
            reader = csv.reader(f, delimiter=delimiter)
            all_list = list(reader)
            if len(all_list) == 0:
                return []
            if has_header:
                head_list = all_list[0]
                data_list = all_list[1:]
                array_obj = []
                for data in data_list:
                    obj = {}
                    for i, attr in enumerate(head_list, start=0):
                        obj[attr] = data[i]
                    array_obj.append(obj)
                # logger.info(array_obj)
                return array_obj
            else:
                return all_list

    @staticmethod
    def csv_to_yaml(wallet_path, dis_path, tw_path, to_path):
        """往文件修改新增"""
        wallets = QGFile.csv_to_array(wallet_path)
        # wallets = QGUtil.txt_to_array(wallet_path)
        dis_tokens = QGFile.txt_to_array(dis_path)
        tws = QGFile.txt_to_array(tw_path)
        full_data = {
            "accounts": []
        }
        for i, row in enumerate(wallets, start=0):
            addr1 = row.get("addr")
            pk1 = row.get("pk")
            if i <= 21:
                continue

            else:
                obj = {
                }
                full_data['accounts'].append(obj)
        with open(to_path, 'w') as file:
            yaml.dump(full_data, file)
        logger.info("数据已成功修改并写回到YAML文件。")

    @staticmethod
    def save_to_yaml(to_path, full_data):
        with open(to_path, 'w') as file:
            yaml.dump(full_data, file)
        logger.info("数据已成功修改并写回到YAML文件。")

    @staticmethod
    def read_xlsx(file_path):
        """
        读取excel成list对象
        """
        try:
            import pandas as pd
            df = pd.read_excel(file_path)
            json_data = df.to_json(orient='records')
            import json
            json_list = json.loads(json_data)
            print(json_list)
        except FileNotFoundError:
            print(f"文件 {file_path} 不存在，请检查文件路径是否正确。")
            return None
        except pd.errors.ParserError:
            print(f"读取 {file_path} 文件时出现解析错误，请确保文件格式正确且数据完整。")
            return None
        except json.JSONDecodeError:
            print(f"将Excel数据转换为JSON格式时出现解码错误，请检查数据内容是否符合JSON规范。")
            return None


if __name__ == '__main__':
    QGFile.read_xlsx("aa.xlsx")