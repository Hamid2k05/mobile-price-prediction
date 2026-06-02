[     UTC     ] Logs for mobile-price-prediction-boqy3hsgcx4wjz7jp3itgm.streamlit.app/

────────────────────────────────────────────────────────────────────────────────────────

[17:38:02] 🖥 Provisioning machine...

[17:38:02] 🎛 Preparing system...

[17:38:02] ⛓ Spinning up manager process...

[17:38:01] 🚀 Starting up repository: 'mobile-price-prediction', branch: 'main', main module: 'app.py'

[17:38:01] 🐙 Cloning repository...

[17:38:02] 🐙 Cloning into '/mount/src/mobile-price-prediction'...

[17:38:02] 🐙 Cloned repository!

[17:38:02] 🐙 Pulling code changes from Github...

[17:38:02] 📦 Processing dependencies...


──────────────────────────────────────── uv ───────────────────────────────────────────


Using uv pip install.

Using Python 3.14.5 environment at /home/adminuser/venv

Resolved 55 packages in 506ms

Prepared 55 packages in 5.75s

Installed 55 packages in 91ms

 + altair==6.1.0

 + anyio==4.13.0

 + attrs==26.1.0

 + blinker==1.9.0

 + cachetools==7.1.4

 + certifi==2026.5.20

 + charset-normalizer==3.4.7

 + click==8.4.1

 + contourpy==1.3.3[2026-06-02 17:38:09.165491] 

 + cycler==0.12.1

 + fonttools==4.63.0

 + gitdb==4.0.12

 + gitpython==3.1.50

 + h11==[2026-06-02 17:38:09.165763] 0.16.0

 + httptools==0.8.0

 + idna==3.18

 + itsdangerous==2.2.0

 + jinja2==3.1.6

 + joblib==1.5.3[2026-06-02 17:38:09.165951] 

 + jsonschema==4.26.0

 + jsonschema-specifications==2025.9.1

 + kiwisolver==1.5.0

 + markupsafe==3.0.3[2026-06-02 17:38:09.166156] 

 + matplotlib==3.10.9

 + narwhals==2.22.0

 + numpy==2.4.6

 + nvidia-nccl-cu12==2.30.4

 + [2026-06-02 17:38:09.166394] packaging==26.2

 + pandas==[2026-06-02 17:38:09.166545] 3.0.3

 + pillow==12.2.0

 + protobuf==7.35.0

 + [2026-06-02 17:38:09.166714] pyarrow==24.0.0

 + pydeck==0.9.2

 + pyparsing==3.3.2

 + python-dateutil==2.9.0.post0[2026-06-02 17:38:09.166840] 

 + python-multipart==0.0.30

 + referencing==0.37.0

 + requests==2.34.2

 + rpds-py[2026-06-02 17:38:09.166984] ==2026.5.1

 + scikit-learn==1.9.0

 + scipy==1.17.1

 + seaborn==0.13.2

 + six==1.17.0

 + smmap==5.0.3

 + starlette==1.2.1

 + [2026-06-02 17:38:09.167281] streamlit==1.58.0

 + tenacity==9.1.4

 + threadpoolctl==3.6.0

 + toml==0.10.2

 + typing-extensions==[2026-06-02 17:38:09.167453] 4.15.0

 + urllib3==2.7.0

 + uvicorn==0.48.0

 + watchdog==6.0.0

 + websockets==16.0

 + xgboost[2026-06-02 17:38:09.167603] ==3.2.0

Checking if Streamlit is installed

Found Streamlit version 1.58.0 in the environment

Installing rich for an improved exception logging

Using uv pip install.

Using Python 3.14.5 environment at /home/adminuser/venv

Resolved 4 packages in 136ms

Prepared 4 packages in 110ms

Installed 4 packages in 13ms

 + markdown-it-py[2026-06-02 17:38:10.767454] ==4.2.0

 + mdurl==0.1.2

 + pygments==2.20.0

 + rich==15.0.0


────────────────────────────────────────────────────────────────────────────────────────


[17:38:11] 🐍 Python dependencies were installed from /mount/src/mobile-price-prediction/requirements.txt using uv.

Check if streamlit is installed

Streamlit is already installed

[17:38:13] 📦 Processed dependencies!

2026-06-02 17:38:14.512 Uvicorn server started on 0.0.0.0:8501




────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:129 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:789 in code_to_exec                                     

                                                                                

  /mount/src/mobile-price-prediction/app.py:2 in <module>                       

                                                                                

     1                                                                          

  ❱  2 from flask import Flask, request, render_template_string                 

     3 import pickle                                                            

     4                                                                          

     5 app = Flask(__name__)                                                    

────────────────────────────────────────────────────────────────────────────────

ModuleNotFoundError: No module named 'flask'

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:129 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:789 in code_to_exec                                     

                                                                                

  /mount/src/mobile-price-prediction/app.py:2 in <module>                       

                                                                                

     1                                                                          

  ❱  2 from flask import Flask, request, render_template_string                 

     3 import pickle                                                            

     4                                                                          

     5 app = Flask(__name__)                                                    

────────────────────────────────────────────────────────────────────────────────

ModuleNotFoundError: No module named 'flask'

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:129 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:789 in code_to_exec                                     

                                                                                

  /mount/src/mobile-price-prediction/app.py:2 in <module>                       

                                                                                

     1                                                                          

  ❱  2 from flask import Flask, request, render_template_string                 

     3 import pickle                                                            

     4                                                                          

     5 app = Flask(__name__)                                                    

────────────────────────────────────────────────────────────────────────────────

ModuleNotFoundError: No module named 'flask'
