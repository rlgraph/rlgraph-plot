# Copyright 2018 The RLgraph project. All Rights Reserved.
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
# ==============================================================================

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import json

from flask import request, render_template
from rlgraph_plot.web import app, gv


@app.route('/', methods=['GET'])
def web_index():
    return render_template('simple_plot.html', graph_markup=gv.get('graph_markup'))


@app.route('/markup', methods=['POST'])
def web_markup():
    data = request.form
    graph_markup = data.get('graph_markup')
    token = data.get('token')

    if gv['token'] and str(token) != str(gv['token']):
        return json.dumps(dict(status='error', error='Invalid token')), 403

    if not graph_markup:
        return json.dumps(dict(status='error', error='No data received')), 400

    gv['graph_markup'] = graph_markup
    return json.dumps(dict(status='ok')), 200
