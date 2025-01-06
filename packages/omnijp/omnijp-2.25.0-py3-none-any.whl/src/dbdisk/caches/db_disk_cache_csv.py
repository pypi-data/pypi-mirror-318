import os
import csv
from src.common.caches.db_disk_cache import DbDiskCache
from src.common.helper import split_into_subsets, zip_directory


class DbDiskCacheCsv(DbDiskCache):

    def save(self, header, data):
        try:
            local_cache_dir = self.get_local_cache_path()
            os.makedirs(local_cache_dir, exist_ok=True)
            subsets = split_into_subsets(data, self.rows_per_file)
            total = 0
           
            for i, subset in enumerate(subsets, 1):
                file_name = f"{self.cache_name}.csv" if len(subsets) == 1 else f"{self.cache_name}_{i}.csv"
                file_path = os.path.join(local_cache_dir, file_name)
                self._save_file(header, subset, file_path)
                total += len(subset)

            self.logger.info(f"Total records saved: {total}")
            if self.can_zip:
                zip_directory(local_cache_dir, local_cache_dir)
        except Exception as e:
            self.logger.error(f"Error saving cache: {e}")
            return False
        self.logger.info(f"Cache saved to {file_path}")
        return True

    def get_local_cache_path(self):
        return os.path.join(self.cache_dir, self.cache_name) if self.can_zip else self.cache_dir

    
    def _save_file(self, header, data, file_path):
        try:
            with open(file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(header)
                for row in data:
                    csv_writer.writerow(row)
        except Exception as e:
            self.logger.error(f"Error saving cache: {e}")
            return False
        
        self.logger.info(f"Cache saved to {file_path}")
        return True
