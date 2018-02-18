import logging
import os


class MetadataSaver:
    def __init__(self, dataset, out_dir):
        self.dataset = dataset
        self.out_dir = out_dir
        self.file_name = 'metadata.csv'

    def save(self, metadata):
        logging.info(f'SAVE METADATA {metadata}')

        data = ','.join(metadata) + '\n'
        for apk in self.dataset:
            data += self.get_line(apk, metadata) + '\n'

        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

        save_path = os.path.join(self.out_dir, self.file_name)
        with open(save_path, 'w+') as file:
            file.write(data)
            file.flush()

    def get_line(self, apk, fields):
        line = ''
        for field in fields:
            line += str(getattr(apk, field)) + ','
        line = line[:-1]
        return line
