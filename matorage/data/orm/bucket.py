# Copyright 2020-present Tae Hwan Jung
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

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKeyConstraint

from matorage.data.orm.compressor import Compressor

Base = declarative_base()

class Bucket(Base):
    __tablename__ = 'bucket'
    id = Column(String(255), primary_key=True, nullable=False)
    additional = Column(Text)
    dataset_name = Column(String(255), nullable=False)
    endpoint = Column(String(255), nullable=False)
    filetype = Column(Text)
    compressor_id = Column(Integer, ForeignKeyConstraint(Compressor.id))

    def __repr__(self):
        return "<Bucket(" \
                   "id='%s', " \
                   "additional='%s', " \
                   "dataset_name='%s'" \
                   "endpoint='%s'" \
                   "filetype='%s'" \
                   "compressor_id='%d'" \
               ")>" % (
            self.id, self.additional, self.dataset_name,
            self.endpoint, self.filetype, self.compressor_id
        )