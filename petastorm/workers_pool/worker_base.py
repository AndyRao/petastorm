#  Copyright (c) 2017-2018 Uber Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import abstractmethod


class WorkerBase(object):
    def __init__(self, worker_id, publish_func, filesystem=None,
                 dataset_path=None,
                 schema=None,
                 ngram=None,
                 split_pieces=None,
                 local_cache=None,
                 transform_spec=None,
                 transformed_schema=None,
                 pyarrow_filters=None):
        """Initializes a worker.

        :param worker_id: An integer uniquely identifying a worker instance
        :param publish_func: Function handler to be used to publish data
        :param args: application specific args
        """
        self.worker_id = worker_id
        self.publish_func = publish_func

        self._filesystem = filesystem
        self._dataset_path = dataset_path
        self._schema = schema
        self._ngram = ngram
        self._split_pieces = split_pieces
        self._local_cache = local_cache
        self._transform_spec = transform_spec
        self._transformed_schema = transformed_schema
        self._pyarrow_filters = pyarrow_filters

    @abstractmethod
    def process(self, *args, **kargs):
        pass

    def shutdown(self):
        pass
